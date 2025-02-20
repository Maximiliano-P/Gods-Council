import pygame
import numpy as np
frequencias= {'do':261.626,'re':293.665,'mi':329.627,'fa':349.228,'sol':391.995,'la':440.0,'si':493.883}

duracao_sons=1.0

class sons():
    def __init__(self,duracao,frequencia):
        self.duracao=duracao
        self.t=np.linspace(0,duracao,int(44100*duracao),False)
        self.tom=np.sin(2*np.pi*frequencia*self.t)
        self.audio=np.int16(self.tom*32767)
        self.audio=np.column_stack((self.audio,self.audio))
    def get(self):
        return self.audio
do=sons(1.0,frequencias['do'])
re=sons(1.0,frequencias['re'])
mi=sons(1.0,frequencias['mi'])
fa=sons(1.0,frequencias['fa'])
sol=sons(1.0,frequencias['sol'])
la=sons(1.0,frequencias['la'])
si=sons(1.0,frequencias['si'])

def run(SCREEN, WIDTH, HEIGHT):
    pygame.init()
    running = True
    x, y = WIDTH // 2, HEIGHT // 2
    size = 50
    speed = 5
    son_do=pygame.sndarray.make_sound(do.get())
    son_do.play()
    while running:
        SCREEN.fill((255, 255, 255))  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x - size > 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x + size < WIDTH:
            x += speed
        if keys[pygame.K_UP] and y - size > 0:
            y -= speed
        if keys[pygame.K_DOWN] and y + size < HEIGHT:
            y += speed

        points = [(x, y - size), (x - size, y + size), (x + size, y + size)]
        pygame.draw.polygon(SCREEN, (255, 0, 0), points)
        pygame.display.flip()
        pygame.time.delay(30)

if __name__ =="__main__":
    largura,altura=1280,720
    tela = pygame.display.set_mode((largura, altura))
    run(tela, altura, largura)
    pygame.quit()