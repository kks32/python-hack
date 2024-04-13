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

# Get the car image dimensions
car_width = car_img.get_width()
car_height = car_img.get_height()

# Set the initial car position
car_x = 0
car_y = window_height // 2 - car_height // 2

# Set the car speed
car_speed = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the car
    car_x += car_speed

    # Check if the car has gone off the screen
    if car_x > window_width:
        car_x = 0  # Reset the car position to the left side of the screen

    # Clear the window
    window.blit(background_img, (0, 0))

    # Draw the car
    window.blit(car_img, (car_x, car_y))

    # Update the display
    pygame.display.update()

# Quit PyGame
pygame.quit()
