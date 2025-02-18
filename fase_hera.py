import pygame
import random
import time
from os.path import join
def run(tela, altura, largura):
    pygame.init()
    clock = pygame.time.Clock()
    running = True



    largura, altura = 800, 600
    tela = pygame.display.set_mode((largura, altura))
    branco, vermelho, preto, verde = (255, 255, 255), (200, 0, 0), (0, 0, 0), (0, 200, 0)

    class Sprites(pygame.sprite.Sprite):
        NumeroIstancia=1
        posLista=0
        def __init__(self, *groups, pasta=str, ImgPath=str, x=0, y=0):
                super().__init__(*groups)
                self.image = pygame.image.load(join(pasta, ImgPath)).convert_alpha()
                self.image = pygame.transform.scale(self.image, (100, 100))
                self.numero =Sprites.NumeroIstancia
                self.rect = self.image.get_frect(center=(x, y)) #cria um retangulo pra cada sprite
                self.posicaoOrigem=(x,y)
                self.TaEmUmSlot= False
                Sprites.NumeroIstancia += 1
    
        all.sprites = ['eu']



        def click(self, pos):
                if self.rect.collidepoint(pos):
                    if self.TaEmUmSlot:
                        self.rect.center=self.posicaoOrigem
                        for slot,estado in Sprites.slots.items():
                            if estado == self.rect:
                                Sprites.slots[slot]='livre'
                                break
                    else:
                        for slot,estado in Sprites.slots.items():
                            if estado == 'livre':
                                Sprites.slots[slot]=self.rect
                                break
                        print(Sprites.slots)
                        self.TaEmUmSlot=True
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


    def iniciar():
        tela.fill(preto)
        font = pygame.font.Font(None, 50)
        tela.blit(font.render("Game show da corna", True, branco),  (largura // 4, altura // 2))


if __name__ == '__main__':
    largura,altura=1280,720
    tela = pygame.display.set_mode((largura, altura))
    run(tela, altura, largura)
    pygame.quit()