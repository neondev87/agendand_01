import flet as ft
from ui.theme import TEXT_COLOR, primary_button

def HomeView(page):
    return ft.View(
        "/home",
        bgcolor="#1E1E1E",
        controls=[
            ft.Column([
                ft.Text("Bienvenido a tu Agenda", size=25, color=TEXT_COLOR),
                primary_button("Cerrar sesión", lambda e: page.go("/")),
            ], alignment=ft.MainAxisAlignment.CENTER)
        ]
    )
