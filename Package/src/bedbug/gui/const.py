from enum import Enum


class PlotConst(Enum):
    EMPTY_VALUE = 0

class Color(Enum):
    PLOT_FG_NORMAL = '#ffffff'
    NAME_FG = '#000000'
    NAME_INACTIVE_BG = '#ddddff'
    NAME_ACTIVE_BG = '#aaaaff'
    PLOT_INACTIVE_BG = '#001160'
    PLOT_ACTIVE_BG = '#0066aa'
    PLOT_FG_SPECIAL = '#ff8800'

SPACE = ' '
HARD_SPLIT = '#'
SOFT_SPLIT = '|'
DOT = '.'
FONT_SIZE = 14
FONT_NORMAL = f'Courier {FONT_SIZE}'
FONT_BOLD = f'Courier {FONT_SIZE} bold'