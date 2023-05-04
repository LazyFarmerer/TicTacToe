from typing import Optional

import pygame.draw
import pygame.mouse
from pygame.surface import Surface

from sub.setting import Setting

class Button:
    def __init__(self, screen: Surface, x: int, y: int, width: int, height: int) -> None:
        self.__screen = screen
        self.rect = pygame.Rect(x, y, width, height)

        self.__out_line_color = Setting.OUT_LINE_COLOR
        self.__idle_color = Setting.INACTIVE_COLOR
        self.__active_color = Setting.ACTIVE_COLOR
        self.__line_width = Setting.LINE_WIDTH

        self.team = None # 정답 체크용

    def update(self) -> Optional[pygame.Rect]:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed() # type: ignore
        if click[0]:
            if self.rect.collidepoint(mouse):
                pygame.draw.rect(self.__screen, self.__active_color, self.rect)
                return self.action()

        pygame.draw.rect(self.__screen, self.__idle_color, self.rect)
        pygame.draw.rect(self.__screen, self.__out_line_color, self.rect, self.__line_width)

    def action(self) -> pygame.Rect:
        # print(f"({self.x}, {self.y}) 버튼 클릭")
        return self.rect

