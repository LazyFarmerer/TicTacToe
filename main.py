
import pygame
import pygame.display
import pygame.event
import pygame.time
import pygame.mouse

from sub.setting import Setting
from sub.game import Game

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((Setting.WIN_SIZE,)*2)
        self.clock = pygame.time.Clock()

        self.game = Game(self.screen)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Setting.run = False
            if event.type == pygame.KEYDOWN:
                self.game.reset()

    def run(self):
        while Setting.run:
            self.screen.fill((255,255,255))
            self.events()
            self.game.update()

            self.clock.tick(Setting.FES)
            pygame.display.update()

        pygame.quit()
        exit()


if __name__ == "__main__":
    Main().run()