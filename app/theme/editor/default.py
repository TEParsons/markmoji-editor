from pygments.token import Token
from pygments.style import Style


__all__ = ["light", "dark", "black"]


class light(Style):
    background_color = "#ffffff"
    line_number_background_color = "#f2f2f2"
    line_number_color = "#000000"
    
    styles = {
        Token: "#000000",
        Token.Generic.Heading: "bold",
    }


class dark(Style):
    background_color = "#253237"
    line_number_background_color = "#5C6B73"
    line_number_color = "#ffffff"
    
    styles = {
        Token: "#ffffff",
        Token.Generic.Heading: "bold",
    }


class black(Style):
    background_color = "#000000"
    line_number_background_color = "#161616"
    line_number_color = "#ffffff"
    
    styles = {
        Token: "#ffffff",
        Token.Generic.Heading: "bold",
    }

