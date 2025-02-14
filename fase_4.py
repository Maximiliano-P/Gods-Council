import pygame
import random
import time
from os.path import join

def run(tela, largura, altura):
    # Inicializa o Pygame
    pygame.init()
    pygame.display.set_caption("Desvie dos Objetos")

    # Cores
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Carrega o sprite do jogador
    player_image = pygame.image.load(join('fundos', 'OBJECTION.png'))  # Substitua pelo caminho da sua imagem
    player_image = pygame.transform.scale(player_image, (100, 100))
    player_rect = player_image.get_rect()
    player_rect.center = (largura // 2, altura - 50)

    # Velocidade do jogador
    player_speed = 5

    # Lista de objetos
    objects = []
    object_speed = 5
    object_spawn_delay = 1000  # Tempo em milissegundos entre o spawn de objetos
    last_object_spawn = pygame.time.get_ticks()

    # Tempo de jogo
    game_duration = 30  # 30 segundos
    start_time = time.time()

    # Função para spawnar objetos
    def spawn_object():
        x = random.randint(0, largura)
        y = 0
        obj_rect = pygame.Rect(x, y, 30, 30)  # Tamanho do objeto
        objects.append(obj_rect)

    # Loop principal do jogo
    running = True
    while running:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= game_duration:
            print("Tempo acabou! Você sobreviveu!")
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimentação do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < largura:
            player_rect.x += player_speed

        # Spawn de objetos
        now = pygame.time.get_ticks()
        if now - last_object_spawn > object_spawn_delay:
            spawn_object()
            last_object_spawn = now

        # Movimentação dos objetos
        for obj in objects:
            obj.y += object_speed
            if obj.colliderect(player_rect):
                print("Você foi atingido!")
                running = False

        # Remove objetos que saíram da tela
        objects = [obj for obj in objects if obj.y < altura]

        # Desenha tudo na tela
        tela.fill(WHITE)
        tela.blit(player_image, player_rect)
        for obj in objects:
            pygame.draw.rect(tela, RED, obj)

        pygame.display.flip()

        # Controla a taxa de atualização
        pygame.time.Clock().tick(60)

    # Finaliza o Pygame

if __name__ == '__main__':
    # Configurações da tela
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run(screen, SCREEN_WIDTH, SCREEN_HEIGHT)