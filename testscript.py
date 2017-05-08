# see if it works this time
# snakey
import pygame

pygame.init()

# setting up game colors

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# sub colors

GREEN_dark = (62, 160, 51)
RED_aqua = (188, 70, 47)

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("slithergame")

gameExit = False

lead_x = display_width/2
lead_y = display_height/2
lead_y_change = 0
lead_x_change = 0

head_size = 20
speed_const = 6
speed_const_change = -6

clock = pygame.time.Clock()

font =pygame.font.SysFont((None, 25)

def message_to_screen (msg, color):
    screen_text = font.render(mag, True, color)
    display.blit(screen_text, [display_width/2, display_height/2])

# event handling
while not gameExit: # while the game is runningr
    for event in pygame.event.get(): # gets the pygame eventsr
        if event.type == pygame.QUIT: # if the event quit is active
            gameExit = True  # quits the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                lead_x_change = speed_const_change
                lead_y_change = 0
            if event.key == pygame.K_d:
                lead_x_change = speed_const
                lead_y_change = 0
            if event.key == pygame.K_w:
                lead_y_change = speed_const_change
                lead_x_change = 0
            if event.key == pygame.K_s:
                lead_y_change = speed_const
                lead_x_change = 0

    if lead_x > display_width or lead_x < 0 or lead_y > display_height or lead_y < 0:
        gameExit = True

    if gameExit == True:
        print("closing")

# logic
    lead_x += lead_x_change
    lead_y += lead_y_change

# graphics
    display.fill(GREEN_dark)
# snake drawing logic
# in order. telling pygame to draw on the displau, telling it what color to use, and then telling it the position ( X and Y ) and the width and height
    pygame.draw.rect(display, RED_aqua, [lead_x, lead_y, head_size, head_size])
    pygame.display.update() # updates the game window

clock.tick(FPS)

pygame.quit()
quit()