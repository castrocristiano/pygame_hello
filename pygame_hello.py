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
    # Mantém a tela aberta até clicar no botão de fechar. 
    while sair == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        # Aqui o relógio define que a tela atualizará a 27 frames por segundo
        relogio.tick(27)
        # Define a cor de fundo da tela como branca
        tela.fill(cor_branca)
        # Coloca as superfices na tela nas respectivas posições
        tela.blit(sup_azul, [50, 50])
        tela.blit(sup_verde, [250, 100])
        # Atualiza a tela
        pygame.display.update()
    # Encerra 
    pygame.quit()


main()
