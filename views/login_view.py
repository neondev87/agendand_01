import flet as ft
from ui.theme import primary_button, TEXT_COLOR
from models.usser_model import UserModel

def LoginView(page: ft.Page):

    # Campos
    username = ft.TextField(label="Usuario", width=300)
    email = ft.TextField(label="Correo", visible=False, width=300)
    password = ft.TextField(label="Contraseña", password=True, width=300)
    msg = ft.Text(color="red")

    # Botones
    btn_login = primary_button("Iniciar sesión", lambda e: login())
    btn_register = primary_button("Registrarme", lambda e: show_register())
    btn_confirm = primary_button("Confirmar", lambda e: register())
    btn_cancel = primary_button("Cancelar", lambda e: cancel_register())

    # Fila dinámica de botones
    buttons_row = ft.Row(
        controls=[btn_login, btn_register],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # Funciones
    def show_register():
        email.visible = True
        msg.value = ""
        # Cambiar botones
        buttons_row.controls = [btn_confirm, btn_cancel]
        # Animación de aparición
        for b in buttons_row.controls:
            b.animate_scale = 0.5
            b.scale = 1.0
        page.update()

    def cancel_register():
        email.visible = False
        msg.value = ""
        buttons_row.controls = [btn_login, btn_register]
        page.update()

    def register():
        if not username.value or not email.value or not password.value:
            msg.value = "Completa todos los campos"
        else:
            ok = UserModel.register(username.value, email.value, password.value)
            msg.value = "Usuario registrado 😁" if ok else "Error registrando usuario"
        page.update()

    def login():
        msg.value = ""
        if not username.value or not password.value:
            msg.value = "Completa usuario y contraseña"
            page.update()
            return

        user = UserModel.login(username.value, password.value)
        if user:
            page.session.set("user", user)
            page.go("/menu")
        else:
            msg.value = "Usuario o contraseña incorrectos"
        page.update()

    # Vista completa
    return ft.View(
        route="/",
        bgcolor="#1E1E1E",
        controls=[
            ft.Column(
                [
                    ft.Text("Agenda – Login", size=22, color=TEXT_COLOR),
                    username,
                    email,
                    password,
                    msg,
                    buttons_row
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        ]
    )
