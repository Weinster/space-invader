from turtle import Turtle
import ctypes
BULLET_SPEED = 2


class Bullet:

    def __init__(self):
        self.bullets = []
        self.can_shoot = True
        # i use this to play the sounds synchronously
        self.mci = ctypes.windll.winmm.mciSendStringW

    def create_bullet(self, pos):
        """create player bullet"""
        if self.can_shoot:
            new_bullet = Turtle()
            new_bullet.penup()
            new_bullet.shape("pictures/bullet.gif")
            new_bullet.setheading(90)
            new_bullet.goto(pos)
            self.bullets.append(new_bullet)
            self.bullet_sound()

    def shoot(self):
        """make player bullets go forward"""
        for b in self.bullets:
            if b.ycor() > 400:
                self.can_shoot = True
                self.bullets.remove(b)
            else:
                self.can_shoot = False
            b.forward(BULLET_SPEED)

    def remove_bullet(self, b):
        """relocate the bullet away from the screen after hitting an enemy"""
        b.goto(0, 360)

    def bullet_sound(self):
        """play sound"""
        command = 'Open "sounds/heat-vision.wav" type mpegvideo alias laser'
        self.mci(command, 0, 0, 0)
        command = 'Play laser from 0'
        self.mci(command, 0, 0, 0)
