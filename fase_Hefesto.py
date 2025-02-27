import pygame
import random
from os.path import join
class Player(pygame.sprite.Sprite):
    def __init__(self, groups,path):
        super().__init__(groups)
        self.velocidade=300
        self.direcao=pygame.Vector2(0,0)
        self.__vida=5
        self.__armadura=0
        self.altura=50
        #carregando imagem e redimencionando pra que ela tenha a altura desejada sem distorções
        self.image=pygame.image.load(join('imagens',path))
        self.mult=self.altura/self.image.get_size()[0]
        self.redimencionado=(self.image.get_size()[0]*self.mult,self.image.get_size()[1]*self.mult)
        self.image=pygame.transform.scale(self.image,(self.redimencionado))
        self.rect=self.image.get_frect(center=(400,400))

    def update(self, dt):

        if self.__vida<=0:
            print('morreu')
            global running
            running=False
        #movimentação
        keys= pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            self.direcao.x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT] 
        else:
            self.direcao.x = keys[pygame.K_d] - keys[pygame.K_a]
        
        if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            self.direcao.y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        else:
            self.direcao.y = keys[pygame.K_s] - keys[pygame.K_w]

        #normalizando o movimento para não ir mais rápido do que deve nas diagonais
        self.direcao= self.direcao.normalize() if self.direcao else self.direcao
        self.rect.center+=self.direcao*self.velocidade*dt
    def colidiu(self,obj):
        if self.__armadura:
            self.__armadura-=1
        else:
            self.__vida-=1


def run(tela, largura, altura):
    largura = 800
    tela = 600
    screen = pygame.display.set_mode((largura, altura))
    pygame.init()
    pygame.display.set_caption("Desvie dos Objetos")

    class Projeteis(pygame.sprite.Sprite):
        def __init__(self, *groups):
            super().__init__(*groups)
            self.tipo=random.choice(['marreta.png','blade of olympus.png','machado.png'])
            self.altura= 40 if self.tipo=='marreta.png' or self.tipo=='machado.png' else 50
            
            #carregando imagem e redimencionando pra que ela tenha a altura desejada sem distorções
            self.image=pygame.image.load(join('imagens',self.tipo))
            self.mult=self.altura/self.image.get_size()[0]
            self.redimencionado=(self.image.get_size()[0]*self.mult,self.image.get_size()[1]*self.mult)
            self.image=pygame.transform.scale(self.image,(self.redimencionado))
            self.rect=self.image.get_frect(center=(random.randint(0,largura),0))
            
            #atributos para movimento
            self.direcao= pygame.Vector2(random.uniform(0,1),1)
            self.velocidade= 500


        def update(self,dt):
            self.rect.center+=self.direcao*self.velocidade*dt

            if self.rect.top>altura:
                self.kill()

        def colidiu(self,obj):
            self.kill()
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    game_duration = 30
    start_time = pygame.time.get_ticks()//1000


    all_sprites=pygame.sprite.Group()
    projeteis=pygame.sprite.Group()
    personagem=Player(all_sprites,'banana1.png')

    clock = pygame.time.Clock()
    running = True
    cooldown=0
    
    while running:
        dt = clock.tick(60) / 1000
        current_time = pygame.time.get_ticks()//1000
        elapsed_time = current_time - start_time
        print(current_time)
        if elapsed_time >= game_duration:
            print("Tempo acabou! Você sobreviveu!")
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if cooldown <= 0:
            Projeteis((projeteis,all_sprites))
            cooldown = 1  # Define o cooldown (1 segundo)
        cooldown -= 1*dt  # Reduz o cooldown
        
        if pygame.sprite.spritecollide(personagem,projeteis,True):
            personagem.colidiu(projeteis)
            pass
        
        tela.fill('WHITE')
        all_sprites.update(dt)
        all_sprites.draw(tela)

        pygame.display.flip()
        pygame.time.Clock()

if __name__ == '__main__':
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
