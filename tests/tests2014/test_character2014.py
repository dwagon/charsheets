import unittest

from charsheets.character import Character2014
from charsheets.constants import Stat, Weapon
from charsheets.reason import Reason
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

    ###################################################################
    def test_stats(self):
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 10)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 10)
        self.assertEqual(int(self.c.stats[Stat.CHARISMA].value), 10)

    ###################################################################
    def test_specific_weapons(self):
        self.c._specific_weapon_proficiencies = Reason("Foo", Weapon.SHORTSWORD, Weapon.SHORTSWORD, Weapon.LONGBOW)
        ans = self.c.specific_weapon_proficiencies()
        self.assertEqual(len(ans), 2)
        self.assertEqual(ans.count(Weapon.SHORTSWORD), 1)
        self.assertEqual(ans.count(Weapon.LONGBOW), 1)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
