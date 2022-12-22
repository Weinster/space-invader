from turtle import Screen
from player import Player
from enemy import Enemy
from bullet import Bullet
from functools import partial
import time

delay = None
to_remove = []
screen = Screen()
screen.bgpic("pictures/bg.GIF")
screen.register_shape(
    "pictures/spaceship.gif")
screen.register_shape("pictures/enemy.gif")
screen.register_shape("pictures/bullet.gif")
# screen.register_shape("oop/space invaders/enemy_bullet.gif")
# screen.register_shape("oop/space invaders/crash.gif")
screen.setup(width=800, height=700)
screen.tracer(0)
player = Player()
bullet = Bullet()
enemy = Enemy()
enemy.create_enemy()

screen.listen()
screen.onkeypress(key="d", fun=player.move_left)
screen.onkeypress(key="D", fun=player.move_left)
screen.onkeypress(key="a", fun=player.move_right)
screen.onkeypress(key="A", fun=player.move_right)
game = True
while game:
    screen.update()
    bullet.shoot()
    enemy.enemy_movements()
    x = player.xcor()
    y = player.ycor() + 25
    pos = (x, y)
    screen.onkeypress(key="space", fun=partial(bullet.create_bullet, pos))

screen.exitonclick()
