import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Iniciando com Pygame")
    tela = pygame.display.set_mode([300, 300])
    relogio = pygame.time.Clock()
    sair = False
    cor_branca = (255, 255, 255)
    cor_azul = (108, 194, 236)
    cor_verde = (152, 231, 114)
    sup = pygame.Surface((200, 200))
    sup.fill(cor_azul)

    while sair == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        relogio.tick(27)
        tela.fill(cor_branca)
        tela.blit(sup, [50, 50])

        pygame.display.update()
    pygame.quit()


main()
