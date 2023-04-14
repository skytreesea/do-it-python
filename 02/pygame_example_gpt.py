import pygame

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((640, 480))

# Create a font
font = pygame.font.SysFont(None, 48)

# Initial message and color
message = 'Hello World'
color = (255, 255, 255)

# Function to display a message
def display_message():
    text = font.render(message, True, color, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = screen.get_rect().center
    screen.blit(text, text_rect)
    pygame.display.flip()

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                message = 'Hello Pygame!'
            elif event.key == pygame.K_c:
                color = (255, 0, 0)  # Change message color to red
            elif event.key == pygame.K_b:
                color = (0, 0, 255)  # Change message color to blue
    # Update the window with the new message and color
    screen.fill((0, 0, 0))
    display_message()
