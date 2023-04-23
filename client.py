import pygame
from network import Network


width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
projectiles = []

def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    for projectile in projectiles:
        if projectile.active:
            projectile.draw(win)
        else:
            projectiles.remove(projectile)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    projectiles.append(p.shoot(x, y))


        p.move()

        for projectile in projectiles:
            projectile.update()

        redrawWindow(win, p, p2)


main()
