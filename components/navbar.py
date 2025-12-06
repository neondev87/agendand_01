import flet as ft

def Navbar(page: ft.Page):
    return ft.Container(
        width=200,
        bgcolor=ft.Colors.GREY_800,
        padding=10,
        content=ft.Column(
            [
                ft.Text("Menú", size=20, color=ft.Colors.WHITE),
                ft.ElevatedButton("Inicio", on_click=lambda e: page.go("/")),
                ft.ElevatedButton("Calendario", on_click=lambda e: page.go("/calendar")),
                ft.ElevatedButton("Tareas", on_click=lambda e: page.go("/tareas")),
                # Agrega más botones de futuras vistas aquí
            ],
            spacing=10
        )
    )
