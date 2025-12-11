import flet as ft
import ui.theme as theme
from components.navbar import Navbar


def SettingsView(page: ft.Page, user=None):

    # Sincroniza tema
    theme._sync()

    # =====================================================
    # CAMBIAR TEMA
    # =====================================================
    def toggle_theme(e):
        theme.toggle_app_theme(page)
        actualizar_icono()
        page.update()

    def actualizar_icono():
        theme_icon.icon = (
            ft.icons.LIGHT_MODE if theme.CURRENT_THEME == "dark"
            else ft.icons.DARK_MODE
        )

    # =====================================================
    # VOLVER AL MENÚ
    # =====================================================
    def volver_menu(e):
        page.go("/menu")

    return_btn = ft.Container(
        bgcolor="#D32F2F",
        padding=8,
        border_radius=12,
        ink=True,
        on_click=volver_menu,
        on_hover=lambda e: (
            setattr(e.control, "bgcolor", "#B71C1C") if e.data == "true"
            else setattr(e.control, "bgcolor", "#D32F2F"),
            page.update()
        ),
        content=ft.Row(
            [
                ft.Icon(ft.icons.ARROW_BACK, color="white", size=20),
                ft.Text("Regresar", color="white",
                        size=14, weight=ft.FontWeight.BOLD)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    # =====================================================
    # USER INFO
    # =====================================================
    user_info = ft.Container(
        alignment=ft.alignment.top_right,
        padding=20,
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
                        user["username"][0].upper() if user else "?",
                        color=theme.TEXT_COLOR
                    )
                )
            ],
            spacing=10
        )
    )

    # =====================================================
    # ICONO DE TEMA
    # =====================================================
    theme_icon = ft.IconButton(
        icon=ft.icons.LIGHT_MODE if theme.CURRENT_THEME == "dark" else ft.icons.DARK_MODE,
        icon_color=theme.TEXT_COLOR,
        tooltip="Cambiar tema",
        on_click=toggle_theme
    )

    # =====================================================
    # BOTÓN CERRAR SESIÓN
    # =====================================================
    def cerrar_sesion(e):
        page.session.clear()
        page.update()
        page.go("/")

    logout_btn = ft.Container(
        bgcolor="#C62828",
        padding=12,
        border_radius=12,
        ink=True,
        on_click=cerrar_sesion,
        on_hover=lambda e: (
            setattr(e.control, "bgcolor", "#8E0000") if e.data == "true"
            else setattr(e.control, "bgcolor", "#C62828"),
            page.update()
        ),
        content=ft.Row(
            [
                ft.Icon(ft.icons.LOGOUT, color="white", size=20),
                ft.Text("Cerrar sesión", color="white", size=14),
            ],
            spacing=8,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    # =====================================================
    # TARJETA DE CONFIGURACIÓN
    # =====================================================
    settings_card = ft.Container(
        width=520,
        padding=30,
        border_radius=20,
        bgcolor=theme.CARD_BG,
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
                ),

                ft.Divider(color=theme.BTN_BORDER),

                ft.Text("Tema de la aplicación",
                        color=theme.TEXT_MUTED, size=16),
                theme_icon,

                ft.Divider(color=theme.BTN_BORDER),

                ft.Text("Cuenta", color=theme.TEXT_MUTED, size=16),
                logout_btn
            ],
            spacing=20
        )
    )

    actualizar_icono()

    # =====================================================
    # VISTA FINAL – navbar + contenido centrado sin bugs
    # =====================================================
    return ft.View(
        route="/settings",
        bgcolor=theme.APP_BG,
        controls=[
            ft.Row(
                [
                    Navbar(page),
                    ft.Container(
                        expand=True,
                        bgcolor=theme.APP_BG,   # ← FIX FINAL
                        content=ft.Column(
                            [
                                user_info,
                                ft.Container(
                                    expand=True,
                                    alignment=ft.alignment.center,
                                    content=settings_card
                                )
                            ],
                            expand=True
                        )
                    )
                ],
                expand=True
            )
        ]
    )
