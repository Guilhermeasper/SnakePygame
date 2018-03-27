import pygame

branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com sucesso")

largura=640
altura=480
tamanho = 10
pos_x=largura/2
pos_y=altura/2

fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    fundo.fill(branco)
    pygame.draw.rect(fundo, preto, [pos_x,pos_y,tamanho,tamanho])
    pos_x+=0.1
        
    pygame.display.update()

pygame.quit()

