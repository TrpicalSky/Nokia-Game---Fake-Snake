import pygame

class Snake:
    red = (255,0,0)
    snake_rect = [10,10]
    length = 1


    def __init__(self,position,screen) -> None:
        self.position = position
        self.screen = screen


    def draw(self,change_x,change_y) -> pygame.rect:
        self.position[0] += change_x
        self.position[1] += change_y
        snake = pygame.draw.rect(self.screen,self.red,[self.position[0],self.position[1],self.snake_rect[0],self.snake_rect[1]])
        return snake