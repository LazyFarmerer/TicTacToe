

class Setting:
    """게임의 기본세팅들 다룸\n
    OX 이름 바꾸거나 추가 하는건 Team 값에서 변경"""
    run = True
    WIN_SIZE = 900
    FES = 60
    line_tile_lenth = 3 # 맵 타일 칸의 갯수
    BLACK = (0, 0, 0)
    ACTIVE_COLOR = (144, 144, 144)  # 마우스로 눌렀을 때 색
    INACTIVE_COLOR = (0, 27, 53)  # 기본색
    OUT_LINE_COLOR = (255, 255, 255)
    WIN_LINE_COLOR = (255, 255, 255)
    LINE_WIDTH = 5

    # @property
    # @staticmethod
    # def size():
    #     return Setting.WIN_SIZE // Setting.line_tile_lenth
    # @property
    @classmethod
    def size(cls):
        return cls.WIN_SIZE // cls.line_tile_lenth