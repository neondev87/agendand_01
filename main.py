import flet as ft

from views.login_view import LoginView
from views.register_view import RegisterView
from views.mainmenu_view import mainmenu_view
from views.calendar_view import calendar_view
from views.tareas_view import tareas_view
from views.settings_view import SettingsView

from ui.theme import load_theme, apply_theme


def main(page: ft.Page):

    # --------------------------------
    # Cargar tema UNA sola vez
    # --------------------------------
    load_theme()
    apply_theme(page)
#   restaurar sesión
    saved_user = page.client_storage.get("user")
    if saved_user:
        page.session.set("user", saved_user)

    # --------------------------------
    # Config ventana
    # --------------------------------
    page.title = "Agenda App"
    page.window_centered = True
    page.window.width = 1200
    page.window.height = 800

# --------------------------------
# Restaurar sesión persistente
# --------------------------------
    saved_user = page.client_storage.get("user")
    if saved_user:
        page.session.set("user", saved_user)


    # --------------------------------
    # Router
    # --------------------------------
    def route_change(e):
        page.views.clear()

        user = page.session.get("user")

        if page.route == "/":
            view = LoginView(page)

        elif page.route == "/register":
            view = RegisterView(page)

        elif page.route == "/menu":
            if not user:
                page.go("/")
                return
            view = mainmenu_view(page, user)

        elif page.route == "/calendar":
            if not user:
                page.go("/")
                return
            view = calendar_view(page, user)

        elif page.route == "/tareas":
            if not user:
                page.go("/")
                return
            view = tareas_view(page, user)

        elif page.route == "/settings":
            if not user:
                page.go("/")
                return
            view = SettingsView(page, user)

        else:
            view = LoginView(page)

        # 🔒 PROTECCIÓN CRÍTICA
        if view is not None:
            page.views.append(view)

        page.update()

    page.on_route_change = route_change

    # --------------------------------
    # Arranque
    # --------------------------------
    page.go("/")


ft.app(target=main)
