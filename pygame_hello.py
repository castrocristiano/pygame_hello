# https://www.pygame.org
import pygame
import sons
# Variáveis que contém a definição de cores
from colisao import Colisao
from cores import cor_azul, cor_verde, cor_branca, cor_vermelha, cor_rosa
from fontes import fonte_perdeu


def main():
    # Iniciando a lib Pygame
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
    ret2 = pygame.Rect(50, 50, 80, 50)
    colisao = Colisao(ret)

    # Inicializando a lib de fontes
    # pygame.font.init()

    # Mantém a tela aberta até clicar no botão de fechar. 
    while sair == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True

        move_ret_por_botoes(event, ret)

        # Aqui o relógio define que a tela atualizará a 27 frames por segundo
        relogio.tick(27)

        configura_tela(sup_azul, sup_verde, tela)

        colisao.set_posicao_anterior(ret.left, ret.top)

        (ret.left, ret.top) = pygame.mouse.get_pos()
        # Segue o mouse
        ret.left -= ret.width / 2
        ret.top -= ret.height / 2

        if colisao.verificar_colisao(ret2):
            texto = fonte_perdeu.render('COLIDIU', 1, (cor_vermelha))
            tela.blit(texto, (150, 150))
            sons.get_explodir().play()
            colisao.voltar_para_posicao_anterior()

        pygame.draw.rect(tela, cor_vermelha, ret)
        pygame.draw.rect(tela, cor_rosa, ret2)

        # Atualiza a tela
        pygame.display.update()

    # Encerra 
    pygame.quit()


def configura_tela(sup_azul, sup_verde, tela):
    # Define a cor de fundo da tela como branca
    tela.fill(cor_branca)

    # Coloca as superfices na tela nas respectivas posições
    tela.blit(sup_azul, [50, 50])
    tela.blit(sup_verde, [250, 50])
    tela.blit(sup_verde, [250, 150])


def move_ret_por_botoes(event, ret):
    """

        https://www.pygame.org/docs/ref/key.html
    """

    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.mouse.set_pos(150, 150)

    # if event.type == pygame.MOUSEMOTION:
    #     ret = ret.move(-10, -10)
    #

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


main()
