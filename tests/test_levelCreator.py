from unittest import TestCase

from core.game_level import LevelCreator


class TestLevelCreator(TestCase):
    def test_load_level_from_file(self):
        lc = LevelCreator()
        ls = lc.load_level_from_file("data/levels/test1.txt")
        self.assertEqual(ls.columns_num, 40)
        self.assertEqual(ls.rows_num, 20)
        self.assertEqual(ls.title, "TEST1")
