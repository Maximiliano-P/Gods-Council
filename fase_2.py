import pygame

def run(SCREEN, WIDTH, HEIGHT):
    running = True
    x, y = WIDTH // 2, HEIGHT // 2
    size = 50
    speed = 5

    while running:
        SCREEN.fill((255, 255, 255))  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x - size > 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x + size < WIDTH:
            x += speed
        if keys[pygame.K_UP] and y - size > 0:
            y -= speed
        if keys[pygame.K_DOWN] and y + size < HEIGHT:
            y += speed

        points = [(x, y - size), (x - size, y + size), (x + size, y + size)]
        pygame.draw.polygon(SCREEN, (255, 0, 0), points)
        pygame.display.flip()
        pygame.time.delay(30)
