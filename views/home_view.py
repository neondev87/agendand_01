import flet as ft
from ui.theme import TEXT_COLOR
from components.navbar import Navbar


def HomeView(page, user):
    nav = Navbar(page)

    content = ft.Column(
        [
            ReturnButton(page, "/menu"),

            ft.Text(
                "Bienvenido a tu Agenda",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=TEXT_COLOR
            ),

            # Aquí podremos poner widgets del dashboard después
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
        bgcolor="#1E1E1E",
        controls=[layout]
    )
