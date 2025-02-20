import pygame
import random
import time
from os.path import join

def run(tela, largura, altura):
    pygame.init()
    pygame.display.set_caption("Desvie dos Objetos")

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Tenta carregar a imagem do jogador
    try:
        player_image = pygame.image.load(join('imagens', 'nota6.png'))
        player_image = pygame.transform.scale(player_image, (100, 100))
    except FileNotFoundError:
        # Cria um quadrado vermelho se a imagem não for encontrada
        player_image = pygame.Surface((100, 100))
        player_image.fill(RED)
        print("Imagem não encontrada! Usando quadrado vermelho.")

    player_rect = player_image.get_rect()
    player_rect.center = (largura // 2, altura - 50)

    # Restante do código permanece igual...
    player_speed = 5
    objects = []
    object_speed = 5
    object_spawn_delay = 1000
    last_object_spawn = pygame.time.get_ticks()
    game_duration = 30
    start_time = time.time()

    def spawn_object():
        x = random.randint(0, largura)
        y = 0
        obj_rect = pygame.Rect(x, y, 30, 30)
        objects.append(obj_rect)

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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < largura:
            player_rect.x += player_speed

        now = pygame.time.get_ticks()
        if now - last_object_spawn > object_spawn_delay:
            spawn_object()
            last_object_spawn = now

        for obj in objects:
            obj.y += object_speed
            if obj.colliderect(player_rect):
                print("Você foi atingido!")
                running = False

        objects = [obj for obj in objects if obj.y < altura]

        tela.fill(WHITE)
        tela.blit(player_image, player_rect)
        for obj in objects:
            pygame.draw.rect(tela, RED, obj)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == '__main__':
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run(screen, SCREEN_WIDTH, SCREEN_HEIGHT)