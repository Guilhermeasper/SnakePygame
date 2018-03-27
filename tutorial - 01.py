import pygame

try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com sucesso")

largura=640
altura=480

pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")

pygame.display.update()

pygame.quit()
quit()
