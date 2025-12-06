import flet as ft
from components.navbar import Navbar

def tareas_view(page: ft.Page, user):
    nav = Navbar(page)

    content = ft.Column(
        [
            ft.Text("Tareas", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        ],
        alignment=ft.MainAxisAlignment.START
    )

    layout = ft.Row([nav, ft.Container(width=20), content], expand=True)

    return ft.View(route="/tareas", controls=[layout])
