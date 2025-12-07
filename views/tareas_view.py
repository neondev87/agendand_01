import flet as ft
from ui import theme
from components.navbar import Navbar


def tareas_view(page, user):

    tareas = []
    lista_tareas = ft.Column(scroll="auto")

    # ------------------------------------------
    # ACTUALIZAR LISTA
    # ------------------------------------------
    def actualizar_lista():
        lista_tareas.controls.clear()

        if not tareas:
            lista_tareas.controls.append(
                ft.Text("No hay tareas registradas.", color=theme.TEXT_MUTED)
            )
        else:
            for t in tareas:
                lista_tareas.controls.append(
                    ft.Container(
                        bgcolor=theme.SURFACE_BG,
                        padding=14,
                        border_radius=theme.BORDER_RADIUS,
                        content=ft.Row(
                            [
                                ft.Text(t, color=theme.TEXT_COLOR, size=16),

                                ft.IconButton(
                                    icon=ft.icons.DELETE_ROUNDED,
                                    icon_color=theme.DANGER,
                                    on_click=lambda e, tarea=t: eliminar_tarea(tarea)
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    )
                )

        page.update()

    # ------------------------------------------
    # ELIMINAR TAREA
    # ------------------------------------------
    def eliminar_tarea(tarea):
        tareas.remove(tarea)
        actualizar_lista()

    # ------------------------------------------
    # MODAL
    # ------------------------------------------
    nueva_tarea = theme.input_field("Descripción de tarea")

    def confirmar_agregar(e):
        if nueva_tarea.value.strip():
            tareas.append(nueva_tarea.value.strip())
            nueva_tarea.value = ""
            dialog.open = False
            actualizar_lista()
        else:
            nueva_tarea.error_text = "Escribe una tarea"
        page.update()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Nueva tarea", color=theme.TEXT_COLOR),
        content=nueva_tarea,
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e: cerrar_modal()),
            ft.TextButton("Agregar", on_click=confirmar_agregar),
        ]
    )

    def abrir_modal(e):
        page.dialog = dialog
        dialog.open = True
        page.update()

    def cerrar_modal():
        dialog.open = False
        page.update()

    # ------------------------------------------
    # UI
    # ------------------------------------------
    nav = Navbar(page)

    content = ft.Column(
        [
            theme.title("Tareas"),

            ft.Container(height=15),

            theme.primary_button(
                "Agregar tarea",
                on_click=abrir_modal,
                icon=ft.icons.ADD_ROUNDED
            ),

            ft.Container(height=20),
            lista_tareas,
        ],
        expand=True,
        scroll="auto",
    )

    layout = ft.Row(
        [
            nav,
            ft.Container(width=20),
            content
        ],
        expand=True
    )

    return ft.View(
        route="/tareas",
        bgcolor=theme.APP_BG,
        controls=[layout]
    )
