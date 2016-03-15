from sys import exit
from time import sleep

from core.game_level import LevelCreator, GameLevel

MAIN_LOOP_SLEEP_SECONDS = int(1 / 25)

class GameGUI(object):
    def __init__(self):
        pass

    def update_if_needed(self, game_clock):
        print("updating game GUI")
        pass


class GameClock(object):
    def __init__(self, sleep_time):
        self.sleep_time = sleep_time
        pass

    def tick(self):
        sleep(self.sleep_time)


def main():
    lc = LevelCreator()
    gs = lc.load_level_from_file('data/levels/test1.txt')
    gl = GameLevel(gs)
    gl.print()
    gg = GameGUI()
    cl = GameClock(MAIN_LOOP_SLEEP_SECONDS)

    exit(0)
    while True:
        gl.update_if_needed(cl)
        gg.update_if_needed(cl)
        cl.tick()
    pass


main()
