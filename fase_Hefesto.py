import pygame
import random
import time
from os.path import join
class Player(pygame.sprite.Sprite):
    def __init__(self, groups,path):
        super().__init__(groups)
        self.velocidade=300
        self.direcao=pygame.Vector2(0,0)
        self.vida=1
        self.armadura=0
        self.altura=50
        #carregando imagem e redimencionando pra que ela tenha a altura desejada sem distorções
        self.image=pygame.image.load(join('imagens',path))
        self.mult=self.altura/self.image.get_size()[0]
        self.redimencionado=(self.image.get_size()[0]*self.mult,self.image.get_size()[1]*self.mult)
        self.image=pygame.transform.scale(self.image,(self.redimencionado))
        self.rect=self.image.get_frect(center=(400,400))

    def update(self, dt):
        #movimentação
        keys= pygame.key.get_pressed()
        self.direcao.x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        self.direcao.y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        #normalizando o movimento para não ir mais rápido do que deve nas diagonais
        self.direcao= self.direcao.normalize() if self.direcao else self.direcao
        self.rect.center+=self.direcao*self.velocidade*dt


def run(tela, largura, altura):
    pygame.init()
    pygame.display.set_caption("Desvie dos Objetos")

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    objects = []
    object_speed = 5
    object_spawn_delay = 1000
    last_object_spawn = pygame.time.get_ticks()
    game_duration = 30
    start_time = time.time()


    all_sprites=pygame.sprite.Group()
    personagem=Player(all_sprites,'banana1.png')
    def spawn_object():
        x = random.randint(0, largura)
        y = 0
        obj_rect = pygame.Rect(x, y, 30, 30)
        objects.append(obj_rect)

    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60) / 1000
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= game_duration:
            print("Tempo acabou! Você sobreviveu!")
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        now = pygame.time.get_ticks()
        if now - last_object_spawn > object_spawn_delay:
            spawn_object()
            last_object_spawn = now

        

        objects = [obj for obj in objects if obj.y < altura]

        tela.fill('WHITE')
        all_sprites.update(dt)
        all_sprites.draw(tela)

        for obj in objects:
            pygame.draw.rect(tela, RED, obj)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == '__main__':
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run(screen, SCREEN_WIDTH, SCREEN_HEIGHT)