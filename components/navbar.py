import flet as ft
from ui.theme import SURFACE_BG, TEXT_COLOR


def Navbar(page):
    return ft.Container(
        width=80,
        bgcolor=SURFACE_BG,  # ✅ usa el color centralizado
        padding=10,
        content=ft.Column(
            controls=[
                ft.Icon(ft.icons.MENU, color=TEXT_COLOR, size=30),
                ft.Divider(height=20, color="white24"),

                ft.IconButton(
                    icon=ft.icons.HOME,
                    icon_color=TEXT_COLOR,
                    tooltip="Inicio",
                    on_click=lambda e: page.go("/menu")
                ),

                ft.IconButton(
                    icon=ft.icons.CALENDAR_MONTH,
                    icon_color=TEXT_COLOR,
                    tooltip="Calendario",
                    on_click=lambda e: page.go("/calendar")
                ),

                ft.IconButton(
                    icon=ft.icons.CHECKLIST,
                    icon_color=TEXT_COLOR,
                    tooltip="Tareas",
                    on_click=lambda e: page.go("/tareas")
                ),

                ft.IconButton(
                    icon=ft.icons.SETTINGS,
                    icon_color=TEXT_COLOR,
                    tooltip="Configuración",
                    on_click=lambda e: page.go("/settings")
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )
