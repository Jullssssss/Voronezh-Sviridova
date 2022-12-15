import pygame

if __name__ == '__main__':
    global position
    pygame.init()

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    run = True
    s1 = 0
    s2 = 1
    clock = pygame.time.Clock()
    while run:
        screen.fill((0, 0, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                s1 = 0
                s2 = 0
        while s2 != 1:
            pygame.draw.circle(screen, (255, 255, 0), position, s1)
            pygame.display.flip()
            s1 += 10
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    s2 = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen.fill((0, 0, 255))
                    pygame.display.flip()
                    position = event.pos
                    s1 = 0
    pygame.quit()
