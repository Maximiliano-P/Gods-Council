import pygame

def run(SCREEN, WIDTH, HEIGHT):
    running = True
    x, y = WIDTH // 2, HEIGHT // 2
    radius = 30
    speed = 5

    while running:
        SCREEN.fill((255, 255, 255))  # Fundo branco

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False  # Volta ao menu
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x - radius > 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x + radius < WIDTH:
            x += speed
        if keys[pygame.K_UP] and y - radius > 0:
            y -= speed
        if keys[pygame.K_DOWN] and y + radius < HEIGHT:
            y += speed

        pygame.draw.circle(SCREEN, (0, 0, 255), (x, y), radius)
        pygame.display.flip()
        pygame.time.delay(30)
