from PyQt5.QtGui import QPalette, QColor
from catppuccin.flavour import Flavour
"""
### Colour roles
QPalette.Button, 
QPalette.Light, QPalette.Midlight, QPalette.Mid, QPalette.Dark,
QPalette.WindowText, QPalette.Text, QPalette.BrightText, QPalette.ButtonText, QPalette.HighlightedText, QPalette.ToolTipText,
QPalette.PlaceholderText,
QPalette.Base, QPalette.AlternateBase,
QPalette.Window, QPalette.ToolTipBase,
QPalette.Shadow, QPalette.Highlight,
QPalette.Link, QPalette.LinkVisited

### Colour states
QPalette.Active, QPalette.Disabled, QPalette.Inactive

### Flavour tags
rosewater, flamingo, pink, mauve, red, maroon, peach, yellow, green, teal, sky, sapphire, blue, lavender
text
subtext1, subtext0
overlay2, overlay1, overlay0,
surface2, surface1, surface0,
base, mantle, crust,
"""
def set_colors(palette, values):
    """
    Set several colour roles to matching flavour objects
    """
    for role, col in values.items():
        if isinstance(col, dict):
            for state, col in col.items():
                palette.setColor(state, role, QColor("#" + col.hex))
        else:
            palette.setColor(role, QColor("#" + col.hex))


# --- Catppuccin Frappe ---
_flav = Flavour.frappe()
frappe = QPalette()
set_colors(frappe, {
    QPalette.Button: {
        QPalette.Active: _flav.crust, 
        QPalette.Inactive: _flav.blue,
        QPalette.Disabled: _flav.base,
    },
    # QPalette.Light: _flav, 
    # QPalette.Midlight: _flav, 
    # QPalette.Mid: _flav,
    # QPalette.Dark: _flav,
    # QPalette.WindowText: _flav, 
    QPalette.Text: _flav.text, 
    # QPalette.BrightText: _flav, 
    # QPalette.ButtonText: _flav, 
    # QPalette.HighlightedText: _flav, 
    # QPalette.ToolTipText: _flav,
    # QPalette.PlaceholderText: _flav,
    QPalette.Base: _flav.base, 
    # QPalette.AlternateBase: _flav,
    QPalette.Window: _flav.mantle, 
    # QPalette.ToolTipBase: _flav,
    # QPalette.Shadow: _flav, 
    # QPalette.Highlight: _flav,
    # QPalette.Link: _flav, 
    # QPalette.LinkVisited: _flav, 
})


# --- Catppuccin Latte ---
_spec = Flavour.latte()
latte = QPalette()


# --- Catppuccin Macchiato ---
_spec = Flavour.macchiato()
macchiato = QPalette()


# --- Catppuccin Mocha ---
_spec = Flavour.mocha()
mocha = QPalette()
