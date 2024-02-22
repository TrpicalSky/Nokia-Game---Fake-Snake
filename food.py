import random
import pygame

class Food:
    green = (0,255,0)
    food_rect = [10,10]
    drawn = False
    current_location = []

    def __init__(self,screen) -> None:
        self.screen = screen

    def draw(self):
        if not self.drawn:
            self.drawn = True
            self.current_location = [random.randint(1,230),random.randint(1,310)]
            food = pygame.draw.rect(self.screen,self.green,[self.current_location[0],self.current_location[1],self.food_rect[0],self.food_rect[1]])
            return food
        else:
            food = pygame.draw.rect(self.screen,self.green,[self.current_location[0],self.current_location[1],self.food_rect[0],self.food_rect[1]])
            return food
        
    def collide(self,scoreObj):
        self.drawn = not self.drawn
        scoreObj.score += 1