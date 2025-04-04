import random
import math
import pygame as pg

# Constants
WINSIZE = (640, 480)
WINCENTER = (320, 240)
CONNECTION_POINTS = []
END_POINTS = []
USED_POINTS = set()
CLICK_COUNT = 0

def calculate_end_point(start_point, length, angle_degrees):
    angle_radians = math.radians(angle_degrees - 30 + 180)
    end_x = start_point[0] + length * math.cos(angle_radians)
    end_y = start_point[1] + length * math.sin(angle_radians)
    return (round(end_x), round(end_y))

def equilateral_triangle_from_point(start_point, side_length, orientation_angle=0):
    x1, y1 = start_point
    angle_rad = math.radians(orientation_angle + 180)
    x2 = round(x1 + side_length * math.cos(angle_rad))
    y2 = round(y1 + side_length * math.sin(angle_rad))
    x3 = round(x1 + side_length * math.cos(angle_rad + math.pi / 3))
    y3 = round(y1 + side_length * math.sin(angle_rad + math.pi / 3))
    return [(x1, y1), (x2, y2), (x3, y3)]

def hexagon_from_point(start_point, side_length, orientation_angle=0):
    #new_center = calculate_end_point(start_point, side_length, orientation_angle)
    #x1, y1 = new_center
    x1, y1 = start_point
    angle_rad = math.radians(orientation_angle)
    return [(round(x1 + side_length * math.cos(angle_rad + i * math.pi / 3)),
             round(y1 + side_length * math.sin(angle_rad + i * math.pi / 3))) for i in range(6)]

def calculate_median_angle_triangle(vertex, opposite_vertex1, opposite_vertex2):
    midpoint = ((opposite_vertex1[0] + opposite_vertex2[0]) / 2,
                (opposite_vertex1[1] + opposite_vertex2[1]) / 2)
    angle_radians = math.atan2(midpoint[1] - vertex[1], midpoint[0] - vertex[0])
    return round(math.degrees(angle_radians + math.pi) % 360 - 30)

def calculate_diagonal_angle_hexagon(vertex, hexagon_vertices):
    center_x = sum(v[0] for v in hexagon_vertices) / len(hexagon_vertices)
    center_y = sum(v[1] for v in hexagon_vertices) / len(hexagon_vertices)
    angle_radians = math.atan2(center_y - vertex[1], center_x - vertex[0])
    return round(math.degrees(angle_radians) % 360 - 30)

def is_point_in_triangle(pt, v):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    b1 = sign(pt, v[0], v[1]) < 0.0
    b2 = sign(pt, v[1], v[2]) < 0.0
    b3 = sign(pt, v[2], v[0]) < 0.0
    return (b1 == b2) and (b2 == b3)

def new_shape(vertices, shape_type, angle=''):
    for point in vertices:
        if point not in USED_POINTS:
            if shape_type == 'triangle':
                return new_triangle(vertices)
            else:
                if angle == '':
                    angle = calculate_diagonal_angle_hexagon(point, vertices)
                return hexagon_from_point(point, 30, angle)
            USED_POINTS.add(point)
            break
    return None

def new_triangle(triangle_vertices):
    for x, point in enumerate(triangle_vertices):
        if point not in CONNECTION_POINTS:
            angle = calculate_median_angle_triangle(triangle_vertices[x], triangle_vertices[(x+1) % 3], triangle_vertices[(x+2) % 3])
            CONNECTION_POINTS.append(point)
            return equilateral_triangle_from_point(point, 50, angle)
    return None

def extend_line(center, vertex, length):
    vector_x, vector_y = vertex[0] - center[0], vertex[1] - center[1]
    vector_length = math.sqrt(vector_x**2 + vector_y**2)
    unit_vector_x, unit_vector_y = vector_x / vector_length, vector_y / vector_length
    extended_x = center[0] + unit_vector_x * length
    extended_y = center[1] + unit_vector_y * length
    return (round(extended_x), round(extended_y))

def find_closest_vertex(pos, vertices, snap_distance):
    return min(vertices, key=lambda vertex: math.dist(vertex, pos), default=pos)

