import flet as ft

class AnimatedImage(ft.Container):
    def __init__(self, src: str):
        super().__init__()
        self.scale = 1.0
        self.animate_scale = ft.Animation(250, ft.AnimationCurve.EASE_OUT)

        self.content = ft.Image(
            src=src,
            fit=ft.ImageFit.CONTAIN,
        )

        self.width = 420
        self.expand = True
        self.alignment = ft.alignment.center

    def zoom_in(self):
        self.scale = 1.05
        self.update()

    def zoom_out(self):
        self.scale = 1.0
        self.update()
