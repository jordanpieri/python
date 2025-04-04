import random
import math
import pygame as pg

# Constants
WINSIZE = [640, 480]
WINCENTER = [320, 240]

def equilateral_triangle_from_point(start_point, side_length, orientation_angle=0):
    """Calculate the vertices of an equilateral triangle from a starting point with a given orientation."""
    x1, y1 = start_point
    angle_rad = math.radians(orientation_angle)
    x2 = x1 + side_length * math.cos(angle_rad)
    y2 = y1 + side_length * math.sin(angle_rad)
    x3 = x1 + side_length * math.cos(angle_rad + math.pi / 3)
    y3 = y1 + side_length * math.sin(angle_rad + math.pi / 3)
    return [(x1, y1), (x2, y2), (x3, y3)]

def calculate_median_angle(vertex, opposite_vertex1, opposite_vertex2):
    """Calculate the angle of the median from a vertex with respect to the horizontal axis."""
    midpoint = (
        (opposite_vertex1[0] + opposite_vertex2[0]) / 2,
        (opposite_vertex1[1] + opposite_vertex2[1]) / 2
    )
    median_vector = (midpoint[0] - vertex[0], midpoint[1] - vertex[1])
    angle_radians = math.atan2(median_vector[1], median_vector[0])
    inverted_angle_radians = angle_radians + math.pi
    inverted_angle_degrees = math.degrees(inverted_angle_radians) % 360 - 30
    return inverted_angle_degrees

def new_triangle():
    """Create a new triangle on one of the vertices."""
    x = random.randint(0, 2)
    point = TRIANGLE_VERTICES[x]
    if x == 0:
        angle = calculate_median_angle(TRIANGLE_VERTICES[0], TRIANGLE_VERTICES[1], TRIANGLE_VERTICES[2])
    elif x == 1:
        angle = calculate_median_angle(TRIANGLE_VERTICES[1], TRIANGLE_VERTICES[0], TRIANGLE_VERTICES[2])
    else:
        angle = calculate_median_angle(TRIANGLE_VERTICES[2], TRIANGLE_VERTICES[0], TRIANGLE_VERTICES[1])
    new_triangle_vertices = equilateral_triangle_from_point(point, 50, angle)
    print(f"angle = {angle}")
    return new_triangle_vertices

def main():
    """Main function to handle triangle generation."""
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("Pygame Triangle Example")
    white = 255, 240, 200
    black = 20, 20, 40
    screen.fill(black)
    clock = pg.time.Clock()
    done = False
    pg.draw.polygon(screen, white, TRIANGLE_VERTICES, 1)
    pg.display.update()
    while not done:
        #screen.fill(black)
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                done = True
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                new_triangle_vertices = new_triangle()
                print(new_triangle_vertices)
                pg.draw.polygon(screen, white, new_triangle_vertices, 1)
                pg.display.update()
        clock.tick(50)
    pg.quit()

if __name__ == "__main__":
    TRIANGLE_VERTICES = equilateral_triangle_from_point((320, 150), 220, 60)
    main()