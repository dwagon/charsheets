import unittest

from charsheets.character import Character2014
from charsheets.constants import Language, Stat
from charsheets.race2014 import Human as Human14
from tests.dummy import DummyBackground


#######################################################################
class TestHuman(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_human",
            DummyBackground(),
            Human14(Language.ORC),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_stats(self):
        self.assertEqual(self.c.speed.value, 30)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 11)
        self.assertEqual(int(self.c.stats[Stat.DEXTERITY].value), 11)
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 11)
        self.assertEqual(int(self.c.stats[Stat.INTELLIGENCE].value), 11)
        self.assertEqual(int(self.c.stats[Stat.WISDOM].value), 11)
        self.assertEqual(int(self.c.stats[Stat.CHARISMA].value), 11)
        self.assertIn(Language.ORC, self.c.languages)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
