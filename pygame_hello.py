#https://www.pygame.org
import pygame


def main():
    #I niciando a lib Pygame
    pygame.init()
    # Definindo o título da janela
    pygame.display.set_caption("Iniciando com Pygame")
    # Definindo o tamanho da janela
    tela = pygame.display.set_mode([300, 300])
    ''' 
        Definindo o clock da tela. 
        O clock (relógio) define quantos frames por segundo será o intervalo de atualização da tela
    '''
    relogio = pygame.time.Clock()
    # Variável para controlar o evento de sair
    sair = False
    # Variáveis que contém a definição de cores
    cor_branca = (255, 255, 255)
    cor_azul = (108, 194, 236)
    cor_verde = (54, 182, 112)
    cor_vermelha =(255, 0, 0)
    '''
        Criando uma superfice que terá a cor azul.
        Os parâmetros definem a área ocupada pela superfice.
        Neste caso, ela ocupará 200 x 200 pixels
    '''
    sup_azul = pygame.Surface((200, 200))
    sup_azul.fill(cor_azul)
    # Mesmo caso anterior, mas esta superfice será verde
    sup_verde = pygame.Surface((100, 100))
    sup_verde.fill(cor_verde)

    ret = pygame.Rect(10, 10, 45, 45)


    # Mantém a tela aberta até clicar no botão de fechar. 
    while sair == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                ret = ret.move(10, 10)
            
            if event.type == pygame.MOUSEMOTION:
                ret = ret.move(-10, -10)
            '''
            # https://www.pygame.org/docs/ref/key.html
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ret.move_ip(-10, 0)
                if event.key == pygame.K_RIGHT:
                    ret.move_ip(10, 0)
                if event.key == pygame.K_UP:
                    ret.move_ip(0, -10)
                if event.key == pygame.K_DOWN:
                    ret.move_ip(0, 10)
                if event.key == pygame.K_SPACE:
                    ret.move_ip(10, 10)
                if event.key == pygame.K_BACKSPACE:
                    ret.move_ip(-10, -10)

        # Aqui o relógio define que a tela atualizará a 27 frames por segundo
        relogio.tick(27)
        # Define a cor de fundo da tela como branca
        tela.fill(cor_branca)
        # Coloca as superfices na tela nas respectivas posições
        tela.blit(sup_azul, [50, 50])
        tela.blit(sup_verde, [250, 100])

        pygame.draw.rect(tela, cor_vermelha, ret)

        # Atualiza a tela
        pygame.display.update()
    # Encerra 
    pygame.quit()


main()
