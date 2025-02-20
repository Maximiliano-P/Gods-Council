import pygame
import random
import time
from os.path import join

#comecando
pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
branco, vermelho, preto, verde = (255, 255, 255), (200, 0, 0), (0, 0, 0), (0, 200, 0)

genius = pygame.transform.scale(pygame.image.load(join('imagens',"genius.jpg")), (50, 50))
woords = pygame.transform.scale(pygame.image.load(join('imagens', 'palavra.jpg')), (50,50))
engracado = pygame.transform.scale(pygame.image.load(join('imagens', 'engrasado.jpg')), (50,50))
fiel = pygame.transform.scale(pygame.image.load(join('imagens', 'nuncatrai.jpg')), (50,50))
fundo = pygame.image.load(join('imagens', 'genius.jpg'))

opcoes = [genius, woords, engracado, fiel]


while True:
    tela.fill(verde)
    tela.blit(fundo)



