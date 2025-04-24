import unittest

from charsheets.character import Character, Character2014
from charsheets.constants import Skill, Feature, Language, Stat
from charsheets.exception import InvalidOption
from charsheets.race2014 import HighElf, WoodElf, Drow
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell
from tests.dummy import DummyCharClass, DummyOrigin, DummyBackground


#######################################################################
class TestDrow(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_drow",
            DummyOrigin(),
            Elf(Lineages.DROW, Skill.INSIGHT),
            Language.ORC,
            Language.GNOMISH,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_spell(self):
        self.assertIn(Spell.DANCING_LIGHTS, self.c.known_spells)
        self.c.add_level(DummyCharClass(skills=[]))
        self.c.add_level(DummyCharClass(hp=1))
        self.c.add_level(DummyCharClass(hp=1))

        self.assertIn(Spell.FAERIE_FIRE, self.c.known_spells)

    ###################################################################
    def test_ability(self):
        self.c.has_feature(Feature.DARKVISION120)
        self.c.has_feature(Feature.TRANCE)
        self.c.has_feature(Feature.FEY_ANCESTRY)

    ###################################################################
    def test_keen_senses(self):
        self.c.has_feature(Feature.KEEN_SENSES)
        self.assertIn(Skill.INSIGHT, self.c.skills)
        with self.assertRaises(InvalidOption):
            Elf(Lineages.DROW, Skill.ARCANA)


#######################################################################
class TestHighElf(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_elf",
            DummyOrigin(),
            Elf(Lineages.HIGH_ELF, Skill.PERCEPTION),
            Language.ORC,
            Language.GNOMISH,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_spell(self):
        self.assertIn(Spell.PRESTIGITATION, self.c.known_spells)
        self.c.add_level(DummyCharClass(skills=[]))
        self.c.add_level(DummyCharClass(hp=1))
        self.c.add_level(DummyCharClass(hp=1))
        self.assertIn(Spell.DETECT_MAGIC, self.c.known_spells)

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 30)

    ###################################################################
    def test_ability(self):
        self.c.has_feature(Feature.DARKVISION60)
        self.c.has_feature(Feature.TRANCE)
        self.c.has_feature(Feature.KEEN_SENSES)
        self.c.has_feature(Feature.FEY_ANCESTRY)


#######################################################################
class TestWoodElf(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_elf",
            DummyOrigin(),
            Elf(Lineages.WOOD_ELF, Skill.SURVIVAL),
            Language.ORC,
            Language.GNOMISH,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 35)

    ###################################################################
    def test_spell(self):
        self.assertIn(Spell.DRUIDCRAFT, self.c.known_spells)
        self.c.add_level(DummyCharClass(skills=[]))
        self.c.add_level(DummyCharClass(hp=1))
        self.c.add_level(DummyCharClass(hp=1))
        self.assertIn(Spell.LONGSTRIDER, self.c.known_spells)

    ###################################################################
    def test_ability(self):
        self.c.has_feature(Feature.DARKVISION60)
        self.c.has_feature(Feature.TRANCE)
        self.c.has_feature(Feature.KEEN_SENSES)
        self.c.has_feature(Feature.FEY_ANCESTRY)


#######################################################################
class TestHighElf14(unittest.TestCase):
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
class TestWoodElf14(unittest.TestCase):
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
class TestDrow14(unittest.TestCase):
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
