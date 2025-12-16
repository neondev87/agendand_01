import flet as ft
import ui.theme as theme


def SettingsView(page: ft.Page, user=None):

    # -------------------------------
    # HANDLERS
    # -------------------------------
    def volver_menu(e):
        page.go("/menu")

    def cerrar_sesion(e):
        page.session.clear()
        page.client_storage.remove("user")
        page.go("/")

    def toggle_theme(e):
        theme.toggle_theme(page)
        page.update()

    # -------------------------------
    # BOTÓN REGRESAR
    # -------------------------------
    return_btn = ft.TextButton(
        content=ft.Row(
            spacing=6,
            controls=[
                ft.Icon(ft.icons.ARROW_BACK, size=18, color=theme.TEXT_MUTED),
                ft.Text("Regresar", size=13, color=theme.TEXT_COLOR),
            ],
        ),
        on_click=volver_menu,
    )

    # -------------------------------
    # USER INFO
    # -------------------------------
    user_info = ft.Row(
        spacing=10,
        controls=[
            ft.Text(
                user["username"] if user else "Invitado",
                size=13,
                color=theme.TEXT_COLOR,
                weight=ft.FontWeight.W_600,
            ),
            ft.CircleAvatar(
                radius=16,
                bgcolor=theme.SURFACE_BG,
                content=ft.Text(
                    user["username"][0].upper() if user else "?",
                    color=theme.TEXT_COLOR,
                ),
            ),
        ],
    )

    # -------------------------------
    # LOGOUT (ROJO FIJO)
    # -------------------------------
    logout_btn = ft.Container(
        height=48,
        border_radius=20,
        alignment=ft.alignment.center,
        bgcolor="#8B2C2C",  # 🔥 ROJO ELEGANTE FIJO
        ink=True,
        on_click=cerrar_sesion,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8,
            controls=[
                ft.Icon(ft.icons.LOGOUT, color="white", size=18),
                ft.Text(
                    "Cerrar sesión",
                    color="white",
                    size=14,
                    weight=ft.FontWeight.W_600,
                ),
            ],
        ),
    )

    # -------------------------------
    # MODAL CARD ÚNICO (GRIS CLARO)
    # -------------------------------
    settings_modal = ft.Container(
        width=560,
        padding=40,
        border_radius=32,
        bgcolor="#323846",  # 🔥 GRIS CLARO PREMIUM
        content=ft.Column(
            spacing=26,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[return_btn, user_info],
                ),

                ft.Text(
                    "Configuración",
                    size=28,
                    weight=ft.FontWeight.W_700,
                    color=theme.TEXT_COLOR,
                ),

                ft.Text(
                    "Preferencias de la aplicación",
                    size=14,
                    color=theme.TEXT_MUTED,
                ),

                ft.Container(
                    padding=16,
                    border_radius=18,
                    bgcolor=theme.SURFACE_BG,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("Modo oscuro", size=15, color=theme.TEXT_COLOR),
                            ft.Switch(
                                value=theme.CURRENT_THEME == "dark",
                                on_change=toggle_theme,
                            ),
                        ],
                    ),
                ),

                logout_btn,
            ],
        ),
    )

    # -------------------------------
    # FINAL
    # -------------------------------
    return ft.Stack(
        expand=True,
        controls=[
            ft.Container(expand=True, bgcolor=theme.APP_BG),
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                content=settings_modal,
            ),
        ],
    )
