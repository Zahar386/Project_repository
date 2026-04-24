import pygame
import sys
import random

pygame.init()
pygame.font.init()

class Fon_object:
    def __init__(self, x,y):
        self.obj_pos = pygame.Vector2(x*80+40,y*80+40)
    
    def movement(self):
        pygame.draw.circle(screen, (120,0,120), self.obj_pos, 40, 3)
        self.obj_pos.x -= 1
        self.obj_pos.y -= 0.5
        if self.obj_pos.x < -40:
            self.obj_pos.x = 1240
        if self.obj_pos.y < -40:
            self.obj_pos.y = 840

class Player:
    def __init__(self, x,y, color):
        self.player_pos = pygame.Vector2(x,y)
        self.color = color
        self.score = 25
        self.direction = "left"
        self.happy = False
    
    def draw(self):
        pygame.draw.polygon(screen, self.color, ((self.player_pos.x-20,self.player_pos.y+20),(self.player_pos.x+20,self.player_pos.y+20),(self.player_pos.x,self.player_pos.y-20)))
        pygame.draw.polygon(screen, "Black", ((self.player_pos.x-21,self.player_pos.y+20),(self.player_pos.x+20,self.player_pos.y+20),(self.player_pos.x,self.player_pos.y-20)), 1)
        pygame.draw.circle(screen, self.color, (self.player_pos.x,self.player_pos.y-25), 20)
        pygame.draw.circle(screen, "Black", (self.player_pos.x,self.player_pos.y-25), 20, 1)
        if self.happy == True:
            pygame.draw.polygon(screen, "White", ((self.player_pos.x-10,self.player_pos.y-20),(self.player_pos.x+10,self.player_pos.y-20),(self.player_pos.x,self.player_pos.y-20+7)))
    
    def movement(self):
        if self.direction == "left":
            if self.player_pos.x-80*dice.index > 125 and self.color == "Red" or self.player_pos.x-80*dice.index > 95 and self.color == "Blue":
                self.player_pos.x -= 80*dice.index
            else:
                self.direction = "up"
                if self.color == "Red":
                    self.player_pos = pygame.Vector2(125,665)
                else:
                    self.player_pos = pygame.Vector2(95,700)
        elif self.direction == "right":
            if self.player_pos.x+80*dice.index < 1085 and self.color == "Red" or self.player_pos.x+80*dice.index < 1055 and self.color == "Blue":
                self.player_pos.x += 80*dice.index
            else:
                self.direction = "down"
                if self.color == "Red":
                    self.player_pos = pygame.Vector2(1085,105)
                else:
                    self.player_pos = pygame.Vector2(1055,140)
        elif self.direction == "up":
            if self.player_pos.y-80*dice.index > 105 and self.color == "Red" or self.player_pos.y-80*dice.index > 140 and self.color == "Blue":
                self.player_pos.y -= 80*dice.index
            else:
                self.direction = "right"
                if self.color == "Red":
                    self.player_pos = pygame.Vector2(125,105)
                else:
                    self.player_pos = pygame.Vector2(95,140)
        elif self.direction == "down":
            if self.player_pos.y+80*dice.index < 665 and self.color == "Red" or self.player_pos.y+80*dice.index < 700 and self.color == "Blue":
                self.player_pos.y += 80*dice.index
            else:
                self.direction = "left"
                if self.color == "Red":
                    self.player_pos = pygame.Vector2(1085,665)
                else:
                    self.player_pos = pygame.Vector2(1055,700)
    
