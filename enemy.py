from turtle import Turtle
import random

ENEMY_STARTING_POS = [(200, 180), (0, 180), (100, 280),
                      (-100, 280), (-200, 180)]

ENEMY_MOVE_SPEED = .2


class Enemy:

    def __init__(self):
        self.enemies = []
        self.bullets = []
        self.count = 0

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
            enemy.forward(ENEMY_MOVE_SPEED)
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

    def crash(self, e):
        e.shape("pictures/crash.gif")
        self.enemies.remove(e)

    def remove_crash_enemy(self, enemies):
        for enemy in enemies:
            enemy.goto(1000, 1000)
