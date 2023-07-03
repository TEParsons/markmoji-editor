from PyQt5.QtGui import QPalette, QColor
from catppuccin.flavour import Flavour


__all__ = ["frappe", "latte", "macchiato", "mocha"]


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
frappe_flavour = Flavour.frappe()
frappe = QPalette()
set_colors(frappe, {
    QPalette.Base: frappe_flavour.base,
    QPalette.AlternateBase: frappe_flavour.crust,
    QPalette.Light: frappe_flavour.overlay2,
    QPalette.Midlight: frappe_flavour.overlay1,
    QPalette.Mid: frappe_flavour.overlay0,
    QPalette.Dark: frappe_flavour.surface2,
    QPalette.Window: frappe_flavour.mantle,
    QPalette.WindowText: frappe_flavour.text,
    QPalette.Shadow: frappe_flavour.overlay0,
    QPalette.Text: frappe_flavour.text,
    QPalette.BrightText: frappe_flavour.rosewater,
    QPalette.PlaceholderText: frappe_flavour.overlay1,
    QPalette.Highlight: frappe_flavour.surface2,
    QPalette.HighlightedText: frappe_flavour.text, 
    QPalette.Link: frappe_flavour.blue,
    QPalette.LinkVisited: frappe_flavour.lavender,
    QPalette.ToolTipBase: frappe_flavour.overlay0,
    QPalette.ToolTipText: frappe_flavour.text,
    QPalette.Button: frappe_flavour.surface0,
    QPalette.ButtonText: frappe_flavour.text,
})


# --- Catppuccin Latte ---
latte_flavour = Flavour.latte()
latte = QPalette()
set_colors(frappe, {
    QPalette.Base: latte_flavour.base,
    QPalette.AlternateBase: latte_flavour.crust,
    QPalette.Light: latte_flavour.overlay2,
    QPalette.Midlight: latte_flavour.overlay1,
    QPalette.Mid: latte_flavour.overlay0,
    QPalette.Dark: latte_flavour.surface2,
    QPalette.Window: latte_flavour.mantle,
    QPalette.WindowText: latte_flavour.text,
    QPalette.Shadow: latte_flavour.overlay0,
    QPalette.Text: latte_flavour.text,
    QPalette.BrightText: latte_flavour.rosewater,
    QPalette.PlaceholderText: latte_flavour.overlay1,
    QPalette.Highlight: latte_flavour.surface2,
    QPalette.HighlightedText: latte_flavour.text, 
    QPalette.Link: latte_flavour.blue,
    QPalette.LinkVisited: latte_flavour.lavender,
    QPalette.ToolTipBase: latte_flavour.overlay0,
    QPalette.ToolTipText: latte_flavour.text,
    QPalette.Button: latte_flavour.surface0,
    QPalette.ButtonText: latte_flavour.text,
})


# --- Catppuccin Macchiato ---
macchiato_flavour = Flavour.macchiato()
macchiato = QPalette()
set_colors(macchiato, {
    QPalette.Base: macchiato_flavour.base,
    QPalette.AlternateBase: macchiato_flavour.crust,
    QPalette.Light: macchiato_flavour.overlay2,
    QPalette.Midlight: macchiato_flavour.overlay1,
    QPalette.Mid: macchiato_flavour.overlay0,
    QPalette.Dark: macchiato_flavour.surface2,
    QPalette.Window: macchiato_flavour.mantle,
    QPalette.WindowText: macchiato_flavour.text,
    QPalette.Shadow: macchiato_flavour.overlay0,
    QPalette.Text: macchiato_flavour.text,
    QPalette.BrightText: macchiato_flavour.rosewater,
    QPalette.PlaceholderText: macchiato_flavour.overlay1,
    QPalette.Highlight: macchiato_flavour.surface2,
    QPalette.HighlightedText: macchiato_flavour.text, 
    QPalette.Link: macchiato_flavour.blue,
    QPalette.LinkVisited: macchiato_flavour.lavender,
    QPalette.ToolTipBase: macchiato_flavour.overlay0,
    QPalette.ToolTipText: macchiato_flavour.text,
    QPalette.Button: macchiato_flavour.surface0,
    QPalette.ButtonText: macchiato_flavour.text,
})


# --- Catppuccin Mocha ---
mocha_flavour = Flavour.mocha()
mocha = QPalette()
set_colors(mocha, {
    QPalette.Base: mocha_flavour.base,
    QPalette.AlternateBase: mocha_flavour.crust,
    QPalette.Light: mocha_flavour.overlay2,
    QPalette.Midlight: mocha_flavour.overlay1,
    QPalette.Mid: mocha_flavour.overlay0,
    QPalette.Dark: mocha_flavour.surface2,
    QPalette.Window: mocha_flavour.mantle,
    QPalette.WindowText: mocha_flavour.text,
    QPalette.Shadow: mocha_flavour.overlay0,
    QPalette.Text: mocha_flavour.text,
    QPalette.BrightText: mocha_flavour.rosewater,
    QPalette.PlaceholderText: mocha_flavour.overlay1,
    QPalette.Highlight: mocha_flavour.surface2,
    QPalette.HighlightedText: mocha_flavour.text, 
    QPalette.Link: mocha_flavour.blue,
    QPalette.LinkVisited: mocha_flavour.lavender,
    QPalette.ToolTipBase: mocha_flavour.overlay0,
    QPalette.ToolTipText: mocha_flavour.text,
    QPalette.Button: mocha_flavour.surface0,
    QPalette.ButtonText: mocha_flavour.text,
})
