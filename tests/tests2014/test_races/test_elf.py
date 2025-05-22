import unittest

from charsheets.character import Character2014
from charsheets.constants import Feature, Language, Stat
from charsheets.race2014 import HighElf, WoodElf, Drow
from charsheets.spell import Spell
from tests.dummy import DummyBackground


#######################################################################
class TestHighElf(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_elf",
            DummyBackground(),
            HighElf(Spell.FAERIE_FIRE, Language.ORC),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 30)

    ###################################################################
    def test_abilities(self):
        self.assertTrue(self.c.has_feature(Feature.KEEN_SENSES14))
        self.assertTrue(self.c.has_feature(Feature.DARKVISION60))
        self.assertTrue(self.c.has_feature(Feature.FEY_ANCESTRY14))
        self.assertIn(Language.ORC, self.c.languages)

    ###################################################################
    def test_stat(self):
        self.assertTrue(self.c.stats[Stat.INTELLIGENCE], 11)
        self.assertTrue(self.c.stats[Stat.DEXTERITY], 12)


#######################################################################
class TestWoodElf(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_elf",
            DummyBackground(),
            WoodElf(),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 35)

    ###################################################################
    def test_abilities(self):
        self.assertTrue(self.c.has_feature(Feature.MASK_OF_THE_WILD14))
        self.assertTrue(self.c.has_feature(Feature.DARKVISION60))
        self.assertTrue(self.c.has_feature(Feature.FEY_ANCESTRY14))

    ###################################################################
    def test_stat(self):
        self.assertTrue(self.c.stats[Stat.WISDOM], 11)
        self.assertTrue(self.c.stats[Stat.DEXTERITY], 12)


#######################################################################
class TestDrow(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_elf",
            DummyBackground(),
            Drow(),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 30)

    ###################################################################
    def test_abilities(self):
        self.assertTrue(self.c.has_feature(Feature.DROW_MAGIC14))
        self.assertTrue(self.c.has_feature(Feature.DARKVISION120))
        self.assertTrue(self.c.has_feature(Feature.SUNLIGHT_SENSITIVITY14))
        self.assertIn(Spell.DANCING_LIGHTS, self.c.known_spells)

    ###################################################################
    def test_stat(self):
        self.assertTrue(self.c.stats[Stat.CHARISMA], 11)
        self.assertTrue(self.c.stats[Stat.DEXTERITY], 12)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
