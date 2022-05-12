import pygame
from pygame.locals import *
from sys import exit  # função para fechar janela

# Iniciando o pygame
pygame.init()

# Defenindo largura e altura da tela
largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

# Definindo nome do jogo
pygame.display.set_caption('Jogo')



# loop do jogo 
while True:
    # Detectando se algum evento ocorreu 
    for event in pygame.event.get():

        #Evento de fechar o jogo
        if event.type == QUIT:
          pygame.quit()
          exit()

    pygame.display.update()