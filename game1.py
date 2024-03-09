import pygame 
import os
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FIRST GAME!")#name of terminal window
WHITE = (255,255,255)
BORDER = pygame.Rect(WIDTH//2 - 5,0,10,HEIGHT)
BLACK = (0,0,0)
FPS = 60
VEL = 5 
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH ,SPACESHIP_HEIGHT = 75, 50
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH ,SPACESHIP_HEIGHT)),90)#rescaling spaceship size and rotating
red_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
red_SPACESHIP =  pygame.transform.rotate(pygame.transform.scale(red_SPACESHIP_IMAGE, (SPACESHIP_WIDTH ,SPACESHIP_HEIGHT)),270)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2






def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    WIN.blit(red_SPACESHIP,(red.x,red.y))
    pygame.display.update()
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > -5: #left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x + 30: #right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 20: #down
        yellow.y += VEL
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH + 30: #right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 20: #down
        red.y += VEL
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(yellow):
            pygame.event.post(pygame.event.EVENT(RED_HIT))
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(red):
            pygame.event.post(pygame.event.EVENT(YELLOW_HIT))
            red_bullets.remove(bullet)




def main():
    red = pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red_bullets = []
    yellow_bullets = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #list of events
            if event.type == pygame.QUIT:
                run = False
            if pygame.event == pygame.KEYDOWN:
                if pygame.event == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if pygame.event == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow)
    pygame.quit()

if __name__ ==  "__main__":
    main()
