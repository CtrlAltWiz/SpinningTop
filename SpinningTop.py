# by CtrlAltWiz
# https://github.com/CtrlAltWiz

import sys
import math
import subprocess

# Check if Pygame is installed
try:
    subprocess.check_output([sys.executable, '-m', 'pip', 'show', 'pygame'])
except subprocess.CalledProcessError:
    print("Pygame is not installed. Installing...")
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'pygame'])

# Import Pygame after making sure it's installed
import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (50, 50, 255)
TOP_COLOR = (255, 50, 50)
STEM_COLOR = (225, 50, 50)
BASE_COLOR = (200, 200, 200)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Top")

# Top and base properties
top_radius = 50
stem_radius = 45
base_radius = 45
center = (WIDTH // 2, HEIGHT // 2)
angle = 0
angular_speed = 5  # Adjust as needed

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Calculate the new position of the top and base
    angle += angular_speed
    if angle >= 360:
        angle -= 360

    # Calculate the positions of the top and base edges
    top_x = center[0] + top_radius * math.cos(math.radians(angle))
    top_y = center[1] + top_radius * math.sin(math.radians(angle))
    stem_x = center[0] + stem_radius * math.cos(math.radians(angle))
    stem_y = center[1] + stem_radius * math.sin(math.radians(angle))
    base_x = center[0] + base_radius * math.cos(math.radians(angle))
    base_y = center[1] + base_radius * math.sin(math.radians(angle))

    # Draw the white base
    pygame.draw.circle(screen, BASE_COLOR, (int(base_x), int(base_y)), base_radius)

    # Draw the stem connecting the base and the top
    pygame.draw.circle(screen, STEM_COLOR, (int(stem_x), int(stem_y)), 8)

    # Draw the red top
    pygame.draw.circle(screen, TOP_COLOR, (int(top_x), int(top_y)), 10)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()