import pygame
from os.path import join

pygame.init()
screen = pygame.display.set_mode((1320, 720))
clock = pygame.time.Clock()
running = True

sprite_image = pygame.image.load(join("imagens","nuncatrai.jpg"))
sprite_image = pygame.transform.scale(sprite_image, (200, 200))

sprite2_image = pygame.image.load(join("imagens", "palavra.jpg"))
sprite2_image = pygame.transform.scale(sprite2_image, (200, 200))

class Espelho:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def desenhar(self, surface):
        surface.blit(self.image, self.rect)

    def colidiu(self, pos):
        return self.rect.collidepoint(pos)


espelhos = [Espelho(sprite_image, i * 220, 100) for i in range(5)]
espelho_real = Espelho(sprite2_image, 1100, 100)

while running:
    screen.fill("purple")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for espelho in espelhos:
                if espelho.colidiu(event.pos):
                    print('bucetinha rosa glitter muito glitter')
            if espelho_real.colidiu(event.pos):
                print('eu ganhei doido')

    for espelho in espelhos:
        espelho.desenhar(screen)

    espelho_real.desenhar(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()