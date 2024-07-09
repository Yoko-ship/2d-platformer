import pygame,random,sys

pygame.init()
screen_width = 1600
screen_heigth = 1000
fps = 60

screen = pygame.display.set_mode((screen_width,screen_heigth))
my_font = pygame.font.SysFont("Times New Roman",20)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
player_speed = 5

score = 0

#*Sprites
player_sprite = pygame.sprite.Group()
all_objects = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
weapon_sprites = pygame.sprite.Group()


#* images
background_image = pygame.image.load("1671729412_kalix-club-p-fon-dlya.jpg")
water_image = pygame.image.load("preview_742.png")
ground_image = pygame.image.load("groundImage.png") 
ground_second_image = pygame.image.load("groundSecond.png")
tree_image = pygame.image.load("groundImage2.png")
groundImage3 = pygame.image.load("groundImage3.png")
groundImage4 = pygame.image.load("groundImage4.png")
enemy_image = pygame.image.load("enemy.png")

#*Animation
player_images = [
    pygame.image.load("playerImage.png"),pygame.image.load("playerImage2.png"),
    pygame.image.load("playerImage3.png"),pygame.image.load("playerImage4.png"),
    pygame.image.load("playerImage5.png"),pygame.image.load("playerImage7 — копия.png"),
    pygame.image.load("playerImage7.png"),pygame.image.load("playerImage8.png")
]


player_image_number = 0


#*Delay
delay = 0


#* Прыжок
jump = False
jump_count = 0
jump_max = 55





class Player(pygame.sprite.Sprite):
    def __init__(self,image,x,y,):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.is_jump = False
        self.speedy = 0
    

    def update(self):
        keys = pygame.key.get_pressed()
        global delay
        delay += pygame.time.get_ticks()
        if delay > 5000:
            delay = 0
        if keys[pygame.K_RIGHT] and delay == 0:
            self.rect.x += player_speed
            global player_image_number
            player_image_number += 1
            if player_image_number >= 4:
                player_image_number = 0
            

        
        if keys[pygame.K_LEFT] and delay == 0 :
            self.rect.x -= player_speed
            player_image_number += 1
            if player_image_number >= 8:
                player_image_number = 4
            

        
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= screen_width:
            self.rect.y += 3
        global run
        if self.rect.right >= screen_width + 90: 
            run = False

        
        #*Teleport to another world        
        # if player.rect.x >= 1400 and player.rect.y <= 100:
        #     run = False



class Objects(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
        global jump_max
        if pygame.sprite.collide_rect(player,object_tree):
            player.rect.bottom = object_tree.rect.top
            jump_max = 55
        if pygame.sprite.collide_rect(player,ground):
            player.rect.bottom = ground.rect.top
        if pygame.sprite.collide_rect(player,ground_object):
            player.rect.bottom = ground_object.rect.top
            jump_max = 55
        if pygame.sprite.collide_rect(player,ground_object_2):
            player.rect.bottom = ground_object_2.rect.top
            jump_max = 55        
        if pygame.sprite.collide_rect(player,ground_object_3):
            player.rect.bottom = ground_object_3.rect.top
            jump_max = 55
        if pygame.sprite.collide_rect(player,ground_end):
            player.rect.bottom = ground_end.rect.top
            jump_max = 55
        
        if not pygame.sprite.groupcollide(player_sprite,all_objects,False,False):
                player.rect.y += 5
                if player.rect.y >= screen_heigth - 150:
                    player.rect.y = screen_heigth - 150 

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image,y):
        super().__init__()
        self.image = image
        self.direction = random.randint(1700,2500)
        self.rect = self.image.get_rect()
        self.rect.center = (self.direction,y)

    def update(self):
        self.rect.x -= 5
        if self.rect.right <= 0:
            self.kill()
        global run
        if pygame.sprite.groupcollide(enemy_sprites,player_sprite,False,False):
            run = False



        

