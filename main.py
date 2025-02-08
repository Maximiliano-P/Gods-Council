import pygame
from os.path import join
# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gods Council")

#carregando imagens

#cadeirajuiz
CadeiraJuiz=pygame.image.load(join('fundos','CadeiraJuiz.png'))
CadeiraJuiz=pygame.transform.scale(CadeiraJuiz,(WIDTH,HEIGHT))

#objection
objectionB=pygame.image.load(join('fundos','OBJECTION.png'))
objectionB=pygame.transform.scale(objectionB,(100,80))
objectionB
# Definição do botão


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(CadeiraJuiz,(0,0))
    screen.blit(objectionB,(600,400))

    pygame.display.flip()

pygame.quit()
