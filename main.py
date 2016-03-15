from curses import wrapper

from core.game_level import LevelCreator, GameLevel
from core.utilities import GameClock
from gui.game_gui import GameGUI

MAIN_LOOP_SLEEP_SECONDS = int(1 / 1)


def main(arg=None):
    lc = LevelCreator()
    gs = lc.load_level_from_file('data/levels/test1.txt')
    gl = GameLevel(gs)
    gl.print()
    gg = GameGUI(arg)
    cl = GameClock(MAIN_LOOP_SLEEP_SECONDS)

    while not gg.stop_main_loop:
        gl.update_if_needed(cl)
        gg.update_if_needed(cl)
        cl.tick()
    pass

wrapper(main)
