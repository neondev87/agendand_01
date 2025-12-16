import flet as ft
from ui import theme
from components.navbar import Navbar



def mainmenu_view(page, user):

    profile_card = ft.Container(
        bgcolor=theme.CARD_BG,
        padding=20,
        border_radius=theme.BORDER_RADIUS,
        width=500,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.CircleAvatar(
                            bgcolor=theme.SURFACE_BG,
                            radius=40,
                            content=ft.Icon(
                                ft.icons.PERSON,
                                color=theme.ICON_COLOR
                            ),
                        ),
                        ft.Column(
                            [
                                ft.Text(
                                    user.get("username", "Usuario"),
                                    color=theme.TEXT_COLOR,
                                    size=24,
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.Text(
                                    "Perfil básico (pronto estilo Steam)",
                                    color=theme.TEXT_MUTED,
                                    size=12
                                ),
                            ],
                            spacing=5
                        )
                    ],
                    spacing=20,
                )
            ],
            spacing=10
        )
    )

    return ft.View(
        route="/menu",
        bgcolor=theme.APP_BG,
        controls=[
            ft.Row(
                [
                    Navbar(page),

                    ft.Container(
                        expand=True,
                        padding=20,
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Menú Principal",
                                    size=28,
                                    color=theme.TEXT_COLOR,
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.Divider(height=20, color=theme.DIVIDER),
                                profile_card
                            ],
                            spacing=25,
                            expand=True
                        ),
                    )
                ],
                expand=True
            )
        ]
    )
