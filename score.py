import pygame

class Score:
    score = 0
    
    

    def __init__(self,screen,font) -> None:
        self.screen = screen
        self.font = font
        self.score_txt = self.font.render(f"Score: {self.score}", False, (255,255,255))
        

    def draw(self):
        self.score_txt = self.font.render(f"Score: {self.score}", False, (255,255,255))
        self.screen.blit(self.score_txt,(0,0))