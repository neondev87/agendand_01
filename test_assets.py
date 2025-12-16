import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text("SI VES ESTO, LA APP FUNCIONA"),
        ft.Image(src="images/hero_login.png")
    )

ft.app(
    target=main,
    assets_dir="assets"
)