class Cell:
    def __init__(self, x,y, color):
        self.cell_pos = pygame.Vector2(x,y)
        self.color = color
    def draw(self):
        if self.color == "Dark red":
            pygame.draw.polygon(screen, self.color, (self.cell_pos,(self.cell_pos.x,self.cell_pos.y+80),(self.cell_pos.x-80,self.cell_pos.y)))
            pygame.draw.polygon(screen, "Black", (self.cell_pos,(self.cell_pos.x,self.cell_pos.y+80),(self.cell_pos.x-80,self.cell_pos.y)), 1)
        elif self.color == "Dark blue":
            pygame.draw.polygon(screen, self.color, ((self.cell_pos.x,self.cell_pos.y+80),(self.cell_pos.x-80,self.cell_pos.y+80),(self.cell_pos.x-80,self.cell_pos.y)))
            pygame.draw.polygon(screen, "Black", ((self.cell_pos.x,self.cell_pos.y+80),(self.cell_pos.x-80,self.cell_pos.y+80),(self.cell_pos.x-80,self.cell_pos.y)), 1)

class Dice(pygame.sprite.Sprite):
    spritemap = pygame.image.load('storoni-igralnogo-kubika.png')
    frames = [spritemap.subsurface(pygame.Rect(0,1,100,100)),spritemap.subsurface(pygame.Rect(107,1,100,100)),spritemap.subsurface(pygame.Rect(214,1,100,100)),spritemap.subsurface(pygame.Rect(321,1,100,100)),spritemap.subsurface(pygame.Rect(428,1,100,100)),spritemap.subsurface(pygame.Rect(535,1,100,100))]
    animtiontick = 0
    maxanimationtick = 15
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.frames[0]
        self.index = 0
    def rolling(self):
        self.animtiontick += 1
        if self.animtiontick == self.maxanimationtick:
            self.animtiontick = 0
            self.index = random.randint(1,6)
            self.image = self.frames[self.index-1]
            self.image = pygame.transform.scale(self.image, (100,100))
            self.rect = self.image.get_rect()
            self.rect.center = (self.rect.center[0],self.rect.center[1])
    def draw(self):
        screen.blit(self.image,(screen.get_width()/2-self.image.get_width()/2,screen.get_height()/2-self.image.get_height()/2))

