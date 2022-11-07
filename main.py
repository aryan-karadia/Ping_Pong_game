import pygame
import os

pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("My First Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BORDER = pygame.Rect(447.5, 0, 5, 500)

FPS = 60

VEL = 5

background_img = pygame.image.load(os.path.join("assets", "background.png"))
player1_img = pygame.image.load(os.path.join('assets', 'player.png'))
player1_img = pygame.transform.scale(player1_img, (25, 50))
player2_img = pygame.image.load(os.path.join('assets', 'player.png'))
player2_img = pygame.transform.scale(player2_img, (25, 50))
ball_img = pygame.image.load(os.path.join('assets', 'ball.png'))
ball_img = pygame.transform.scale(ball_img, (20, 20))

def draw_window(p1, p2):

    screen.blit(background_img, (0, 0))
    pygame.draw.rect(screen, WHITE, BORDER)
    screen.blit(player1_img, (p1.x, p1.y))
    screen.blit(player2_img, (p2.x, p2.y))
    screen.blit(ball_img, (450, 250))
    pygame.display.update()

def p1_movement(keys_pressed, p1):
    if keys_pressed[pygame.K_w] and p1.y - VEL > 0: # Player 1 going up
        p1.y -= VEL
    if keys_pressed[pygame.K_s] and p1.y + VEL + p1.height < 500: # Player 1 going down
        p1.y += VEL

def p2_movement(keys_pressed, p2):
    if keys_pressed[pygame.K_UP] and p2.y - VEL > 0: # Player 2 going up
        p2.y -= VEL
    if keys_pressed[pygame.K_DOWN] and p2.y + VEL + p2.height < 500: # Player 2 going down
        p2.y += VEL

def main():
    p1 = pygame.Rect(0, 250, 25, 50)
    p2 = pygame.Rect(870, 250, 25, 50)

    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False
        
        keys_pressed = pygame.key.get_pressed()

        p1_movement(keys_pressed, p1)
        p2_movement(keys_pressed, p2)

        draw_window(p1, p2)

    pygame.quit()


if __name__ == '__main__':
    main()