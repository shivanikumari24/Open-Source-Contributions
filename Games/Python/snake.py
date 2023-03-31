import pygame
import random

# Set up the game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
CELL_SIZE = 20
pygame.init()
pygame.display.set_caption("Snake Game")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set up the snake
snake = [(200, 200)]
snake_direction = "right"

# Set up the food
food = (random.randint(0, (WINDOW_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
        random.randint(0, (WINDOW_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

# Set up the game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"
            elif event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"

    # Move the snake
    if snake_direction == "up":
        new_head = (snake[0][0], snake[0][1] - CELL_SIZE)
    elif snake_direction == "down":
        new_head = (snake[0][0], snake[0][1] + CELL_SIZE)
    elif snake_direction == "left":
        new_head = (snake[0][0] - CELL_SIZE, snake[0][1])
    elif snake_direction == "right":
        new_head = (snake[0][0] + CELL_SIZE, snake[0][1])
    snake.insert(0, new_head)

    # Check for collisions with the food
    if snake[0] == food:
        food = (random.randint(0, (WINDOW_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (WINDOW_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
    else:
        snake.pop()

    # Draw the snake and food
    window.fill((0, 0, 0))
    for cell in snake:
        pygame.draw.rect(window, (255, 255, 255), (cell[0], cell[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(window, (255, 0, 0), (food[0], food[1], CELL_SIZE, CELL_SIZE))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(10)

# Clean up
pygame.quit()
