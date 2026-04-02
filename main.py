# import pygame module
import pygame

# initializing imported module
pygame.init()

# Displaying a window of height 
# 500 and width 400
screen = pygame.display.set_mode((640, 360))

# Here we set name or title of our
# pygame window
pygame.display.set_caption('WorkOS')

# Here we load the image we want to 
# use
Icon = pygame.image.load('assets/icon.jpg')

# We use set_icon to set new icon
pygame.display.set_icon(Icon)

# Creating a bool value which checks if 
# game is running
running = True

# Keep game running till running is true
while running:
    screen.fill((0, 0, 0))  # black background
    # Check for event if user has pushed 
    # any event in queue

    for event in pygame.event.get():
        
        # If event is of type quit then set 
        # running bool to false
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()