import pygame
import sys
import random

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5
BALL_SPEED_X = 5
BALL_SPEED_Y = 5


player_y = (WINDOW_HEIGHT - PADDLE_HEIGHT) // 2
computer_y = (WINDOW_HEIGHT - PADDLE_HEIGHT) // 2
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))


pygame.init()


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong Game")


black = (0, 0, 0)
white = (255, 255, 255)


clock = pygame.time.Clock()


def draw_objects(player_y, computer_y, ball_x, ball_y):
    pygame.draw.rect(screen, white, (50, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, white, (WINDOW_WIDTH - 50 - PADDLE_WIDTH, computer_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, white, (ball_x, ball_y), BALL_RADIUS)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        player_y += PADDLE_SPEED

  
    if computer_y + PADDLE_HEIGHT // 2 < ball_y:
        computer_y += PADDLE_SPEED
    elif computer_y + PADDLE_HEIGHT // 2 > ball_y:
        computer_y -= PADDLE_SPEED

    
    ball_x += ball_speed_x
    ball_y += ball_speed_y

   
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= WINDOW_HEIGHT:
        ball_speed_y = -ball_speed_y

    
    if (
        (50 <= ball_x - BALL_RADIUS <= 50 + PADDLE_WIDTH and player_y <= ball_y <= player_y + PADDLE_HEIGHT) or
        (WINDOW_WIDTH - 50 - PADDLE_WIDTH <= ball_x + BALL_RADIUS <= WINDOW_WIDTH - 50 and
         computer_y <= ball_y <= computer_y + PADDLE_HEIGHT)
    ):
        ball_speed_x = -ball_speed_x

    
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WINDOW_WIDTH:
       
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2
        ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
        ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

   
    screen.fill(black)
    draw_objects(player_y, computer_y, ball_x, ball_y)
    pygame.display.flip()
    clock.tick(60)
