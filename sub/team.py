
from random import randint
from enum import Enum, auto

import pygame
import pygame.draw
import pygame.font
from pygame.surface import Surface

from sub.setting import Setting

class Team(Enum):
    O = auto()
    X = auto()

class TeamFild:
    "Button 클릭 시 버튼대신 들어가는 놈"
    def __init__(self, screen: Surface, team: Team, rect: pygame.Rect) -> None:
        self.__screen = screen
        self.team = team
        self.rect = rect
        self.__color = Setting.INACTIVE_COLOR
        self.__out_line_color = Setting.OUT_LINE_COLOR
        self.__line_width = Setting.LINE_WIDTH

        self.__font_size = round(Setting.size() * 0.9)
        self.__font = pygame.font.Font(None, self.__font_size)

    def __text_render(self) -> None:
        font = self.__font.render(self.team.name, True, (255,255,255))
        rect = font.get_rect()
        rect.center = self.rect.center
        self.__screen.blit(font, rect)

    def update(self) -> None:
        pygame.draw.rect(self.__screen, self.__color, self.rect)
        self.__text_render()
        pygame.draw.rect(self.__screen, self.__out_line_color, self.rect, self.__line_width)

class TeamController:
    "Team 이넘값을 컨트롤하기 위한 클래스"
    def __init__(self) -> None:
        self.__team_list = [i for i in Team]
        self.__team_lenth = len(Team)
        self.__index = randint(0, 1)
        self.team = self.__team_list[self.__index]

    def change(self) -> Team:
        self.__index = 0 if self.__team_lenth <= self.__index + 1 else self.__index + 1
        self.team = self.__team_list[self.__index]
        return self.team

    # @property
    # def team(self):
    #     return self.team.value