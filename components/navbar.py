import flet as ft
import ui.theme as theme


def Navbar(page: ft.Page):

    # =====================================
    # ESTADO GLOBAL (SESSION)
    # =====================================
    if page.session.get("nav_collapsed") is None:
        page.session.set("nav_collapsed", False)

    nav = ft.Container(
        padding=14,
        bgcolor=theme.SURFACE_BG,
        border_radius=16,
        animate=ft.Animation(250, ft.AnimationCurve.EASE_OUT),
    )

    # =====================================
    # HELPERS
    # =====================================
    def safe_go(route: str):
        if page.route != route:
            page.go(route)

    def toggle_nav(e):
        current = page.session.get("nav_collapsed")
        page.session.set("nav_collapsed", not current)
        render()
        page.update()

    def nav_icon(icon, route, tooltip):
        active = page.route == route

        return ft.Container(
            width=44,
            height=44,
            border_radius=12,
            alignment=ft.alignment.center,
            ink=True,
            on_click=lambda e: safe_go(route),
            content=ft.Icon(
                icon,
                size=22,
                color=theme.TEXT_COLOR if active else theme.ICON_COLOR,
            ),
            tooltip=tooltip,
        )

    # =====================================
    # RENDER DINÁMICO
    # =====================================
    def render():
        collapsed = page.session.get("nav_collapsed")

        nav.width = 56 if collapsed else 80

        if collapsed:
            nav.content = ft.Column(
                spacing=18,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=44,
                        height=44,
                        border_radius=12,
                        alignment=ft.alignment.center,
                        ink=True,
                        on_click=toggle_nav,
                        content=ft.Icon(
                            ft.icons.CHEVRON_RIGHT,
                            size=22,
                            color=theme.TEXT_MUTED,
                        ),
                    ),
                ],
            )
        else:
            nav.content = ft.Column(
                spacing=18,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=44,
                        height=44,
                        border_radius=12,
                        alignment=ft.alignment.center,
                        ink=True,
                        on_click=toggle_nav,
                        content=ft.Icon(
                            ft.icons.MENU,
                            size=22,
                            color=theme.TEXT_COLOR,
                        ),
                    ),

                    nav_icon(ft.icons.HOME, "/menu", "Inicio"),
                    nav_icon(ft.icons.CALENDAR_MONTH, "/calendar", "Calendario"),
                    nav_icon(ft.icons.CHECKLIST, "/tareas", "Tareas"),
                    nav_icon(ft.icons.SETTINGS, "/settings", "Configuración"),
                ],
            )

    # render inicial
    render()

    return nav
