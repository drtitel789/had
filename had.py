import pygame
import time
import random
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (100, 255, 200)
yellow = (255, 255, 0)
white = (255, 255, 255)
pygame.init()
x = 100
y = 100
x1 = 200
y2 = 200
z = 2
narocnost = 0
speed = 10
direction = None
screen_width = 800
screen_height = 600
points = 0
segments = [(x, y)]
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("comicsansms", 30)

def konec(konec):
    if konec == 1:
        screen.fill((yellow))
        score_text = font.render(f"Skóre: {points}", True, white)
        screen.blit(score_text, (screen_width // 2 - 100, screen_height // 2 - 30))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
        pygame.quit()
        exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if x < -z or x > screen_width - z or y < -z or y > screen_height - z:
        konec(1)

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

    segments.insert(0, (x, y))
    if len(segments) > points + 1:
        segments.pop()

    if x1 - 25 <= x <= x1 + 25 and y2 - 25 <= y <= y2 + 25:
        points += 1
        speed += narocnost
        x1 = random.randint(25, screen_width - 25)
        y2 = random.randint(25, screen_height - 25)

    for segment in segments[1:]:
        if segments[0] == segment:
            konec(1)

    screen.fill((green))
    pygame.draw.circle(screen, blue, (x1, y2), 25)

    for segment in segments:
        pygame.draw.circle(screen, black, segment, 27)
        pygame.draw.circle(screen, red, segment, 25)

    head_x, head_y = segments[0]
    pygame.draw.circle(screen, black, (head_x, head_y), 27)
    pygame.draw.circle(screen, red, (head_x, head_y), 25)

    pupil_radius = 2
    eye_radius = 5

    if direction == "left":
        left_eye_offset = (-10, -10)
        right_eye_offset = (-10, 10)
    elif direction == "right":
        left_eye_offset = (10, -10)
        right_eye_offset = (10, 10)
    elif direction == "up":
        left_eye_offset = (-10, -10)
        right_eye_offset = (10, -10)
    elif direction == "down":
        left_eye_offset = (-10, 10)
        right_eye_offset = (10, 10)
    else:
        left_eye_offset = (-10, -10)
        right_eye_offset = (-10, 10)

    pygame.draw.circle(screen, white, (head_x + left_eye_offset[0], head_y + left_eye_offset[1]), eye_radius)
    pygame.draw.circle(screen, black, (head_x + left_eye_offset[0], head_y + left_eye_offset[1]), pupil_radius)
    pygame.draw.circle(screen, white, (head_x + right_eye_offset[0], head_y + right_eye_offset[1]), eye_radius)
    pygame.draw.circle(screen, black, (head_x + right_eye_offset[0], head_y + right_eye_offset[1]), pupil_radius)

    score_text = font.render(f"Skóre: {points}", True, white)
    rychlost = font.render(f"Rychlost: {speed}", True, white)
    screen.blit(rychlost, (10, 50))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    time.sleep(0.07)



