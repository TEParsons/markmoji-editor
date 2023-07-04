import markdown
import markmoji
import time
import threading
import traceback
import PyQt5.QtCore as util
import PyQt5.QtWidgets as qt
import PyQt5.QtGui as gui

from pathlib import Path

from . import stc, viewer, toggle, menu


class MarkmojiApp(qt.QApplication):
    def __init__(self, show_splash=True, argv=[]):
        qt.QApplication.__init__(
            self, argv
        )
        self.setStyle("Fusion")
        # show splash (if requested)
        if show_splash:
            splash = qt.QSplashScreen(
                gui.QPixmap('markmoji_editor/assets/Splash.png')
            )
            splash.show()
            splash.start_time = time.time()
        
        # set theme
        from .theme import current
        self.theme = current
        # make main window
        self.win = MarkmojiFrame(self)

        # close splash (if shown)
        if show_splash:    
            while time.time() - self.app.splash.start_time < 2.5:
                pass
            splash.close()

class MarkmojiFrame(qt.QMainWindow):
    def __init__(self, app, filename=None):
        # create
        qt.QWidget.__init__(self)
        self.app = app

        # setup interpreter
        self.md = markdown.Markdown(
            extensions=["extra", markmoji.Markmoji()]
        )

        # setup window
        self.setWindowIcon(gui.QIcon('markmoji_editor/assets/Emblem@16w.png'))
        self.setWindowTitle(f"Markmoji (v{markmoji.__version__})")
        self.resize(1080, 720)

        # add menu
        self.menu = menu.MarkmojiMenu(self)
        self.setMenuBar(self.menu)

        # setup panel
        self.panel = qt.QWidget(self)
        self.setCentralWidget(self.panel)
        self.sizer = qt.QVBoxLayout(self.panel)
        self.panel.setLayout(self.sizer)

        # setup panel
        self.ctrls = qt.QSplitter(self.panel)
        self.ctrls.setChildrenCollapsible(False)
        self.sizer.addWidget(self.ctrls)
        # raw text ctrl
        self.md_ctrl = MarkmojiEditor(frame=self)
        self.ctrls.addWidget(self.md_ctrl)
        # raw html ctrl
        self.html_ctrl = HTMLReader(frame=self)
        self.ctrls.addWidget(self.html_ctrl)
        # rendered HTML ctrl
        self.html_view = viewer.HTMLViewer(frame=self)
        self.ctrls.addWidget(self.html_view)

        # bind rendering to text edit
        self.md_ctrl.textChanged.connect(self.on_text)

        # add view toggle
        self.view_ctrl = toggle.ViewToggle(self)
        self.view_ctrl.add_button(ctrl=self.md_ctrl, icon_name="view_md")
        self.view_ctrl.add_button(ctrl=self.html_ctrl, icon_name="view_html")
        self.view_ctrl.add_button(ctrl=self.html_view, icon_name="view_preview")
        self.view_ctrl.set_values((True, False, True))
        self.sizer.addWidget(self.view_ctrl, alignment=util.Qt.AlignHCenter)

        # setup shortcuts
        self.shortcuts = {
            qt.QShortcut(gui.QKeySequence('Ctrl+N'), self): self.new,
            qt.QShortcut(gui.QKeySequence('Ctrl+S'), self): self.save,
            qt.QShortcut(gui.QKeySequence('Ctrl+Alt+S'), self): self.save_as,
            qt.QShortcut(gui.QKeySequence('Ctrl+O'), self): self.open,
        }
        for sc, fcn in self.shortcuts.items():
            sc.activated.connect(fcn)

        # load file
        if filename is not None:
            self.open(filename=filename)

        # show
        self.apply_theme()
        self.show()

    def apply_theme(self):
        self.app.setPalette(self.app.theme.app.spec)
        self.app.setStyle("Fusion")
        self.md_ctrl.style_text()
        self.html_ctrl.style_text()
        self.html_view.refresh_content()
    
    def on_text(self, evt=None):
        """
        Handle when raw text value is changed.

        #### Args
        evt (qt.QSignal, optional)
        :    Event generated by the `textChanged` event. Defaults to None.
        """
        # style markdown
        self.md_ctrl.style_text()
        # render HTML
        threading.Thread(target=self.render_html).run()
    
    def render_html(self):
        """
        Render markdown content into HTML
        """
        # get markdown
        content_md = self.md_ctrl.toPlainText()
        # parse to HTML
        try:
            content_html = self.md.convert(content_md)
        except Exception as err:
            tb = "\n".join(traceback.format_exception(err))
            content_html = (
                f"<h1>Error</h1>\n"
                f"<p>Could not parse Markdown. Error from Python:</p>\n"
                f"<pre><code>{tb}</code></pre>\n"
                )
        # apply to HTML ctrl
        self.html_ctrl.setPlainText(content_html)
        self.html_ctrl.style_text()
        # apply to HTML viewer
        self.html_view.set_body(content_html)
    
    def new(self):
        # create a new frame
        MarkmojiFrame(self.app)
    
    def open(self, filename=None):
        if filename is None:
            # open file dlg
            filename, _ = qt.QFileDialog.getOpenFileName(self, "Open...", "C://", "Markdown files (*.md)")
            # cancel if cancelled
            if not filename:
                return
        # store filename
        self.filename = Path(filename)
        # read file
        content_md = self.filename.read_text(encoding="utf-8")
        # set text
        self.md_ctrl.setText(content_md)
    
    def save(self):
        # call save as on current file
        self.save_as(filename=self.filename)

    def save_as(self, filename=None):
        if filename is None:
            # open file dlg
            filename, _ = qt.QFileDialog.getSaveFileName(self, "Save as...", "C://", "Markdown files (*.md)")
            # cancel if cancelled
            if not filename:
                return
        # store filename
        self.filename = Path(filename)
        # get markdown content
        content_md = self.md_ctrl.toPlainText()
        # save markdown content
        self.filename.write_text(content_md, encoding="utf-8")
    
    def export_raw_html(self, filename=None):
        if filename is None:
            # open file dlg
            filename, _ = qt.QFileDialog.getSaveFileName(self, "Export as...", "C://", "HTML files (*.html)")
            # cancel if cancelled
            if not filename:
                return
        # pathify filename
        filename = Path(filename)
        # get HTML
        content_html = self.html_ctrl.getPlainText()
        # export html content
        filename.write_text(content_html, encoding="utf-8")

    def export_styled_html(self, filename=None):
        if filename is None:
            # open file dlg
            filename, _ = qt.QFileDialog.getSaveFileName(self, "Export as...", "C://", "HTML files (*.html)")
            # cancel if cancelled
            if not filename:
                return
        # pathify filename
        filename = Path(filename)
        # todo: get HTML
        content_html = ""
        # export html content
        filename.write_text(content_html, encoding="utf-8")


class MarkmojiEditor(stc.StyledTextCtrl):
    def __init__(self, frame):
        stc.StyledTextCtrl.__init__(self, frame, language="markdown")
        
        
class HTMLReader(stc.StyledTextCtrl):
    def __init__(self, frame):
        stc.StyledTextCtrl.__init__(self, frame, language="html")
        self.setReadOnly(True)
    
