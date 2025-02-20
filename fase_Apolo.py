import pygame
from os.path import join
import random
#https://freesound.org/people/Jaz_the_MAN_2/packs/17749/
def run(tela, altura, largura):
    # pygame setup
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    
    posicoesEx=[[(largura/2)-110,600],[largura/2,600],[(largura/2)+110,600]]
    class Sprites(pygame.sprite.Sprite):

        slots = {'slot1':'livre','slot2':'livre','slot3':'livre'}
        NumeroIstancia=1
        posLista=0
        def __init__(self, *groups, pasta=str, ImgPath=str, x=0, y=0):
            super().__init__(*groups)
            try:
                self.image = pygame.image.load(join(pasta, ImgPath)).convert_alpha()
            except FileNotFoundError:
                self.image = pygame.surface.Surface((100,100))
                self.image.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.numero =Sprites.NumeroIstancia
            self.rect = self.image.get_frect(center=(x, y)) #cria um retangulo pra cada sprite
            self.posicaoOrigem=(x,y)
            self.TaEmUmSlot= False
            Sprites.NumeroIstancia += 1

        def click(self, pos):
            if self.rect.collidepoint(pos):
                if self.TaEmUmSlot:
                    self.rect.center=self.posicaoOrigem
                    for slot,estado in Sprites.slots.items():
                        if estado == self.rect:
                            Sprites.slots[slot]='livre'
                            break
                    self.TaEmUmSlot=False
                else:
                    for slot,estado in Sprites.slots.items():
                        if estado == 'livre':
                            Sprites.slots[slot]=self.rect
                            break
                    self.TaEmUmSlot=True

        def update(self):
            if self.rect==Sprites.slots['slot1']:
                self.rect.center=posicoesEx[0]
            elif self.rect==Sprites.slots['slot2']:
                self.rect.center=posicoesEx[1]
            elif self.rect==Sprites.slots['slot3']:
                self.rect.center=posicoesEx[2]

    all_sprites = pygame.sprite.Group()
    pasta = 'imagens'  # Diretório onde as imagens estão armazenadas
    sprites_img = ['nota1.png', 'nota2.png', 'nota3.png', 'nota4.png', 'nota5.png', 'nota6.png', 'nota7.png']

    x_pos = 100  # Posição inicial x

    for img in sprites_img:
        sprite = Sprites(all_sprites, pasta=pasta, ImgPath=img, x=x_pos, y=300)
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
