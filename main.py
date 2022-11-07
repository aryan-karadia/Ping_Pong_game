import pygame
import os

pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("My First Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

player1_img = pygame.image.load(os.path.join('assets', 'player.png'))
player2_img = pygame.image.load(os.path.join('assets', 'player.png'))
ball_img = pygame.image.load(os.path.join('assets', 'ball.png'))

def draw_window():

    screen.fill(BLACK)
    screen.blit(player1_img, (0, 250))
    screen.blit(player2_img, (850, 250))
    screen.blit(ball_img, (450, 250))
    pygame.display.update()

def main():

    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False
        
        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()