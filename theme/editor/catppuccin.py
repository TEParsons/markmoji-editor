from pygments.token import Token

from catppuccin.extras.pygments import FrappeStyle
from catppuccin.extras.pygments import LatteStyle
from catppuccin.extras.pygments import MacchiatoStyle
from catppuccin.extras.pygments import MochaStyle


class frappe(FrappeStyle):
    background_color = "#303446"
    line_number_background_color = "#292c3c"
    line_number_color = "#c6d0f5"
    
    styles = FrappeStyle.styles
    styles.update({
        Token: "#c6d0f5",
        Token.Generic.Heading: "bold",
    })


class latte(LatteStyle):
    background_color = "#eff1f5"
    line_number_background_color = "#e6e9ef"
    line_number_color = "#4c4f69"
    
    styles = LatteStyle.styles
    styles.update({
        Token: "#4c4f69",
        Token.Generic.Heading: "bold",
    })


class macchiato(MacchiatoStyle):
    background_color = "#24273a"
    line_number_background_color = "#1e2030"
    line_number_color = "#cad3f5"
    
    styles = LatteStyle.styles
    styles.update({
        Token: "#cad3f5",
        Token.Generic.Heading: "bold",
    })


class mocha(MochaStyle):
    background_color = "#1e1e2e"
    line_number_background_color = "#181825"
    line_number_color = "#cdd6f4"
    
    styles = LatteStyle.styles
    styles.update({
        Token: "#cdd6f4",
        Token.Generic.Heading: "bold",
    })


