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

### Flavour tags
rosewater, flamingo, pink, mauve, red, maroon, peach, yellow, green, teal, sky, sapphire, blue, lavender
text
subtext1, subtext0
overlay2, overlay1, overlay0,
surface2, surface1, surface0,
base, mantle, crust,
"""
def QC(value):
    """
    Shorthand for converting a Catppuccin colour to a PyQt colour.
    """
    return QColor("#" + value.hex)

# --- Catppuccin Frappe ---
_flav = Flavour.frappe()
frappe = QPalette()
frappe.setColor(QPalette.Window, QC(_flav.mantle))
frappe.setColor(QPalette.Button, QC(_flav.crust))
frappe.setColor(QPalette.Base, QC(_flav.base))


# --- Catppuccin Latte ---
_spec = Flavour.latte()
latte = QPalette()


# --- Catppuccin Macchiato ---
_spec = Flavour.macchiato()
macchiato = QPalette()


# --- Catppuccin Mocha ---
_spec = Flavour.mocha()
mocha = QPalette()