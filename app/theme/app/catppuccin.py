from PyQt5.QtGui import QPalette
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
"""



# --- Catppuccin Frappe ---
_spec = Flavour.frappe()
frappe = QPalette()
frappe.setColorGroup()
frappe.setColor(QPalette.Base, _spec.base)


# --- Catppuccin Latte ---
_spec = Flavour.latte()
latte = QPalette()


# --- Catppuccin Macchiato ---
_spec = Flavour.macchiato()
macchiato = QPalette()


# --- Catppuccin Mocha ---
_spec = Flavour.mocha()
mocha = QPalette()
