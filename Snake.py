import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 640
height = 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set up game variables
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, width//10) * 10, random.randrange(1, height//10) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

# Set up game clock
clock = pygame.time.Clock()
fps = 15

# Game Over function
def game_over():
    font = pygame.font.SysFont('Arial', 30)
    text = font.render('Game Over!', True, white)
    text_rect = text.get_rect()
    text_rect.midtop = (width/2, height/4)
    window.fill(black)
    window.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            elif event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'

    # Validate direction
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Update snake position
    if direction == 'RIGHT':
        snake_position[0] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10

    # Snake body mechanics
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn food
    if not food_spawn:
        food_position = [random.randrange(1, width//10) * 10, random.randrange(1, height//10) * 10]
    food_spawn = True

    # Draw game elements
    window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, red, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > width-10 or snake_position[1] < 0 or snake_position[1] > height-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Update score
    font = pygame.font.SysFont('Arial', 20)
    score_text = font.render(f'Score: {score}', True, white)
    window.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(fps)
