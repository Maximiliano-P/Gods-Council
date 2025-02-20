import pygame
import random
import time
from os.path import join

#comecando
pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
branco, vermelho, preto, verde = (255, 255, 255), (200, 0, 0), (0, 0, 0), (0, 200, 0)
running = True
genius = pygame.transform.scale(pygame.image.load(join('imagens',"genius.jpg")), (50, 50))
woords = pygame.transform.scale(pygame.image.load(join('imagens', 'palavra.jpg')), (50,50))
engracado = pygame.transform.scale(pygame.image.load(join('imagens', 'engrasado.jpg')), (50,50))
fiel = pygame.transform.scale(pygame.image.load(join('imagens', 'nuncatrai.jpg')), (50,50))
fundo = pygame.image.load(join('imagens', 'genius.jpg'))
fundo = pygame.transform.scale(fundo,(largura,altura))

opcoes = [genius, woords, engracado, fiel]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    tela.blit(fundo)
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60

pygame.quit()
