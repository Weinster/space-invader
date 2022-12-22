class Collision:

    def is_enemy_hit(self, b, e):
        for b in b.bullets:
            for e in e.enemies:
                if b.distance(e) < 30:
                    return [e, b]

    def is_player_hit(self, b, p):
        for b in b.bullets:
            if p.distance(b) < 30:
                return b

    def collision_enemy_player(self, e, p):
        for e in e.enemies:
            if p.distance(e) < 30:
                return True
