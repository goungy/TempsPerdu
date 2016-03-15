import curses


class GameGUI(object):
    def __init__(self, arg):
        self.stdscr = arg
        curses.halfdelay(5)
        begin_x = 0
        begin_y = 2
        height = 5
        width = 40
        self.debug_win = curses.newwin(height, width, begin_y, begin_x)
        self.stop_main_loop = False
        pass

    def update_if_needed(self, game_clock):
        if game_clock:
            pass
        try:
            idx = 0
            while 1:
                idx += 1
                # self.stdscr.clear()
                self.stdscr.addstr(0, 0, "Waiting for your input adventurer[" + str(idx) + "]", curses.color_pair(1))
                self.stdscr.refresh()
                self.debug_win.refresh()
                c = self.stdscr.getch()
                if c == ord('p'):
                    self.debug_win.addstr(1, 0, "Pretty text", curses.color_pair(1))
                    pass
                elif c == ord('q'):
                    self.stop_main_loop = True
                    break  # Exit the while()
                elif c == curses.KEY_HOME:
                    self.debug_win.addstr(1, 0, "Home")
                elif c == curses.KEY_UP:
                    self.debug_win.addstr(1, 0, "Up")
        except curses.error:
            pass
        pass
