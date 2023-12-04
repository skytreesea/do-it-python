import pygame
import random

# 초기화
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 화면 크기 정의
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("공 피하기 게임")

# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 25))
        self.surf.fill(BLUE)
        self.rect = self.surf.get_rect(center=(WIDTH / 2, HEIGHT - 30))

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # 경계선 확인
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# 공 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(center=(random.randint(0, WIDTH), 0))
        self.speed = random.randint(2, 6)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.kill()

player = Player()
balls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    if random.random() < 0.02:
        ball = Ball()
        balls.add(ball)
        all_sprites.add(ball)

    player.move()
    balls.update()
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, balls):
        player.kill()
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()