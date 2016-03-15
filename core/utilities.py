from time import sleep


class GameClock(object):
    def __init__(self, sleep_time):
        self.sleep_time = sleep_time
        pass

    def tick(self):
        sleep(self.sleep_time)
