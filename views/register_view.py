import flet as ft
import ui.theme as theme
from models.usser_model import UserModel



def RegisterView(page: ft.Page):

    username = theme.input_field("Usuario", autofocus=True)
    email = theme.input_field("Correo")
    password = theme.input_field("Contraseña", password=True)

    msg = ft.Text("", color=theme.DANGER, size=14)

    def register(e):
        msg.value = ""

        if not username.value or not email.value or not password.value:
            msg.value = "Completa todos los campos"
            page.update()
            return

        ok = UserModel.register(username.value, email.value, password.value)

        if ok:
            msg.value = "Usuario registrado exitosamente"
            msg.color = theme.SUCCESS
        else:
            msg.value = "Error registrando usuario"
            msg.color = theme.DANGER

        page.update()

    def go_login(e):
        page.go("/")

    return ft.View(
        route="/register",
        bgcolor=theme.APP_BG,
        controls=[
            ft.Row(
                [
                    ft.Container(
                        padding=20,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Crear cuenta",
                                    size=28,
                                    weight=ft.FontWeight.BOLD,
                                    color=theme.TEXT_COLOR
                                ),
                                ft.Container(height=18),
                                username,
                                email,
                                password,
                                msg,
                                ft.Row(
                                    [
                                        theme.primary_button("Registrar", register),
                                        theme.secondary_button("Volver al login", go_login),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=12
                                )
                            ],
                            spacing=14,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            width=360
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True
            )
        ]
    )
