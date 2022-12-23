from turtle import Screen
from player import Player
from enemy import Enemy
from bullet import Bullet
from dashboard import Dashboard
from collision import Collision
from functools import partial
import time

delay = None
to_remove = []
screen = Screen()
screen.title("Space Invader")
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
dashboard = Dashboard()
dashboard.display()
enemy.create_enemy()
screen.listen()
screen.onkeypress(key="d", fun=player.move_left)
screen.onkeypress(key="D", fun=player.move_left)
screen.onkeypress(key="a", fun=player.move_right)
screen.onkeypress(key="A", fun=player.move_right)
game = True
while game:
    screen.update()
    if len(enemy.enemies) == 0:
        time.sleep(0.5)
        enemy.enemy_extra_bullet_remove()
        enemy.enemy_move_speed += .5  # make enemy faster next level
        enemy.count_number_of_turns = 0  # reset number of count
        dashboard.level += 1  # increase level
        enemy.create_enemy()
        if dashboard.level < 4:
            dashboard.update()
    if dashboard.level > 3:
        dashboard.victory()
        game = False
    if len(dashboard.health_bar) == 0:
        dashboard.game_over()
        game = False
    enemy.enemy_movements()
    enemy.enemy_create_bullet()
    enemy.enemy_shoot()
    pos = (player.xcor(), player.ycor() + 25)
    screen.onkeypress(key="space", fun=partial(bullet.create_bullet, pos))
    bullet.shoot()
    enemy_hit_by_bullet = collision.is_enemy_hit(bullet, enemy)
    enemy_bullet_used = collision.is_player_hit(enemy, player)
    if enemy_hit_by_bullet:
        enemy.crash(enemy_hit_by_bullet[0])
        bullet.remove_bullet(enemy_hit_by_bullet[1])
        to_remove.append(enemy_hit_by_bullet[0])
        delay = round(time.time() + .5, 1)  # set a delay after crash
    if enemy_bullet_used:
        enemy.remove_bullet(enemy_bullet_used)
        dashboard.minus_health()
    if delay == round(time.time(), 1):
        # move enemy away after delay is satisfied
        enemy.remove_crash_enemy(to_remove)
    if collision.collision_enemy_player(enemy, player):
        dashboard.game_over()
        game = False

screen.exitonclick()
