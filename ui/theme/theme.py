import flet as ft
from config.theme.theme_store import ThemeStore


# =====================================================
# ESTADO DEL TEMA
# =====================================================
CURRENT_THEME = "dark"

# =====================================================
# PALETAS DEFINITIVAS (PROFESIONAL)
# =====================================================
THEMES = {
    "dark": {
        "APP_BG": "#0D1015",
        "SURFACE_BG": "#161B24",
        "CARD_BG": "#202634",

        "BTN_BG": "#232938",
        "BTN_BG_HOVER": "#2A3142",
        "BTN_BORDER": "#00000000",  # sin líneas

        "TEXT_COLOR": "#E7EAF0",
        "TEXT_MUTED": "#9AA1B2",
        "ICON_COLOR": "#C9CED8",

        "ACCENT": "#E7EAF0",
        "DANGER": "#8B2C2C",        # rojo elegante
        "DIVIDER": "#2A3040",
    },

    "light": {
        "APP_BG": "#F1F3F6",
        "SURFACE_BG": "#E5E8EE",
        "CARD_BG": "#FFFFFF",

        "BTN_BG": "#E2E6EC",
        "BTN_BG_HOVER": "#D6DBE4",
        "BTN_BORDER": "#C4CBD6",

        "TEXT_COLOR": "#1E232B",
        "TEXT_MUTED": "#5F6775",
        "ICON_COLOR": "#1E232B",

        "ACCENT": "#6B7F7C",
        "DANGER": "#C62828",
        "DIVIDER": "#D1D6DF",
    }
}

# =====================================================
# VARIABLES GLOBALES
# =====================================================
APP_BG = ""
CARD_BG = ""
SURFACE_BG = ""
BTN_BG = ""
BTN_BG_HOVER = ""
BTN_BORDER = ""
TEXT_COLOR = ""
TEXT_MUTED = ""
ICON_COLOR = ""
ACCENT = ""
DANGER = ""
DIVIDER = ""

# =====================================================
# CONFIG GENERAL
# =====================================================
BORDER_RADIUS = 12
ANIMATION_MS = 200

# =====================================================
# SYNC INTERNO
# =====================================================
def _sync():
    global APP_BG, CARD_BG, SURFACE_BG
    global BTN_BG, BTN_BG_HOVER, BTN_BORDER
    global TEXT_COLOR, TEXT_MUTED, ICON_COLOR
    global ACCENT, DANGER, DIVIDER

    theme = THEMES[CURRENT_THEME]

    APP_BG = theme["APP_BG"]
    CARD_BG = theme["CARD_BG"]
    SURFACE_BG = theme["SURFACE_BG"]
    BTN_BG = theme["BTN_BG"]
    BTN_BG_HOVER = theme["BTN_BG_HOVER"]
    BTN_BORDER = theme["BTN_BORDER"]
    TEXT_COLOR = theme["TEXT_COLOR"]
    TEXT_MUTED = theme["TEXT_MUTED"]
    ICON_COLOR = theme["ICON_COLOR"]
    ACCENT = theme["ACCENT"]
    DANGER = theme["DANGER"]
    DIVIDER = theme["DIVIDER"]

# =====================================================
# LOAD / SAVE
# =====================================================
def load_theme():
    global CURRENT_THEME
    data = ThemeStore.load() or {}
    CURRENT_THEME = data.get("current_theme", "dark")
    _sync()

def save_theme():
    ThemeStore.save({"current_theme": CURRENT_THEME})

# =====================================================
# APLICAR A FLET
# =====================================================
def apply_theme(page: ft.Page):
    _sync()
    page.bgcolor = APP_BG
    page.theme_mode = (
        ft.ThemeMode.DARK
        if CURRENT_THEME == "dark"
        else ft.ThemeMode.LIGHT
    )

# =====================================================
# TOGGLE
# =====================================================
def toggle_theme(page: ft.Page):
    global CURRENT_THEME
    CURRENT_THEME = "light" if CURRENT_THEME == "dark" else "dark"
    save_theme()
    apply_theme(page)

# =====================================================
# HELPERS UI
# =====================================================
def title(text: str):
    return ft.Text(text, size=28, weight=ft.FontWeight.BOLD, color=TEXT_COLOR)

def subtitle(text: str):
    return ft.Text(text, size=16, color=TEXT_MUTED)

def primary_button(text: str, on_click=None, icon=None):
    return ft.ElevatedButton(
        text=text,
        icon=icon,
        on_click=on_click,
        bgcolor=BTN_BG,
        color=TEXT_COLOR,
        height=46,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=BORDER_RADIUS),
            elevation=0,
        ),
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
        border_radius=BORDER_RADIUS,
    )

def card(content):
    return ft.Container(
        content=content,
        bgcolor=CARD_BG,
        padding=24,
        border_radius=BORDER_RADIUS,
    )
