'''
game objects for theevolutiongame
'''
import pygame 
import random

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

class Npc(Character):
    '''
    class for non-playable characters
    '''
    
    def check_collision(self, collider):
        '''
        check collision with an object
        '''
        if (
            self.x_pos < collider.x_pos + collider.width and
            self.x_pos + self.width > collider.x_pos and
            self.y_pos < collider.y_pos + collider.height and
            self.y_pos + self.height > collider.y_pos
            ):
            return True
        return False

    def reproduce(self):
        child = Npc(
            self.x_pos, self.y_pos, 
            self.width, self.height, 
            self.speed, self.colour
        )
        return child

    def mutate(self):
        '''
        mutates the characteristics of the NPC
        '''
        self.x_pos += random.randint(-50, 50)
        self.y_pos += random.randint(-50, 50)
        #self.width = width
        #self.height = height
        #self.speed = speed
        #self.colour = colour