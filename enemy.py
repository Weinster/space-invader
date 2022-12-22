from turtle import Turtle
import random
import ctypes

ENEMY_STARTING_POS = [(200, 180), (0, 180), (100, 280),
                      (-100, 280), (-200, 180)]


class Enemy:

    def __init__(self):
        self.enemies = []
        self.bullets = []
        self.count = 0
        self.enemy_move_speed = .5
        self.mci = ctypes.windll.winmm.mciSendStringW

    def create_enemy(self):
        for e in ENEMY_STARTING_POS:
            new_enemy = Turtle()
            new_enemy.penup()
            new_enemy.shape("pictures/enemy.gif")
            new_enemy.goto(e)
            self.enemies.append(new_enemy)

    def enemy_movements(self):
        if self.count == 4:
            for enemy in self.enemies:
                enemy.goto(enemy.xcor(), enemy.ycor() - 60)
                self.count = 0
        for enemy in self.enemies:
            enemy.forward(self.enemy_move_speed)
            if enemy.xcor() > 360 or enemy.xcor() < -360:
                self.turn()
                self.count += 1

    def turn(self):
        for enemy in self.enemies:
            enemy.right(180)

    def enemy_create_bullet(self):
        random_spawn = random.randint(1, 500)
        if random_spawn == 1:
            try:
                random_enemy = random.choice(self.enemies)
            except IndexError:
                pass
            else:
                x = random_enemy.xcor()
                y = random_enemy.ycor() - 30
                new_bullet = Turtle()
                new_bullet.shape("pictures/bullet_enemy.gif")
                new_bullet.penup()
                new_bullet.setheading(270)
                new_bullet.goto(x, y)
                self.bullets.append(new_bullet)

    def enemy_shoot(self):
        for b in self.bullets:
            if b.ycor() < -360:
                b.hideturtle()
                self.bullets.remove(b)
            b.forward(.5)

    def remove_bullet(self, e):
        self.bullets.remove(e)
        e.goto(1000, 1000)

    def crash(self, e):
        e.shape("pictures/crash.gif")
        self.crash_sound()
        self.enemies.remove(e)

    def remove_crash_enemy(self, enemies):
        for enemy in enemies:
            enemy.goto(1000, 1000)

    def crash_sound(self):
        command = 'Open "sounds/Explosion7.wav" type mpegvideo alias explo'
        self.mci(command, 0, 0, 0)
        command = 'Play explo from 0'
        self.mci(command, 0, 0, 0)

    def enemy_extra_bullet_remove(self):
        for bullets in self.bullets:
            bullets.goto(-1000, -1000)
        self.bullets.clear()
