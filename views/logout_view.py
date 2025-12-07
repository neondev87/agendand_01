import flet as ft
from ui.theme import TEXT_COLOR

def LogoutView(page):
    return ft.View(
        route="/logout",
        bgcolor="#1E1E1E",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                [
                    ft.Text("Sesión cerrada", size=30, weight="bold", color=TEXT_COLOR),
                    ft.Text("Gracias por usar la app.", size=18, color=TEXT_COLOR),
                    ft.ElevatedButton(
                        "Ir al inicio",
                        on_click=lambda e: page.go("/login"),
                        bgcolor="#3A3A3A",
                        color=TEXT_COLOR,
                        height=45,
                        width=180
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
    )
