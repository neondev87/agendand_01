import flet as ft
from models.usser_model import UserModel

def RegisterView(page: ft.Page):
    # Campos
    username = ft.TextField(label="Usuario", width=360, bgcolor="#2A2A2A", border_color="#444", autofocus=True)
    email = ft.TextField(label="Correo", width=360, bgcolor="#2A2A2A", border_color="#444")
    password = ft.TextField(label="Contraseña", width=360, password=True, bgcolor="#2A2A2A", border_color="#444")
    msg = ft.Text("", color="#FF6464", size=14)

    btn_style = ft.ButtonStyle(
        bgcolor="#2F2F2F",
        color="white",
        shape=ft.RoundedRectangleBorder(radius=6),
        padding=12,
        elevation=2,
    )

    # Funciones
    def register(e):
        msg.value = ""
        if not username.value or not email.value or not password.value:
            msg.value = "Completa todos los campos"
            page.update()
            return

        ok = UserModel.register(username.value, email.value, password.value)
        if ok:
            msg.value = "Usuario registrado exitosamente"
            msg.color = "#7ED957"
            # opcional: navegar al login automáticamente
            # page.go("/")
        else:
            msg.value = "Error registrando usuario"
            msg.color = "#FF6464"
        page.update()

    def go_login(e):
        page.go("/")

    # Vista centrada
    return ft.View(
        route="/register",
        bgcolor="#1E1E1E",
        controls=[
            ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Crear cuenta", size=28, weight=ft.FontWeight.BOLD, color="white"),
                                ft.Container(height=18),
                                username,
                                email,
                                password,
                                msg,
                                ft.Row(
                                    [
                                        ft.ElevatedButton("Registrar", on_click=register, style=btn_style),
                                        ft.ElevatedButton("Volver al login", on_click=go_login, style=btn_style),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=12
                                )
                            ],
                            spacing=14,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            width=360
                        ),
                        alignment=ft.alignment.center,
                        padding=20
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        ]
    )
