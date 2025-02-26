import pygame
import random
import time
from os.path import join

# Inicializando o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

# Definindo as cores
verde = (0, 255, 0)
fundo = pygame.image.load(join('imagens', 'viktor.jpg'))
fundo = pygame.transform.scale(fundo, (largura, altura))
font = pygame.font.Font(None, 50)

# Lista de frases
frases = ['Você pode fazer melhor que isso!', 'Tente melhor.', 'urg...', 'Eu pedi um BOM motivo...', 'Hahaha! atena.. você é ilaria!']

# Variável para o controle de tempo
tempo_inicial = time.time()
tempo_em_tela = 2  # Tempo que o texto ficará visível
texto_mostrado = False
frase = ""

# Loop principal
correndo = True
while correndo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correndo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Exemplo de clicar e mostrar uma frase
            frase = random.choice(frases)  # Escolhe uma frase aleatória
            tempo_inicial = time.time()  # Reseta o tempo inicial
            texto_mostrado = True  # Marca que o texto foi mostrado

    # Verificar o tempo e exibir o texto por 2 segundos
    if texto_mostrado:
        tempo_atual = time.time()
        if tempo_atual - tempo_inicial <= tempo_em_tela:
            # Certifique-se de que 'frase' é uma string
            if isinstance(frase, str):  # Garantir que 'frase' é uma string
                tela.blit(font.render(frase, True, verde), (0, 0))  # Exibe a frase
        else:
            texto_mostrado = False  # Após 2 segundos, o texto desaparece

    # Preenche a tela com o fundo e a frase
    tela.fill((0, 0, 0))  # Cor de fundo preta
    tela.blit(fundo, (0, 0))  # Exibe o fundo

    pygame.display.flip()  # Atualiza a tela
    clock.tick(60)  # Limita o FPS a 60

pygame.quit()
