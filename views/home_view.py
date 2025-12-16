import flet as ft
import ui.theme as theme
from components.navbar import Navbar


def HomeView(page, user):
    nav = Navbar(page)

    content = ft.Column(
        [
            ft.Text(
                "Bienvenido a tu Agenda",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=theme.TEXT_COLOR
            ),
            # widgets del dashboard después
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        expand=True
    )

    layout = ft.Row(
        [
            nav,
            ft.Container(width=20),
            content
        ],
        expand=True
    )

    return ft.View(
        route="/home",
        bgcolor=theme.APP_BG,
        controls=[layout]
    )
