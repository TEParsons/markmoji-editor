import markdown
import markmoji
import time
import threading
import traceback
import PyQt5.QtCore as util
import PyQt5.QtWidgets as qt
import PyQt5.QtGui as gui

from . import stc, viewer, toggle


class MarkmojiApp(qt.QApplication):
    def __init__(self, show_splash=True, argv=[]):
        qt.QApplication.__init__(
            self, argv
        )
        # show splash (if requested)
        if show_splash:
            splash = qt.QSplashScreen(
                gui.QPixmap('markmoji_editor/assets/Splash.png')
            )
            splash.show()
            splash.start_time = time.time()
        
        # set theme
        from ..theme import current
        self.theme = current
        # make main window
        self.win = MarkmojiFrame(self)

        # close splash (if shown)
        if show_splash:    
            while time.time() - self.app.splash.start_time < 2.5:
                pass
            splash.close()

class MarkmojiFrame(qt.QWidget):
    def __init__(self, app):
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
        self.sizer = qt.QVBoxLayout(self)

        # setup panel
        self.panel = qt.QSplitter(self)
        self.panel.setChildrenCollapsible(False)
        self.sizer.addWidget(self.panel)
        # raw text ctrl
        self.md_ctrl = MarkmojiEditor(frame=self)
        self.md_ctrl.setMinimumWidth(128)
        self.panel.addWidget(self.md_ctrl)
        # raw html ctrl
        self.html_ctrl = HTMLReader(frame=self)
        self.panel.addWidget(self.html_ctrl)
        # rendered HTML ctrl
        self.html_view = viewer.HTMLViewer(frame=self)
        self.panel.addWidget(self.html_view)

        # bind rendering to text edit
        self.md_ctrl.textChanged.connect(self.on_text)

        # add view toggle
        self.view_ctrl = toggle.ViewToggle(self)
        self.view_ctrl.add_button(ctrl=self.md_ctrl, icon_name="view_md")
        self.view_ctrl.add_button(ctrl=self.html_ctrl, icon_name="view_html")
        self.view_ctrl.add_button(ctrl=self.html_view, icon_name="view_preview")
        self.view_ctrl.set_values((True, False, True))
        self.sizer.addWidget(self.view_ctrl, alignment=util.Qt.AlignHCenter)

        # show
        self.apply_theme()
        self.show()
    
    def apply_theme(self):
        self.md_ctrl.style_text()
        self.html_ctrl.style_text()
        self.html_view.apply_theme()
    
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


class MarkmojiEditor(stc.StyledTextCtrl):
    def __init__(self, frame):
        stc.StyledTextCtrl.__init__(self, frame, language="markdown")
        
        
class HTMLReader(stc.StyledTextCtrl):
    def __init__(self, frame):
        stc.StyledTextCtrl.__init__(self, frame, language="html")
        self.setReadOnly(True)
    
