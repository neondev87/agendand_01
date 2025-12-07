import flet as ft
from ui import theme


def SettingsView(page: ft.Page, user=None):

    # ==========================
    # TOGGLE THEME
    # ==========================
    def toggle_theme(e):
        theme.toggle_app_theme(page)
        actualizar_icono()
        page.update()

    # ==========================
    # ICONO DINÁMICO
    # ==========================
    def actualizar_icono():
        theme_icon.icon = (
            ft.icons.LIGHT_MODE if theme.CURRENT_THEME == "dark"
            else ft.icons.DARK_MODE
        )

    # ==========================
    # BOTÓN RETURN (ICONO ASSETS)
    # ==========================
    def volver_menu(e):
        page.go("/menu")

    return_btn = ft.Container(
        content=ft.Image(
            src="assets/return.png",   # cambia el nombre si tu archivo es otro
            width=28,
            height=28
        ),
        on_click=volver_menu,
        ink=True,
        border_radius=10,
        padding=6
    )

    # ==========================
    # USER INFO
    # ==========================
    user_info = ft.Container(
        alignment=ft.alignment.top_right,
        padding=10,
        content=ft.Row(
            [
                ft.Text(
                    user["username"] if user else "Invitado",
                    color=theme.TEXT_COLOR,
                    size=14,
                    weight=ft.FontWeight.BOLD
                ),
                ft.CircleAvatar(
                    bgcolor=theme.SURFACE_BG,
                    radius=16,
                    content=ft.Text(
                        (user["username"][0].upper() if user else "?"),
                        color=theme.TEXT_COLOR
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.END
        )
    )

    # ==========================
    # ICONO TEMA
    # ==========================
    theme_icon = ft.IconButton(
        icon=ft.icons.LIGHT_MODE if theme.CURRENT_THEME == "dark" else ft.icons.DARK_MODE,
        icon_color=theme.TEXT_COLOR,
        tooltip="Cambiar tema",
        on_click=toggle_theme
    )

    # ==========================
    # TARJETA
    # ==========================
    settings_card = ft.Container(
        width=520,
        padding=30,
        border_radius=20,
        bgcolor=theme.CARD_BG,
        animate=ft.Animation(300, "easeOut"),
        shadow=ft.BoxShadow(
            blur_radius=20,
            color="#00000033",
            offset=ft.Offset(0, 6)
        ),
        content=ft.Column(
            [
                ft.Row(
                    [
                        return_btn,
                        ft.Text(
                            "Configuración",
                            size=28,
                            color=theme.TEXT_COLOR,
                            weight=ft.FontWeight.BOLD
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10
                ),

                ft.Divider(color=theme.BTN_BORDER),

                ft.Text(
                    "Tema de la aplicación",
                    size=16,
                    color=theme.TEXT_MUTED
                ),

                theme_icon
            ],
            spacing=20
        )
    )

    # ==========================
    # ACTUALIZAR ICONO AL INICIO
    # ==========================
    actualizar_icono()

    # ==========================
    # VIEW FINAL
    # ==========================
    return ft.View(
        route="/settings",
        bgcolor=theme.APP_BG,
        controls=[
            user_info,
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=settings_card
            )
        ]
    )
