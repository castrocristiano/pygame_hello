import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Iniciando com Pygame")
    tela = pygame.display.set_mode([300, 300])
    relogio = pygame.time.Clock()
    sair = False
    cor_branca = (255,255,255)

    while sair == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        relogio.tick(27)
        tela.fill(cor_branca)
        pygame.display.update()
    pygame.quit()

main()