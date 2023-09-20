import pygame

pygame.init()


class Text():
    def __init__(self,x,y,txt,size=24):
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("freeserif", size)
        self.txt = str(txt)
        self.updateText(txt)
        
        
    
    def updateText(self,txt):
        self.txt = str(txt)
        self.text_surface = self.font.render(self.txt, True, (255, 255, 255))
        self.backgroundSurface = pygame.Surface((self.text_surface.get_width(), self.text_surface.get_height()))
        # Create a sequence of lines that form a gradient
        # for y in range(self.text_surface.get_height()):
        #     normalized_Y = y/self.text_surface.get_height()
        #     # pick colors in RGB
        #     color = (255, 255, normalized_Y * 255)
        #     pygame.draw.line(self.gradient_surface, color, (0, y), (self.text_surface.get_width(), y))
        # then overlap the gradient with the letters using BLEND_RGBA_MULT
        # self.backgroundSurface.fill("black")
        self.text_surface.blit(self.text_surface, (0, 0))
    
    def draw(self,display):
        # display.blit(self.backgroundSurface,(self.x-self.text_surface.get_width()//2,self.y-self.text_surface.get_height()//2))
        display.blit(self.text_surface,(self.x-self.text_surface.get_width()//2,self.y-self.text_surface.get_height()//2))
    
    def resize(self,newSize):
        self.font = pygame.font.SysFont("freeserif", newSize)
        





