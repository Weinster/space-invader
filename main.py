from turtle import Screen
from player import Player
from enemy import Enemy
from bullet import Bullet
from collision import Collision
from functools import partial
import time
import threading

delay = None
to_remove = []
screen = Screen()
screen.bgpic("pictures/bg.GIF")
screen.register_shape(
    "pictures/spaceship.gif")
screen.register_shape("pictures/enemy.gif")
screen.register_shape("pictures/bullet.gif")
screen.register_shape("pictures/bullet_enemy.gif")
screen.register_shape("pictures/crash.gif")
screen.setup(width=800, height=700)
screen.tracer(0)
player = Player()
bullet = Bullet()
enemy = Enemy()
collision = Collision()
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
    enemy.enemy_create_bullet()
    enemy.enemy_shoot()
    pos = (player.xcor(), player.ycor() + 25)
    screen.onkeypress(key="space", fun=partial(bullet.create_bullet, pos))
    enemy_hit_by_bullet = collision.is_enemy_hit(bullet, enemy)
    if enemy_hit_by_bullet:
        enemy.crash(enemy_hit_by_bullet[0])
        bullet.remove_bullet(enemy_hit_by_bullet[1])
        to_remove.append(enemy_hit_by_bullet[0])
        delay = round(time.time() + .5, 1)
    if delay == round(time.time(), 1):
        enemy.remove_crash_enemy(to_remove)
    # if collision.collision_enemy_player(enemy, player):
screen.exitonclick()
