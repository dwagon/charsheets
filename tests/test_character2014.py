import unittest
from charsheets.character import Character2014
from charsheets.constants import Stat
from charsheets.race import MountainDwarf


#######################################################################
class TestCharacter2014(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            MountainDwarf(),
            strength=7,
            dexterity=14,
            constitution=8,
            wisdom=20,
            intelligence=5,
            charisma=11,
        )

    def test_stats(self):
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 10)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 8)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
