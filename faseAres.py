import pygame
import random
import time
from os.path import join

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))

branco, vermelho, preto, verde = (255, 255, 255), (200, 0, 0), (0, 0, 0), (0, 200, 0)

inicio, batalha, gameover, vitoria = "inicio", "batalha", "fim de jogo", "vitoria"

#carregando os sprites

jogador_parado = pygame.transform.scale(pygame.image.load(join('imagens','banana2.png')), (50, 50))
jogador_movendo = pygame.transform.scale(pygame.image.load(join('imagens','banana1.png')), (50, 50))
jogador_movendo_delado = pygame.transform.scale(pygame.image.load(join('imagens','banana3.png')), (100, 50))
lanca = pygame.transform.scale(pygame.image.load(join('imagens', 'lanca2.png')), (46,120))
fundo = pygame.image.load(join('imagens', 'nuncatrai.jpg'))


#classe do player
class Jogador(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image = jogador_parado
        self.rect = self.image.get_rect(center=(400, 300))
        self.vel = 4
        self.vida = 100

    def update(self, keys, boundary):
        if keys[pygame.K_a]:
            self.image = jogador_movendo_delado
        elif keys[pygame.K_d]:
            self.image = jogador_movendo
        else:
            self.image = jogador_parado

        if keys[pygame.K_a]: self.rect.x -= self.vel
        if keys[pygame.K_d]: self.rect.x += self.vel
        if keys[pygame.K_w]: self.rect.y -= self.vel
        if keys[pygame.K_s]: self.rect.y += self.vel

        self.rect.clamp_ip(boundary)

    def Dano_tomado(self, tomado):
        self.vida -= tomado
        return self.vida <= 0


# classe da lanca
class Projetil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = lanca
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y += 5
        if self.rect.top > altura:
            self.kill()

#classe do campo de batalha
class Batalha:
    def __init__(self):
        self.box = pygame.Rect(266, 300, 400, 200)
        self.jogador = Jogador()
        self.projetil = pygame.sprite.Group()
        self.timer = 0
        self.jogador.rect.center = self.box.center
        self.tempo_inicio = time.time()


    #da update nas coisas de batalha
    def update(self, keys):
        self.jogador.update(keys, self.box)
        self.projetil.update()
        self.timer += 1

        if time.time() - self.tempo_inicio >= 30:
            return "vitoria"
        #dentro de 30 segundos vai cair lanca do céu
        if self.timer % 30 == 0:
            self.projetil.add(Projetil(random.randint(self.box.left + 10, self.box.right - 10), self.box.top-100))

        #morte
        for p in self.projetil:
            if self.jogador.rect.colliderect(p.rect):
                if self.jogador.Dano_tomado(10):
                    return "fim de jogo"
                p.kill()

        return None


    def draw(self):
        #desenha caixa jogador e projeteis
        pygame.draw.rect(tela, branco, self.box, 3)
        tela.blit(self.jogador.image, self.jogador.rect)
        self.projetil.draw(tela)
        #desenha a barra de vida
        pygame.draw.rect(tela, vermelho, (self.box.left + 320, self.box.top -250, self.jogador.vida * 2, 10))

        #desenha o timer
        tempo_restante = max(0, 30 - int(time.time() - self.tempo_inicio))
        font = pygame.font.Font(None, 40)
        texto_tempo = font.render(f"Tempo: {tempo_restante}s", True, branco)
        tela.blit(texto_tempo, (largura - 150, 10))


# Funcoes das telas de morte
def mostrar_gameover():
    tela.fill(preto)
    font = pygame.font.Font(None, 50)
    tela.blit(font.render("Você Morreu!", True, vermelho), (266, 200))
    tela.blit(font.render("Pressione R para reiniciar", True, branco), (200, 300))
    pygame.display.flip()

def mostrar_vitoria():
    tela.fill(preto)
    font = pygame.font.Font(None, 50)
    tela.blit(font.render("Parabéns Você Sobreviveu!", True, verde), (160, 200))
    pygame.display.flip()

jogador = Jogador()
batalha = None  
clock = pygame.time.Clock()
game_state = inicio

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
        if game_state == "fim de jogo" and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            game_state = inicio
            
    #define as telas do jogo
    if game_state == inicio:
        jogador.update(keys, pygame.Rect(0, 0, largura, altura))
        tela.blit(jogador.image, jogador.rect)
        font = pygame.font.Font(None, 50)
        tela.blit(font.render("Pressione espaço para iniciar", True, branco), (200, 300))
    elif game_state == "batalha":
        resultado = batalha.update(keys)
        if resultado:
            game_state = resultado
        batalha.draw()
    elif game_state == "fim de jogo":
        mostrar_gameover()
    elif game_state == "vitoria":
        mostrar_vitoria()

    pygame.display.flip()
    clock.tick(60)