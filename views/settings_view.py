import flet as ft
from ui import theme


def SettingsView(page: ft.Page, user=None):

    # ==========================
    # FUNCIONES
    # ==========================
    def toggle_theme(e):
        # Alterna dark/light en todo el sistema
        theme.toggle_app_theme(page)
        page.update()

    # ==========================
    # INFO USUARIO (SUPERIOR DERECHA)
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
    # TARJETA PRINCIPAL
    # ==========================
    settings_card = ft.Container(
        width=520,
        padding=30,
        border_radius=16,
        bgcolor=theme.CARD_BG,
        animate=ft.Animation(400, "easeOut"),
        shadow=ft.BoxShadow(
            blur_radius=20,
            color="#00000044",
            offset=ft.Offset(0, 6)
        ),
        content=ft.Column(
            [
                ft.Text(
                    "Configuración",
                    size=28,
                    color=theme.TEXT_COLOR,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Divider(color=theme.BTN_BORDER),

                ft.Text(
                    "Tema de la aplicación",
                    color=theme.TEXT_MUTED,
                    size=16
                ),

                ft.Container(
                    margin=ft.margin.only(top=10),
                    content=ft.IconButton(
                        icon=ft.icons.BRIGHTNESS_6,
                        icon_color=theme.TEXT_COLOR,
                        tooltip="Cambiar tema",
                        on_click=toggle_theme
                    )
                )
            ],
            spacing=20
        )
    )

    # ==========================
    # VISTA FINAL
    # ==========================
    return ft.View(
        "/settings",
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
