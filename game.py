from player import Player


class Game:
    def __init__(self, game_id, max_players=2):
        self.id = game_id
        self.max_players = max_players
        self.players = []
        self.projectiles = []
        self.projectiles_count = 0

    def can_player_join(self):
        return len(self.players) < self.max_players

    def join_new_player(self):
        player_id = len(self.players)
        player = Player(player_id, 25, 25, 20)
        self.players.append(player)

    def update_player(self, player):
        self.players[player.id] = player

    def update_projectiles(self, projectile):
        self.projectiles_count += 1
        projectile.id = self.projectiles_count
        self.projectiles.append(projectile)

    def get_other_players(self, player):
        return [p for p in self.players if p.id != player.id]

    def get_other_projectiles(self):
        send_projectiles = []
        for projectile in self.projectiles:
            if projectile.known < self.max_players:
                projectile.known += 1
                send_projectiles.append(projectile)
            else:
                self.projectiles.remove(projectile)
        return send_projectiles

    def get_last_player_joined(self):
        return self.players[-1]
