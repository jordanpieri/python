import random
import math
import typing

import pygame as pg

# Constants
WINSIZE = (640, 480)
WINCENTER = (320, 240)
CONNECTION_POINTS = []
END_POINTS = []
USED_POINTS = set()


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
                if angle=='':
                    if x < len(vertices) - 1:
                        angle = calculate_median_angle_triangle(vertices[x], vertices[(x+1) % len(vertices)], vertices[(x+2) % len(vertices)])
                    else:
                        angle = calculate_median_angle_triangle(vertices[x], vertices[0], vertices[1])
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
            CONNECTION_POINTS.append(t)
            USED_POINTS.add(t)


def main():
    """Main function to handle shape generation."""
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("Pygame Shape Example")
    white = 255, 240, 200
    black = 20, 20, 40
    yellow = 255, 255, 0
    red = 255,0,0
    cyan = 0, 255, 255
    r_of_rgb=0
    g_of_rgb=0
    b_of_rgb=0
    font_size = 24
    snap_distance = 10
    font = pg.font.Font(None, font_size)
    screen.fill(black)
    clock = pg.time.Clock()
    done = False
    add_to_connection_points(WINCENTER)

    first_shape_vertices = hexagon_from_point(WINCENTER, 60, 30)

    #first_shape_vertices = new_shape(hexagon_from_point, shape, angle)
    pg.draw.polygon(screen, (30,255,255), first_shape_vertices, 1)

    # List to keep track of all shapes
    # layers = [('hexagon',[HEXAGON_VERTICES])]
    # pg.draw.polygon(screen, white, HEXAGON_VERTICES, 1)

    layers = [('hexagon',[first_shape_vertices])]
    #pg.draw.polygon(screen, white, HEXAGON_VERTICES, 1)
    pg.display.update()

    while not done:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                done = True
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                print(f'CONNECTION_POINTS: {CONNECTION_POINTS}')

                pos = e.pos
                # Find the closest vertex within the snap distance
                snap_pos = find_closest_vertex(pos, CONNECTION_POINTS, snap_distance)
                # Draw a small cyan circle at the click position
                pg.draw.circle(screen, (r_of_rgb,255,255), snap_pos, 5)
                r_of_rgb += 10
                g_of_rgb += 15
                b_of_rgb += 20
                if r_of_rgb >= 250:
                    r_of_rgb = 0
                if g_of_rgb >= 250:
                    g_of_rgb = 0
                if b_of_rgb >= 250:
                    b_of_rgb = 0
                # Render the coordinates as text
                coord_text = font.render(f"({snap_pos[0]}, {snap_pos[1]})", True, white)

                # Blit the text onto the screen
                screen.blit(coord_text, (snap_pos[0] + 10, snap_pos[1] - 10))
                # center_x = sum(v[0] for v in HEXAGON_VERTICES) / len(HEXAGON_VERTICES)
                # center_y = sum(v[1] for v in HEXAGON_VERTICES) / len(HEXAGON_VERTICES)
                center_x = sum(v[0] for v in layers[-1][1][0]) / len(layers[-1][1][0])
                center_y = sum(v[1] for v in layers[-1][1][0]) / len(layers[-1][1][0])
                center = (round(center_x), round(center_y))
                #for vertex in HEXAGON_VERTICES:
                for vertex in layers[-1][1][0]:
                    print(f"line 237 - vertex: {vertex}")
                    if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                        pg.draw.line(screen, cyan, center, vertex, 5)
                        extended_endpoint = extend_line(center, vertex, 100)  # Extend by 100 units
                        pg.draw.line(screen, (r_of_rgb,g_of_rgb,b_of_rgb), center, extended_endpoint, 1)
                        print(f'extended_endpoint: {extended_endpoint}')
                        add_to_connection_points(vertex)
                        #CONNECTION_POINTS.append(center)
                        #CONNECTION_POINTS.append(vertex)
                        END_POINTS.append(extended_endpoint)
                    elif e.type == pg.MOUSEBUTTONDOWN:
                        print(f'button button... {e.button}')
                    if e.type == pg.MOUSEBUTTONDOWN and e.button == 2:
                        print(f'is this a right click?')

                # Add elements from CONNECTION_POINTS that are not in USED_POINTS to new_vertices
                # Use a set to ensure no duplicates
                new_vertices_set = {point for point in CONNECTION_POINTS if point not in USED_POINTS}
                print(f'new_vertices_set: {new_vertices_set}')

                # Convert the set back to a list if needed
                new_vertices = list(new_vertices_set)


                print("New vertices:", new_vertices)
                shape_choice = random.choice(['triangle', 'hexagon'])
                print(f'Shape choice:{shape_choice}')
                #layers.append((shape_choice, [new_vertices]))
                #CONNECTION_POINTS.append([new_vertices])
                new_vertices_set = {}
                new_vertices = []
                print(layers)
                last_vertices = layers[-1][1][0]
                for vertex in last_vertices:
                    if shape_choice == 'hexagon':
                        a_new_shape = hexagon_from_point(vertex, 20, 30)
                    if shape_choice == 'triangle':
                        #angle = calculate_median_angle_triangle(vertex)
                        angle = calculate_diagonal_angle_hexagon(vertex, last_vertices)
                        a_new_shape = equilateral_triangle_from_point(vertex,40, angle)
                        n = new_shape(a_new_shape, 'triangle')
                        if not n:
                            print('make a new layer?')
                    #first_shape_vertices = new_shape(hexagon_from_point, shape, angle)
                    print(f'a_new_shape is {a_new_shape}')
                    for v in a_new_shape:
                        add_to_connection_points(v)

                    pg.draw.polygon(screen, (r_of_rgb,255,255), a_new_shape, 1)

                pg.display.update()


                    # if len(layers) == 1:
                    #     current_layer = layers[-1]
                    #     for shape in current_layer:
                    #         if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                    #             print(f'shape is {shape}')
                    #             print(f'current_layer is {current_layer}')
                    #             current_layer_child = current_layer[1]
                    #             current_layer_grandchild = current_layer_child[0]
                    #             #third_layer = second_layer[0]
                    #             # print(f'next_layer is {next_layer}')
                    #             # print(f'second_layer is {second_layer}')
                    #             # print(f'third_layer is {third_layer}')
                    #             for x in current_layer_grandchild:
                    #                 if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                    #                     angle = calculate_diagonal_angle_hexagon(x, current_layer_grandchild)
                    #                     new = new_shape(current_layer_grandchild, shape, angle)
                    #                     start_point = x#(320, 240)  # Starting point of the line
                    #                     length = 30               # Length of the line
                    #                     bangle = 45                # Angle in degrees
                    #                     end_point = calculate_end_point(start_point, length, angle)
                    #                     line_thickness = 1        # Thickness of the line
                    #                     pg.draw.line(screen, yellow, start_point, end_point, line_thickness)
                    #                     pg.display.update()


                        #new_shape_vertices = new_shape(second_layer, shape)
    #                     if new_shape_vertices is None: continue
    #             else:
    #                 current_layer = layers[-1]
    #                 print(f'Current Layer:{current_layer} is one of {len(layers)}')
    #                 shape_type = random.choice(['triangle', 'hexagon'])
    #                 for shape in current_layer:
    #                     new_shape_vertices = new_shape(shape, shape_type)
    #                     if new_shape_vertices is None:
    #                         # new_layer = []
    #                         # shape_type = random.choice(['triangle', 'hexagon'])
    #                         # if new_layer:
    #                         #     layers.append(new_layer) 
    #                         continue  # Skip if no new shape was created
    #                     if not any(triangles_overlap(new_shape_vertices, existing) for existing in current_layer):
    #                         new_layer = []
    #                         shape_type = random.choice(['triangle', 'hexagon'])
    #                         new_layer.append(new_shape_vertices)
    #                         pg.draw.polygon(screen, white, new_shape_vertices, 1)
    #                         pg.display.update()
    #             #if new_layer:
    #             #    layers.append(new_layer)  # Move to the next layer
    #     clock.tick(50)


    # while not done:
    #     for e in pg.event.get():
    #         if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
    #             done = True
    #         if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
    #             for triangle in triangles:
    #                 new_triangle_vertices = new_triangle(triangle)
    #                 if not any(triangles_overlap(new_triangle_vertices, existing) for existing in triangles):
    #                     triangles.append(new_triangle_vertices)
    #                     pg.draw.polygon(screen, white, new_triangle_vertices, 1)
    #                     pg.display.update()
    #                     break  # Exit the loop after adding one triangle
    #    clock.tick(50)
    pg.quit()

if __name__ == "__main__":
    #HEXAGON_VERTICES = hexagon_from_point((320, 240), 60, 0)
    main()