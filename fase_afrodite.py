import pygame
from os.path import join
pygame.init()
screen = pygame.display.set_mode((1320, 720))
clock = pygame.time.Clock()
running = True

sprite_image = pygame.image.load(join('imagens', 'afrodite.png'))
sprite_espelho2 = pygame.image.load(join('imagens', 'afrodite2.png'))
sprite_espelho2 = pygame.transform.scale(sprite_espelho2, (200, 200))
sprite_image = pygame.transform.scale(sprite_image, (200, 200))

sprite2_image = pygame.image.load(join('imagens', 'afrodite_verdadeira.png'))
sprite2_image = pygame.transform.scale(sprite2_image, (200, 200))

# Variaveis para exibir as msg
mensagem = ""
tempo_mensagem = 0
fonte = pygame.font.Font(None, 50)

#classe dos espelhos de afrodite
class Espelho:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def desenhar(self, surface):
        surface.blit(self.image, self.rect)

    def colidiu(self, pos):
        return self.rect.collidepoint(pos)

#cria uma lista com os obj espelho
espelhos = [Espelho(sprite_image, i * 220, 100) for i in range(5)]
espelhos_debaixo= [Espelho(sprite_espelho2, i * 220, 400) for i in range(6)]
espelho_real = Espelho(sprite2_image, 1100, 100)

while running:
    screen.fill("purple")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #faz a mensagem aparecer se o mouse for clicado
            for espelho in espelhos:
                if espelho.colidiu(event.pos):
                    mensagem = "Você falhou!"
                    tempo_mensagem = pygame.time.get_ticks()
            for espelho in espelhos_debaixo:
                if espelho.colidiu(event.pos):
                    mensagem = "Você falhou!"
                    tempo_mensagem = pygame.time.get_ticks()
            if espelho_real.colidiu(event.pos):
                mensagem = "Parabéns! Você achou a Afrodite verdadeira!"
                tempo_mensagem = pygame.time.get_ticks()

    #for para desenhar os espelhos
    for espelho in espelhos:
        espelho.desenhar(screen)

    for espelho in espelhos_debaixo:
        espelho.desenhar(screen)

    espelho_real.desenhar(screen)

    # titulo 
    texto_titulo = fonte.render("Ache a Afrodite verdadeira", True, (255, 255, 255))
    screen.blit(texto_titulo, (450, 30))

    # Exibe a mensagem por 2 segundos
    if mensagem and pygame.time.get_ticks() - tempo_mensagem < 2000:
        texto_mensagem = fonte.render(mensagem, True, (255, 255, 255))
        screen.blit(texto_mensagem, (450, 600))
    else:
        mensagem = ""

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
