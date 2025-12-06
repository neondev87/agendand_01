# ui/theme.py
import flet as ft

# -----------------------------
#  PALETA DE COLORES PRO
# -----------------------------
APP_BG = "#1E1E1E"           # Fondo general estilo ChatGPT
CARD_BG = "#242424"          # Cajas y contenedores
SURFACE_BG = "#2D2D2D"       # Superficies más claras
BTN_BG = "#3A3A3A"           # Botón normal
BTN_BG_HOVER = "#4A4A4A"     # Hover suave
BTN_BORDER = "#5A5A5A"       # Bordes muy sutiles estilo VSCode
TEXT_COLOR = "#FFFFFF"       # Texto principal
TEXT_MUTED = "#B0B0B0"       # Texto menos importante


# -----------------------------
#  TEMA GLOBAL
# -----------------------------
def apply_dark_theme(page: ft.Page):
    page.theme_mode = "dark"
    page.bgcolor = APP_BG
    page.padding = 40
    page.fonts = {
        "inter": "https://rsms.me/inter/inter.ttf"
    }
    page.theme = ft.Theme(
        font_family="inter",
    )
    page.update()


# -----------------------------
#  BOTÓN PRINCIPAL (PRO)
# -----------------------------
def primary_button(text: str, on_click=None, icon=None):
    return ft.ElevatedButton(
        text,
        icon=icon,
        on_click=on_click,
        bgcolor=BTN_BG,
        color=TEXT_COLOR,
        height=45,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            padding=20,
            overlay_color=BTN_BG_HOVER,
            elevation=1,
        )
    )


# -----------------------------
#  BOTÓN SECUNDARIO (OUTLINE)
# -----------------------------
def outline_button(text: str, on_click=None, icon=None):
    return ft.OutlinedButton(
        text,
        icon=icon,
        on_click=on_click,
        height=45,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=6),
            padding=20,
            side=ft.BorderSide(1, BTN_BORDER),
            color=TEXT_COLOR,
            overlay_color=BTN_BG_HOVER,
        )
    )


# -----------------------------
#  TARJETA / PANEL
# -----------------------------
def card(content):
    return ft.Container(
        content,
        bgcolor=CARD_BG,
        padding=20,
        border_radius=10,
    )
