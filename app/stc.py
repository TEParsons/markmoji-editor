import markmoji
import pygments, pygments.lexers
import PyQt5.QtCore as util
import PyQt5.QtWidgets as qt
import PyQt5.QtGui as gui


class StyledTextCtrl(qt.QTextEdit):
    def __init__(self, frame, language):
        # initialise
        qt.QTextEdit.__init__(self)
        self.frame = frame
        self.app = self.frame.app
        self.setAcceptRichText(False)
        # set minimum size
        self.setMinimumWidth(128)
        # setup lexer
        self.lexer = pygments.lexers.get_lexer_by_name(language)
        # setup right click
        self.setContextMenuPolicy(util.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)
    
    def on_context_menu(self):
        # setup menu style
        style = self.app.theme.editor.spec
        stylesheet = (
            f"QMenu::item{{"
            f"   background-color: {style.background_color};"
            f"   color: #{style.style_for_token(pygments.token.Token)['color']};"
            f"   font-family: JetBrains Mono,Noto Emoji;"
            f"}}"

            f"QMenu::item:selected{{"
            f"   background-color: {style.line_number_background_color};"
            f"   color: {style.line_number_color};"
            f"}}"
        )
        # make menu
        menu = self.createStandardContextMenu()
        menu.setStyleSheet(stylesheet)
        # add emoji section
        menu.addSeparator()
        submenu = menu.addMenu("Insert &Handler")
        submenu.setStyleSheet(stylesheet)
        # add emojis
        for emoji, cls in markmoji.handlers.map.items():
            # skip base classes
            if emoji in ("?", "〽️", "❓"):
                continue
            # add emoji
            submenu.addAction(f"{emoji} {cls.__name__}", self.insert_emoji)
            
        menu.exec_(gui.QCursor.pos())
    
    def insert_emoji(self, evt=None):
        # get emoji
        text = self.sender().text()
        emoji = text.split(" ")[0]
        # insert emoji
        self.insertPlainText(emoji + "[]()")
    
    def style_text(self):
        """
        Apply pyments.style to text contents
        """
        # don't trigger any events while this method executes
        self.blockSignals(True)

        # get cursor handle
        cursor = gui.QTextCursor(self.document())
        # get style dict
        style = self.app.theme.editor.spec
        # set base style
        self.setStyleSheet(
            f"background-color: {style.background_color};"
            f"font-family: JetBrains Mono, Noto Emoji;"
            f"font-size: 14pt;"
            f"border: 1px solid {style.line_number_background_color};"
        )
        # lex content to get tokens
        tokens = pygments.lex(self.toPlainText(), lexer=self.lexer)
        # re-add characters with styling
        i = 0
        for token, text in tokens:
            # get style for this token
            token_style = style.style_for_token(token)
            # create format object
            char_format = gui.QTextCharFormat()
            char_format.setFontFamily("JetBrains Mono")
            char_format.setFontItalic(token_style['italic'])
            if token_style['bold']:
                char_format.setFontWeight(600)
            char_format.setFontUnderline(token_style['underline'])
            char_format.setForeground(gui.QColor("#" + token_style['color']))
            # select corresponding chars
            cursor.setPosition(i)
            cursor.movePosition(cursor.Right, n=len(text), mode=cursor.KeepAnchor)
            # format selection
            cursor.setCharFormat(char_format)
            # move forward to next token
            i += len(text)

        # allow signals to trigger again
        self.blockSignals(False)