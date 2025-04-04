import random
import math
import pygame as pg

# Constants
WINSIZE = [640, 480]
WINCENTER = [320, 240]
CONNECTION_POINTS = []

def equilateral_triangle_from_point(start_point, side_length, orientation_angle=0):
    """Calculate the vertices of an equilateral triangle from a starting point with a given orientation."""
    x1, y1 = start_point
    angle_rad = math.radians(orientation_angle)
    x2 = round(x1 + side_length * math.cos(angle_rad))
    y2 = round(y1 + side_length * math.sin(angle_rad))
    x3 = round(x1 + side_length * math.cos(angle_rad + math.pi / 3))
    y3 = round(y1 + side_length * math.sin(angle_rad + math.pi / 3))
    return [(x1, y1), (x2, y2), (x3, y3)]

def calculate_median_angle(vertex, opposite_vertex1, opposite_vertex2):
    """Calculate the angle of the median from a vertex with respect to the horizontal axis."""
    midpoint = (
        round((opposite_vertex1[0] + opposite_vertex2[0]) / 2),
        round((opposite_vertex1[1] + opposite_vertex2[1]) / 2)
    )
    median_vector = (midpoint[0] - vertex[0], midpoint[1] - vertex[1])
    angle_radians = math.atan2(median_vector[1], median_vector[0])
    inverted_angle_radians = angle_radians + math.pi
    inverted_angle_degrees = round(math.degrees(inverted_angle_radians) % 360 - 30)
    return inverted_angle_degrees

def triangles_overlap(triangle1, triangle2):
    """Check if two triangles overlap."""
    for vertex in triangle1:
        if vertex in CONNECTION_POINTS:
            continue
        if is_point_in_triangle(vertex, triangle2):
            return True
    for vertex in triangle2:
        if vertex in CONNECTION_POINTS:
            continue
        if is_point_in_triangle(vertex, triangle1):
            return True
    return False

def is_point_in_triangle(pt, v):
    """Check if a point is inside a triangle using barycentric coordinates."""
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    b1 = sign(pt, v[0], v[1]) < 0.0
    b2 = sign(pt, v[1], v[2]) < 0.0
    b3 = sign(pt, v[2], v[0]) < 0.0
    return ((b1 == b2) and (b2 == b3))

def new_triangle(triangle_vertices):
    """Create a new triangle on one of the vertices."""
    new_triangle_vertices = None 
    for x in range(3):
        point = triangle_vertices[x]
        if point not in CONNECTION_POINTS:
            if x == 0:
                angle = calculate_median_angle(triangle_vertices[0], triangle_vertices[1], triangle_vertices[2])
            elif x == 1:
                angle = calculate_median_angle(triangle_vertices[1], triangle_vertices[0], triangle_vertices[2])
            else:
                angle = calculate_median_angle(triangle_vertices[2], triangle_vertices[0], triangle_vertices[1])
            new_triangle_vertices = equilateral_triangle_from_point(point, 50, angle)
            CONNECTION_POINTS.append(point)
            break  # Exit the loop after creating a new triangle
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

    # List to keep track of all triangles
    triangles = [TRIANGLE_VERTICES]
    pg.draw.polygon(screen, white, TRIANGLE_VERTICES, 1)
    pg.display.update()

    while not done:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                done = True
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                for triangle in triangles:
                    new_triangle_vertices = new_triangle(triangle)
                    if new_triangle_vertices is None:
                        continue  # Skip if no new triangle was created
                    if not any(triangles_overlap(new_triangle_vertices, existing) for existing in triangles):
                        triangles.append(new_triangle_vertices)
                        pg.draw.polygon(screen, white, new_triangle_vertices, 1)
                        pg.display.update()
                        break  # Exit the loop after adding one triangle
        clock.tick(50)
    pg.quit()

if __name__ == "__main__":
    TRIANGLE_VERTICES = equilateral_triangle_from_point((320, 150), 220, 60)
    main()