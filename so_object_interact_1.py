#https://stackoverflow.com/questions/43179682/how-can-i-create-an-interactive-object-in-pygame
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
x = 30
y = 30

clock = pygame.time.Clock()

# RGB values for red
red = (255, 0 ,0)

# Your three button rects :
simulator_rect = pygame.Rect(225, 125, 30, 30)
quiz_rect = pygame.Rect(600, 125, 30, 30)
quit_rect = pygame.Rect(375, 425, 30, 30)
# These represent your three option rects
option_rects = [simulator_rect, quiz_rect, quit_rect]

# Your blue selector rect
selector_rect = pygame.Rect(50, 50, 60, 60)
# The 50, 50 xy coords are temporary

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 0: y -= 5
    if pressed[pygame.K_DOWN] and y < 600 - 60: y += 5
    if pressed[pygame.K_LEFT] and x > 0: x -= 5
    if pressed[pygame.K_RIGHT] and x < 800 - 60: x += 5

    # Set the slector rect's coords to x/y
    selector_rect.x, selector_rect.y = x, y

    screen.fill((0, 0, 0))

    color = (0, 128, 255)
    pygame.draw.rect(screen, color, selector_rect)

    myfont = pygame.font.SysFont("monospace", 15)

    label = myfont.render("Start the experiment simulator", 1, (255,255,255))
    screen.blit(label, (100, 100))

    label2 = myfont.render("Start the quiz", 1, (255,255,255))
    screen.blit(label2, (550, 100))

    label3 = myfont.render("Quit game", 1, (255,255,255))
    screen.blit(label3, (350, 400))

    # Use our created rects
    pygame.draw.rect(screen, red, simulator_rect)
    pygame.draw.rect(screen, red, quiz_rect)
    pygame.draw.rect(screen, red, quit_rect)

    # Check to see if the user presses the enter key
    if pressed[pygame.K_RETURN]:
        # Check to see if the selection rect
        # collides with any other rect
        for rect in option_rects:
            # Add rects as needed
            if selector_rect.colliderect(rect):
                if rect == simulator_rect:
                    # Do simulations stuff!
                    print('Simulating!')
                elif rect == quiz_rect:
                    # Do quizzing stuff!
                    print('Quizzing!')
                elif rect == quit_rect:
                    # Quit!
                    done = True




    pygame.display.flip()
    clock.tick(60)