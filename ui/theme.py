import flet as ft

# -----------------------------
#  TEMA ACTIVO
# -----------------------------
CURRENT_THEME = "dark"

# -----------------------------
#  PALETAS MEJORADAS
# -----------------------------
THEMES = {
    "dark": {
        "APP_BG": "#121212",
        "CARD_BG": "#1F1F1F",
        "SURFACE_BG": "#262626",
        "BTN_BG": "#2F2F2F",
        "BTN_BG_HOVER": "#3A3A3A",
        "BTN_BORDER": "#555555",
        "TEXT_COLOR": "#FFFFFF",
        "TEXT_MUTED": "#CCCCCC",
        "ACCENT": "#00FF9C",
        "DANGER": "#FF6666",
    },
    "light": {
        "APP_BG": "#FFFFFF",
        "CARD_BG": "#EEEEEE",
        "SURFACE_BG": "#F5F5F5",
        "BTN_BG": "#DDDDDD",
        "BTN_BG_HOVER": "#CCCCCC",
        "BTN_BORDER": "#BBBBBB",
        "TEXT_COLOR": "#000000",
        "TEXT_MUTED": "#444444",
        "ACCENT": "#008F5A",
        "DANGER": "#CC3333",
    }
}

# -----------------------------
#  VARIABLES GLOBALES
# -----------------------------
APP_BG = ""
CARD_BG = ""
SURFACE_BG = ""
BTN_BG = ""
BTN_BG_HOVER = ""
BTN_BORDER = ""
TEXT_COLOR = ""
TEXT_MUTED = ""
ACCENT = ""
DANGER = ""

BORDER_RADIUS = 12
ANIMATION_MS = 200


# -----------------------------
#  SYNC
# -----------------------------
def _sync():
    global APP_BG, CARD_BG, SURFACE_BG
    global BTN_BG, BTN_BG_HOVER, BTN_BORDER
    global TEXT_COLOR, TEXT_MUTED, ACCENT, DANGER

    t = THEMES[CURRENT_THEME]
    APP_BG = t["APP_BG"]
    CARD_BG = t["CARD_BG"]
    SURFACE_BG = t["SURFACE_BG"]
    BTN_BG = t["BTN_BG"]
    BTN_BG_HOVER = t["BTN_BG_HOVER"]
    BTN_BORDER = t["BTN_BORDER"]
    TEXT_COLOR = t["TEXT_COLOR"]
    TEXT_MUTED = t["TEXT_MUTED"]
    ACCENT = t["ACCENT"]
    DANGER = t["DANGER"]


# -----------------------------
#  APLICAR TEMA
# -----------------------------
def apply_theme(page: ft.Page):
    _sync()
    page.bgcolor = APP_BG
    page.padding = 30
    page.theme_mode = (
        ft.ThemeMode.DARK if CURRENT_THEME == "dark" else ft.ThemeMode.LIGHT
    )
    page.update()


# -----------------------------
#  TOGGLE
# -----------------------------
def toggle_app_theme(page: ft.Page):
    global CURRENT_THEME
    CURRENT_THEME = "light" if CURRENT_THEME == "dark" else "dark"
    apply_theme(page)
    page.update()


# -----------------------------
#  UI HELPERS
# -----------------------------
def title(text: str):
    return ft.Text(text, size=28, weight=ft.FontWeight.BOLD, color=TEXT_COLOR)


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
            shape=ft.RoundedRectangleBorder(radius=10),
            elevation=0
        )
    )


def input_field(label: str, password: bool = False):
    return ft.TextField(
        label=label,
        password=password,
        bgcolor=SURFACE_BG,
        color=TEXT_COLOR,
        border_color=BTN_BORDER,
        focused_border_color=ACCENT,
        label_style=ft.TextStyle(color=TEXT_MUTED),
        text_style=ft.TextStyle(color=TEXT_COLOR),
        border_radius=10
    )


def card(content):
    return ft.Container(
        content=content,
        bgcolor=CARD_BG,
        padding=24,
        border_radius=BORDER_RADIUS
    )
