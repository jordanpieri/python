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

def hexagon_from_point(start_point, side_length, orientation_angle=0):
    """Calculate the vertices of a hexagon from a starting point with a given orientation."""
    x1, y1 = start_point
    angle_rad = math.radians(orientation_angle)
    vertices = []
    for i in range(6):
        angle = angle_rad + i * math.pi / 3
        x = round(x1 + side_length * math.cos(angle))
        y = round(y1 + side_length * math.sin(angle))
        vertices.append((x, y))
    return vertices

def calculate_median_angle_triangle(vertex, opposite_vertex1, opposite_vertex2):
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

def calculate_diagonal_angle_hexagon(vertex, hexagon_vertices):
    """Calculate the angle of a diagonal from a vertex through the center of a hexagon."""
    # Calculate the center of the hexagon
    center_x = sum(v[0] for v in hexagon_vertices) / len(hexagon_vertices)
    center_y = sum(v[1] for v in hexagon_vertices) / len(hexagon_vertices)
    center = (round(center_x), round(center_y))
    
    # Calculate the vector from the vertex to the center
    diagonal_vector = (center[0] - vertex[0], center[1] - vertex[1])
    angle_radians = math.atan2(diagonal_vector[1], diagonal_vector[0])
    angle_degrees = round(math.degrees(angle_radians) % 360)
    return angle_degrees

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

def new_shape(vertices):
    """Create a new shape (triangle or hexagon) on one of the vertices."""
    new_shape_vertices = None
    for x in range(len(vertices)):
        point = vertices[x]
        if point not in CONNECTION_POINTS:
            shape_type = random.choice(['triangle', 'hexagon'])
            if shape_type == 'triangle':
                if x < len(vertices) - 1:
                    angle = calculate_median_angle_triangle(vertices[x], vertices[(x+1) % len(vertices)], vertices[(x+2) % len(vertices)])
                else:
                    angle = calculate_median_angle_triangle(vertices[x], vertices[0], vertices[1])
                new_shape_vertices = equilateral_triangle_from_point(point, 50, angle)
            else:
                if x < len(vertices) - 1:
                    angle = calculate_diagonal_angle_hexagon(vertices[x], vertices)
                else:
                    angle = calculate_diagonal_angle_hexagon(vertices[x], vertices)
                new_shape_vertices = hexagon_from_point(point, 30, angle)
            CONNECTION_POINTS.append(point)
            break  # Exit the loop after creating a new shape
    return new_shape_vertices

def main():
    """Main function to handle shape generation."""
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("Pygame Shape Example")
    white = 255, 240, 200
    black = 20, 20, 40
    screen.fill(black)
    clock = pg.time.Clock()
    done = False

    # List to keep track of all shapes
    shapes = [HEXAGON_VERTICES]
    pg.draw.polygon(screen, white, HEXAGON_VERTICES, 1)
    pg.display.update()

    while not done:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                done = True
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                for shape in shapes:
                    new_shape_vertices = new_shape(shape)
                    if new_shape_vertices is None:
                        continue  # Skip if no new shape was created
                    if not any(triangles_overlap(new_shape_vertices, existing) for existing in shapes):
                        shapes.append(new_shape_vertices)
                        pg.draw.polygon(screen, white, new_shape_vertices, 1)
                        pg.display.update()
                        break  # Exit the loop after adding one shape
        clock.tick(50)
    pg.quit()

if __name__ == "__main__":
    HEXAGON_VERTICES = hexagon_from_point((320, 240), 60, 0)
    main()