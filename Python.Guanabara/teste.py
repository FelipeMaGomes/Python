import sys
import time
import curses
import random
import os


screen = curses.initscr()


screen_x, screen_y = screen.getmaxyx()

'''if screen_x < 24 or screen_y < 81:
    screen.clear()
    curses.edwin()
    print('Tamanho atual do terminhal: {} x {}'. format(screen_x, screen_y))
    print('\n0 seu terminal tem que ter no minimo 24 linhas por  81 colunas.\n')
    print('Reajuste o tamanho do seu terminal para poder jogar... \n')
    sys.exist(0)


screen.notimeout(False)
screen.keypad(True)
screen.clear()

curses.mousemask(curses.ALL_MOUSE_EVENTS)

curses.start_color()
curses.use_deafult_colors()

curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_YELLOW)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)

curses.init_pair(10, curses.COLOR_YELLOW, curses.COLOR_BLACK)
'''