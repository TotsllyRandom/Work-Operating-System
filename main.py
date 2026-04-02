# import pygame package
import pygame

# initializing imported module
pygame.init()

# displaying a window of height
pygame.display.set_mode((640, 360))

Icon = pygame.image.load('assets/icon.jpg')
pygame.display.set_caption("WorkOS")
pygame.display.set_icon(Icon)

# creating a bool value which checks
# if game is running
running = True

# keep game running till running is true
while running:
    
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():
        
        # if event is of type quit then 
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False