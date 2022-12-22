from turtle import Turtle
import ctypes
BULLET_SPEED = 1.5


class Bullet:

    def __init__(self):
        self.bullets = []
        self.can_shoot = True
        self.mci = ctypes.windll.winmm.mciSendStringW

    def create_bullet(self, pos):
        if self.can_shoot:
            new_bullet = Turtle()
            self.bullet_sound()
            new_bullet.penup()
            new_bullet.shape("pictures/bullet.gif")
            new_bullet.setheading(90)
            new_bullet.goto(pos)
            self.bullets.append(new_bullet)

    def shoot(self):
        for b in self.bullets:
            if b.ycor() > 400:
                self.can_shoot = True
                self.bullets.remove(b)
            else:
                self.can_shoot = False
            b.forward(BULLET_SPEED)

    def remove_bullet(self, b):
        b.goto(0, 360)

    def bullet_sound(self):
        command = 'Open "sounds/heat-vision.wav" type mpegvideo alias laser'
        self.mci = (command, 0, 0, 0)
        command = 'Play laser from 0'
        self.mci = (command, 0, 0, 0)
