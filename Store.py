import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 7

# Enemy settings
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 5

# Clock
clock = pygame.time.Clock()

# Game loop
def game_loop():
    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
            player_pos[0] += player_speed

        # Enemy movement
        enemy_pos[1] += enemy_speed
        if enemy_pos[1] >= HEIGHT:
            enemy_pos[1] = 0
            enemy_pos[0] = random.randint(0, WIDTH - enemy_size)

        # Collision detection
        if (
            player_pos[0] < enemy_pos[0] + enemy_size and
            player_pos[0] + player_size > enemy_pos[0] and
            player_pos[1] < enemy_pos[1] + enemy_size and
            player_pos[1] + player_size > enemy_pos[1]
        ):
            print("Game Over!")
            running = False

        # Draw player and enemy
        pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))
        pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()

game_loop()
