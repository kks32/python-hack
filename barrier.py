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

# Load the car image
car_img = pygame.image.load("car.png")

# Load the barrier image
barrier_img = pygame.image.load("barrier.png")

# Get the car image dimensions
car_width = car_img.get_width()
car_height = car_img.get_height()

# Create a Sprite for the car
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = window_height // 2 - car_height // 2

# Create a Sprite for the barrier
class Barrier(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = barrier_img
        self.rect = self.image.get_rect()
        self.rect.x = window_width // 2 - barrier_img.get_width() // 2
        self.rect.y = window_height // 2 - barrier_img.get_height() // 2

# Create instances of the car and barrier
car = Car()
barrier = Barrier()

# Set the car speed
car_speed = 2

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the car
    car.rect.x += car_speed

    # Check if the car has gone off the screen or collided with the barrier
    if car.rect.right >= window_width or car.rect.colliderect(barrier.rect):
        car.rect.x = 0  # Reset the car position to the left side of the screen

    # Clear the window
    window.blit(background_img, (0, 0))

    # Draw the barrier
    window.blit(barrier.image, barrier.rect)

    # Draw the car
    window.blit(car.image, car.rect)

    # Update the display
    pygame.display.update()

# Quit PyGame
pygame.quit()