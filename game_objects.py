'''
game objects for theevolutiongame
'''
import pygame 

class Character:
    '''
    Generic class for Player and NPCs
    '''
    def __init__(self, x_pos, y_pos, width, height, speed, colour): 
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.speed = speed
        self.colour = colour
    
    def draw(self, screen):
        '''
        ...
        '''
        pygame.draw.rect(screen, self.colour, (self.x_pos, self.y_pos, self.width, self.height))

class Player(Character):
    def move(self, keys):
        '''
        ...
        '''
        if keys[pygame.K_LEFT]:
            self.x_pos -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x_pos += self.speed
        if keys[pygame.K_UP]:
            self.y_pos -= self.speed
        if keys[pygame.K_DOWN]:
            self.y_pos += self.speed
