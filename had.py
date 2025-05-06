import pygame
import time
import random

red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)  # Barva textu
pygame.init()
x = 100
y = 100
x1 = 200
y2 = 200
z = 2
speed = 10
direction = None
screen_width = 800
screen_height = 600
points = 0
segments = [(x, y)]  # Seznam segmentů hada, začíná pouze hlavou
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Inicializace fontu
font = pygame.font.SysFont("comicsansms", 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if x < -z or x > screen_width - z or y < -z or y > screen_height - z:
        # Zobrazení skóre před ukončením
        screen.fill((0, 0, 0))  # Vyplnění obrazovky černou barvou

        score_text = font.render(f"Skóre: {points}", True, white)
        screen.blit(score_text, (screen_width // 2 - 100, screen_height // 2 - 30))
        pygame.display.flip()

        # Čekání na stisknutí klávesy
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # Stisknutí libovolné klávesy
                    waiting = False
                if event.type == pygame.QUIT:  # Zavření okna
                    pygame.quit()
                    exit()

        pygame.quit()
        exit()

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

    # Přidání nové pozice hlavy do seznamu segmentů
    segments.insert(0, (x, y))
    # Odstranění posledního segmentu, pokud není přidán nový bod
    if len(segments) > points + 1:
        segments.pop()

    # Kontrola kolize s modrým kruhem
    if x1 - 25 <= x <= x1 + 25 and y2 - 25 <= y <= y2 + 25:  # Upraveno pro kruh
        points += 1
        x1 = random.randint(25, screen_width - 25)  # Náhodná pozice s ohledem na poloměr
        y2 = random.randint(25, screen_height - 25)

    screen.fill((0, 0, 0))  # Vyplnění obrazovky černou barvou
    pygame.draw.circle(screen, blue, (x1, y2), 25)  # Vykreslení modrého kruhu

    # Vykreslení všech segmentů hada jako kruhů
    for segment in segments:
        pygame.draw.circle(screen, red, segment, 25)  # Vykreslení červeného kruhu

    # Vykreslení skóre během hry
    score_text = font.render(f"Skóre: {points}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    time.sleep(0.1)


