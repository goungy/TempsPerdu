class LevelSettings(object):
    def __init__(self):
        self.rows_num = 0
        self.columns_num = 0
        self.title = "TO BE FILLED"
        pass


class LevelCreator(object):
    def __init__(self):
        self.level_settings = None
        pass

    def interpret_one_arg_line(self, line):
        vn = line[0]
        vv = line[1]
        if vn == 'rows':
            self.level_settings.rows_num = int(vv)
        elif vn == 'columns':
            self.level_settings.columns_num = int(vv)
        elif vn == 'title':
            self.level_settings.title = vv

    def load_level_from_file(self, fullpath):
        self.level_settings = LevelSettings()
        with open(fullpath) as f:
            ln = 1
            for l in f:
                l = l.rstrip()
                if not len(l): ln += 1; continue
                l = l.split(':')
                if len(l) == 2:
                    self.interpret_one_arg_line(l)
                else:
                    print("@", ln, "line:", l)
                    raise BaseException("Unknown variable in file")
                ln += 1
        return self.level_settings


class GameLevel(object):
    def __init__(self, settings):
        self.level_title = settings.title
        self.level_rows_num, self.level_columns_num = settings.rows_num, settings.columns_num
        pass

    def print(self):
        print("Level", self.level_title)
        print("Level rows", self.level_rows_num)
        print("Level columns", self.level_columns_num)

    def update_if_needed(self, game_clock):
        print("updating game level")
        pass
