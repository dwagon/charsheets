import unittest

from charsheets.abilities import MagicInitiateCleric, MagicInitiateDruid
from charsheets.constants import Stat, Skill, Tool
from charsheets.exception import InvalidOption
from charsheets.spells import Spells
from charsheets.origins import Guide
from tests.dummy import DummyCharClass, DummyOrigin, DummySpecies


#######################################################################
class TestGuide(unittest.TestCase):
    def test_guide(self):
        initiate = MagicInitiateDruid(Stat.WISDOM, Spells.THAUMATURGY, Spells.MESSAGE, Spells.CURE_WOUNDS)
        origin = Guide(Stat.DEXTERITY, Stat.DEXTERITY, Stat.DEXTERITY, initiate)
        self.char = DummyCharClass(
            "test_char",
            origin,
            DummySpecies(),
            Skill.DECEPTION,
            Skill.PERCEPTION,
            charisma=10,
            dexterity=10,
            wisdom=10,
        )
        self.assertEqual(int(self.char.stats[Stat.DEXTERITY].value), 13)
        self.assertIn(Spells.CURE_WOUNDS, self.char.prepared_spells)
        self.assertIn(Tool.CARTOGRAPHERS_TOOLS, self.char.tool_proficiencies)


#######################################################################
class TestMagicInitiate(unittest.TestCase):
    def test_know_spell(self):
        self.char = DummyCharClass(
            "test_char",
            DummyOrigin(Stat.STRENGTH, Stat.WISDOM, Stat.WISDOM),
            DummySpecies(),
            Skill.DECEPTION,
            Skill.PERCEPTION,
            strength=10,
            wisdom=10,
            intelligence=10,
        )
        abil = MagicInitiateCleric(Stat.WISDOM, Spells.THAUMATURGY, Spells.MESSAGE, Spells.MAGIC_MISSILE)
        self.char.add_ability(abil)
        self.assertIn(Spells.THAUMATURGY, self.char.known_spells)
        self.assertIn(Spells.MAGIC_MISSILE, self.char.prepared_spells)

        self.assertIn("Spellcasting ability is wisdom", abil.desc)


#######################################################################
class TestOrigin(unittest.TestCase):
    ###################################################################
    def testStatIncrease(self):
        self.char = DummyCharClass(
            "test_char",
            DummyOrigin(Stat.STRENGTH, Stat.WISDOM, Stat.WISDOM),
            DummySpecies(),
            Skill.DECEPTION,
            Skill.PERCEPTION,
            strength=10,
            wisdom=10,
            intelligence=10,
        )
        self.assertEqual(int(self.char.stats[Stat.STRENGTH].value), 11)
        self.assertEqual(int(self.char.stats[Stat.WISDOM].value), 12)
        self.assertEqual(int(self.char.stats[Stat.INTELLIGENCE].value), 10)

    ###################################################################
    def test_validation(self):
        with self.assertRaises(InvalidOption):
            char = DummyCharClass(
                "test_char",
                DummyOrigin(Stat.STRENGTH, Stat.DEXTERITY, Stat.WISDOM),
                DummySpecies(),
                Skill.DECEPTION,
                Skill.PERCEPTION,
            )


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
