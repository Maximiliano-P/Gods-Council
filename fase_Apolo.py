import pygame
from os.path import join
import random
import numpy as np

def run(tela, altura, largura):
    # pygame setup
    pygame.init()
    pygame.mixer.init()  # Inicializa o mixer de áudio
    clock = pygame.time.Clock()
    running = True

    posicoesEx = [[(largura / 2) - 110, 600], [largura / 2, 600], [(largura / 2) + 110, 600]]

    frequencias = {'do': 261.626, 're': 293.665, 'mi': 329.627, 'fa': 349.228, 'sol': 391.995, 'la': 440.0, 'si': 493.883}
    duracao_sons = 1.0

    class Sons:
        def __init__(self, duracao, frequencia):   
            self.duracao = duracao
            self.t = np.linspace(0, duracao, int(44100 * duracao), False)
            if type(frequencia)==float:
                self.tom = np.sin(2 * np.pi * frequencia * self.t)
            else:
                self.tom=frequencia
            self.audio = np.int16(self.tom * 32767)
            self.audio = np.column_stack((self.audio, self.audio))  # Converte para estéreo

        def get(self):
            return self.audio
        
        def get_tom(self):
            return self.tom
        
        def get_duracao(self):
            return self.duracao

        def __add__(self,*instancias):
            senoide=self.tom
            duracao=self.duracao
            NumeroDeInstanciasSomadas=1
            for instancia in instancias:
                senoide= np.concatenate([senoide,instancia.get_tom()])
                duracao= duracao+instancia.get_duracao()
                NumeroDeInstanciasSomadas+=1
            senoide/=NumeroDeInstanciasSomadas

            soma=Sons(duracao,senoide)
            return soma


    do = Sons(1.0, frequencias['do'])
    re = Sons(1.0, frequencias['re'])
    mi = Sons(1.0, frequencias['mi'])
    fa = Sons(1.0, frequencias['fa'])
    sol = Sons(1.0, frequencias['sol'])
    la = Sons(1.0, frequencias['la'])
    si = Sons(1.0, frequencias['si'])
    lis_sons = [do, re, mi, fa, sol, la, si]
    som_res=do+re+mi
    som_res=pygame.sndarray.make_sound(som_res.get())
    class Sprites(pygame.sprite.Sprite):
        slots = {'slot1': 'livre', 'slot2': 'livre', 'slot3': 'livre'}
        NumeroIstancia = 1
        posLista = 0

        def __init__(self, *groups, pasta=str, ImgPath=str, x=0, y=0, som):
            super().__init__(*groups)
            try:
                self.image = pygame.image.load(join(pasta, ImgPath)).convert_alpha()
            except FileNotFoundError:
                self.image = pygame.surface.Surface((100, 100))
                self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.numero = Sprites.NumeroIstancia
            self.rect = self.image.get_frect(center=(x, y))  # Cria um retângulo para cada sprite
            self.posicaoOrigem = (x, y)
            self.som = pygame.sndarray.make_sound(som.get())
            self.TaEmUmSlot = False
            
            Sprites.NumeroIstancia += 1

        def click(self, pos):
            if self.rect.collidepoint(pos):
                pygame.mixer.stop()
                self.som.play()  # Toca o som no canal associado
                if self.TaEmUmSlot:
                    self.rect.center = self.posicaoOrigem
                    for slot, estado in Sprites.slots.items():
                        if estado == self.rect:
                            Sprites.slots[slot] = 'livre'
                            self.TaEmUmSlot = False
                            break
                else:
                    for slot, estado in Sprites.slots.items():
                        if estado == 'livre':
                            Sprites.slots[slot] = self.rect
                            self.TaEmUmSlot = True
                            break

        def update(self):
            if self.rect == Sprites.slots['slot1']:
                self.rect.center = posicoesEx[0]
            elif self.rect == Sprites.slots['slot2']:
                self.rect.center = posicoesEx[1]
            elif self.rect == Sprites.slots['slot3']:
                self.rect.center = posicoesEx[2]

    all_sprites = pygame.sprite.Group()
    pasta = 'imagens'  # Diretório onde as imagens estão armazenadas
    sprites_img = ['nota1.png', 'nota2.png', 'nota3.png', 'nota4.png', 'nota5.png', 'nota6.png', 'nota7.png']

    x_pos = 100  # Posição inicial x

    for s, img in enumerate(sprites_img):
        sprite = Sprites(all_sprites, pasta=pasta, ImgPath=img, x=x_pos, y=300, som=lis_sons[s])
        all_sprites.add(sprite)
        x_pos += 1080 / 6  # Incrementa a posição x para o próximo sprite
    som_res.play()
    while running:
        # Poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for sprite in all_sprites:
                    sprite.click(pos)

        # Fill the screen with a color to wipe away anything from last frame
        tela.fill("purple")
        all_sprites.update()
        # RENDER YOUR GAME HERE
        all_sprites.draw(tela)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # Limits FPS to 60

if __name__ == '__main__':
    largura, altura = 1280, 720
    tela = pygame.display.set_mode((largura, altura))
    run(tela, altura, largura)
    pygame.quit()