import flet as ft
from theme import apply_theme
from views.mainmenu_view import mainmenu_view
from views.calendar_view import calendar_view
from views.tareas_view import tareas_view
from models.usser_model import UserModel

def main(page: ft.Page):

    # ------------------------------
    # 1. Aplicar tema
    # ------------------------------
    apply_theme(page)

    # ------------------------------
    # 2. Configuración ventana
    # ------------------------------
    page.title = "Agenda App"
    page.window_width = 1000
    page.window_height = 700

    try:
        page.window_top = (page.screen.height - page.window_height) / 2
        page.window_left = (page.screen.width - page.window_width) / 2
    except:
        pass

    # ------------------------------
    # 3. Estilo para botones
    # ------------------------------
    button_style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=6),
        bgcolor="#2F2F2F",
        color="white",
        padding=15,
        elevation=3,
    )

    # ------------------------------
    # 4. Campos login / registro
    # ------------------------------
    username = ft.TextField(label="Usuario", width=300, bgcolor="#2A2A2A", border_color="#444", autofocus=True)
    email = ft.TextField(label="Correo", width=300, bgcolor="#2A2A2A", border_color="#444", visible=False)
    password = ft.TextField(label="Contraseña", width=300, password=True, bgcolor="#2A2A2A", border_color="#444")
    msg = ft.Text(color="#FF6464", size=14)

    # ------------------------------
    # 5. Funciones login / registro
    # ------------------------------
    def mostrar_registro(e):
        email.visible = True
        msg.value = ""
        page.update()

    def registrar_usuario(e):
        if not username.value or not email.value or not password.value:
            msg.value = "Completa todos los campos"
        else:
            ok = UserModel.register(username.value, email.value, password.value)
            msg.value = "Registro exitoso 😁" if ok else "Error registrando usuario"
        page.update()

    def iniciar_sesion(e):
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

    # ------------------------------
    # 6. Router
    # ------------------------------
    def route_change(route):
        page.views.clear()
        user = page.session.get("user")

        if page.route == "/":
            # Login view
            page.views.append(
                ft.View(
                    route="/",
                    bgcolor="#1E1E1E",
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Agenda Personal", size=32, weight=ft.FontWeight.BOLD, color="white"),
                        username,
                        email,
                        password,
                        msg,
                        ft.Row(
                            [
                                ft.ElevatedButton("Iniciar sesión", on_click=iniciar_sesion, style=button_style),
                                ft.ElevatedButton("Registrar", on_click=mostrar_registro, style=button_style),
                                ft.ElevatedButton("Confirmar registro", on_click=registrar_usuario, style=button_style),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ]
                )
            )
        elif page.route == "/menu":
            if not user:
                page.go("/")
                return
            page.views.append(mainmenu_view(page, user))
        elif page.route == "/calendar":
            if not user:
                page.go("/")
                return
            page.views.append(calendar_view(page, user))
        elif page.route == "/tareas":
            if not user:
                page.go("/")
                return
            page.views.append(tareas_view(page, user))

        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
