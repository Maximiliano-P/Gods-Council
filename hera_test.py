import pygame
import random
import time
from os.path import join

def run(tela, altura, largura):

    
    largura, altura = 800, 600
    tela = pygame.display.set_mode((largura, altura))

    branco, vermelho, preto, verde = (255, 255, 255), (200, 0, 0), (0, 0, 0), (0, 200, 0)
    # pygame setup
    pygame.init()
    clock = pygame.time.Clock()
    running = True

    vidas, inicio, tente_de_novo, tente_de_novo2, game_over, vitoria = 3, 'Apenas uma bo razão', 'tente mais!', 'você consegue fazer melhor!', 'Perdeu fia', 'Libere ele.'

    class Perguntas(pygame.sprite.Sprite):
        vidas = 3
        def __init__(self, *groups, pasta=str, ImgPath=str, x=0, y=0):
            super().__init__(*groups)
            self.image = pygame.image.load(join(pasta, ImgPath)).convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_frect(center=(x, y)) #cria um retangulo pra cada sprite
            self.posicaoOrigem=(x,y)

        
        all_sprites = pygame.sprite.Group()
        pasta = 'imagens'  # Diretório onde as imagens estão armazenadas
        sprites_img = ['nota1.png', 'nota2.png', 'nota3.png', 'nota4.png', 'nota5.png', 'nota6.png', 'nota7.png']

        x_pos = 100  # Posição inicial x

        
    all_sprites = pygame.sprite.Group()
    pasta = 'imagens'  # Diretório onde as imagens estão armazenadas
    sprites_img = ['genius.jpg', 'engrasado.jpg', 'nuncatrai.jpg', 'palavra.jpg']
    for img in sprites_img:

        sprite = Perguntas(all_sprites, pasta=pasta, ImgPath=img, x=x_pos, y=300)
        all_sprites.add(sprite)
        x_pos += 1080/6  # Incrementa a posição x para o próximo sprite

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for sprite in all_sprites:
                    sprite.click(pos)
        # fill the screen with a color to wipe away anything from last frame
        tela.fill("purple")
        all_sprites.update()
        # RENDER YOUR GAME HERE
        all_sprites.draw(tela)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

if __name__ == '__main__':
    largura,altura=1280,720
    tela = pygame.display.set_mode((largura, altura))
    run(tela, altura, largura)
    pygame.quit()
