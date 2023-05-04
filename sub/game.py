
from typing import List, Union

import numpy as np
import pygame
import pygame.font
import pygame.draw
from pygame.surface import Surface

from sub.setting import Setting
from sub.button import Button
from sub.team import TeamController, TeamFild

class Game:
    "아마도 게임 본체"
    def __init__(self, screen: Surface) -> None:
        self.__screen = screen
        self.__line_tile_lenth = Setting.line_tile_lenth

        # self.map_list: list = [[None] * Setting.line_tile_lenth] * Setting.line_tile_lenth
        self.map_list: List[List[Union[Button, TeamFild]]] = np.array([]) # 틱택토 맵 리스트
        self.team = TeamController()

        self.__font_size = round(Setting.WIN_SIZE * 0.3)
        self.__font = pygame.font.Font(None, self.__font_size)

        self.reset()

    def reset(self) -> None:
        "게임 리셋"
        self.win: bool = False # 게임 끝났을 때 true
        self.win_line = [(0,0), (0,0)] # 나중에 ((x, y), (x, y)) 튜플 들어옴, 게임 끝나고 선 긋는 용

        size = Setting.size()
        map_list = []
        for y in range(self.__line_tile_lenth):
            row_list = []
            y = y * size
            for x in range(self.__line_tile_lenth):
                x = x * size
                row_list.append(Button(self.__screen, x, y, size, size))
            map_list.append(row_list)
        self.map_list = np.array(map_list)

    def __text_render(self):
        font = self.__font.render(f"{self.team.team.name} win!!!", True, (255,255,255), Setting.BLACK)
        rect = font.get_rect()
        rect.center = self.__screen.get_rect().center
        self.__screen.blit(font, rect)

    def __win_check(self, rect: pygame.Rect) -> bool:
        """대각선 체크 -> 쳇GPT 고마워
        너 덕분에 넘파이도 써보네"""
        x, y = rect.x, rect.y
        size = Setting.size()
        y = round(y / size)
        x = round(x / size)
        print(x, y)
        if all(self.team.team == i.team for i in self.map_list[:, x]): # type: ignore
            print("x모두 같은거임")
            self.win_line = ((self.map_list[:, x][0].rect.center), (self.map_list[:, x][-1].rect.center)) # type: ignore
            self.win = True
        elif all(self.team.team == i.team for i in self.map_list[y]):
            print("y모두 같은거임")
            self.win_line = ((self.map_list[y][0].rect.center), (self.map_list[y][-1].rect.center))
            self.win = True

        elif all(self.team.team == i.team for i in np.diag(self.map_list)):
            print("대각선 모두 같은거임")
            self.win_line = ((np.diag(self.map_list)[0].rect.center), (np.diag(self.map_list)[-1].rect.center))
            self.win = True
        elif all(self.team.team == i.team for i in np.diag(np.fliplr(self.map_list))):
            print("대각선 반대 모두 같은거임")
            self.win_line = ((np.diag(np.fliplr(self.map_list))[0].rect.center), (np.diag(np.fliplr(self.map_list))[-1].rect.center))
            self.win = True
        else:
            print("게임 안끝남")

        return self.win

    def update(self) -> None:
        # self.__screen.fill((0, 0, 255))

        for y in range(self.__line_tile_lenth):
            for x in range(self.__line_tile_lenth):
                is_active = self.map_list[y][x].update()
                # 만약 게임이 끝났다면
                if self.win:
                    continue
                # 만약 클릭이 활성화 되었다면
                if is_active is not None:
                    self.map_list[y][x] = TeamFild(self.__screen, self.team.team, is_active)
                    if self.__win_check(is_active) is False:
                        self.team.change()
                    # break
        if self.win is True:
            self.__text_render()
            pygame.draw.line(self.__screen, Setting.WIN_LINE_COLOR, *self.win_line, Setting.LINE_WIDTH) # type: ignore

