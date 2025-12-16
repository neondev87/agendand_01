import flet as ft
import ui.theme as theme
from components.navbar import Navbar


def calendar_view(page: ft.Page, user):
    nav = Navbar(page)

    content = ft.Column(
        [
            theme.title("Calendario"),

            # Aquí irá el contenido real del calendario
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
        route="/calendar",
        bgcolor=theme.APP_BG,
        controls=[layout]
    )
