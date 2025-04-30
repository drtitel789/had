import pygame
import time
red= (255, 0, 0)
blue = (0,0,255)  # Define red color
pygame.init()
x = 100
y = 100
x1= 200
y2= 200
z= 2
speed = 10
direction = None
screen_width = 800
screen_height = 600
points = 0
screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if x < -z or x > screen_width -z or y < -z or y > screen_height-z:
        pygame.quit()
        exit()
  # Draw a blue square

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = "left"
    if keys[pygame.K_RIGHT]:
        direction = "right"
    if keys[pygame.K_UP]:
        direction = "up"
    if keys[pygame.K_DOWN]:
        direction = "down"
    if direction == "left":
        x -= speed
    if direction == "right":
        x += speed
    if direction == "up":
        y -= speed
    if direction == "down":
        y += speed
    
    screen.fill((0, 0, 0)) 
    pygame.key.get_pressed() # Fill the screen with black
    pygame.draw.rect(screen, red, (x, y, 50, 50))  # Draw a red square
    pygame.draw.rect(screen, blue, (x1, y2, 50, 50))
    pygame.display.flip()
    time.sleep(0.1)  



