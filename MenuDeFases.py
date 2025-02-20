import pygame
from os.path import join
import fase_apolo, fase_2, fase_3, fase_4, fase_5, hera_test  # Importando todas as fases

# Inicializa o Pygame
pygame.init()

# Configuração da tela
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Principal")

# Cores
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Criar classe para botões
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, pasta, imagem, fase):
        super().__init__()
        self.image = pygame.image.load(join(pasta, imagem))
        self.image = pygame.transform.scale(self.image, (150, 80))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.fase = fase

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Definir posições dos botões
button_positions = [
    (100, 100), (300, 100), (100, 300),
    (300, 300), (100, 500), (300, 500)
]

# Criar lista de botões
buttons = [
    Button(x, y, "fundos", "OBJECTION.png", i+1) 
    for i, (x, y) in enumerate(button_positions)
]

# Função para carregar a fase
def load_fase(fase):
    if fase == 1:
        fase_apolo.run(SCREEN, WIDTH, HEIGHT)
    elif fase == 2:
        fase_2.run(SCREEN, WIDTH, HEIGHT)
    elif fase == 3:
        fase_3.run(SCREEN, WIDTH, HEIGHT)
    elif fase == 4:
        fase_4.run(SCREEN, WIDTH, HEIGHT)
    elif fase == 5:
        fase_5.run(SCREEN, WIDTH, HEIGHT)
    elif fase == 6:
        hera_test.run(SCREEN, WIDTH, HEIGHT)

# Loop principal
running = True
while running:
    SCREEN.fill(GRAY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.is_clicked(event.pos):
                    load_fase(button.fase)

    for button in buttons:
        button.draw(SCREEN)

    pygame.display.flip()

pygame.quit()
