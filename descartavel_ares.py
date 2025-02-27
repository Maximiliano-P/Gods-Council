import pygame
import random
import time
from os.path import join

def run():

    # Configurações iniciais
    pygame.init()


    largura, altura = 800, 600
    tela = pygame.display.set_mode((largura, altura))


    branco, vermelho, preto, verde = (255, 255, 255), (200, 0, 0), (0, 0, 0), (0, 200, 0)


    # Estados do jogo
    inicio, batalha, gameover, vitoria = "inicio", "batalha", "fim de jogo", "vitoria"


    # Carrega e transforma os sprites
    jogador_parado = pygame.transform.scale(pygame.image.load(join('imagens',"nota7.png")), (50, 50))
    jogador_movendo = pygame.transform.scale(pygame.image.load(join("imagens", "nota2.png")), (50, 50))


    class Jogador(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = jogador_parado
            self.rect = self.image.get_rect(center=(largura // 2, altura // 2))
            self.vel = 4
            self.vida = 100


        def update(self, keys, boundary):
            movendo = any(keys[k] for k in (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s))
            self.image = jogador_movendo if movendo else jogador_parado


            if keys[pygame.K_a]: self.rect.x -= self.vel
            if keys[pygame.K_d]: self.rect.x += self.vel
            if keys[pygame.K_w]: self.rect.y -= self.vel
            if keys[pygame.K_s]: self.rect.y += self.vel


            self.rect.clamp_ip(boundary)


        def Dano_tomado(self, tomado):
            self.vida -= tomado
            return self.vida <= 0


    class Projetil(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.Surface((10, 10))
            self.rect = pygame.Rect(x, y, 10, 10)
            self.image.fill(vermelho)


        def update(self):
            self.rect.y += 5
            if self.rect.top > altura:
                self.kill()


    class Batalha:
        def __init__(self):
            self.box = pygame.Rect(largura // 3, altura // 2, largura // 2, altura // 3)
            self.jogador = Jogador()
            self.projetil = pygame.sprite.Group()
            self.timer = 0
            self.jogador.rect.center = self.box.center
            self.tempo_inicio = time.time()


        def update(self, keys):
            self.jogador.update(keys, self.box)
            self.projetil.update()
            self.timer += 1


            # Se passar os 30 segundos vc vence
            if time.time() - self.tempo_inicio >= 30:
                return "vitoria"


            # Cria o projetil a cada 30 frames
            if self.timer % 30 == 0:
                self.projetil.add(Projetil(random.randint(self.box.left + 10, self.box.right - 10), self.box.top))


            # ve se o player foi atacadp
            for p in self.projetil:
                if self.jogador.rect.colliderect(p.rect):
                    if self.jogador.Dano_tomado(10):
                        return "fim de jogo"
                    p.kill()


            return None


        def draw(self):
            pygame.draw.rect(tela, branco, self.box, 3)
            tela.blit(self.jogador.image, self.jogador.rect)
            self.projetil.draw(tela)
            pygame.draw.rect(tela, vermelho, (self.box.left, self.box.top - 20, self.jogador.vida * 2, 10))


    def mostrar_gameover():
        tela.fill(preto)
        font = pygame.font.Font(None, 50)
        tela.blit(font.render("Você Morreu!", True, vermelho), (largura // 3, altura // 3))
        tela.blit(font.render("Pressione R para reiniciar", True, branco), (largura // 4, altura // 2))
        pygame.display.flip()


    def mostrar_vitoria():
        tela.fill(preto)
        font = pygame.font.Font(None, 50)
        tela.blit(font.render("Parabéns Você Sobreviveu!", True, verde), (largura // 5, altura // 3))
        pygame.display.flip()


    # Inicializa o minegame
    jogador = Jogador()
    batalha = None  
    clock = pygame.time.Clock()
    game_state = inicio


    # roda o codigo
    while True:
        tela.fill(preto)
        keys = pygame.key.get_pressed()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_state == inicio and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                batalha = Batalha()
                game_state = "batalha"
            if game_state == "batalha" and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_state = inicio
            if (game_state == "fim de jogo") and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game_state = inicio


        if game_state == inicio:
            jogador.update(keys, pygame.Rect(0, 0, largura, altura))
            tela.blit(jogador.image, jogador.rect)
            font = pygame.font.Font(None, 50)
            tela.blit(font.render("Pressione espaço para iniciar", True, branco), (largura // 4, altura // 2))


        elif game_state == "batalha":
            resultado = batalha.update(keys)
            if resultado == "fim de jogo":
                game_state = "fim de jogo"
            elif resultado == "vitoria":
                game_state = "vitoria"
            batalha.draw()


        elif game_state == "fim de jogo":
            mostrar_gameover()


        elif game_state == "vitoria":
            mostrar_vitoria()


        pygame.display.flip()
        clock.tick(60)




