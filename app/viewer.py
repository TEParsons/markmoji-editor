import time
import PyQt5.QtWebEngineWidgets as html
import PyQt5.QtCore as util

from pathlib import Path


class HTMLViewer(html.QWebEngineView):
    def __init__(self, frame):
        # initalise
        html.QWebEngineView.__init__(self)
        self.frame = frame
        self.app = self.frame.app

        # array to store render times in
        self._render_durs = [0]
        self._last_render = 0

        # set minimum size
        self.setMinimumWidth(128)
        # set initial content
        self.body = ""
        self.refresh_content()
    
    def refresh_content(self, evt=None):
        # set content again
        self.set_body(self.body)
    
    def set_body(self, content):
        # start timing
        start = time.time()
        # store value
        self.body = content
        # stop here if viewer isn't shown
        if not self.isVisible():
            return
        # construct HTML
        content_html = (
            f"<head>\n"
            f"<style>\n"
            f"{self.app.theme.viewer.spec}\n"
            f"</style>\n"
            f"</head>\n"
            f"<body>\n"
            f"{self.body}\n"
            f"</body>"
        )
        # get base url
        if hasattr(self.frame, "filename") and self.frame.filename is not None:
            filename = Path(self.frame.filename)
            base = filename.parent / (filename.stem + ".html")
        else:
            filename = Path(__file__)
            base = filename.parent.parent / "assets" / "untitled.html"
        base_url = util.QUrl.fromLocalFile(str(base))
        # set HTML
        self.setHtml(content_html, base_url)
        # store time of this render
        self._last_render = time.time()
        # store render dur
        self._render_durs.append(self._last_render - start)
        # only keep last 10 render durs
        if len(self._render_durs) > 10:
            self._render_durs = self._render_durs[-10:]

    def showEvent(self, event):
        self.refresh_content()
        return html.QWebEngineView.showEvent(self, event)
    
    def hideEvent(self, event):
        return html.QWebEngineView.hideEvent(self, event)
