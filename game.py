import pygame,random,time

pygame.init()
WIDTH = 400
HEIGHT = 300
screen = pygame.display.set_mode((HEIGHT,WIDTH))
title = pygame.display.set_caption("Game Simple by Khanh")
speed = 1
run=True
clock = pygame.time.Clock()
game_over = False 
a,b = [],[]
is_cooldown=True
kill=False
class player:
    def __init__(self):
        self.player_surface = pygame.Rect(300//2,300,30,30)
    def control(self,keys):
        if keys[pygame.K_LEFT]:
            self.player_surface.x-=3
        elif keys[pygame.K_RIGHT]:
            self.player_surface.x+=3
        elif keys[pygame.K_UP]:
            self.player_surface.y-=3
        elif keys[pygame.K_DOWN]:
             self.player_surface.y+=3

            
    def conditionp(self,HEIGHT):
        if self.player_surface.x>=HEIGHT-50:
            self.player_surface.x=HEIGHT-50
        if self.player_surface.x<=0:
            self.player_surface.x=0
    def draw(self,screen):
        pygame.draw.rect(screen,(123,123,123),self.player_surface)

class armor(player):
    def __init__(self):
        super().__init__()
        self.armor = pygame.Rect(Khanh.player_surface.x+12, Khanh.player_surface.y,10, 10)
    def drawarmor(self):
        self.armor.y-=9
        pygame.draw.rect(screen, (255,255,255), self.armor)
    def dame(self):
        if self.armor.colliderect(Ball.ball):
            Ball.hp-=1
            print(Ball.hp)

class ball():
    def __init__(self):
        self.ball = pygame.Rect(100, 100, 20, 20)
        self.speed_x = 1  # Initial speed in the x-direction
        self.speed_y = 1  # Initial speed in the y-direction
        self.ball.x = random.randint(0,100)
        self.ball.y = random.randint(0,100)
        self.hp = 50
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), self.ball)
    def conditionb(self,WIDTH,HEIGHT):
        if self.ball.right >= HEIGHT:
            self.speed_x = -1
        if self.ball.x<=0:
            self.speed_x = 1
        if self.ball.bottom >= WIDTH:
            self.speed_y = -1
        if self.ball.y <=0:
            self.speed_y=1
        #if self.ball.y== self.player_surface.y and (self.ball.x>=self.player_surface.x and self.ball.x <= self.player_surface.x+50):   
    def move(self):
        self.ball.x+=self.speed_x
        self.ball.y+=self.speed_y
class box(ball,armor):
    def __init__(self):
        super().__init__()
        self.box = pygame.Rect(random.randint(0,HEIGHT),random.randint(0,100),20,20)
        self.speed_y_fall = 0
    def vacham(self):
        global game_over
        if self.box.colliderect(Khanh.player_surface):
            game_over=True
    def fall(self):
        self.box.y+=4
    def drawbox(self):
        self.fall()
        pygame.draw.rect(screen,(45,45,45),self.box)

Khanh = player()
Ball = ball()
while run:
    for i in pygame.event.get():
        if i == pygame.QUIT:
            pygame.quit()
            run = False  
            break
    
    if not game_over:  
        clock.tick(60)
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        Khanh.control(keys)
        Khanh.conditionp(HEIGHT)

        Ball.conditionb(WIDTH, HEIGHT)
        Ball.move()
        Ball.draw(screen)
        if not a:
            dan = armor()
            a.append(dan)
        for i in a:
            i.drawarmor()
            if i.armor.colliderect(Ball.ball):
                Ball.hp-=1
                a.remove(i)
                print(Ball.hp)
            elif i.armor.y <=00:
                a.remove(i)
        if not b:
            Box = box()
            b.append(Box)
        for j in b:
            j.drawbox()
            j.vacham()
            if j.box.y >=WIDTH:
                b.remove(j)
        if Ball.hp==0: 
            del ball 
            print("You Win!")
        if Khanh.player_surface.colliderect(Ball.ball):
            game_over=True
        Khanh.draw(screen)    
    if game_over:
        BLACK = (0,0,0)
        WHITE = (255,255,255)
        screen.fill((105,105,105))
    
        font = pygame.font.Font(None, 60)
        game_over_text = font.render("Game Over", True, BLACK)
        game_over_text_rect = game_over_text.get_rect()
        game_over_text_rect.center = (WIDTH // 2-50, HEIGHT // 2 - 30)


        screen.fill(WHITE)
        screen.blit(game_over_text, game_over_text_rect)

    

    pygame.display.update()
