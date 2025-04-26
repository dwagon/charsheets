import unittest

from charsheets.character import Character, Character2014
from charsheets.constants import DamageType, Language, Stat, Feature, Tool
from charsheets.race2014 import Gnome, RockGnome, ForestGnome
from charsheets.spell import Spell
from tests.dummy import DummyOrigin, DummyBackground


#######################################################################
class TestGnome(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_gnome",
            DummyBackground(),
            Gnome(),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_stats(self):
        self.assertEqual(self.c.speed.value, 25)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 10)
        self.assertEqual(int(self.c.stats[Stat.INTELLIGENCE].value), 12)
        self.assertEqual(int(self.c.stats[Stat.CHARISMA].value), 10)
        self.assertIn(Language.GNOMISH, self.c.languages)
        self.assertTrue(self.c.find_feature(Feature.GNOMISH_CUNNING14))
        self.assertTrue(self.c.find_feature(Feature.DARKVISION60))


#######################################################################
class TestForestGnome(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_gnome",
            DummyBackground(),
            ForestGnome(),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_stats(self):
        self.assertEqual(self.c.speed.value, 25)
        self.assertEqual(int(self.c.stats[Stat.DEXTERITY].value), 11)
        self.assertEqual(int(self.c.stats[Stat.INTELLIGENCE].value), 12)
        self.assertEqual(int(self.c.stats[Stat.CHARISMA].value), 10)
        self.assertTrue(self.c.find_feature(Feature.NATURAL_ILLUSIONIST14))
        self.assertTrue(self.c.find_feature(Feature.SPEAK_WITH_SMALL_BEASTS14))
        self.assertIn(Spell.MINOR_ILLUSION, self.c.known_spells)


#######################################################################
class TestRockGnome(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_gnome",
            DummyBackground(),
            RockGnome(),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_stats(self):
        self.assertEqual(self.c.speed.value, 25)
        self.assertEqual(int(self.c.stats[Stat.DEXTERITY].value), 10)
        self.assertEqual(int(self.c.stats[Stat.INTELLIGENCE].value), 12)
        self.assertEqual(int(self.c.stats[Stat.CHARISMA].value), 10)
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 11)

        self.assertTrue(self.c.find_feature(Feature.ARTIFICERS_LORE14))
        self.assertTrue(self.c.find_feature(Feature.TINKER14))
        self.assertIn(Tool.TINKERS_TOOLS, self.c.tool_proficiencies)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
