from asyncio import events
import pygame
from pygame.locals import *
from sys import exit  # função para fechar janela


pygame.init()  # Iniciando o pygame


largura = 640
altura = 480

# centrlizado objeto na tela
x = largura / 2
y = altura / 2

# Defenindo largura e altura da tela
tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('Jogo')  # Definindo nome do jogo
relogio = pygame.time.Clock()  # Frame


# loop do jogo

while True:

    relogio.tick(60)  # Frame
    tela.fill((0, 0, 0))  # tela preta

    for event in pygame.event.get():  # Detectando se algum evento ocorreu

        # Evento de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Movimentação por telcas
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))

    pygame.display.update()
