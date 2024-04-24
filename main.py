import pygame
pygame.init()
screen=pygame.display.set_mode((600,800))
class Circle():
    def __init__(self,color,size,x,y):
        self.color=color
        self.size=size
        self.where=x,y
        self.screen=screen
    def draw (self):
        pygame.draw.circle(self.screen,self.color,self.where,self.size)
    def grow(self):
        self.size+=10
        pygame.draw.circle(self.screen,self.color,self.where,self.size)
c1=Circle("pink",20,70,70)
c3=Circle("pink",15,90,70)
screen.fill("violet")
while True:
    pygame.draw.circle(screen,"pink",(40,70),20)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            c1.draw()
            c3.draw()
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            c1.grow()
            pygame.display.update()
        if event.type==pygame.MOUSEMOTION:
            #screen.fill("violet")
            pos=pygame.mouse.get_pos()
            c2=Circle("blue",3,pos[0],pos[1])
            c2.draw()
            pygame.display.update()Practise: 
#Make a rect class with grow function, utilize the mouse events to make the changes to the rectangle


