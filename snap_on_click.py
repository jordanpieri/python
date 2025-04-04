import pygame as pg
import math

# Initialize Pygame
pg.init()

# Constants
WINSIZE = [640, 480]
CYAN = (0, 255, 255)  # RGB color for cyan
WHITE = (255, 255, 255)  # RGB color for white
RED = (255, 0, 0)  # RGB color for red
FONT_SIZE = 24
SNAP_DISTANCE = 5  # Maximum distance to snap to a vertex

# Set up the display
screen = pg.display.set_mode(WINSIZE)
pg.display.set_caption("Snap to Vertices")

# Set up font
font = pg.font.Font(None, FONT_SIZE)

# Define the hexagon vertices
HEXAGON_VERTICES = [(320, 180), (400, 240), (400, 320), (320, 380), (240, 320), (240, 240)]
CONNECTION_POINTS = HEXAGON_VERTICES.copy()

# Function to find the closest vertex within the snap distance
def find_closest_vertex(pos, vertices, snap_distance):
    for vertex in vertices:
        distance = math.sqrt((vertex[0] - pos[0])**2 + (vertex[1] - pos[1])**2)
        if distance <= snap_distance:
            return vertex
    return pos  # Return the original position if no vertex is close enough

# Function to extend a line from the center to a vertex
def extend_line(center, vertex, length):
    vector_x = vertex[0] - center[0]
    vector_y = vertex[1] - center[1]
    vector_length = math.sqrt(vector_x**2 + vector_y**2)
    unit_vector_x = vector_x / vector_length
    unit_vector_y = vector_y / vector_length
    extended_x = center[0] + unit_vector_x * length
    extended_y = center[1] + unit_vector_y * length
    return (round(extended_x), round(extended_y))

# Main loop
running = True
while running:
    for e in pg.event.get():
        if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
            running = False
        if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
            # Fill the screen with a black background
            screen.fill((0, 0, 0))

            # Draw the hexagon
            pg.draw.polygon(screen, WHITE, HEXAGON_VERTICES, 1)

            pos = e.pos
            # Find the closest vertex within the snap distance
            snap_pos = find_closest_vertex(pos, CONNECTION_POINTS, SNAP_DISTANCE)

            # Draw a small cyan circle at the snap position
            pg.draw.circle(screen, CYAN, snap_pos, 5)

            # Render the coordinates as text
            coord_text = font.render(f"({snap_pos[0]}, {snap_pos[1]})", True, WHITE)

            # Blit the text onto the screen
            screen.blit(coord_text, (snap_pos[0] + 10, snap_pos[1] - 10))

            # Calculate the center of the hexagon
            center_x = sum(v[0] for v in HEXAGON_VERTICES) / len(HEXAGON_VERTICES)
            center_y = sum(v[1] for v in HEXAGON_VERTICES) / len(HEXAGON_VERTICES)
            center = (round(center_x), round(center_y))

            # Draw lines from the center to each vertex and extend them
            for vertex in HEXAGON_VERTICES:
                pg.draw.line(screen, RED, center, vertex, 1)
                extended_endpoint = extend_line(center, vertex, 100)  # Extend by 100 units
                pg.draw.line(screen, CYAN, center, extended_endpoint, 2)
                CONNECTION_POINTS.append(vertex)
                CONNECTION_POINTS.append(extended_endpoint)

            # Update the display
            pg.display.flip()

# Quit Pygame
pg.quit()