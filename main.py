import random
from collections import deque
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.label import Label
from kivy.uix.widget import Widget

Window.size = (360, 640)

class BrawlGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Ton code de logique de jeu ici...
        pass

class MainApp(App):
    def build(self):
        return BrawlGame()

if __name__ == "__main__":
    MainApp().run()
