from enum import Enum


class PlotConst(Enum):
    EMPTY_VALUE = 0

class Color(Enum):
    PLOT_FG_NORMAL = '#ffffff'
    NAME_FG = '#000000'
    NAME_INACTIVE_BG = '#ddddff'
    NAME_ACTIVE_BG = '#aaaaff'
    PLOT_BG = '#001160'
    PLOT_FG_SPECIAL = '#ff8800'

SPACE = ' '
HARD_SPLIT = '#'
SOFT_SPLIT = '|'
DOT = '.'
FONT_NORMAL = 'Courier 16'
FONT_BOLD = 'Courier 16 bold'