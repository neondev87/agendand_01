import flet as ft
from components.navbar import Navbar

def mainmenu_view(page: ft.Page, user):
    # Navbar
    nav = Navbar(page)

    # Contenido principal
    main_content = ft.Column(
        [
            ft.Text(f"Bienvenido, {user['username']}!", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Text("Selecciona una opción del menú", color=ft.Colors.GREY_300)
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20,
    )

    # Layout completo
    layout = ft.Row(
        [
            nav,
            ft.Container(width=20),  # Espaciado
            main_content
        ],
        expand=True
    )

    return ft.View(
        route="/menu",
        controls=[layout]
    )
