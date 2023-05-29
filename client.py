import pygame
from network import Network
from player import Player
from button import Button


class Client:
    def __init__(self):
        pygame.init()
        self.width = 500
        self.height = 500
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Client")
        self.font = pygame.font.SysFont("Arial", 20)
        self.network_client = None
        self.local_player = None
        self.players = {}
        self.projectiles = set()
        self.background = pygame.image.load("assets/background.jpg")
        self.player_sprite = pygame.transform.scale(pygame.image.load("assets/player.png"), (50, 50))
        self.projectile_sprite = pygame.transform.scale(pygame.image.load("assets/projectile.png"), (14, 14))

    def setup_players(self):
        self.local_player = self.network_client.connect()
        print(self.local_player)
        for i in range(2):
            if i == self.local_player.id:
                self.players[i] = self.local_player
            else:
                self.players[i] = Player(i, 25, 25, 20)

    def redraw_window(self):
        self.window.blit(self.background, (0,0))
        for player in self.players.copy().values():
            if player.alive:
                player.draw(self.window, self.player_sprite)
            else:
                del self.players[player.id]
        for projectile in self.projectiles.copy():
            if projectile.active:
                projectile.draw(self.window, self.projectile_sprite)
            else:
                self.projectiles.remove(projectile)
        text_surface = self.font.render(str(self.local_player.health), True, (0, 0, 0))
        self.window.blit(text_surface, (self.width - 40, self.height - 40))
        pygame.display.update()

    def process_player_input(self):
        if self.local_player.alive:
            self.local_player.update(pygame.key.get_pressed())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.local_player.alive:
                x, y = pygame.mouse.get_pos()
                if (projectile := self.local_player.shoot(x, y)) is not None:
                    self.projectiles.add(projectile)
                    self.network_client.send_projectile(projectile)

    def update_projectiles(self):
        for projectile in self.projectiles.copy():
            if projectile.active:
                projectile.update()
                self.check_for_collision(projectile)
            else:
                self.projectiles.remove(projectile)

    def share_data_with_server(self):
        enemies, projectiles = self.network_client.send_player(self.local_player)
        if enemies is not None:
            self.players.update({enemy.id: enemy for enemy in enemies})
        if projectiles is not None:
            self.projectiles.update(projectiles)

    def check_for_collision(self, projectile):
        for player in self.players.copy().values():
            if self.check_circle_overlap((projectile.x, projectile.y), projectile.radius, (player.x, player.y), player.radius):
                print('hit registered')
                projectile.active = False
                if player is self.local_player:
                    print('sending damage')
                    player.take_damage()

    def check_circle_overlap(self, pos1, radius1, pos2, radius2):
        distance_squared = (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2
        radi_squared = (radius1 + radius2) ** 2
        return distance_squared <= radi_squared

    def main_menu(self):
        while True:
            self.window.fill((0, 0, 0))
            mouse_pos = pygame.mouse.get_pos()

            play_button = Button(pos=(self.width/2, self.height/2),
                                 text_input="PLAY", font=self.font, base_color="#ffffff",
                                 hovering_color="Light Green")

            play_button.change_color(mouse_pos)
            play_button.update(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.check_for_input(mouse_pos):
                        self.network_client = Network()
                        self.setup_players()
                        self.run()

            pygame.display.update()

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            self.share_data_with_server()
            self.update_projectiles()
            self.process_player_input()
            self.redraw_window()


client = Client()
client.main_menu()




