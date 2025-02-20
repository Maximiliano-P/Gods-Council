import pygame


pygame.init()


WIDTH, HEIGHT = 500, 300
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parte 2")
 
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 250, 0)


font = pygame.font.Font(None, 30)

options = ["Diálogo", "Batalha"]
selected_option = 0

#texto da caixinha de dialogo
dialogue_text = "Fuja ou Dialogue"

#Cia a caixa de dialogo
dialogue_box = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 50, 400, 100)
option_positions = [
    (WIDTH // 2 - 100, HEIGHT // 2 + 20),
    (WIDTH // 2 + 50, HEIGHT // 2 + 20)
]

running = True
while running:
    tela.fill(preto)

    pygame.draw.rect(tela, branco, dialogue_box, 3)

    #pega a posição
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Renderiza o menu de seleção
    for i, option in enumerate(options):
        x, y = option_positions[i]

        # Verificação se o mouse esta no luga coeto para fucionar a seleão
        if x <= mouse_x <= x + 100 and y <= mouse_y <= y + 30:
            selected_option = i  # Muda a seleção se o if fo verdadeiro

        color = verde if i == selected_option else branco
        text = font.render(option, True, color)
        tela.blit(text, (x, y))

    #rendeiza o texto
    dialogue_render = font.render(dialogue_text, True, branco)
    tela.blit(dialogue_render, (dialogue_box.x + 20, dialogue_box.y + 20))

    # Atualiza a tela
    pygame.display.flip()

    # Processamento dos eventos do pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                if selected_option == 0:
                    dialogue_text = "Você iniciou o diálogo com Ares..."
                else:
                    dialogue_text = "Você morreu!"
                    running = False  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selected_option = max(0, selected_option - 1)
            elif event.key == pygame.K_RIGHT:
                selected_option = min(len(options) - 1, selected_option + 1)
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    dialogue_text = "Você iniciou o diálogo com Ares..."
                else:
                    dialogue_text = "Você morreu!"
                    running = False  


pygame.quit()
