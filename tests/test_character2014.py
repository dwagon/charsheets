import unittest

from charsheets.character import Character2014
from charsheets.constants import Stat
from tests.dummy import DummyRace, DummyBackground


#######################################################################
class TestCharacter2014(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=10,
            dexterity=10,
            constitution=10,
            wisdom=10,
            intelligence=10,
            charisma=10,
        )

    def test_stats(self):
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 10)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 10)
        self.assertEqual(int(self.c.stats[Stat.CHARISMA].value), 10)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
