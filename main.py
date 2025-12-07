import flet as ft
from ui.theme import apply_theme

# VISTAS
from views.mainmenu_view import mainmenu_view
from views.calendar_view import calendar_view
from views.tareas_view import tareas_view
from views.login_view import LoginView
from views.register_view import RegisterView
from views.settings_view import SettingsView


def main(page: ft.Page):

    # ------------------------------
    # Tema general (controlado por ui.theme)
    # ------------------------------
    apply_theme(page)

    # ------------------------------
    # Configuración de ventana (MODERNA)
    # ------------------------------
    page.title = "Agenda App"

    page.window.width = 1200
    page.window.height = 800

    # Centrar ventana
    try:
        page.window.top = (page.screen.height - page.window.height) / 2
        page.window.left = (page.screen.width - page.window.width) / 2
    except:
        pass

    # ------------------------------
    # Router
    # ------------------------------
    def route_change(route):
        page.views.clear()
        user = page.session.get("user")

        if page.route == "/":
            page.views.append(LoginView(page))

        elif page.route == "/register":
            page.views.append(RegisterView(page))

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

        elif page.route == "/settings":
            if not user:
                page.go("/")
                return
            page.views.append(SettingsView(page, user))

        page.update()

    page.on_route_change = route_change

    # Iniciar app
    page.go("/")


# IMPORTANTE: habilitar carpeta de assets
ft.app(target=main, assets_dir="assets")
