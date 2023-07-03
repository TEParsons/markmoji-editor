import time
import PyQt5.QtWebEngineWidgets as html


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
        self.apply_theme()
    
    def apply_theme(self):
        # get stylesheet
        self.stylesheet = self.app.theme.viewer.spec
        # set content again
        self.set_body(self.body)
    
    def set_body(self, content):
        # start timing
        start = time.time()
        # store value
        self.body = content
        # preview HTML
        content_html = (
            f"<head>\n"
            f"<style>\n"
            f"{self.stylesheet}\n"
            f"</style>\n"
            f"</head>\n"
            f"<body>\n"
            f"{self.body}\n"
            f"</body>"
        )
        self.setHtml(content_html)
        # store time of this render
        self._last_render = time.time()
        # store render dur
        self._render_durs.append(self._last_render - start)
        # only keep last 10 render durs
        if len(self._render_durs) > 10:
            self._render_durs = self._render_durs[-10:]