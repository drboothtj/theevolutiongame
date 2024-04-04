import random
import pygame
import game_objects as go

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def setup_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("The Evolution Game")
    return screen

def setup_player():
    '''
    create an instance of the player class
        arguments:
            None
        returns:
            player: the player
    '''
    player_width = 50 #make global for editing
    player_height = 50 #make global for editing
    player = go.Player(
        SCREEN_WIDTH // 2 - player_width // 2,
        SCREEN_HEIGHT // 2 - player_height // 2,
        player_width, 
        player_height,
        5, #speed
        (0,0,0) #color black!
        )
    return player

def setup_npcs(number):
    '''
    spawn initial npcs
        arguments:
            number: number to spawn on initialisation
        returns:
            npcs: list of Character objects for spawning
    '''
    npc_width = 10 #make global for editing
    npc_height = 10 #make global for editing
    npcs = []
    for spawn in range(0, number):
        npc = go.Npc(
            random.randint(0, SCREEN_WIDTH),
            random.randint(0, SCREEN_HEIGHT),
            npc_width,
            npc_height,
            speed = 0,
            colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        )
        npcs.append(npc)
    return npcs
