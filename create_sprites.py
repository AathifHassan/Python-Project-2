import pygame
import os

# Initialize pygame
pygame.init()

# Create the assets/images directory if it doesn't exist
if not os.path.exists("assets/images"):
    os.makedirs("assets/images")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Create player sprite
def create_player_sprite():
    # Create a transparent surface for the player ship
    surface = pygame.Surface((50, 40), pygame.SRCALPHA)
    
    # Draw the ship body (triangle)
    pygame.draw.polygon(surface, BLUE, [(25, 0), (0, 40), (50, 40)])
    
    # Draw the cockpit
    pygame.draw.rect(surface, YELLOW, (18, 25, 14, 10))
    
    # Draw engine flames
    pygame.draw.polygon(surface, RED, [(15, 40), (20, 50), (30, 50), (35, 40)])
    
    # Save the image
    pygame.image.save(surface, "assets/images/player.png")
    
    # Create a mini version for lives display
    mini = pygame.Surface((25, 20), pygame.SRCALPHA)
    pygame.draw.polygon(mini, BLUE, [(12, 0), (0, 20), (25, 20)])
    pygame.draw.rect(mini, YELLOW, (9, 12, 7, 5))
    pygame.image.save(mini, "assets/images/player_mini.png")
    
    return surface

# Create enemy sprites (3 different types)
def create_enemy_sprites():
    enemies = []
    
    # Enemy Type 1: Basic saucer
    enemy1 = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.ellipse(enemy1, RED, (0, 5, 30, 20))
    pygame.draw.ellipse(enemy1, YELLOW, (5, 0, 20, 30))
    pygame.image.save(enemy1, "assets/im
