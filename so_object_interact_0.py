#https://stackoverflow.com/questions/43179682/how-can-i-create-an-interactive-object-in-pygame
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
x = 30
y = 30
red = 255, 0, 0

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 0: y -= 5
    if pressed[pygame.K_DOWN] and y < 600 - 60: y += 5
    if pressed[pygame.K_LEFT] and x > 0: x -= 5
    if pressed[pygame.K_RIGHT] and x < 800 - 60: x += 5

    screen.fill((0, 0, 0))
    color = (0, 128, 255)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    myfont = pygame.font.SysFont("monospace", 15)

    label = myfont.render("Start the experiment simulator", 1, (255,255,255))
    screen.blit(label, (100, 100))

    label2 = myfont.render("Start the quiz", 1, (255,255,255))
    screen.blit(label2, (550, 100))

    label3 = myfont.render("Quit game", 1, (255,255,255))
    screen.blit(label3, (350, 400))

    pygame.draw.rect(screen, red, pygame.Rect(600, 125, 30, 30))
    pygame.draw.rect(screen, red, pygame.Rect(225, 125, 30, 30))
    pygame.draw.rect(screen, red, pygame.Rect(375, 425, 30, 30))

    pygame.display.flip()
    clock.tick(60)

    if pressed[pygame.K_RETURN] and (x >= 375 and x <= 405) and (y >= 425 and y <= 455):
        pygame.display.quit()
        pygame.quit()
        #sys.exit()