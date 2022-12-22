from turtle import Turtle

ENEMY_STARTING_POS = [(200, 180), (0, 180), (100, 280),
                      (-100, 280), (-200, 180)]

ENEMY_MOVE_SPEED = .2


class Enemy:

    def __init__(self):
        self.enemies = []

    def create_enemy(self):
        for e in ENEMY_STARTING_POS:
            new_enemy = Turtle()
            new_enemy.penup()
            new_enemy.shape("pictures/enemy.gif")
            new_enemy.goto(e)
            self.enemies.append(new_enemy)

    def enemy_movements(self):
        for enemy in self.enemies:
            enemy.forward(ENEMY_MOVE_SPEED)
            if enemy.xcor() > 360 or enemy.xcor() < -360:
                self.turn()

    def turn(self):
        for enemy in self.enemies:
            enemy.right(180)
