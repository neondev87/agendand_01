from ui.theme import toggle_theme
import flet as ft
import ui.theme as theme

class ThemeTransition:
    def __init__(self, page: ft.Page):
        self.page = page
        self.overlay = ft.Container(
            expand=True,
            opacity=0,
            animate_opacity=300,
        )

    def animate(self):
        # cubrir con color actual
        self.overlay.bgcolor = theme.APP_BG
        self.overlay.opacity = 1
        self.page.update()

        # cambiar tema
        toggle_theme(self.page)

        # descubrir con nuevo color
        self.overlay.bgcolor = theme.APP_BG
        self.overlay.opacity = 0
        self.page.update()
