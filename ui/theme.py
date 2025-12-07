# ui/theme.py
import flet as ft

# -----------------------------
#  ESTADO GLOBAL DEL TEMA
# -----------------------------
CURRENT_THEME = "dark"

# -----------------------------
#  PALETAS MEJORADAS
# -----------------------------
THEMES = {
    "dark": {
        # Fondos más suaves, no negro absoluto
        "APP_BG": "#121212",
        "CARD_BG": "#1A1A1A",
        "SURFACE_BG": "#222222",

        # Botones
        "BTN_BG": "#2F2F2F",
        "BTN_BG_HOVER": "#3A3A3A",
        "BTN_BORDER": "#4A4A4A",

        # Textos
        "TEXT_COLOR": "#FFFFFF",
        "TEXT_MUTED": "#D0D0D0",
    },
    "light": {
        "APP_BG": "#F6F6F6",
        "CARD_BG": "#FFFFFF",
        "SURFACE_BG": "#EEEEEE",

        "BTN_BG": "#DDDDDD",
        "BTN_BG_HOVER": "#CCCCCC",
        "BTN_BORDER": "#BBBBBB",

        "TEXT_COLOR": "#000000",
        "TEXT_MUTED": "#333333",
    }
}

# -----------------------------
#  VARIABLES ACTIVAS
# -----------------------------
APP_BG = ""
CARD_BG = ""
SURFACE_BG = ""
BTN_BG = ""
BTN_BG_HOVER = ""
BTN_BORDER = ""
TEXT_COLOR = ""
TEXT_MUTED = ""

BORDER_RADIUS = 12
ANIMATION_MS = 200


# -----------------------------
#  SINCRONIZAR VARIABLES
# -----------------------------
def _sync():
    global APP_BG, CARD_BG, SURFACE_BG, BTN_BG, BTN_BG_HOVER
    global BTN_BORDER, TEXT_COLOR, TEXT_MUTED

    t = THEMES[CURRENT_THEME]
    APP_BG = t["APP_BG"]
    CARD_BG = t["CARD_BG"]
    SURFACE_BG = t["SURFACE_BG"]
    BTN_BG = t["BTN_BG"]
    BTN_BG_HOVER = t["BTN_BG_HOVER"]
    BTN_BORDER = t["BTN_BORDER"]
    TEXT_COLOR = t["TEXT_COLOR"]
    TEXT_MUTED = t["TEXT_MUTED"]


# -----------------------------
#  APLICAR TEMA A PÁGINA
# -----------------------------
def apply_theme(page: ft.Page):
    _sync()
    page.bgcolor = APP_BG
    page.padding = 30
    page.fonts = {"inter": "https://rsms.me/inter/inter.ttf"}
    page.theme = ft.Theme(font_family="inter")
    page.session.set("theme_mode", CURRENT_THEME)
    page.update()


# -----------------------------
#  TOGGLE DE TEMA
# -----------------------------
def toggle_app_theme(page: ft.Page):
    global CURRENT_THEME
    CURRENT_THEME = "light" if CURRENT_THEME == "dark" else "dark"
    apply_theme(page)


# -----------------------------
#  HELPERS UI
# -----------------------------
def title(text: str):
    return ft.Text(text, size=26, weight=ft.FontWeight.BOLD, color=TEXT_COLOR)


def subtitle(text: str):
    return ft.Text(text, size=16, color=TEXT_MUTED)


def primary_button(text: str, on_click=None, icon=None):
    return ft.ElevatedButton(
        text,
        icon=icon,
        on_click=on_click,
        bgcolor=BTN_BG,
        color=TEXT_COLOR,
        height=46,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=20,
            overlay_color=BTN_BG_HOVER,
            elevation=1
        )
    )


def input_field(label: str, password: bool = False):
    return ft.TextField(
        label=label,
        password=password,
        bgcolor=SURFACE_BG,
        color=TEXT_COLOR,
        border_color=BTN_BORDER,
        focused_border_color=BTN_BG_HOVER,
        label_style=ft.TextStyle(color=TEXT_MUTED),
        text_style=ft.TextStyle(color=TEXT_COLOR),
        border_radius=8
    )


# -----------------------------
#  COMPONENTES BASE
# -----------------------------
def card(content):
    return ft.Container(
        content=content,
        bgcolor=CARD_BG,
        padding=20,
        border_radius=BORDER_RADIUS,
        animate=ft.Animation(ANIMATION_MS, "easeInOut")
    )


def primary_btn(text, on_click=None, icon=None):
    return primary_button(text, on_click, icon)
