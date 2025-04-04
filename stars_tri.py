#!/usr/bin/env python
""" pg.examples.stars

    We are all in the gutter,
    but some of us are looking at the stars.
                                            -- Oscar Wilde

A simple starfield example. Note you can move the 'center' of
the starfield by leftclicking in the window. This example show
the basics of creating a window, simple pixel plotting, and input
event management.
"""
import random
import math
import pygame as pg

# constants
WINSIZE = [640, 480]
WINCENTER = [320, 240]
NUMSTARS = 150

# Define the triangle vertices
TRIANGLE_VERTICES = [(270, 300), (370, 300), (320, 200)]

# Define the triangle vertices (larger triangle)
TRIANGLE_VERTICES = [(220, 350), (420, 350), (320, 150)]

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
        pg.draw.polygon(screen, white, TRIANGLE_VERTICES, 1)  # 1 for line thickness
        pg.display.update()
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                done = 1
                break
            if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                WINCENTER[:] = list(e.pos)
        clock.tick(50)
    pg.quit()


# So `python -m pygame.example.stars` will work.
if __name__ == "__main__":
    main()

    # I prefer the time of insects to the time of stars.
    #
    #                              -- Wisława Szymborska
