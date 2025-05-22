import unittest

from charsheets.character import Character
from charsheets.constants import Skill, Feature, Language, Stat
from charsheets.exception import InvalidOption
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestDrow(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_drow",
            DummyOrigin(),
            Elf(Lineages.DROW, Skill.INSIGHT, Stat.INTELLIGENCE),
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
            Elf(Lineages.DROW, Skill.ARCANA, Stat.INTELLIGENCE)


#######################################################################
class TestHighElf(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_elf",
            DummyOrigin(),
            Elf(Lineages.HIGH_ELF, Skill.PERCEPTION, Stat.INTELLIGENCE),
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
            Elf(Lineages.WOOD_ELF, Skill.SURVIVAL, Stat.INTELLIGENCE),
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
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
