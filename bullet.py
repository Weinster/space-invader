from turtle import Turtle

BULLET_SPEED = 1


class Bullet:

    def __init__(self):
        self.bullets = []
        self.can_shoot = True

    def create_bullet(self, pos):
        if self.can_shoot:
            new_bullet = Turtle()
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
