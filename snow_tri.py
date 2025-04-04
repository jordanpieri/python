import random
import math
import pygame as pg

# constants
WINSIZE = [640, 480]
WINCENTER = [320, 240]
NUMSTARS = 150


def equilateral_triangle_from_point(start_point, side_length, orientation_angle=0):
    """Calculate the vertices of an equilateral triangle from a starting point with a given orientation."""
    x1, y1 = start_point

    # Convert the orientation angle from degrees to radians
    angle_rad = math.radians(orientation_angle)

    # Calculate the second vertex
    x2 = x1 + side_length * math.cos(angle_rad)
    y2 = y1 + side_length * math.sin(angle_rad)

    # Calculate the third vertex
    x3 = x1 + side_length * math.cos(angle_rad + math.pi / 3)
    y3 = y1 + side_length * math.sin(angle_rad + math.pi / 3)

    return [(x1, y1), (x2, y2), (x3, y3)]


# Define the triangle vertices (old small one)
TRIANGLE_VERTICES_0 = [(270, 300), (370, 300), (320, 200)]

# Define the triangle vertices (larger triangle)
TRIANGLE_VERTICES = [(220, 350), (420, 350), (320, 150)]

# make it equilateral
start_point = (320, 150)
side_length = 220
orientation_angle = 60
TRIANGLE_VERTICES = equilateral_triangle_from_point(start_point,side_length, orientation_angle)

def init_star(steps=-1):
    "creates new star values"
    dir = random.randrange(100000)
    steps_velocity = 1 if steps == -1 else steps * 0.09
    velmult = steps_velocity * (random.random() * 0.6 + 0.4)
    vel = [math.sin(dir) * velmult, math.cos(dir) * velmult]
    # Randomize initial position within the triangle
    pos = random_point_in_triangle(TRIANGLE_VERTICES)
    if steps is None:
        return [vel, [WINCENTER[0] + (vel[0] * steps), WINCENTER[1] + (vel[1] * steps)]]
    return [vel, WINCENTER[:]]


def random_point_in_triangle(vertices):
    """Generate a random point inside a triangle using barycentric coordinates."""
    while True:
        s, t = sorted([random.random(), random.random()])
        a, b, c = vertices
        point = (
            s * a[0] + (t - s) * b[0] + (1 - t) * c[0],
            s * a[1] + (t - s) * b[1] + (1 - t) * c[1]
        )
        return point


def initialize_stars():
    "creates a new starfield"
    random.seed()
    stars = [init_star(steps=random.randint(0, WINCENTER[0])) for _ in range(NUMSTARS)]
    move_stars(stars)
    return stars


def draw_stars(surface, stars, color):
    "used to draw (and clear) the stars"
    for _, pos in stars:
        pos = (int(pos[0]), int(pos[1]))
        # surface.set_at(pos, color)
        if is_point_in_triangle(pos, TRIANGLE_VERTICES):
            surface.set_at(pos, color)


def move_stars(stars):
    "animate the star values"
    for vel, pos in stars:
        pos[0] = pos[0] + vel[0]
        pos[1] = pos[1] + vel[1]
        if not 0 <= pos[0] <= WINSIZE[0] or not 0 <= pos[1] <= WINSIZE[1]:
            vel[:], pos[:] = init_star()
        else:
            vel[0] = vel[0] * 1.05
            vel[1] = vel[1] * 1.05


def is_point_in_triangle(pt, v):
    """Check if a point is inside a triangle using barycentric coordinates."""
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    b1 = sign(pt, v[0], v[1]) < 0.0
    b2 = sign(pt, v[1], v[2]) < 0.0
    b3 = sign(pt, v[2], v[0]) < 0.0

    return ((b1 == b2) and (b2 == b3))


