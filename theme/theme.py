import flet as ft

def apply_theme(page: ft.Page):
    page.title = "Agenda App"
    page.theme_mode = "dark"
    page.bgcolor = "#1E1E1E"
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary="#10A37F",
            secondary="#2A2A2A",
            on_primary="#FFFFFF",
            background="#1E1E1E",
            surface="#2C2C2C",
        )
    )
