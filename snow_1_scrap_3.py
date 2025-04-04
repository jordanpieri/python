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

# Function to calculate the end point of the line
def calculate_end_point(start_point, length, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    inverted_angle_radians = angle_radians - 30 + math.pi
    inverted_angle_degrees = round(math.degrees(inverted_angle_radians) % 360 + 60)
    end_x = start_point[0] + length * math.cos(inverted_angle_radians)
    end_y = start_point[1] + length * math.sin(inverted_angle_radians)
    return (round(end_x), round(end_y))

def equilateral_triangle_from_point(start_point, side_length, orientation_angle=''):
    """Calculate the vertices of an equilateral triangle from a starting point with a given orientation."""
    x1, y1 = start_point
    if orientation_angle == '':
        orientation_angle = 0
    angle_rad = math.radians(orientation_angle)
    inverted_angle_radians = angle_rad + math.pi
    inverted_angle_degrees = round(math.degrees(inverted_angle_radians) % 360 - 30)
    x2 = round(x1 + side_length * math.cos(inverted_angle_radians))
    y2 = round(y1 + side_length * math.sin(inverted_angle_radians))
    x3 = round(x1 + side_length * math.cos(inverted_angle_radians + math.pi / 3))
    y3 = round(y1 + side_length * math.sin(inverted_angle_radians + math.pi / 3))
    return [(x1, y1), (x2, y2), (x3, y3)]

def hexagon_from_point(start_point, side_length, orientation_angle=0):
    """Calculate the vertices of a hexagon from a starting point with a given orientation."""
    new_center = calculate_end_point(start_point, side_length, orientation_angle)
    #extend_line(center, vertex, length)
    x1, y1 = new_center
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
    angle_degrees = round(math.degrees(angle_radians) % 360 - 30)
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

def new_shape(vertices, shape_type, angle=''):
    """Create a new shape (triangle or hexagon) on one of the vertices."""
    print(f'starting new_shape functions with vertices:{vertices}, shape_type:{shape_type}, angle:{angle}')
    new_shape_vertices = None
    for x in range(len(vertices)):
        point = vertices[x]
        if point not in USED_POINTS:
            if shape_type == 'triangle':
                new_shape_vertices = new_triangle(vertices)
                return new_shape_vertices
                # if angle=='':
                    # if x < len(vertices) - 1:
                    #     angle = calculate_median_angle_triangle(vertices[x], vertices[(x+1) % len(vertices)], vertices[(x+2) % len(vertices)])
                    # else:
                    #     angle = calculate_median_angle_triangle(vertices[x], vertices[0], vertices[1])
                print(f'triangle angle is {angle}')
                new_shape_vertices = equilateral_triangle_from_point(point, 50, angle)
            else:
                if angle=='':
                    angle = calculate_diagonal_angle_hexagon(vertices[x], vertices)
                print(f'hexagon angle is {angle}')
                new_shape_vertices = hexagon_from_point(point, 30, angle)
            USED_POINTS.add(point)
            break  # Exit the loop after creating a new shape
        else: break
    print(f'new_shape_vertices: {new_shape_vertices}')
    return new_shape_vertices

def new_triangle(triangle_vertices):
    """Create a new triangle on one of the vertices."""
    new_triangle_vertices = None
    for x in range(3):
        point = triangle_vertices[x]
        if point not in CONNECTION_POINTS:
            if x == 0:
                angle = calculate_median_angle_triangle(triangle_vertices[0], triangle_vertices[1], triangle_vertices[2])
            elif x == 1:
                angle = calculate_median_angle_triangle(triangle_vertices[1], triangle_vertices[0], triangle_vertices[2])
            else:
                angle = calculate_median_angle_triangle(triangle_vertices[2], triangle_vertices[0], triangle_vertices[1])
            new_triangle_vertices = equilateral_triangle_from_point(point, 50, angle)
            CONNECTION_POINTS.append(point)
            break  # Exit the loop after creating a new triangle
    return new_triangle_vertices

def extend_line(center, vertex, length):
    # Calculate the vector from the center to the vertex
    vector_x = vertex[0] - center[0]
    vector_y = vertex[1] - center[1]

    # Calculate the length of the vector
    vector_length = math.sqrt(vector_x**2 + vector_y**2)

    # Normalize the vector
    unit_vector_x = vector_x / vector_length
    unit_vector_y = vector_y / vector_length

    # Scale the vector to the desired length
    extended_x = center[0] + unit_vector_x * length
    extended_y = center[1] + unit_vector_y * length

    return (round(extended_x), round(extended_y))

# Function to find the closest vertex within the snap distance
def find_closest_vertex(pos, vertices, snap_distance):
    for vertex in vertices:
        distance = math.sqrt((vertex[0] - pos[0])**2 + (vertex[1] - pos[1])**2)
        if distance <= snap_distance:
            return vertex
    return pos  # Return the original position if no vertex is close enough

def add_to_connection_points(t):
    if not isinstance(t, tuple):
        print(f"t is not a tuple. its type is {type(t).__name__}")
    else:
        if t not in USED_POINTS:
            if t in CONNECTION_POINTS:
                print(f"Adding {t} to USED_POINTS: {USED_POINTS} because its already  in CONNECTION_POINTS:{CONNECTION_POINTS}")
                USED_POINTS.add(t)
            else:
                print(f"Adding {t} to CONNECTION_POINTS: {CONNECTION_POINTS}")
                CONNECTION_POINTS.append(t)

def initialize_pygame():
    """Initialize Pygame and set up the display."""
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("Pygame Shape Example")
    return screen

def draw_initial_shape(screen):
    """Draw the initial shape on the screen."""
    first_shape_vertices = hexagon_from_point(WINCENTER, 60, 30)
    pg.draw.polygon(screen, (30, 255, 255), first_shape_vertices, 1)
    return first_shape_vertices

def draw_initial_diagonals(layers, screen, r_of_rgb, g_of_rgb, b_of_rgb):
    center_x = sum(v[0] for v in layers[-1][1][0]) / len(layers[-1][1][0])
    center_y = sum(v[1] for v in layers[-1][1][0]) / len(layers[-1][1][0])
    center = (round(center_x), round(center_y))
    print(f'center_x {center_x} center_y {center_y} center {center} ')
    for vertex in layers[-1][1][0]:
        print(f'for vertex {vertex} in layers[-1][1][0] {layers[-1][1][0]}: drawing line from center through vertex')
        pg.draw.line(screen, (0, 255, 255), center, vertex, 5)
        extended_endpoint = extend_line(center, vertex, 100)
        pg.draw.line(screen, (r_of_rgb, g_of_rgb, b_of_rgb), center, extended_endpoint, 1)
        #add_to_connection_points(vertex)
        END_POINTS.append(extended_endpoint)

def create_layer(layers, shape, vertices):
    #layers = [('hexagon', [first_shape_vertices])]
    print(f'create_layer(layers, shape, vertices)\n layers: {layers}\n shape: {shape}\n vertices: {vertices}')
    new_layer = (shape, vertices)
    layers.append(new_layer)

def handle_mouse_click(e, screen, font, layers, r_of_rgb, g_of_rgb, b_of_rgb, snap_distance):
    """Handle mouse click events."""
    global CLICK_COUNT
    CLICK_COUNT += 1
    print(f'Start of handle_mouse_click. CLICK_COUNT: {CLICK_COUNT}')
    print(f'layers: {layers}.\n layers[-1]{layers[-1]}.\n layers[-1][0]{layers[-1][0]}.\n layers[-1][1]{layers[-1][1]}.\n layers[-1][1][0]{layers[-1][1][0]}\n\n')
    pos = e.pos
    snap_pos = find_closest_vertex(pos, CONNECTION_POINTS, snap_distance)
    pg.draw.circle(screen, (r_of_rgb, 255, 255), snap_pos, 5)
    r_of_rgb = (r_of_rgb + 10) % 250
    g_of_rgb = (g_of_rgb + 15) % 250
    b_of_rgb = (b_of_rgb + 20) % 250
    coord_text = font.render(f"({snap_pos[0]}, {snap_pos[1]})", True, (255, 240, 200))
    screen.blit(coord_text, (snap_pos[0] + 10, snap_pos[1] - 10))

    if CLICK_COUNT == 1:
        print(f'CLICK_COUNT {CLICK_COUNT} == 1')
        draw_initial_diagonals(layers, screen, r_of_rgb, g_of_rgb, b_of_rgb)

    new_vertices_set = {point for point in CONNECTION_POINTS if point not in USED_POINTS}
    new_vertices = list(new_vertices_set)
    shape_choice = random.choice(['triangle', 'hexagon'])
    last_vertices = layers[-1][1][0]

    points_to_check = layers[-1][1][0]
    if all(point in USED_POINTS for point in points_to_check):
        # Perform the new action
        print("All points are in USED_POINTS. Performing the new action.")
        create_layer(layers, shape_choice, [new_vertices])
        last_vertices = layers[-1][1][0]
    else:
        print("Not all points are in USED_POINTS.")


    #shape_choice = layers[-1][0]
    print(f'new_vertices_set: \n{new_vertices_set}. new_vertices: \n{new_vertices}. shape_choice: {shape_choice}. last_vertices: \n{last_vertices}\n\n')
    for vertex in last_vertices:
        print(f'for vertex {vertex} in last_vertices {last_vertices}:')
        if vertex in USED_POINTS:
            print(f'Skipping this vertex: {vertex} because it is in USED_POINTS: {USED_POINTS}. ')
            continue
        else:
            if shape_choice == 'hexagon':
                a_new_shape = hexagon_from_point(vertex, 20, 30)
            if shape_choice == 'triangle':
                angle = calculate_diagonal_angle_hexagon(vertex, last_vertices)
                a_new_shape = equilateral_triangle_from_point(vertex, 40, angle)
                n = new_shape(a_new_shape, 'triangle')
                if not n:
                    print('make a new layer?')
            for v in a_new_shape:
                print(f'for v {v} in a_new_shape {a_new_shape}({shape_choice}):')
                add_to_connection_points(v)
            pg.draw.polygon(screen, (r_of_rgb, 255, 255), a_new_shape, 1)
            pg.display.update()
            print(f'handle_mouse_click break\n\n')
            break


def main():
    """Main function to handle shape generation."""
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