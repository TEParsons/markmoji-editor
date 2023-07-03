import importlib
from pathlib import Path

from PyQt5.QtGui import QPalette
from pygments.style import Style as PygmentsStyle


__folder__ = Path(__file__).parent


class ViewerStyle:
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
    def __init__(self, stem):
        # store stem
        self.stem = stem
        # find style file
        self.path = __folder__ / "viewer" / f"{self.stem}.css"
        # make sure style file exists
        assert self.path.is_file(), (
            f"Could not find file for viewer style '{self.stem}'"
        )
        # read style file
        self.spec = self.path.read_text(encoding="utf-8")


class EditorStyle:
    """
    Object to store parameters for styling the text editor
    
    #### Args
    stem (str)
    :    File stem of the Python file containing the subclass of pygments.Style for the editor's colours

    #### Attributes
    stem (str)
    :    File stem of the Python file containing the subclass of pygments.Style for the editor's colours
    path (pathlib.Path)
    :    Import path (from the "editor" folder) to the subclass of pygments.Style for the editor's colours, e.g. `catppuccin.latte`.
    spec (str)
    :    Loaded pygments.Style object
    """    
    def __init__(self, stem):
        # store stem
        self.stem = stem
        # get name of package and variable to find object by
        if "." in self.stem:
            package_name, variable = self.stem.split(".", maxsplit=1)
        else:
            package_name = self.stem
            variable = "style"
        # import package
        package = importlib.import_module(f".theme.editor.{package_name}", package="markmoji_editor")
        # get spec
        self.spec = getattr(package, variable)


class AppStyle:
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
    
    def __init__(self, stem):
        # store stem
        self.stem = stem
        # get name of package and variable to find object by
        if "." in self.stem:
            package_name, variable = self.stem.split(".", maxsplit=1)
        else:
            package_name = self.stem
            variable = "style"
        # import package
        package = importlib.import_module(f".theme.app.{package_name}", package="markmoji_editor")
        # get spec
        self.spec = getattr(package, variable)


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
            editor="catppuccin.frappe",
            app="catppuccin.frappe"
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
