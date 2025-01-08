import unittest

from charsheets.classes import (
    Rogue,
    RogueSoulknife,
    RogueAssassin,
    RogueThief,
    RogueArcaneTrickster,
)
from charsheets.constants import Skill, Stat, Ability, Proficiency, Tool
from charsheets.main import render
from charsheets.spells import Spells
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestRogue(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Rogue(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERSUASION,
            Skill.ATHLETICS,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.hit_dice, 8)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())

        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertIsNone(self.c.spell_casting_ability)

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_ability(Ability.SNEAK_ATTACK))
        self.assertTrue(self.c.has_ability(Ability.THIEVES_CANT))
        self.assertTrue(self.c.has_ability(Ability.EXPERTISE))
        self.assertTrue(self.c.has_ability(Ability.WEAPON_MASTERY))

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_ability(Ability.CUNNING_ACTION))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_ability(Ability.STEADY_AIM))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertEqual(self.c.level, 5)
        self.assertTrue(self.c.has_ability(Ability.UNCANNY_DODGE))
        self.assertTrue(self.c.has_ability(Ability.CUNNING_STRIKE))


###################################################################
class TestArcaneTrickster(unittest.TestCase):

    def setUp(self):
        self.c = RogueArcaneTrickster(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.SLEIGHT_OF_HAND,
            Skill.INVESTIGATION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=15,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_ability(Ability.MAGE_HAND_LEGERDERMAIN))
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_casting_ability, Stat.INTELLIGENCE)
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\FirstLevelSpellSlotsTotal{2}", output)
        self.assertIn(r"\SpellcastingAbility{Intelligence}", output)
        self.assertIn(r"\SpellcastingClass{Arcane Trickster 3}", output)
        self.assertIn(Spells.MAGE_HAND, self.c.known_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertEqual(self.c.max_spell_level(), 1)


###################################################################
class TestAssassin(unittest.TestCase):
    def setUp(self):
        self.c = RogueAssassin(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.STEALTH,
            Skill.PERCEPTION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=10,
        )
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_ability(Ability.ASSASSINATE))
        self.assertTrue(self.c.has_ability(Ability.ASSASSINS_TOOLS))
        self.assertIn(Tool.POISONERS_KIT, self.c.tool_proficiencies)


###################################################################
class TestSoulKnife(unittest.TestCase):
    def setUp(self):
        self.c = RogueSoulknife(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.STEALTH,
            Skill.SLEIGHT_OF_HAND,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_ability(Ability.PSYCHIC_BLADES))
        self.assertTrue(self.c.has_ability(Ability.PSIONIC_POWER_ROGUE))


###################################################################
class TestThief(unittest.TestCase):
    def setUp(self):
        self.c = RogueThief(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERCEPTION,
            Skill.STEALTH,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_ability(Ability.SECOND_STORY_WORK))
        self.assertTrue(self.c.has_ability(Ability.FAST_HANDS))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
