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
altura=280
tamanho = 10
placar = 40

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])

def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])

def jogo():
    sair = True
    fimdejogo = False
    pos_x=randrange(0,largura-tamanho,10)
    pos_y=randrange(0,altura-tamanho-placar,10)
    maca_x=randrange(0,largura-tamanho,10)
    maca_y=randrange(0,altura-tamanho-placar,10)
    velocidade_x=0
    velocidade_y=0
    CobraXY = []
    CobraComp = 1
    pontos = 0
    while sair:
        while fimdejogo:
            fundo.fill(branco)
            texto("Fim de jogo, para continuar tecle C ou S para sair", vermelho, 15, largura/10, altura/2)
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
                        pos_y=randrange(0,altura-tamanho-placar,10)
                        maca_x=randrange(0,largura-tamanho,10)
                        maca_y=randrange(0,altura-tamanho-placar,10)
                        velocidade_x=0
                        velocidade_y=0
                        CobraXY = []
                        CobraComp = 1
                        pontos = 0
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
                maca_y=randrange(0,altura-tamanho-placar,10)
                CobraComp += 1
                pontos += 1

            if pos_x + tamanho > largura:
                pos_x = 0
            if pos_x < 0:
                pos_x=largura-tamanho
            if pos_y + tamanho > altura-placar:
                pos_y = 0
            if pos_y < 0:
                pos_y= altura-tamanho-placar
    ##        if pos_x + tamanho > largura:
    ##            fimdejogo = True
    ##        if pos_x < 0:
    ##            fimdejogo = True
    ##        if pos_y + tamanho > altura:
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
            
            pygame.draw.rect(fundo, preto, [0, altura-placar, largura, placar])
            texto("Pontuação:"+str(pontos), branco, 20, 10, altura-30)
            cobra(CobraXY)        
            maca(maca_x,maca_y)
            pygame.display.update()
            relogio.tick(15)
    
jogo()
pygame.quit()
