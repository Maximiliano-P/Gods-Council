import pygame
import random
import time
from os.path import join

# Inicializando o pygame
pygame.init()
clock = pygame.time.Clock()
tempo_em_tela = 0
tempo_inicial = pygame.time.get_ticks()
frases = ['Você pode fazer melhor que isso!', 'Tente melhor.', 'urg...', 'Eu pedi um BOM motivo...', 'Hahaha! atena.. você é ilaria!']
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
correndo=True
# Definindo as cores
branco, vermelho, preto, verde = (255, 255, 255), (200, 0, 0), (0, 0, 0), (0, 200, 0)
fundo = pygame.image.load(join('imagens', 'viktor.jpg'))
fundo = pygame.transform.scale(fundo, (largura, altura))
font = pygame.font.Font(None, 50)
teste = 'hm'
class Sprites(pygame.sprite.Sprite):
    def __init__(self, *groups, pasta=str, ImgPath=str, x=0, y=0, correta=False):
        super().__init__(*groups)
        self.correta = correta
        try:
            self.image = pygame.image.load(join(pasta, ImgPath))
            print('loaded')
        except FileNotFoundError:
            self.image = pygame.surface.Surface((100, 100))
            self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_frect(center=(x, y))  # Cria um retângulo para cada sprite
        self.posicaoOrigem = (x, y)



    def clicar(self, pos, frases, tempo_inicial):
        if self.rect.collidepoint(pos):
            if self.correta:
                tela.blit(font.render('LIBERE ELE!', True, verde), (0, 0))
                print('xoxota')
            else: 
                if frases and pygame.time.get_ticks()-tempo_em_tela <2000:
                    global frase
                    tela.blit(font.render(random.choice(frases), True, verde), (0, 0))
                else:
                    frase = ''



              
            
                   

all_sprites = pygame.sprite.Group()
pasta = 'imagens'  
sprites_img = ['palavra.jpg', 'engrasado.jpg' ,'genius.jpg']
x_pos = 100
for s, img in enumerate(sprites_img):
    sprite = Sprites(all_sprites, pasta=pasta, ImgPath=img, x=x_pos, y=300)
    x_pos += 800 / 4 
print(x_pos)
respostacerta =  Sprites(all_sprites, pasta=pasta, ImgPath='nuncatrai.jpg',x=x_pos,y=300,correta=True )




while correndo:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correndo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for sprite in all_sprites:
                sprite.clicar(pos, frases,tempo_inicial)
                frase = tela.blit(font.render(frase, True, verde), (0,0))

            


    
    
    tela.fill(preto)
    tela.blit(fundo, (0, 0))
    all_sprites.draw(tela)

    

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
