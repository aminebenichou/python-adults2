# Example file showing a basic pygame "game loop"
import random
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
x, y = 100, 100
x_food, y_food = 200, 200
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, 'red', pygame.Rect(x, y, 20, 20))
    # snake
    pygame.draw.rect(screen, 'green', pygame.Rect(x_food, y_food, 20, 20))
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x += 10
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x -= 10
    if pygame.key.get_pressed()[pygame.K_UP]:
        y -= 10
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        y += 10
    
    # generate new food
    if x_food-10 <= x and x_food+10 >=x and y_food-10 <= y and y_food+10 >=y:
        x_food = random.randint(10,1270)
        y_food = random.randint(10,700)



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()