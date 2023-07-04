import PyQt5.QtWidgets as qt
from .theme import current, get_all_themes, get_combi_themes


class MarkmojiMenu(qt.QMenuBar):
    def __init__(self, parent):
        # initialise
        qt.QMenuBar.__init__(self, parent=parent)
        self.parent = parent
        # remove border
        self.setStyleSheet("border: none;")

        # theme menu
        self.theme_menu = self.addMenu("&Theme")
        self.theme_menu.submenus = {}
        themes = get_all_themes()
        # combination themes
        menu = self.theme_menu.submenus['all'] = self.theme_menu.addMenu("&Combination")
        combi_themes = get_combi_themes()
        for sub in combi_themes:
            submenu = menu.addMenu(sub)
            for item in themes['app'][sub]:
                btn = submenu.addAction(item, self.set_theme)
                btn.data = ("all", f"{sub}.{item}")
                btn.setToolTip(f"{sub}.{item}")
        # app themes
        menu = self.theme_menu.submenus['app'] = self.theme_menu.addMenu("&App")
        for sub in themes['app']:
            submenu = menu.addMenu(sub)
            for item in themes['app'][sub]:
                btn = submenu.addAction(item, self.set_theme)
                btn.data = ("app", f"{sub}.{item}")
                btn.setToolTip(f"{sub}.{item}")
        # editor themes
        menu = self.theme_menu.submenus['editor'] = self.theme_menu.addMenu("&Editor")
        for sub in themes['editor']:
            submenu = menu.addMenu(sub)
            for item in themes['editor'][sub]:
                btn = submenu.addAction(item, self.set_theme)
                btn.data = ("editor", f"{sub}.{item}")
                btn.setToolTip(f"{sub}.{item}")
        # viewer themes
        menu = self.theme_menu.submenus['viewer'] = self.theme_menu.addMenu("&Viewer")
        for sub in themes['viewer']:
            submenu = menu.addMenu(sub)
            for item in themes['viewer'][sub]:
                btn = submenu.addAction(item, self.set_theme)
                btn.data = ("viewer", f"{sub}.{item}")
                btn.setToolTip(f"{sub}.{item}")
    
    def set_theme(self, evt=None):
        # get button
        btn = self.sender()
        # get data
        target, theme = btn.data
        # make target iterable
        if target == "all":
            target = ("app", "editor", "viewer")
        elif isinstance(target, str):
            target = [target]
        # set theme
        for t in target:
            setattr(current, t, theme)
        # apply theme
        self.parent.apply_theme()

