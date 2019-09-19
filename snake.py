''' A biblioteca pygame é importada, 
juntamente do modulo locals dela, além 
disso o metodo randrange que usaremos 
para gerar numeros aleatórios para as 
posições da cobra e maçã '''
import pygame
import pygame.locals
from random import randrange
print("Módulos importados com sucesso")


''' Utilizando um bloco de tentativa e erro
para checar se o pygame foi iniciado corretamente '''
try:
    pygame.init()
    print("O modulo pygame foi inicializado com sucesso")
except:
    print("O modulo pygame não foi inicializado com sucesso")


''' Declaração das váriaveis globais que utilizaremos
em todo o código, altura e largura da tela, tamanho da
cobra e maçã, tamanho do placar e cores no formato RGB'''
largura=320
altura=280
tamanho = 10
placar = 40
branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
prata=(192,192,192)
laranja=(255,69,0)
cinza=(79,79,79)
cinzaClaro=(220,220,220)


''' Definição de configurações do jogo, relógio para
definir o fps, fundo para desenhar tudo do jogo e o 
título da janela do jogo '''
relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake Game")



''' Classe texto servirá para criar objetos de texto
que serão exibidos nas telas do jogo, recebe a mensagem
a cor e o tamanho como parâmetros '''
class Texto:
    def __init__(self, msg, cor, tam):
        self.font = pygame.font.SysFont(None, tam)
        self.texto = self.font.render(msg, True, cor)
        
    ''' Método show desenha na tela o texto criado pelo
    construtor da classe '''
    def show(self, x, y):
        fundo.blit(self.texto, [x, y])


''' Classe cobra definirá os elementos do objeto
cobra, como cabeça, comprimento e direção, bem
como o array que contém a posição de cada pedaço
da cobra, recebe as coordenadas x e y como parâmetro, 
que será o local na tela onde ela começará o jogo '''
class Cobra:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cabeca = [x,y]
        self.comp = 1
        self.cobra = [self.cabeca]
        self.direcao = ""

    ''' Método move, recebe os parâmetro x e y,
    que serão as novas coordenadas da cabeça e 
    insere a nova cabeça no array das posições '''
    def move(self, x, y):
        self.cabeca = [x,y]
        self.cobra.append([x,y])

    ''' Método cresce, aumenta o comprimento da
    cobra '''
    def cresce(self):
        self.comp += 1

    ''' Método show, desenha cada pedaço da cobra
    na tela '''
    def show(self):
        for XY in self.cobra:
            pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])

    ''' Método rastro, remove a cauda quando o
    tamanho do array é maior que o comprimento da
    cobra '''
    def rastro(self):
        if len(self.cobra) > self.comp:
                del self.cobra[0]

    ''' Método morreu, verifica se a cobra comeu
    ela mesma, se sim retorna verdadeiro, caso 
    contrário, retorna falso '''
    def morreu(self):
        if any(Bloco == self.cabeca for Bloco in self.cobra[:-1]):
            return True
        return False

    ''' Método reinicia, redefine todos os valores 
    da cobra para os valores iniciais, para caso
    depois de ter perdido o jogados possa continuar
    jogando '''
    def reinicia(self,x , y):
        self.x = x
        self.y = y
        self.cabeca = [x,y]
        self.comp = 1
        self.cobra = [self.cabeca]


''' Classe maçã que definirá o objeto maçã,
não recebe nenhum parâmetro, possui os atributos
x e y que é a posição da maçã na tela '''
class Maca:
    def __init__(self):
        self.x = randrange(0,largura-tamanho,10)
        self.y = randrange(0,altura-tamanho-placar,10)

    ''' Método show, desenha a maçã na tela '''
    def show(self):
        pygame.draw.rect(fundo, vermelho, [self.x, self.y, tamanho, tamanho])

    ''' Método reposicionar, define novos x e y
    aleatórios para a maçã após ser comida pela cobra '''
    def reposicionar(self):
        self.x = randrange(0,largura-tamanho,10)
        self.y = randrange(0,altura-tamanho-placar,10)

