import flet as ft
from components.navbar import Navbar


def mainmenu_view(page, user):

    # --------------------------
    # TARJETA DE PERFIL (estilo Steam simple)
    # --------------------------
    profile_card = ft.Container(
        bgcolor="#2A2A2A",
        padding=20,
        border_radius=12,
        width=500,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.CircleAvatar(
                            bgcolor="#444444",
                            radius=40,
                            content=ft.Icon(ft.icons.PERSON, color="white"),
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    user.get("username", "Usuario"),
                                    color="white",
                                    size=24,
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.Text(
                                    "Perfil básico (pronto estilo Steam)",
                                    color="#CCCCCC",
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

    # --------------------------
    # VISTA PRINCIPAL
    # --------------------------
    return ft.View(
        route="/menu",
        bgcolor="#1E1E1E",
        controls=[
            ft.Row(
                controls=[
                    # NAVBAR
                    Navbar(page),

                    # CONTENIDO PRINCIPAL
                    ft.Container(
                        expand=True,
                        padding=20,
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Menú Principal",
                                    size=28,
                                    color="white",
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.Divider(height=20, color="white24"),
                                profile_card
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            spacing=25,
                            expand=True
                        ),
                    )
                ],
                expand=True
            )
        ]
    )
