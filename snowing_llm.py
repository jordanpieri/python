import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Snowflake class
class Snowflake:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

    def fall(self):
        # Move the snowflake down by its speed
        self.y += self.speed
        # If the snowflake goes off the screen, reset it to the top
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self, screen):
        # Draw the snowflake as a circle
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

# Function to generate snowflakes
def generate_snowflakes(count, min_size, max_size, min_speed, max_speed):
    snowflakes = []
    for _ in range(count):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(-50, SCREEN_HEIGHT)
        size = random.randint(min_size, max_size)
        speed = random.uniform(min_speed, max_speed)
        snowflakes.append(Snowflake(x, y, size, speed))
    return snowflakes

def main():
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snowflake Generator")

    # Snowflake settings
    snowflake_count = 100  # Number of snowflakes
    min_size = 2           # Minimum size of snowflakes
    max_size = 5           # Maximum size of snowflakes
    min_speed = 1          # Minimum speed of snowflakes
    max_speed = 3          # Maximum speed of snowflakes

    # Generate snowflakes
    snowflakes = generate_snowflakes(snowflake_count, min_size, max_size, min_speed, max_speed)

    # Main loop
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill(BLACK)

        # Update and draw each snowflake
        for snowflake in snowflakes:
            snowflake.fall()
            snowflake.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()