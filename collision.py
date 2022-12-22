class Collision:

    def is_enemy_hit(self, b, e):
        for b in b.bullets:
            for e in e.enemies:
                if b.distance(e) < 30:
                    return [e, b]

    def collision_enemy_player(self, e, p):
        for e in e.enemies:
            if p.distance(e) < 30:
                return True
