import curses
from curses import wrapper
from time import sleep

from core.game_level import LevelCreator, GameLevel

MAIN_LOOP_SLEEP_SECONDS = int(1 / 25)

class GameGUI(object):
    def __init__(self, arg):
        self.stdscr = arg
        pass

    def update_if_needed(self, game_clock):
        print("updating game GUI")
        self.stdscr.refresh()
        self.stdscr.addstr("Pretty text", curses.color_pair(1))
        self.stdscr.refresh()
        self.stdscr.getkey()
        while 1:
            c = self.stdscr.getch()
            if c == ord('p'):
                pass
            elif c == ord('q'):
                break  # Exit the while()
            elif c == curses.KEY_HOME:
                x = y = 0
        pass


class GameClock(object):
    def __init__(self, sleep_time):
        self.sleep_time = sleep_time
        pass

    def tick(self):
        sleep(self.sleep_time)


def main_loop_core_gui(arg=None):
    lc = LevelCreator()
    gs = lc.load_level_from_file('data/levels/test1.txt')
    gl = GameLevel(gs)
    gl.print()
    gg = GameGUI(arg)
    cl = GameClock(MAIN_LOOP_SLEEP_SECONDS)
    while True:
        gl.update_if_needed(cl)
        gg.update_if_needed(cl)
        cl.tick()
    pass


def main(arg=None):
    print(arg)
    main_loop_core_gui(arg)


wrapper(main)
