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
        # get name of stylesheet and variable to find object by
        if "." in self.stem:
            folder, stylesheet = self.stem.split(".", maxsplit=1)
            terminus = Path(folder) / f"{stylesheet}.css"
        else:
            terminus = f"{self.stem}.css"
        # find style file
        self.path = __folder__ / "viewer" / terminus
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
        package = importlib.import_module(f".app.theme.editor.{package_name}", package="markmoji_editor")
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
        package = importlib.import_module(f".app.theme.app.{package_name}", package="markmoji_editor")
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
            viewer="catppuccin.latte",
            editor="catppuccin.latte",
            app="catppuccin.latte"
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


def get_all_themes():
    from PyQt5.QtGui import QPalette
    from pygments.style import Style

    def get_modules(module, cls):
        """
        Get the spec objects for the given module (editor or app) which match the given class
        """
        themes = {}
        # import folder as package
        pkg = importlib.import_module(f".app.theme.{module}", package="markmoji_editor")
        # iterate through names
        for name in dir(pkg):
            # skip private names
            if name.startswith("_"):
                continue
            # get names from __all__
            themes[name] = getattr(pkg, name).__all__
        
        return themes
    
    def get_files(folder, ext):
        themes = {}
        # iterate through subfolders
        for subfolder in folder.glob("*/"):
            # add key to dict
            themes[subfolder.stem] = []
            # iterate through theme files
            for file in subfolder.glob(f"*.{ext}"):
                # add its name to dict
                themes[subfolder.stem].append(file.stem)
        
        return themes


    themes = {}
    # get app themes
    themes['app'] = get_modules("app", QPalette)
    # get editor themes
    themes['editor'] = get_modules("editor", Style)
    # get viewer themes
    themes['viewer'] = get_files(__folder__ / "viewer", "css")

    return themes


def get_combi_themes():
    """
    Get themes dict for only items present across all types (app, editor and viewer)
    """
    themes = get_all_themes()
    # split all sets by target
    app_sets = list(themes['app'])
    editor_sets = list(themes['editor'])
    viewer_sets = list(themes['viewer'])
    # get list of unique set names
    all_sets = list(set(app_sets + editor_sets + viewer_sets))
    combi_sets = []
    for this_set in all_sets:
        # where is it present?
        present_in = (
            this_set in app_sets, 
            this_set in editor_sets, 
            this_set in viewer_sets
        )
        # if present in all, add to combi sets
        if all(present_in):
            combi_sets.append(this_set)
    
    # iterate through combi sets
    combi_themes = {}
    for this_set in combi_sets:
        app_themes = themes['app'][this_set]
        editor_themes = themes['editor'][this_set]
        viewer_themes = themes['viewer'][this_set]
        # get list of unique theme names
        all_themes = list(set(app_themes + editor_themes + viewer_themes))
        combi_themes[this_set] = []
        for this_theme in all_themes:
            # where is it present?
            present_in = (
                this_theme in app_themes,
                this_theme in editor_themes,
                this_theme in viewer_themes
            )
            # if present in all, add to combi themes
            if all(present_in):
                combi_themes[this_set].append(this_theme)
    
    return combi_themes


current = Theme()
