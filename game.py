'''
a simple game to demonstrate evolution
'''
import pygame
import sys
sys.path.append(".")  # update this as a package
import game_objects as go
import setup

#keep global
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main(npcs):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #drawing
        screen.fill(WHITE) #note: we need to redraw the white screen on every frame
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.draw(screen)
        for npc in npcs:
            npc.draw(screen)
            print('spawning npc!')
        pygame.display.flip()
        # Cap the frame rate
        pygame.time.Clock().tick(60)

pygame.init()
screen = setup.setup_screen()
player = setup.setup_player()
npcs = setup.setup_npcs(10)
print(npcs)
main(npcs)

pygame.quit()
sys.exit()
