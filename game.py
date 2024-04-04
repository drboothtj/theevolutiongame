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

def eat(npcs):
    '''
    ...
    '''
    surviving_npcs = []
    for npc in npcs:
        if npc.check_collision(player) == False:
            surviving_npcs.append(npc)
    return surviving_npcs

def reproduce(npcs):
    new_npcs = []
    for npc in npcs:
        new_npc = npc.reproduce()
        new_npcs.append(new_npc)
    return new_npcs

def mutate(npcs):
    for npc in npcs:
        npc.mutate()

def main(npcs):
    '''
    gameplay loop
    '''
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #movement
        keys = pygame.key.get_pressed()
        player.move(keys)
        npcs = eat(npcs) #selection
        if len(npcs) < 90:
            new_npcs = reproduce(npcs)
            mutate(new_npcs)
            npcs.extend(new_npcs)

        #draw
        screen.fill(WHITE) #note: we need to redraw the white screen on every frame
        player.draw(screen)
        for npc in npcs:
            npc.draw(screen)
        pygame.display.flip()
        # Cap the frame rate
        pygame.time.Clock().tick(60)

pygame.init()
screen = setup.setup_screen()
player = setup.setup_player()
npcs = setup.setup_npcs(100)
main(npcs)

pygame.quit()
sys.exit()
