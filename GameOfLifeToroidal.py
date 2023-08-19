import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game of Life - Toroidal")

# Grid dimensions
rows, cols = 50, 50
cell_size = width // rows

# Initialize grid
grid = np.random.choice([0, 1], size=(rows, cols))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Main loop
running = True
playing = False

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = not playing
        elif event.type == pygame.MOUSEBUTTONDOWN and not playing:
            x, y = pygame.mouse.get_pos()
            row, col = y // cell_size, x // cell_size
            grid[row, col] = 1 - grid[row, col]  # Toggle cell state

    if playing:
        new_grid = grid.copy()
        for row in range(rows):
            for col in range(cols):
                # Calculate the sum of the neighboring cells
                total = int(
                    grid[(row - 1) % rows, (col - 1) % cols]
                    + grid[(row - 1) % rows, col]
                    + grid[(row - 1) % rows, (col + 1) % cols]
                    + grid[row, (col - 1) % cols]
                    + grid[row, (col + 1) % cols]
                    + grid[(row + 1) % rows, (col - 1) % cols]
                    + grid[(row + 1) % rows, col]
                    + grid[(row + 1) % rows, (col + 1) % cols]
                )
                if grid[row, col] == 1:
                    if total < 2 or total > 3:
                        new_grid[row, col] = 0
                else:
                    if total == 3:
                        new_grid[row, col] = 1

        grid = new_grid

    for row in range(rows):
        for col in range(cols):
            color = WHITE if grid[row, col] == 1 else BLACK
            pygame.draw.rect(
                screen,
                color,
                (
                    col * cell_size,
                    row * cell_size,
                    cell_size,
                    cell_size,
                ),
            )

    pygame.display.flip()

pygame.quit()
