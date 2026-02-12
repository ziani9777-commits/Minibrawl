# ---------- CONFIG MOBILE ----------
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'resizable', False)
Config.set('kivy', 'keyboard_mode', 'systemanddock')

# ---------- IMPORTS ----------
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from random import randint

# ---------- BALLE ----------
class Bullet(Widget):
    velocity_y = NumericProperty(10)

    def update(self):
        self.y += self.velocity_y
        if self.y > self.parent.height:
            self.parent.remove_widget(self)

# ---------- JOUEUR ----------
class Player(Widget):
    velocity_x = NumericProperty(0)

    def update(self):
        self.x += self.velocity_x

        # limite écran
        if self.x < 0:
            self.x = 0
        if self.right > self.parent.width:
            self.right = self.parent.width

    def shoot(self):
        bullet = Bullet(size=(10,20), pos=(self.center_x-5, self.top))
        with bullet.canvas:
            Color(1,0,0)
            Rectangle(pos=bullet.pos, size=bullet.size)
        self.parent.add_widget(bullet)

# ---------- JEU ----------
class GameWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # fond
        with self.canvas:
            Color(0.1,0.1,0.1)
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # joueur
        self.player = Player(size=(80,80), pos=(200,50))
        with self.player.canvas:
            Color(0,1,0)
            Rectangle(pos=self.player.pos, size=self.player.size)
        self.add_widget(self.player)

        Clock.schedule_interval(self.update, 1/60)

    def update_bg(self,*a):
        self.bg.size = self.size

    def update(self, dt):
        self.player.update()

        for child in self.children[:]:
            if isinstance(child, Bullet):
                child.update()

# ---------- CONTROLES TACTILES ----------
class MobileControls(Widget):
    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.game = game

        # gauche
        btn_left = Button(text="◀", size_hint=(.25,.2), pos_hint={"x":0,"y":0})
        btn_left.bind(on_press=self.left_down, on_release=self.stop)

        # droite
        btn_right = Button(text="▶", size_hint=(.25,.2), pos_hint={"x":.26,"y":0})
        btn_right.bind(on_press=self.right_down, on_release=self.stop)

        # tir
        btn_fire = Button(text="🔥", size_hint=(.25,.2), pos_hint={"right":1,"y":0})
        btn_fire.bind(on_press=self.fire)

        self.add_widget(btn_left)
        self.add_widget(btn_right)
        self.add_widget(btn_fire)

    def left_down(self,*a):
        self.game.player.velocity_x = -6

    def right_down(self,*a):
        self.game.player.velocity_x = 6

    def stop(self,*a):
        self.game.player.velocity_x = 0

    def fire(self,*a):
        self.game.player.shoot()

# ---------- APP ----------
class MiniBrawlApp(App):
    def build(self):
        root = Widget()

        game = GameWidget()
        controls = MobileControls(game)

        root.add_widget(game)
        root.add_widget(controls)

        return root

MiniBrawlApp().run()
