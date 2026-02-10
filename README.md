
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty, StringProperty
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.core.audio import SoundLoader
from random import randint, choice
import json, os

kivy.require('2.1.0')

SAVE_FILE = 'save.json'

# --- Sons ---
shoot_sound = SoundLoader.load('shoot.wav')
hit_sound = SoundLoader.load('hit.wav')
super_sound = SoundLoader.load('super.wav')
explosion_sound = SoundLoader.load('explosion.wav')
music = SoundLoader.load('music.mp3')
if music:
    music.loop = True
    music.play()

# --- Joueur ---
class Player(Widget):
    health = NumericProperty(100)
    super_energy = NumericProperty(0)
    color = ListProperty([0,1,0,1])
    score = NumericProperty(0)
    skin = NumericProperty(0)

    def move(self, dx, dy):
        self.pos = Vector(dx, dy) + self.pos

    def shoot(self):
        bullet = Bullet(owner='player', color=self.color)
        bullet.center = self.center
        bullet.velocity = Vector(15, 0)
        self.parent.add_widget(bullet)
        if shoot_sound:
            shoot_sound.play()
        self.super_energy = min(100, self.super_energy + 10)

    def super_attack(self):
        if self.super_energy >= 100:
            for angle in range(0, 360, 15):
                bullet = Bullet(owner='player', color=[1,1,0,1])
                bullet.center = self.center
                bullet.velocity = Vector(20, 0).rotate(angle)
                self.parent.add_widget(bullet)
            self.super_energy = 0
            if super_sound:
                super_sound.play()

# --- Ennemi ---
class Enemy(Widget):
    health = NumericProperty(50)
    shoot_cooldown = NumericProperty(0)
    color = ListProperty([1,0,0,1])
    type = StringProperty('basic')

    def move_random(self):
        if self.type == 'fast':
            dx = randint(-6,6)
            dy = randint(-6,6)
        elif self.type == 'tank':
            dx = randint(-2,2)
            dy = randint(-2,2)
        else:
            dx = randint(-3,3)
            dy = randint(-3,3)
        self.pos = Vector(dx, dy) + self.pos

    def shoot(self, player):
        if self.type == 'shooter' and self.shoot_cooldown <=0:
            bullet = Bullet(owner='enemy', color=self.color)
            bullet.center = self.center
            direction = Vector(player.center_x - self.center_x, player.center_y - self.center_y).normalize() * 12
            bullet.velocity = direction
            self.parent.add_widget(bullet)
            self.shoot_cooldown = randint(40,80)
        else:
            self.shoot_cooldown -=1

# --- Bullet ---
class Bullet(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    owner = StringProperty('')
    color = ListProperty([1,1,1,1])

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

# --- Health Bar ---
class HealthBar(Widget):
    target = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update,1/60)

    def update(self, dt):
        if self.target:
            self.size = (self.target.width * self.target.health / 100, 5)
            self.pos = (self.target.x, self.target.top + 2)

# --- Game ---
class Game(Widget):
    player = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.enemies = []
        self.health_bars = []
        # Spawn différents types d'ennemis
        for _ in range(2):
            self.spawn_enemy('basic')
            self.spawn_enemy('fast')
            self.spawn_enemy('tank')
            self.spawn_enemy('shooter')
        # Score label
        self.score_label = Label(text='Score: 0', pos=(10, 760), font_size=20)
        self.add_widget(self.score_label)
        # Player health bar
        self.player_bar = HealthBar()
        # Charger progression
        self.load_progression()
        Clock.schedule_interval(self.update,1/60)

    def spawn_enemy(self, type_):
        enemy = Enemy(type=type_)
        enemy.pos = (randint(100,500),randint(100,700))
        if type_=='fast': enemy.color=[1,1,0,1]
        if type_=='tank': enemy.color=[0.5,0.2,0,1]
        if type_=='shooter': enemy.color=[1,0,1,1]
        self.add_widget(enemy)
        self.enemies.append(enemy)
        hb = HealthBar(target=enemy)
        self.add_widget(hb)
        self.health_bars.append(hb)

    def on_touch_move(self, touch):
        self.player.center = touch.pos

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.player.super_attack()
        else:
            self.player.shoot()

    def update(self, dt):
        # Déplacer bullets
        for bullet in [b for b in self.children if isinstance(b, Bullet)]:
            bullet.move()
            if bullet.owner=='player':
                for enemy in self.enemies:
                    if bullet.collide_widget(enemy):
                        enemy.health -= 10
                        if hit_sound:
                            hit_sound.play()
                        self.remove_widget(bullet)
                        if enemy.health <=0:
                            if explosion_sound: explosion_sound.play()
                            self.remove_widget(enemy)
                            self.enemies.remove(enemy)
                            self.player.score += 10
                            self.score_label.text=f'Score: {self.player.score}'
                            # Respawn un nouvel ennemi aléatoire
                            self.spawn_enemy(choice(['basic','fast','tank','shooter']))
                        break
            elif bullet.owner=='enemy':
                if bullet.collide_widget(self.player):
                    self.player.health -=5
                    if hit_sound:
                        hit_sound.play()
                    self.remove_widget(bullet)
        # Déplacer ennemis et tirer
        for enemy in self.enemies:
            enemy.move_random()
            enemy.shoot(self.player)
        # Mettre à jour player health bar
        self.player_bar.update(dt)
        # Sauvegarder score
        self.save_progression()

    def load_progression(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE,'r') as f:
                    data=json.load(f)
                    self.player.score = data.get('score',0)
                    self.player.skin = data.get('skin',0)
                    self.player.color = data.get('color',[0,1,0,1])
            except: pass

    def save_progression(self):
        try:
            data = {'score':self.player.score,'skin':self.player.skin,'color':self.player.color}
            with open(SAVE_FILE,'w') as f:
                json.dump(data,f)
        except: pass

# --- App ---
class MiniBrawlApp(App):
    def build(self):
        game = Game()
        player = Player()
        player.pos = (300,300)
        game.player = player
        game.add_widget(player)
        # Player health bar
        game.player_bar.target = player
        game.add_widget(game.player_bar)
        return game

if __name__=='__main__':
    MiniBrawlApp().run()