import unittest

from charsheets.classes import Rogue, RogueSoulknife, RogueAssassin, RogueThief, RogueArcaneTrickster
from charsheets.constants import Skill, Stat, Feature, Proficiency, Tool, Language
from charsheets.exception import InvalidOption
from charsheets.features import Expertise
from charsheets.main import render
from charsheets.spell import Spell
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
        with self.assertRaises(InvalidOption):
            self.c.level1(expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING))
        with self.assertRaises(InvalidOption):
            self.c.level1(language=Language.CELESTIAL)

        self.c.level1(expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING), language=Language.CELESTIAL)
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.SNEAK_ATTACK))
        self.assertTrue(self.c.has_feature(Feature.THIEVES_CANT))
        self.assertTrue(self.c.has_feature(Feature.EXPERTISE))
        self.assertTrue(self.c.has_feature(Feature.WEAPON_MASTERY))
        self.assertEqual(self.c.sneak_attack_dmg, 1)
        self.assertEqual(self.c.spell_slots(1), 0)
        self.assertIn(Language.CELESTIAL, self.c.languages)
        self.assertTrue(self.c.skills[Skill.ARCANA].expert)
        self.assertFalse(self.c.skills[Skill.HISTORY].expert)
        self.assertTrue(self.c.skills[Skill.ANIMAL_HANDLING].expert)

    ###################################################################
    def test_level2(self):
        self.c.level1(expertise=Expertise(Skill.ACROBATICS, Skill.ATHLETICS), language=Language.ORC)
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.CUNNING_ACTION))
        self.assertEqual(self.c.sneak_attack_dmg, 1)

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=1, force=True)
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_feature(Feature.STEADY_AIM))
        self.assertEqual(self.c.sneak_attack_dmg, 2)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.sneak_attack_dmg, 3)
        self.assertTrue(self.c.has_feature(Feature.UNCANNY_DODGE))
        self.assertTrue(self.c.has_feature(Feature.CUNNING_STRIKE))
        cs = self.c.find_feature(Feature.CUNNING_STRIKE)
        dc = 8 + self.c.dexterity.modifier + self.c.proficiency_bonus
        self.assertIn(f"DC {dc}", cs.desc)

    ###################################################################
    def test_level6(self):
        with self.assertRaises(InvalidOption):
            self.c.level6(hp=1, force=True)
        self.c.level6(hp=1, force=True, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE))
        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.sneak_attack_dmg, 3)

        self.assertTrue(self.c.has_feature(Feature.EXPERTISE))

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.sneak_attack_dmg, 4)
        self.assertTrue(self.c.has_feature(Feature.EVASION))
        self.assertTrue(self.c.has_feature(Feature.RELIABLE_TALENT))

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.sneak_attack_dmg, 5)


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
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_feature(Feature.MAGE_HAND_LEGERDERMAIN))
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_casting_ability, Stat.INTELLIGENCE)
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\FirstLevelSpellSlotsTotal{2}", output)
        self.assertIn(r"\SpellcastingAbility{Intelligence}", output)
        self.assertIn(r"\SpellcastingClass{Arcane Trickster 3}", output)
        self.assertIn(Spell.MAGE_HAND, self.c.known_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertTrue(self.c.has_feature(Feature.MAGICAL_AMBUSH))


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
        self.c.level3(hp=5 + 6, force=True)
        self.assertEqual(self.c.level, 3)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_feature(Feature.ASSASSINATE))
        self.assertTrue(self.c.has_feature(Feature.ASSASSINS_TOOLS))
        self.assertIn(Tool.POISONERS_KIT, self.c.tool_proficiencies)

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.INFILTRATION_EXPERTISE))


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

    ###################################################################
    def test_basics(self):
        self.c.level3(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.PSYCHIC_BLADES))
        self.assertTrue(self.c.has_feature(Feature.PSIONIC_POWER_ROGUE))
        self.assertEqual(self.c.energy_dice, "4d6")
        self.assertIn("4d6", self.c.class_special)
        ppr = self.c.find_feature(Feature.PSIONIC_POWER_ROGUE)
        self.assertEqual(ppr.goes, 4)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertEqual(self.c.energy_dice, "6d8")

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertEqual(self.c.energy_dice, "8d8")
        self.assertTrue(self.c.has_feature(Feature.SOUL_BLADES))


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
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_feature(Feature.SECOND_STORY_WORK))
        self.assertTrue(self.c.has_feature(Feature.FAST_HANDS))

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.SUPREME_SNEAK))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
