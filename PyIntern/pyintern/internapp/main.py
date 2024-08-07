from manim import *
from . import db

f = ''

class RunningText(Scene):
    def construct(self):
        self.camera.frame_width = 1.0
        self.camera.frame_height = 1.0
        text = Text(f, font_size=30)

        text_width = text.width
        text_height = text.height

        text.move_to(RIGHT * (text_width / 2 + 0.5))

        running_animation = ApplyMethod(text.shift, LEFT * (text_width + 1))

        self.play(running_animation)

