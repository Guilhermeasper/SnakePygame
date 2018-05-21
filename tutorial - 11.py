import pygame
from random import randrange

branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com sucesso")

largura=320
altura=240
tamanho = 10

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")
font = pygame.font.SysFont(None, 15)

def texto(msg, cor):
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [largura/10, altura/2])

def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])

def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])

def jogo():
    sair = True
    fimdejogo = False
    pos_x=randrange(0,largura-tamanho,10)
    pos_y=randrange(0,altura-tamanho,10)
    maca_x=randrange(0,largura-tamanho,10)
    maca_y=randrange(0,altura-tamanho,10)
    velocidade_x=0
    velocidade_y=0
    CobraXY = []
    CobraComp = 1
    while sair:
        while fimdejogo:
            fundo.fill(branco)
            texto("Fim de jogo, para continuar tecle C ou S para sair", vermelho)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = True
                        fimdejogo = False
                        pos_x=randrange(0,largura-tamanho,10)
                        pos_y=randrange(0,altura-tamanho,10)
                        maca_x=randrange(0,largura-tamanho,10)
                        maca_y=randrange(0,altura-tamanho,10)
                        velocidade_x=0
                        velocidade_y=0
                        CobraXY = []
                        CobraComp = 1
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y=0
                    velocidade_x=-tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y=0
                    velocidade_x=tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x=0
                    velocidade_y=-tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x=0
                    velocidade_y=tamanho
                if event.key == pygame.K_SPACE:
                    CobraComp += 1
        if sair:
            fundo.fill(branco)
            pos_x+=velocidade_x
            pos_y+=velocidade_y

            if pos_x == maca_x and pos_y == maca_y:
                maca_x=randrange(0,largura-tamanho,10)
                maca_y=randrange(0,altura-tamanho,10)
                CobraComp += 1

            if pos_x > largura:
                pos_x = 0
            if pos_x < 0:
                pos_x=largura-tamanho
            if pos_y > altura:
                pos_y = 0
            if pos_y < 0:
                pos_y= altura-tamanho
    ##        if pos_x > largura:
    ##            fimdejogo = True
    ##        if pos_x < 0:
    ##            fimdejogo = True
    ##        if pos_y > altura:
    ##            fimdejogo = True
    ##        if pos_y < 0:
    ##            fimdejogo = True

            CobraInicio = []
            CobraInicio.append(pos_x)
            CobraInicio.append(pos_y)
            CobraXY.append(CobraInicio)
            if len(CobraXY) > CobraComp:
                del CobraXY[0]
            
            if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                fimdejogo = True

            
            cobra(CobraXY)
                    
            maca(maca_x,maca_y)
            pygame.display.update()
            relogio.tick(15)
    
jogo()
pygame.quit()