def add_to_connection_points(t):
    if isinstance(t, tuple) and t not in USED_POINTS:
        if t in CONNECTION_POINTS:
            USED_POINTS.add(t)
        else:
            CONNECTION_POINTS.append(t)

def initialize_pygame():
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("Pygame Shape Example")
    return screen

def draw_initial_shape(screen):
    first_shape_vertices = hexagon_from_point(WINCENTER, 60, 30)
    pg.draw.polygon(screen, (30, 255, 255), first_shape_vertices, 1)
    return first_shape_vertices

def draw_initial_diagonals(layers, screen, r_of_rgb, g_of_rgb, b_of_rgb):
    center_x = sum(v[0] for v in layers[-1][1][0]) / len(layers[-1][1][0])
    center_y = sum(v[1] for v in layers[-1][1][0]) / len(layers[-1][1][0])
    center = (round(center_x), round(center_y))
    for vertex in layers[-1][1][0]:
        pg.draw.line(screen, (0, 255, 255), center, vertex, 5)
        extended_endpoint = extend_line(center, vertex, 100)
        pg.draw.line(screen, (r_of_rgb, g_of_rgb, b_of_rgb), center, extended_endpoint, 1)
        END_POINTS.append(extended_endpoint)

def create_layer(layers, shape, vertices):
    layers.append((shape, vertices))

def handle_mouse_click(e, screen, font, layers, r_of_rgb, g_of_rgb, b_of_rgb, snap_distance):
    global CLICK_COUNT
    CLICK_COUNT += 1
    pos = e.pos
    snap_pos = find_closest_vertex(pos, CONNECTION_POINTS, snap_distance)
    pg.draw.circle(screen, (r_of_rgb, 255, 255), snap_pos, 5)
    r_of_rgb = (r_of_rgb + 10) % 250
    g_of_rgb = (g_of_rgb + 15) % 250
    b_of_rgb = (b_of_rgb + 20) % 250
    coord_text = font.render(f"({snap_pos[0]}, {snap_pos[1]})", True, (255, 240, 200))
    screen.blit(coord_text, (snap_pos[0] + 10, snap_pos[1] - 10))

    if CLICK_COUNT == 1:
        draw_initial_diagonals(layers, screen, r_of_rgb, g_of_rgb, b_of_rgb)

    new_vertices_set = {point for point in CONNECTION_POINTS if point not in USED_POINTS}
    new_vertices = list(new_vertices_set)
    shape_choice = random.choice(['triangle', 'hexagon'])
    last_vertices = layers[-1][1][0]

    if all(point in USED_POINTS for point in last_vertices):
        create_layer(layers, shape_choice, [new_vertices])
        last_vertices = layers[-1][1][0]

    for vertex in last_vertices:
        if vertex in USED_POINTS:
            continue
        else:
            if shape_choice == 'hexagon':
                a_new_shape = hexagon_from_point(vertex, 20, 30)
            else:
                angle = calculate_diagonal_angle_hexagon(vertex, last_vertices)
                a_new_shape = equilateral_triangle_from_point(vertex, 40, angle)
                n = new_shape(a_new_shape, 'triangle')
                if not n:
                    print('make a new layer?')
            for v in a_new_shape:
                add_to_connection_points(v)
            pg.draw.polygon(screen, (r_of_rgb, 255, 255), a_new_shape, 1)
            pg.display.update()
            break

def main():
    screen = initialize_pygame()
    font = pg.font.Font(None, 24)
    screen.fill((20, 20, 40))
    clock = pg.time.Clock()
    done = False
    add_to_connection_points(WINCENTER)
    first_shape_vertices = draw_initial_shape(screen)
    layers = [('hexagon', [first_shape_vertices])]
    pg.display.update()
    r_of_rgb, g_of_rgb, b_of_rgb = 0, 0, 0
    snap_distance = 10

    while not done:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                done = True
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                handle_mouse_click(e, screen, font, layers, r_of_rgb, g_of_rgb, b_of_rgb, snap_distance)
        clock.tick(50)
    pg.quit()

if __name__ == "__main__":
    main()