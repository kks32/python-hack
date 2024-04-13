import pygame

# Initialize PyGame
pygame.init()

# Set the window size
window_width = 1200
window_height = 800
window = pygame.display.set_mode((window_width, window_height))

# Set the window title
pygame.display.set_caption("Intersection Simulation")

# Load the background image
background_img = pygame.image.load("intersection.png")

# Set up the sprite groups
all_sprites = pygame.sprite.Group()
car_sprites = pygame.sprite.Group()

# Define the car sprite class
class CarSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = window_height // 2 - self.rect.height // 2
        self.speed = 5

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > window_width:
            self.rect.x = 0

# Create the car sprite
car = CarSprite()
all_sprites.add(car)
car_sprites.add(car)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprites
    all_sprites.update()

    # Clear the window
    window.blit(background_img, (0, 0))

    # Draw the sprites
    all_sprites.draw(window)

    # Update the display
    pygame.display.update()

# Quit PyGame
pygame.quit()
