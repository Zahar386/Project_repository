import pygame
import sys

pygame.init()
pygame.font.init()

class Fon_object:
    def __init__(self, x,y):
        self.obj_pos = pygame.Vector2(x*80+40,y*80+40)
    
    def movement(self):
        self.obj_pos.x -= 1
        self.obj_pos.y -= 0.5
        if self.obj_pos.x < -40:
            self.obj_pos.x = 1240
        if self.obj_pos.y < -40:
            self.obj_pos.y = 840

font1 = pygame.font.SysFont('impact', 125)
nadpis1 = font1.render('СУДЬБОВЛАДЕЛЬЦЫ', True, (200,0,200), (0,200,0))
font2 = pygame.font.SysFont('impact', 75)
nadpis2 = font2.render('Start', True, (255,255,0), "Red")
time = pygame.time.Clock()
game_status = 0

screen = pygame.display.set_mode((1200,800))
fon_obj = []
for x in range(16):
    for y in range(11):
        fon_obj.append(Fon_object(x,y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] in range(int(300+100/2)-100,int(300+100/2)+100) and pygame.mouse.get_pos()[1] in range(int(485+100/2)-25,int(485+100/2)+25):
                game_status = 1
            
    screen.fill((0,80,0))
    for obj in fon_obj:
        pygame.draw.circle(screen, (100,0,100), obj.obj_pos, 40, 3)
        obj.movement()
        
    if game_status == 0:
        screen.blit(nadpis1, (screen.get_width()/2-nadpis1.get_width()/2,screen.get_height()/2-nadpis1.get_height()/2))
        screen.blit(nadpis2, (300,485))
    
    time.tick(60)
    
    pygame.display.flip()