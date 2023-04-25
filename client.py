import pygame
from network import Network
from player import Player
from projectile import Projectile


class Client:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Client")
        self.network_client = Network()
        self.local_player = None
        self.players = {}
        self.projectiles = set()
        self.setup_players()

    def setup_players(self):
        self.local_player = self.network_client.connect()

        for i in range(2):
            if i == self.local_player.id:
                self.players[i] = self.local_player
            else:
                self.players[i] = Player(i, 25, 25, 20)

    def redraw_window(self):
        self.window.fill((255, 255, 255))
        for player in self.players.values():
            player.draw(self.window)
        for projectile in self.projectiles.copy():
            if projectile.active:
                projectile.draw(self.window)
            else:
                self.projectiles.remove(projectile)
        pygame.display.update()

    def update_players(self):
        for player in self.players:
            if player == self.local_player:
                player.update()

    def update_projectiles(self):
        for projectile in self.projectiles.copy():
            if projectile.active:
                projectile.update()
            else:
                self.projectiles.remove(projectile)

    def process_input(self):
        self.local_player.move()

    def share_data_with_server(self):
        enemies, projectiles = self.network_client.send(self.local_player)
        if enemies is not None:
            self.players.update({enemy.id: enemy for enemy in enemies})
        if projectiles is not None:
            self.projectiles.update(projectiles)

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            self.update_players()
            self.update_projectiles()
            self.process_input()
            self.share_data_with_server()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # if mouse_presses[0]:
                    if (projectile := self.local_player.shoot(x, y)) is not None:
                        self.projectiles.add(projectile)
                        self.network_client.send(projectile)

            self.redraw_window()


client = Client()
client.run()
