import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a hexagon
def draw_hexagon(surface, color, center, size):
    points = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = center[0] + size * math.cos(angle)
        y = center[1] + size * math.sin(angle)
        points.append((x, y))
    pygame.draw.polygon(surface, color, points, 1)

# Function to draw a triangle
def draw_triangle(surface, color, center, size):
    points = []
    for i in range(3):
        angle = math.radians(120 * i - 30)
        x = center[0] + size * math.cos(angle)
        y = center[1] + size * math.sin(angle)
        points.append((x, y))
    pygame.draw.polygon(surface, color, points, 1)

# Function to add a new shape
def add_shape(shapes, center, size):
    # Randomly choose to add a hexagon or triangle
    shape_type = random.choice(['hexagon', 'triangle'])
    # Calculate new size
    new_size = size * random.uniform(0.5, 0.8)
    # Calculate new positions symmetrically around the center
    for i in range(6):
        angle = math.radians(60 * i)
        new_center = (
            center[0] + size * math.cos(angle),
            center[1] + size * math.sin(angle)
        )
        shapes.append((shape_type, new_center, new_size))

def main():
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Interactive Snowflake Generator")

    # Initial hexagon settings
    initial_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    initial_size = 100

    # List to store shapes
    shapes = [('hexagon', initial_center, initial_size)]

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Add new shapes on mouse click
                for shape in shapes:
                    add_shape(shapes, shape[1], shape[2])

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw all shapes
        for shape_type, center, size in shapes:
            if shape_type == 'hexagon':
                draw_hexagon(screen, WHITE, center, size)
            elif shape_type == 'triangle':
                draw_triangle(screen, WHITE, center, size)

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()