class Bonus(pygame.sprite.Sprite):
    bonus_frames = [pygame.transform.scale(pygame.image.load("Bonuses\Bonus_1.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_2.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_3.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_4.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_5.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_6.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_7.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_8.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_9.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_10.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_11.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_12.png"), (40,40)),pygame.transform.scale(pygame.image.load("Bonuses\Bonus_13.png"), (40,40))]
    def __init__(self, x,y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.bonus_frames[random.randint(0,len(self.bonus_frames)-1)]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.color = color
    
    def collition(self,player_pos):
        global turns_till_the_end, turn, skip_turns
        if player_pos.x in range(self.rect.center[0]-20,self.rect.center[0]+20) and player_pos.y in range(self.rect.center[1]-20,self.rect.center[1]+20):
            if self.image == self.bonus_frames[0]:
                turns_till_the_end += 3
            elif self.image == self.bonus_frames[1]:
                skip_turns += 1
            elif self.image == self.bonus_frames[2]:
                if turn == "Red":
                    pl1.happy = True
                    pl2.score = int(pl2.score/2)
                elif turn == "Blue":
                    pl2.happy = True
                    pl1.score = int(pl1.score/2)
            elif self.image == self.bonus_frames[3]:
                if turn == "Red":
                    pl1.happy = True
                elif turn == "Blue":
                    pl2.happy = True
            elif self.image == self.bonus_frames[4]:
                if turn == "Red":
                    if pl2.happy == False:
                        pl2.score = int(pl2.score/2)
                    else:
                        pl2.happy = False
                elif turn == "Blue":
                    if pl1.happy == False:
                        pl1.score = int(pl1.score/2)
                    else:
                        pl1.happy = False
            elif self.image == self.bonus_frames[5]:
                if turn == "Red":
                    pl2.score -= 5
                elif turn == "Blue":
                    pl1.score -= 5
            elif self.image == self.bonus_frames[6]:
                if turn == "Red":
                    pl2.score += 5
                elif turn == "Blue":
                    pl1.score += 5
            elif self.image == self.bonus_frames[7]:
                if turn == "Red":
                    pl2.score *= 2
                elif turn == "Blue":
                    pl1.score *= 2
            elif self.image == self.bonus_frames[8]:
                choice = random.randint(0,1)
                if choice == 0:
                    pl1.score -= 5
                    pl2.score += 5
                elif choice == 1:
                    pl2.score -= 5
                    pl1.score += 5
            elif self.image == self.bonus_frames[9]:
                if turn == "Red":
                    pl1.happy = True
                    pl2.score -= 3
                elif turn == "Blue":
                    pl2.happy = True
                    pl1.score -= 3
            elif self.image == self.bonus_frames[10]:
                if turn == "Red":
                    pl2.happy = False
                elif turn == "Blue":
                    pl1.happy = False
            elif self.image == self.bonus_frames[11]:
                if turn == "Red" and pl1.happy == True:
                    pl2.score = int(pl2.score/2)
                elif turn == "Blue" and pl2.happy == True:
                    pl1.score = int(pl1.score/2)
            elif self.image == self.bonus_frames[12]:
                if turn == "Red":
                    pl2.score = int(pl2.score/2)
                elif turn == "Blue":
                    pl1.score = int(pl1.score/2)
def draw_cells(color):
    for i in range(1,12):
        cells.append(Cell(i*80+150,650,color))
        cells.append(Cell(i*80+150,90,color))
    for i in range(1,7):
        cells.append(Cell(1110,i*80+90,color))
        cells.append(Cell(150,i*80+90,color))

def draw_corner_cell(x,y):
    pygame.draw.rect(screen, "Green", (x,y,80,80))
    pygame.draw.rect(screen, "Black", (x,y,80,80), 1)
    pygame.draw.line(screen, "Black", (x,y),(x+80,y+80), 2)

def make_bonuses(color):
    limit = 0
    if color == "Blue":
        limit = -35
    for i in range(1,12):
        bonuses.add(Bonus(i*80+125+limit,675-limit, color))
        bonuses.add(Bonus(i*80+125+limit,115-limit, color))
    for i in range(1,7):
        bonuses.add(Bonus(1085+limit,i*80+115-limit, color))
        bonuses.add(Bonus(125+limit,i*80+115-limit, color))

def skip_turn():
    global turn, skip_turns
    while skip_turns > 0:
        if turn == "Red":
            turn = "Blue"
        elif turn == "Blue":
            turn = "Red"
        skip_turns -= 1

font1 = pygame.font.SysFont('impact', 125)
name_of_game = font1.render('СУДЬБОВЛАДЕЛЬЦЫ', True, (200,0,200), (0,200,0))
font2 = pygame.font.SysFont('Times new roman', 75)
start_button = font2.render('Старт', True, (255,200,0), "Red")
restart_button = font2.render('Начать заново', True, (255,255,0), "Violet")

screen = pygame.display.set_mode((1200,800))

pl1 = Player(1085,665, "Red")
pl2 = Player(1055,700, "Blue")
dice = Dice()

skip_turns = 0

time = pygame.time.Clock()
game_status = 0
turn = "Red"
roll = False
turns_till_the_end = 40

fon_obj = []
players = []
cells = []
bonuses = pygame.sprite.Group()

make_bonuses("Red")
make_bonuses("Blue")

for x in range(16):
    for y in range(11):
        fon_obj.append(Fon_object(x,y))
players.append(pl1)
players.append(pl2)

draw_cells("Dark red")
draw_cells("Dark blue")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] in range(int(screen.get_width()/2-start_button.get_width()/2),int(screen.get_width()/2+start_button.get_width()/2)) and pygame.mouse.get_pos()[1] in range(int(screen.get_height()/2-start_button.get_height()+100/2),int(screen.get_height()/2+start_button.get_height()/2)+100) and game_status == 0:
                game_status = 1
            if pygame.mouse.get_pos()[0] in range(int(screen.get_width()/2-dice.image.get_width()/2),int(screen.get_width()/2-dice.image.get_width()/2+100)) and pygame.mouse.get_pos()[1] in range(int(screen.get_height()/2-dice.image.get_height()/2),int(screen.get_height()/2-dice.image.get_height()/2+100)):
                if roll == False:
                    roll = True
                elif roll == True:
                    roll = False
                    skip_turns += 1
                    skip_turn()
                    if turn == "Red":
                        pl1.movement()
                        for bonus in bonuses:
                            bonus.collition(pl1.player_pos)
                    elif turn == "Blue":
                        pl2.movement()
                        for bonus in bonuses:
                            bonus.collition(pl2.player_pos)
                    turns_till_the_end -= 1
            if pygame.mouse.get_pos()[0] in range(int(screen.get_width()/2-restart_button.get_width()/2),int(screen.get_width()/2+restart_button.get_width()/2)) and pygame.mouse.get_pos()[1] in range(int(screen.get_height()/2-restart_button.get_height()/2+100),int(screen.get_height()/2+restart_button.get_height()/2)+100) and game_status == 2:
                game_status = 0
                turn = "Red"
                turns_till_the_end = 40
                pl1.player_pos = pygame.Vector2(1085,665)
                pl1.direction = "left"
                pl1.score = 25
                pl2.player_pos = pygame.Vector2(1055,700)
                pl2.direction = "left"
                pl2.score = 25
                    
    if turns_till_the_end <= 0 or pl1.score <= 0 or pl2.score <= 0:
        game_status = 2
            
    screen.fill((0,80,0))
    for obj in fon_obj:
        obj.movement()
    
    if roll == True:
        dice.rolling()
        
    if game_status == 0:
        screen.blit(name_of_game, (screen.get_width()/2-name_of_game.get_width()/2,screen.get_height()/2-name_of_game.get_height()/2))
        screen.blit(start_button, (screen.get_width()/2-start_button.get_width()/2,screen.get_height()/2-restart_button.get_height()/2+100))
    elif game_status == 1:
        money1 = font2.render(f'{pl1.score} $', True, "Blue")
        screen.blit(money1, (1200-money1.get_width(),0))
        money2 = font2.render(f'{pl2.score} $', True, "Red")
        screen.blit(money2, (0,0))
        turns_till_the_ending = font2.render(f'Осталось {turns_till_the_end} ходов', True, 'yellow')
        screen.blit(turns_till_the_ending, (screen.get_width()/2-turns_till_the_ending.get_width()/2,screen.get_height()/2-turns_till_the_ending.get_height()/2+200))
        draw_corner_cell(1030,650)
        draw_corner_cell(70,650)
        draw_corner_cell(70,90)
        draw_corner_cell(1030,90)
        for cell in cells:
            cell.draw()
        bonuses.update()
        bonuses.draw(screen)
        for player in players:
            player.draw()
        dice.draw()
    elif game_status == 2:
        money1 = font2.render(f'{pl1.score} $', True, "Blue")
        screen.blit(money1, (1200-money1.get_width(),0))
        money2 = font2.render(f'{pl2.score} $', True, "Red")
        screen.blit(money2, (0,0))
        if pl1.score < pl2.score:
            winner = font1.render('Победил красный!', True, 'Red')
        elif pl1.score > pl2.score:
            winner = font1.render('Победил синий!', True, 'Blue')
        else:
            winner = font1.render('Победила ничья!', True, 'Grey')
        screen.blit(winner, (screen.get_width()/2-winner.get_width()/2,screen.get_height()/2-winner.get_height()/2))
        screen.blit(restart_button, (screen.get_width()/2-restart_button.get_width()/2,screen.get_height()/2-restart_button.get_height()/2+100))
    
    dt = time.tick(60)/1000
    
    pygame.display.flip()