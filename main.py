import pygame
import os
import sys
import random

screen_width = 900
screen_height = 500

#initialise pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")

#colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
bg_colour = pygame.Color('grey12')
LIGHT_GREY = (200, 200, 200)

#global variables
FPS = 60

VEL = 5
ball_vel_x = 7 * random.choice((1,-1))
ball_vel_y = 7 * random.choice((1,-1))

#images
player1_img = pygame.image.load(os.path.join('assets', 'player.png'))
player1_img = pygame.transform.scale(player1_img, (25, 100))
player2_img = pygame.image.load(os.path.join('assets', 'player.png'))
player2_img = pygame.transform.scale(player2_img, (25, 100))
ball_img = pygame.image.load(os.path.join('assets', 'ball.png'))
ball_img = pygame.transform.scale(ball_img, (20, 20))

def draw_window(p1, p2, ball):

    screen.fill(bg_colour)
    screen.blit(player1_img, (p1.x, p1.y))
    screen.blit(player2_img, (p2.x, p2.y))
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, LIGHT_GREY,(screen_width/2, 0), (screen_width/2, screen_height))
    pygame.display.update()

def p1_movement(keys_pressed, p1):
    if keys_pressed[pygame.K_w] and p1.y - VEL > 0: # Player 1 going up
        p1.y -= VEL
    if keys_pressed[pygame.K_s] and p1.y + VEL + p1.height < screen_height: # Player 1 going down
        p1.y += VEL

def p2_movement(keys_pressed, p2):
    if keys_pressed[pygame.K_UP] and p2.y - VEL > 0: # Player 2 going up
        p2.y -= VEL
    if keys_pressed[pygame.K_DOWN] and p2.bottom + VEL < screen_height: # Player 2 going down
        p2.y += VEL

def ball_movement(ball, p1, p2):
    global ball_vel_x, ball_vel_y
    ball.x += ball_vel_x
    ball.y += ball_vel_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_vel_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_update(ball)

    if ball.colliderect(p1) or ball.colliderect(p2):
        ball_vel_x *= -1

def ball_update(ball):
    global ball_vel_x, ball_vel_y
    ball.center = (screen_width/2, screen_height/2)
    ball_vel_x *= random.choice((1,-1))
    ball_vel_y *= random.choice((1,-1))

def main():
    p1 = pygame.Rect(0, screen_height/2, 25, 100)
    p2 = pygame.Rect(870, screen_height/2, 25, 100)
    ball = pygame.Rect(440, 240, 20, 20)

    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False
        
        #ball movement
        ball_movement(ball, p1, p2)

        #player movement
        keys_pressed = pygame.key.get_pressed()

        p1_movement(keys_pressed, p1)
        p2_movement(keys_pressed, p2)

        #draw window
        draw_window(p1, p2, ball)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()