import pygame
from pygame.locals import *
from sys import exit  # função para fechar janela


pygame.init()  # Iniciando o pygame


largura = 640
altura = 480

x = largura / 2
y = 0

# Defenindo largura e altura da tela
tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('Jogo')  # Definindo nome do jogo
relogio = pygame.time.Clock()  # Frame


# loop do jogo

while True:

    relogio.tick(320)  # Frame
    tela.fill((0, 0, 0))  # tela preta

    for event in pygame.event.get():  # Detectando se algum evento ocorreu

        # Evento de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))

    
    if y >= altura:
        y = 0

    y = y+1

    pygame.display.update()