''' Classe Jogo, definirá todo o restante do jogo, 
como variaveis de controle para continuar jogando,
perder, posição e velocidade da cobra, pontos, bem como
são criados os objetos maçã e cobra, não recebe parâmetros '''
class Jogo:
    def __init__(self):
        self.jogando = True
        self.perdeu = False
        
        self.pos_x=randrange(0,largura-tamanho,10)
        self.pos_y=randrange(0,altura-tamanho-placar,10)
        
        self.velocidade_x=0
        self.velocidade_y=0
        
        self.pontos = 0

        self.cobra = Cobra(self.pos_x, self.pos_y)
        self.maca = Maca()


    ''' Método iniciar, possui o loop principal do jogo,
    que faz absolutamente tudo que acontece no jogo '''
    def iniciar(self):
        while self.jogando:

            ''' Iterador de eventos, todos os eventos que
            acontecem durante o tempo de execução estão podem
            ser obtidos pelo "pygame.event.get()", sendo assim 
            verificado se o jogo não foi fechado, bem como se
            nenhuma das setas foi apertada para mover a cobra '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.cobra.direcao != "direita":
                        self.cobra.direcao = "esquerda"
                    if event.key == pygame.K_RIGHT and self.cobra.direcao != "esquerda":
                        self.cobra.direcao = "direita"
                    if event.key == pygame.K_UP and self.cobra.direcao != "baixo":
                        self.cobra.direcao = "cima"
                    if event.key == pygame.K_DOWN and self.cobra.direcao != "cima":
                        self.cobra.direcao = "baixo"
                    if event.key == pygame.K_SPACE:
                        self.cobra.cresce()

            ''' Checa se o jogador ainda não perdeu o jogo '''
            if self.jogando:

                ''' Limpa a tela a cada novo inicio de loop '''
                fundo.fill(branco)
                
                ''' Checa para qual direção a cobra está seguindo e 
                redefine a nova posição naquela direção '''
                if self.cobra.direcao == "cima":
                    self.pos_y -= tamanho
                elif self.cobra.direcao == "baixo":
                    self.pos_y += tamanho
                elif self.cobra.direcao == "esquerda":
                    self.pos_x -= tamanho
                elif self.cobra.direcao == "direita":
                    self.pos_x += tamanho
                else:
                    pass

                ''' Checa se a cobra e a maçã estão na mesma posição,
                caso estejam, a maçã é reposicionada, a cobra aumenta e
                o placar de pontos aumenta '''
                if self.pos_x == self.maca.x and self.pos_y == self.maca.y:
                    self.maca.reposicionar()
                    self.cobra.cresce()
                    self.pontos += 1

    ##            if self.pos_x + tamanho > largura:
    ##                self.pos_x = 0
    ##            if self.pos_x < 0:
    ##                self.pos_x=largura-tamanho
    ##            if self.pos_y + tamanho > altura-placar:
    ##                self.pos_y = 0
    ##            if self.pos_y < 0:
    ##                self.pos_y= altura-tamanho-placar

                ''' Checa se a cobra ultrapassou alguma das bordas,
                caso tenha ultrapassado é definido que não se está
                mais jogando porque perdeu e é chamado o método "perdido" '''
                if self.pos_x + tamanho > largura:
                    self.jogando = False
                    self.perdeu = True
                    self.perdido()
                if self.pos_x < 0:
                    self.jogando = False
                    self.perdeu = True
                    self.perdido()
                if self.pos_y + tamanho > altura:
                    self.jogando = False
                    self.perdeu = True
                    self.perdido()
                if self.pos_y < 0:
                    self.jogando = False
                    self.perdeu = True
                    self.perdido()

                ''' Move a cobra para a nova posição que é 
                definida como parâmetro do método '''
                self.cobra.move(self.pos_x, self.pos_y)

                ''' Limpa o rastro deixado pelo blocos adicionais '''
                self.cobra.rastro()

                ''' Checa se a cobra comeu ela mesma, caso
                tenha comido o jogo é definido perdido, e o 
                método "perdido" é chamado '''
                if self.cobra.morreu():
                    self.jogando = False
                    self.perdeu = True
                    self.perdido()

                ''' Desenha a cobra na tela '''
                self.cobra.show()

                ''' Desenha o placa e o texto contendo a pontuação atual '''
                pygame.draw.rect(fundo, preto, [0, altura-placar, largura, placar])
                textoPlacarSombra = Texto("Pontuação:"+str(self.pontos), cinza, 25)
                textoPlacarSombra.show(9, altura-31)
                textoPlacar = Texto("Pontuação:"+str(self.pontos), branco, 25)
                textoPlacar.show(10, altura-30)
                
                ''' Desenha a maçã na tela '''
                self.maca.show()

                ''' Atualiza toda a tela com todos os
                elementos que foram desenhados anteriormente '''
                pygame.display.update()

                ''' Define o fps do jogo '''
                relogio.tick(15)
        return 0


    ''' Método perdido, possui o loop da tela de
    derrota, faz tudo que acontece ao perder, 
    podendo o jogador voltar a jogar ou sair do jogo '''
    def perdido(self):
        while self.perdeu:

            ''' Iterador de eventos, todos os eventos que
            acontecem durante o tempo de execução estão podem
            ser obtidos pelo "pygame.event.get()", é verificado
            se o jogador quis sair do jogo ou quer voltar a jogar,
            caso queira voltar, todo o jogo é redefinido e se retorna
            para o método iniciar '''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogando = False
                    self.perdeu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.jogando = True
                        self.perdeu = False
                        self.pos_x=randrange(0,largura-tamanho,10)
                        self.pos_y=randrange(0,altura-tamanho-placar,10)
                        self.cobra.direcao = ""
                        self.maca.reposicionar()
                        self.cobra.reinicia(self.pos_x, self.pos_y)
                        self.velocidade_x=0
                        self.velocidade_y=0
                        self.pontos = 0
                    if event.key == pygame.K_s:
                        self.jogando = False
                        self.perdeu = False
            
            ''' Limpa a tela '''
            fundo.fill(branco)

            ''' Desenha "Fim de jogo" na tela '''
            textoPerdeuSombra = Texto("Fim de jogo", cinza, 50)
            textoPerdeuSombra.show(64, 29)
            textoPerdeu = Texto("Fim de jogo", laranja, 50)
            textoPerdeu.show(65, 30)

            ''' Desenha a pontuação final do jogador '''
            textoPontuacaoSombra = Texto("Pontuação Final: "+str(self.pontos), cinzaClaro, 30)
            textoPontuacaoSombra.show(69, 79)
            textoPontuacao = Texto("Pontuação Final: "+str(self.pontos), preto, 30)
            textoPontuacao.show(70, 80)

            ''' Desenha o botão de continuar jogando '''
            pygame.draw.rect(fundo, prata, [43, 118, 139, 31])
            pygame.draw.rect(fundo, preto, [45, 120, 135, 27])
            textoContinuar = Texto("Continuar(C)", branco, 30)
            textoContinuar.show(50, 125)

            ''' Desenha o botão de sair do jogo '''
            pygame.draw.rect(fundo, prata, [188, 118, 79, 31])
            pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
            textoSair = Texto("Sair(S)", branco, 30)
            textoSair.show(195, 125)

            ''' Atualiza a tela com todos os elementos '''
            pygame.display.update()
        return 0

''' Instancia do jogo '''
instancia = Jogo()

''' Iniciando o jogo através da instância '''
instancia.iniciar()

''' Fecha a janela principal do jogo '''
pygame.quit()