def calculate_median_angle(vertex, opposite_vertex1, opposite_vertex2):
    """Calculate the angle of the median from a vertex with respect to the horizontal axis."""
    # Calculate the midpoint of the opposite side
    midpoint = (
        (opposite_vertex1[0] + opposite_vertex2[0]) / 2,
        (opposite_vertex1[1] + opposite_vertex2[1]) / 2
    )

    # Calculate the median vector
    median_vector = (midpoint[0] - vertex[0], midpoint[1] - vertex[1])

    # Calculate the angle of the median using atan2
    angle_radians = math.atan2(median_vector[1], median_vector[0])
    angle_degrees = math.degrees(angle_radians)

    # Invert the angle by adding pi radians (180 degrees)
    inverted_angle_radians = angle_radians + math.pi

    # Convert the inverted angle to degrees
    inverted_angle_degrees = math.degrees(inverted_angle_radians)

    # Normalize the angle to be within [0, 360) degrees
    inverted_angle_degrees = inverted_angle_degrees % 360 - 30

    return inverted_angle_degrees

    return angle_degrees

# # Example usage
# A = (0, 0)
# B = (4, 0)
# C = (2, 3)
# median_angle = calculate_median_angle(A, B, C)
# print(f"Angle of the median from A: {median_angle:.2f} degrees")


def new_triangle():
    "create a new triangle on one of the vertices"
    x = random.randint(0,2)
    point = TRIANGLE_VERTICES[x]
    # angle = random.randint(0,12) * 30

    if x == 0:
        angle = calculate_median_angle(TRIANGLE_VERTICES[0],TRIANGLE_VERTICES[1],TRIANGLE_VERTICES[2])
    if x == 1:
        angle = calculate_median_angle(TRIANGLE_VERTICES[1],TRIANGLE_VERTICES[0],TRIANGLE_VERTICES[2])
    if x == 2:
        angle = calculate_median_angle(TRIANGLE_VERTICES[2],TRIANGLE_VERTICES[0],TRIANGLE_VERTICES[1])

    #TRIANGLE_VERTICES = [(220, 350), (420, 350), (320, 150)]
    #New_TRIANGLE_VERTICES = [(170, 400),(220, 350), (270, 400)]
    print(f"angle = {angle}")
    New_TRIANGLE_VERTICES = equilateral_triangle_from_point(point,50,angle)
    return New_TRIANGLE_VERTICES
    #pg.draw.polygon(screen, white, New_TRIANGLE_VERTICES, 1)


def main():
    "This is the starfield code"
    # create our starfield
    stars = initialize_stars()

    # initialize and prepare screen
    pg.init()
    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("pygame Stars Example")
    white = 255, 240, 200
    black = 20, 20, 40
    screen.fill(black)

    clock = pg.time.Clock()

    # main game loop
    done = 0
    while not done:
        draw_stars(screen, stars, black)
        move_stars(stars)
        draw_stars(screen, stars, white)
        # Draw the triangle
        #TRIANGLE_VERTICES = [(220, 350), (420, 350), (320, 150)]
        start_point = (320, 150)
        side_length = 220
        orientation_angle = 60
        a = equilateral_triangle_from_point(start_point,side_length, orientation_angle)
        #print(f"Vertices of the equilateral triangle: {a}")
        #pg.draw.polygon(screen, white, TRIANGLE_VERTICES, 1)  # 1 for line thickness
        pg.draw.polygon(screen, white, a, 1)  # 1 for line thickness
        pg.display.update()
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                done = 1
                break
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                WINCENTER[:] = list(e.pos)
                print(e.pos)
                x = new_triangle()
                pg.draw.polygon(screen, white, x, 1)  # 1 for line thickness
                # for _ in TRIANGLE_VERTICES:
                #     y = equilateral_triangle_from_point(_,50)
                #     pg.draw.polygon(screen, white, y, 1)
        clock.tick(50)
    pg.quit()

def calculate_distance(point1, point2):
    """Calculate the distance between two points."""
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def measure_triangle_sides(vertices):
    """Measure the sides of a triangle given its vertices."""
    a = calculate_distance(vertices[0], vertices[1])
    b = calculate_distance(vertices[1], vertices[2])
    c = calculate_distance(vertices[2], vertices[0])
    return a, b, c

# Measure the sides of the triangle
sides = measure_triangle_sides(TRIANGLE_VERTICES)
print(f"Sides of the triangle: {sides}")

# So `python -m pygame.example.stars` will work.
if __name__ == "__main__":
    main()

    # I prefer the time of insects to the time of stars.
    #
    #                              -- Wisława Szymborska
