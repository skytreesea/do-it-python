import pygame
import sys

# pygame 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Drawing App")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

drawing = False
last_pos = None

screen.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None

    if drawing:
        current_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, BLACK, last_pos, current_pos, 5)
        last_pos = current_pos

    pygame.display.flip()
