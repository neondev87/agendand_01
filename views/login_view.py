import flet as ft


# ======================================================
# BACKEND / LÓGICA
# ======================================================

def validate_login(username: str, password: str) -> tuple[bool, str]:
    """
    Valida credenciales (placeholder).
    Aquí luego conectarás DB / API / modelo real.
    """
    if not username or not password:
        return False, "Completa todos los campos"

    # lógica futura (ej: hash, DB, etc.)
    return True, ""


def login_user(page: ft.Page, username: str):
    """
    Manejo de sesión (backend).
    """
    user_data = {"username": username}
    page.session.set("user", user_data)
    page.client_storage.set("user", user_data)


# ======================================================
# FRONTEND / VISTA
# ======================================================

def LoginView(page: ft.Page):

    # ------------------------------
    # COLORES / THEME LOCAL
    # ------------------------------
    BG = "#0F0F0F"
    CARD = "#1A1A1A"
    GREEN = "#00FF9C"
    ERROR = "#FF5C5C"

    # ------------------------------
    # COMPONENTES DE ESTADO
    # ------------------------------
    msg = ft.Text("", size=13, color=ERROR)

    # ------------------------------
    # HERO (IMAGEN)
    # ------------------------------
    hero = ft.Container(
        width=500,
        alignment=ft.alignment.center,
        scale=1.0,
        animate_scale=ft.Animation(250, ft.AnimationCurve.EASE_OUT),
        border_radius=24,                          # 🔵 bordes
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS, # 🔵 recorte real
        content=ft.Image(
            src="images/hero_login.png",
            fit=ft.ImageFit.CONTAIN
        )
    )

    def hero_zoom(active: bool):
        hero.scale = 1.05 if active else 1.0
        hero.update()

    # ------------------------------
    # INPUTS (REFERENCIAS REALES)
    # ------------------------------
    username_field = ft.TextField(
        label="Usuario",
        autofocus=True,
        bgcolor="#121212",
        color=GREEN,
        border_color=GREEN,
        focused_border_color=GREEN,
        label_style=ft.TextStyle(color=GREEN),
    )

    password_field = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        bgcolor="#121212",
        color="white",
        border_color="white24",
        focused_border_color="white",
        label_style=ft.TextStyle(color="white54"),
    )

    # Wrappers SOLO para hover
    username = ft.Container(
        on_hover=lambda e: hero_zoom(e.data == "true"),
        content=username_field
    )

    password = ft.Container(
        on_hover=lambda e: hero_zoom(e.data == "true"),
        content=password_field
    )

    # ------------------------------
    # LOGIN ACTION
    # ------------------------------
    def do_login(e=None):
        msg.value = ""

        user = username_field.value.strip()
        pwd = password_field.value.strip()

        valid, error = validate_login(user, pwd)
        if not valid:
            msg.value = error
            page.update()
            return

        login_btn.disabled = True
        page.update()

        try:
            login_user(page, user)
            page.go("/menu")

        except Exception:
            msg.value = "Error al iniciar sesión"
            login_btn.disabled = False
            page.update()

    username_field.on_submit = do_login
    password_field.on_submit = do_login

    # ------------------------------
    # BOTÓN
    # ------------------------------
    login_btn = ft.ElevatedButton(
        text="Entrar",
        width=420,
        height=48,
        bgcolor=GREEN,
        color="black",
        on_click=do_login,
        on_hover=lambda e: hero_zoom(e.data == "true")
    )

    # ------------------------------
    # CARD LOGIN
    # ------------------------------
    card = ft.Container(
        width=450,
        bgcolor=CARD,
        padding=40,
        border_radius=20,
        content=ft.Column(
            spacing=16,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=8,
                    controls=[
                        ft.Text(
                            "🔥",
                            size=30,
                            color="#FF3B30"   # rojo elegante (tipo iOS)
                        ),
                        ft.Text(
                            "Bienvenido",
                            size=34,
                            weight=ft.FontWeight.BOLD,
                            color="white"
                        )
                    ]
                ),

                ft.Text("Login", size=18, color="white60"),
                ft.Divider(height=25, color="transparent"),
                username,
                password,
                msg,
                ft.Divider(height=10, color="transparent"),
                login_btn,
            ]
        )
    )

    # ------------------------------
    # LAYOUT
    # ------------------------------
    layout = ft.Row(
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[hero, card]
    )

    return ft.View(
        route="/",
        bgcolor=BG,
        controls=[layout]
    )
