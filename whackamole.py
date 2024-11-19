import pygame
import random


def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        molexpos = 0
        moleypos = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousex = event.pos[0]
                    mousey = event.pos[1]
                    newmouse= (mousex//32, mousey//32)
                    if newmouse == (molexpos, moleypos):
                        molexpos = random.randrange(0,20 )
                        moleypos = random.randrange(0,16)
            screen.fill((81, 72, 112))
            for x in range(0,641, 32):
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
            for y in range(0,513, 32):
                pygame.draw.line(screen, "black", (0, y), (640, y))
            screen.blit(mole_image, mole_image.get_rect(topleft=(molexpos*32, moleypos*32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
