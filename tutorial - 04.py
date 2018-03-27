import pygame
from random import randint

branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com sucesso")

relogio = pygame.time.Clock()

largura=640
altura=480
tamanho = 10
pos_x=randint(0,(largura-tamanho)/10)*10
pos_y=randint(0,(altura-tamanho)/10)*10
velocidade_x=0
velocidade_y=0

fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_x-=10
            if event.key == pygame.K_RIGHT:
                pos_x+=10
            if event.key == pygame.K_UP:
                pos_y-=10
            if event.key == pygame.K_DOWN:
                pos_y+=10
    pos_x+=10
    fundo.fill(branco)
    pygame.draw.rect(fundo, preto, [pos_x,pos_y,tamanho,tamanho])
        
    pygame.display.update()
    relogio.tick(10)

pygame.quit()

