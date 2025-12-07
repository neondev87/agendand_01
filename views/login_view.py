import flet as ft


def LoginView(page: ft.Page):

    # ------------------------------
    # COLORES
    # ------------------------------
    BG = "#0F0F0F"
    CARD = "#1A1A1A"
    GREEN = "#00FF9C"

    # ------------------------------
    # CAMPOS
    # ------------------------------
    username = ft.TextField(
        label="Usuario",
        color=GREEN,
        border_color=GREEN,
        focused_border_color=GREEN,
        label_style=ft.TextStyle(color=GREEN),
        bgcolor="#121212"
    )

    password = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        color="white",
        border_color="white24",
        focused_border_color="white",
        label_style=ft.TextStyle(color="white54"),
        bgcolor="#121212"
    )

    # ------------------------------
    # FUNCIÓN LOGIN
    # ------------------------------
    def do_login(e):
        if username.value.strip() == "":
            return

        page.session.set("user", {"username": username.value})
        page.go("/menu")

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

                ft.Divider(height=20, color="transparent"),

                ft.ElevatedButton(
                    text="Entrar",
                    on_click=do_login,
                    width=420,
                    height=48,
                    bgcolor=GREEN,
                    color="black"
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=18
        )
    )

    # ------------------------------
    # VIEW FINAL
    # ------------------------------
    return ft.View(
        "/",
        bgcolor=BG,
        controls=[
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=card
            )
        ]
    )
