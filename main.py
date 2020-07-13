import pygame

class Farben:
    ORANGE = 255, 140, 0
    GELB = 127, 127, 0
    ROT = 255, 0, 0
    GRUEN = 0, 255, 0
    SCHWARZ = 0, 0, 0
    WEISS = 255, 255, 255


def mainloop():
    pygame.init()

    width, height = 800, 600

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mein erstes Pygame-Spiel")

    clock = pygame.time.Clock()

    spiel_aktiv = True
    while spiel_aktiv:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spiel_aktiv = False
                print("Spieler hat den Quit-Button angeclickt.")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.key == pygame.K_RIGHT:
                    print("Spieler hat Pfeiltaste rechts gedrückt.")
                elif event.key == pygame.K_LEFT:
                    print("Spieler hat Pfeiltaste links gedrückt.")
                elif event.key == pygame.K_UP:
                    print("Spieler hat Pfeiltaste oben gedrückt.")
                elif event.key == pygame.K_DOWN:
                    print("Spieler hat Pfeiltaste unten gedrückt.")
                elif event.key == pygame.K_SPACE:
                    print("Spieler hat Leertaste gedrückt.")
                else:
                    pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Spieler hat Mousebutton gedrückt.")
            else:
                pass


        # Hier kann man spielen ...
        screen.fill(Farben.SCHWARZ)
        pygame.draw.rect(screen, Farben.GELB, [1, 20, 11, 11], 10)


        
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

    return 'Fertig'


if __name__ == "__main__":
    print (mainloop())