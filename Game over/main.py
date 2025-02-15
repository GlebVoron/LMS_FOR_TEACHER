import pygame
import os
import sys

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 300

BLUE = (0, 0, 255)

SPEED = 200


def load_image(name):
    fullname = os.path.join("data", name)
    return pygame.image.load(fullname)


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Сценарий окончания игры")

    image = load_image("gameover.png")
    rect = image.get_rect()

    rect.x = -rect.width
    rect.y = (SCREEN_HEIGHT - rect.height) // 2

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        delta_time = clock.tick(60) / 1000  # Время в секундах
        offset = SPEED * delta_time

        if rect.right < SCREEN_WIDTH:
            rect.x += offset
        else:
            rect.x = SCREEN_WIDTH - rect.width

        screen.fill(BLUE)
        screen.blit(image, rect)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
