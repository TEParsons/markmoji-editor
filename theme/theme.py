import importlib
from pathlib import Path

from PyQt5.QtGui import QPalette
from pygments.style import Style as PygmentsStyle


__folder__ = Path(__file__).parent


class _BaseStyle:
    """
    Base class from which style objects for viewer, app and editor are derived.
    """

    folder = __folder__
    ext = ""

    def __init__(self, stem):
        # store stem
        self.stem = stem
        # find style file
        self.path = self.folder / f"{stem}.{self.ext}"
        # make sure style file exists
        assert self.path.is_file(), (
            f"Could not find file for {self.folder.stem} style '{stem}'"
        )
        # read in style
        self.spec = self.load()
    
    def load(self):
        raise NotImplementedError("_BaseStyle should never be instantiated directly.")


class ViewerStyle(_BaseStyle):
    """
    Object to store parameters for styling the HTML preview
    
    #### Args
    stem (str)
    :    File stem of the CSS file used to style the HTML preview

    #### Attributes
    stem (str)
    :    File stem of the CSS file used to style the HTML preview
    path (pathlib.Path)
    :    Path to the CSS file used to style the HTML preview
    spec (str)
    :    Loaded CSS style string
    """

    folder = __folder__ / "viewer"
    ext = "css"

    def load(self):
        return self.path.read_text(encoding="utf-8")


class EditorStyle(_BaseStyle):
    """
    Object to store parameters for styling the text editor
    
    #### Args
    stem (str)
    :    File stem of the Python file containing the subclass of pygments.Style for the editor's colours

    #### Attributes
    stem (str)
    :    File stem of the Python file containing the subclass of pygments.Style for the editor's colours
    path (pathlib.Path)
    :    Path to the Python file containing the subclass of pygments.Style for the editor's colours
    spec (str)
    :    Loaded pygments.Style object
    """

    folder = __folder__ / "editor"
    ext = "py"
    
    def load(self):
        # not implemented yet - just use default palette
        return PygmentsStyle()


class AppStyle(_BaseStyle):
    """
    Object to store parameters for styling the text editor
    
    #### Args
    stem (str)
    :    File stem of the Python file containing the subclass of PyQt5.QPalette for the app's colours

    #### Attributes
    stem (str)
    :    File stem of the Python file containing the subclass of PyQt5.QPalette for the app's colours
    path (pathlib.Path)
    :    Path to the Python file containing the subclass of PyQt5.QPalette for the app's colours
    spec (str)
    :    Loaded PyQt5.QPalette object
    """

    folder = __folder__ / "editor"
    ext = "py"
    
    def load(self):
        # not implemented yet - just use default palette
        from PyQt5.QtWidgets import QWidget
        return QWidget().palette()


class Theme:
    """
    Specifies a theme 
        
    #### Args
    viewer (str)
    :    File stem of the CSS file used to style the HTML preview
    editor (str)
    :    File stem of the Python file containing the subclass of pygments.Style for the editor's colours
    app (str)
    :    File stem of the Python file containing the subclass of PyQt5.QPalette for the app's colours
    """

    def __init__(
            self,
            viewer="light",
            editor="light",
            app="light"
    ):
       self.viewer = viewer
       self.editor = editor
       self.app = app

    @property
    def viewer(self):
        """
        ViewerStyle object for the viewer.
        """
        return self._viewer
    
    @viewer.setter
    def viewer(self, value):
        self._viewer = ViewerStyle(value)
    
    @property
    def editor(self):
        """
        EditorStyle object for the editor.
        """
        return self._editor
    
    @editor.setter
    def editor(self, value):
        self._editor = EditorStyle(value)
    
    @property
    def app(self):
        """
        AppStyle object for the viewer.
        """
        return self._app
    
    @app.setter
    def app(self, value):
        self._app = AppStyle(value)


current = Theme()
