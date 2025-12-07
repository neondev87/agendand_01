import flet as ft
from components.navbar import Navbar

def calendar_view(page: ft.Page, user):
    nav = Navbar(page)

    content = ft.Column(
        [
            ft.Text(
                "Calendario",
                size=28,
                weight=ft.FontWeight.BOLD,
                color="white"
            ),

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
        controls=[layout],
        bgcolor="#1E1E1E"
    )