class Weapon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1,1))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 40
        self.speedx = 0
 
    def update(self):
        keys = pygame.key.get_pressed()             
        global score
        if keys[pygame.K_SPACE]:
            self.image = pygame.image.load("weaponImage_pixian_ai.png")
            self.speedx += 3
            self.rect.x = player.rect.x
            self.rect.y = player.rect.y + 40
        if pygame.sprite.groupcollide(weapon_sprites,enemy_sprites,True,True):
            score += 10
        if self.rect.right >= screen_width:
            self.kill()

        self.rect.x += self.speedx


player = Player(player_images[player_image_number],30,screen_heigth - 70)
player_sprite.add(player)


 
another_enemy = Enemy(enemy_image,screen_heigth / 2 - 200)
enemy_sprites.add(another_enemy)

button_surface = pygame.Surface((150,50))
button_text = my_font.render("Start game",True,(0,0,0))
button_text_rect = button_text.get_rect(center = (button_surface.get_width() / 2,button_surface.get_height() /2 ))
button_rect = pygame.Rect(700,400,150,50)

quit_surface = pygame.Surface((150,50))
quit_text = my_font.render("Quit game",True,(0,0,0))
quit_text_rect = quit_text.get_rect(center = (quit_surface.get_width() / 2,quit_surface.get_height() /2 ))
quit_rect = pygame.Rect(700,600,150,50)


main_menu = False
while (main_menu == False):
    clock.tick(fps)
    screen.fill((215,209,121))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                main_menu = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if quit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface,(215,115,222),(1,1,148,48))
    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

    

    if quit_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(quit_surface,(192,192,192),(1,1,148,48))
    else:
        pygame.draw.rect(quit_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(quit_surface, (255, 255, 255), (1, 1, 148, 48))
        pygame.draw.rect(quit_surface, (0, 0, 0), (1, 1, 148, 1), 2)
        pygame.draw.rect(quit_surface, (0, 100, 0), (1, 48, 148, 10), 2)
    
    
    button_surface.blit(button_text,button_text_rect)
    screen.blit(button_surface,(button_rect.x,button_rect.y))
    quit_surface.blit(quit_text,quit_text_rect)
    screen.blit(quit_surface,(quit_rect.x,quit_rect.y))
    
    
    
    
    pygame.display.flip()

paused = False
run = True
while run:

    clock.tick(fps)

    #*Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
        


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
            #* Прыжок
            if not jump and event.key == pygame.K_UP :
                jump = True
                jump_count = jump_max
        
                #* Прыжок
    if jump:
        player.rect.y -= jump_count
        if jump_count > -jump_max:
            jump_count -= 1
        else:
            jump = False


    
    #*Sprites

    if not paused:    
        player_sprite.update()

        if len(all_objects) == 0:
            object_tree = Objects(tree_image,1300,800)
            all_objects.add(object_tree)
            ground = Objects(groundImage3,800,800)
            all_objects.add(ground)
            ground_object = Objects(groundImage3,1500,500)
            all_objects.add(ground_object)
            ground_object_2 = Objects(groundImage4,950,400)
            all_objects.add(ground_object_2)
            ground_object_3 = Objects(groundImage4,250,400)
            all_objects.add(ground_object_3)
            ground_end = Objects(groundImage3,1500,150)
            all_objects.add(ground_end)
        all_objects.update()

        if len(enemy_sprites) == 0:
            enemy = Enemy(enemy_image,screen_heigth - 50)
            enemy_sprites.add(enemy)
            another_enemy = Enemy(enemy_image,screen_heigth / 2 - 200)
            enemy_sprites.add(another_enemy)
        enemy_sprites.update()

        if len(weapon_sprites) == 0:
            weapon = Weapon()
            weapon_sprites.add(weapon)

        weapon_sprites.update()

        screen.blit(background_image,(0,0))
        screen.blit(ground_image,(-30,screen_heigth - 50))
        screen.blit(groundImage4,(900,screen_heigth - 50))
        #*Animation
        screen.blit(player_images[player_image_number],player)
        enemy_sprites.draw(screen)
        all_objects.draw(screen)
        weapon_sprites.draw(screen)
        score_text = my_font.render(f"Score: {score}",True,(255,255,255))
        screen.blit(score_text,(10,20))
        pygame.display.flip()
pygame.quit()


