import pygame
pygame.init()

while True:
    for event in pygame.event.get():
        pass

    screen=pygame.display.set_mode()
    screen.fill('green')
    pygame.draw.circle(screen, "pink", [200, 150], 50)
    pygame.draw.circle(screen, "white", [300, 150], 50)
    pygame.draw.circle(screen, "red", [400, 150], 50)
    pygame.time.wait(1000)
    pygame.display.flip() #helps the blue become visible
    screen.fill("blue")
    pygame.draw.circle(screen, "pink", [200, 100], 50)
    pygame.draw.circle(screen, "white", [300, 150], 50)
    pygame.draw.circle(screen, "red", [400, 150], 50)
    pygame.display.flip()
    pygame.time.wait(500)
    screen.fill("purple")
    pygame.draw.circle(screen, "pink", [200, 150], 50)
    pygame.draw.circle(screen, "white", [300, 150], 50)
    pygame.draw.circle(screen, "red", [400, 150], 50)
    pygame.display.flip()
    pygame.time.wait(500)

    
