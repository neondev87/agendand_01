import flet as ft

def LoginView(page: ft.Page):

    # ------------------------------
    # COLORES (DISEÑO FIJO)
    # ------------------------------
    BG = "#0F0F0F"
    CARD = "#1A1A1A"
    GREEN = "#00FF9C"
    ERROR = "#FF5C5C"

    # ------------------------------
    # MENSAJE DE ERROR
    # ------------------------------
    msg = ft.Text("", size=13, color=ERROR)

    # ------------------------------
    # FUNCIÓN LOGIN
    # ------------------------------
    def do_login(e=None):
        msg.value = ""

        user = username.value.strip()
        pwd = password.value.strip()

        if not user or not pwd:
            msg.value = "Completa todos los campos"
            page.update()
            return

        # 🔒 bloquear botón para evitar doble submit
        login_btn.disabled = True
        page.update()

        try:
            # aquí luego conectarás tu UserModel real
            user_data = {"username": user}

            page.session.set("user", user_data)
            page.client_storage.set("user", user_data)  # 🔐 persistente

            page.go("/menu")

        except Exception:
            msg.value = "Error al iniciar sesión"
            login_btn.disabled = False
            page.update()


    # ------------------------------
    # CAMPOS
    # ------------------------------
    username = ft.TextField(
        label="Usuario",
        color=GREEN,
        border_color=GREEN,
        focused_border_color=GREEN,
        label_style=ft.TextStyle(color=GREEN),
        bgcolor="#121212",
        autofocus=True,
        on_submit=do_login
    )

    password = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        color="white",
        border_color="white24",
        focused_border_color="white",
        label_style=ft.TextStyle(color="white54"),
        bgcolor="#121212",
        on_submit=do_login
    )

    # ------------------------------
    # BOTÓN
    # ------------------------------
    login_btn = ft.ElevatedButton(
        text="Entrar",
        on_click=do_login,
        width=420,
        height=48,
        bgcolor=GREEN,
        color="black"
    )

    # ------------------------------
    # TARJETA CENTRAL
    # ------------------------------
    card = ft.Container(
        width=450,
        bgcolor=CARD,
        padding=40,
        border_radius=20,
        content=ft.Column(
            [
                ft.Text("Bienvenido", size=34, color="white", weight=ft.FontWeight.BOLD),
                ft.Text("Login", size=18, color="white60"),

                ft.Divider(height=25, color="transparent"),

                username,
                password,
                msg,

                ft.Divider(height=10, color="transparent"),

                login_btn,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16
        )
    )

    # ------------------------------
    # VIEW FINAL
    # ------------------------------
    return ft.View(
        route="/",
        bgcolor=BG,
        controls=[
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=card
            )
        ]
    )
