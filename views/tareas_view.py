import flet as ft
from ui.theme import TEXT_COLOR
from components.navbar import Navbar


def tareas_view(page, user):

    tareas = []
    lista_tareas = ft.Column(scroll="auto")

    # -------------------------------------------------
    # Actualizar lista visual
    # -------------------------------------------------
    def actualizar_lista():
        lista_tareas.controls.clear()

        if not tareas:
            lista_tareas.controls.append(
                ft.Text("No hay tareas registradas.", color="#888")
            )
        else:
            for t in tareas:
                lista_tareas.controls.append(
                    ft.Container(
                        bgcolor="#2A2A2A",
                        padding=12,
                        border_radius=8,
                        content=ft.Row(
                            [
                                ft.Text(t, color=TEXT_COLOR, size=16),
                                ft.IconButton(
                                    icon=ft.icons.DELETE_ROUNDED,
                                    icon_size=20,
                                    icon_color="#FF5555",
                                    on_click=lambda e, tarea=t: eliminar_tarea(tarea)
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    )
                )

        page.update()

    # -------------------------------------------------
    # Eliminar tarea
    # -------------------------------------------------
    def eliminar_tarea(tarea):
        tareas.remove(tarea)
        actualizar_lista()

    # -------------------------------------------------
    # Modal para agregar tarea
    # -------------------------------------------------
    nueva_tarea = ft.TextField(
        label="Descripción de tarea",
        width=300,
        bgcolor="#2A2A2A",
        border_color="#444"
    )

    def confirmar_agregar(e):
        if nueva_tarea.value.strip():
            tareas.append(nueva_tarea.value.strip())
            nueva_tarea.value = ""
            dialog.open = False
            actualizar_lista()
        else:
            nueva_tarea.error_text = "Escribe una tarea"
        page.update()

    def cerrar_modal(e=None):
        dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Nueva tarea", color=TEXT_COLOR),
        content=nueva_tarea,
        actions=[
            ft.TextButton("Cancelar", on_click=cerrar_modal),
            ft.TextButton("Agregar", on_click=confirmar_agregar),
        ]
    )

    def abrir_modal(e):
        page.dialog = dialog
        dialog.open = True
        page.update()

    # -------------------------------------------------
    # Layout con Navbar
    # -------------------------------------------------
    nav = Navbar(page)

    content = ft.Column(
        [
            ft.Text(
                "Tareas",
                size=32,
                weight=ft.FontWeight.BOLD,
                color=TEXT_COLOR
            ),

            ft.Container(height=15),

            ft.ElevatedButton(
                "Agregar tarea",
                icon=ft.icons.ADD_ROUNDED,
                on_click=abrir_modal,
                bgcolor="#3B3B3B",
                color="white",
                height=45
            ),

            ft.Container(height=15),

            lista_tareas,
        ],
        expand=True,
        scroll="auto",
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START
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
        bgcolor="#1E1E1E",
        controls=[layout]
    )
