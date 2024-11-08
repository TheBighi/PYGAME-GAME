# Example file showing a circle moving on screen
import pygame
from pygame import mixer

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

pygame.mixer.init()
mixer.music.load("C:\\Users\\sander.tamm\\Downloads\\music.wav")

#player
imp = pygame.image.load("C:\\Users\\sander.tamm\\Downloads\\mam.png").convert()
imp = pygame.transform.scale(imp, (125, 125))
imp.set_colorkey(pygame.Color(255, 255, 255, 255))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2 * 1.6)

mixer.music.play(loops=-1)

#tree
tree = pygame.image.load("C:\\Users\\sander.tamm\\Downloads\\tree.png").convert()
tree = pygame.transform.scale(tree, (1000, 600))
tree_pos = tree.get_rect()
tree_pos.centerx = (screen.get_width() / 2)
tree_pos.centery = (screen.get_height() / 2 * 0.8)

#grass
grass = pygame.image.load

tree.set_colorkey(pygame.Color(0, 0, 0, 255))
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("chartreuse4")

    screen.blit(imp, (player_pos))
    screen.blit(tree, tree_pos)

    keys = pygame.key.get_pressed()

   
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time ian seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()