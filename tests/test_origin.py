import unittest

from charsheets.character import Character
from charsheets.constants import Stat, Skill, Tool, Language
from charsheets.exception import InvalidOption
from charsheets.features import MagicInitiateCleric, MagicInitiateDruid
from charsheets.origins import Guide
from charsheets.spell import Spell
from tests.dummy import DummyCharClass, DummyOrigin, DummySpecies


#######################################################################
class TestGuide(unittest.TestCase):
    def test_guide(self):
        initiate = MagicInitiateDruid(Stat.WISDOM, Spell.THAUMATURGY, Spell.MESSAGE, Spell.CURE_WOUNDS)
        origin = Guide(Stat.DEXTERITY, Stat.DEXTERITY, Stat.DEXTERITY, initiate)
        self.char = Character(
            "test_char",
            origin,
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=10,
            constitution=10,
            charisma=10,
            intelligence=10,
            dexterity=10,
            wisdom=10,
        )
        self.assertEqual(int(self.char.stats[Stat.DEXTERITY].value), 13)
        self.assertIn(Spell.CURE_WOUNDS, self.char.prepared_spells)
        self.assertIn(Tool.CARTOGRAPHERS_TOOLS, self.char.tool_proficiencies)


#######################################################################
class TestMagicInitiate(unittest.TestCase):
    def test_know_spell(self):
        self.char = Character(
            "test_char",
            DummyOrigin(Stat.STRENGTH, Stat.WISDOM, Stat.WISDOM),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=10,
            dexterity=10,
            constitution=10,
            wisdom=10,
            intelligence=10,
            charisma=10,
        )
        abil = MagicInitiateCleric(Stat.WISDOM, Spell.THAUMATURGY, Spell.MESSAGE, Spell.MAGIC_MISSILE)
        self.char.add_feature(abil)
        self.assertIn(Spell.THAUMATURGY, self.char.known_spells)
        self.assertIn(Spell.MAGIC_MISSILE, self.char.prepared_spells)

        self.assertIn("Spellcasting ability is wisdom", abil.desc)


#######################################################################
class TestOrigin(unittest.TestCase):
    ###################################################################
    def testStatIncrease(self):
        self.char = Character(
            "test_char",
            DummyOrigin(Stat.STRENGTH, Stat.WISDOM, Stat.WISDOM),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=10,
            dexterity=10,
            constitution=10,
            wisdom=10,
            intelligence=10,
            charisma=10,
        )
        self.assertEqual(int(self.char.stats[Stat.STRENGTH].value), 11)
        self.assertEqual(int(self.char.stats[Stat.WISDOM].value), 12)
        self.assertEqual(int(self.char.stats[Stat.INTELLIGENCE].value), 10)

    ###################################################################
    def test_validation(self):
        with self.assertRaises(InvalidOption):
            char = Character(
                "test_char",
                DummyOrigin(Stat.STRENGTH, Stat.DEXTERITY, Stat.WISDOM),
                DummySpecies(),
                Language.ORC,
                Language.GNOMISH,
            )


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
