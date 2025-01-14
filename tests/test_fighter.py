import unittest

from charsheets.classes import (
    Fighter,
    FighterEldritchKnight,
    FighterChampion,
    FighterPsiWarrior,
    FighterBattleMaster,
    Parry,
)
from charsheets.constants import Skill, Stat, Ability, Proficiency, Tool
from charsheets.exception import InvalidOption
from charsheets.feats import AbilityScoreImprovement
from charsheets.main import render
from charsheets.spells import Spells
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestFighter(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Fighter(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERSUASION,
            Skill.ANIMAL_HANDLING,
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=8,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_fighter(self):
        self.assertEqual(self.c.hit_dice, 10)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CONSTITUTION))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIsNone(self.c.spell_casting_ability)
        self.assertEqual(self.c.spell_slots(1), 0)

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_ability(Ability.SECOND_WIND))
        self.assertEqual(int(self.c.hp), 10 + 1)  # 1 for CON

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 10 + 2)  # 2 for CON
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_ability(Ability.WEAPON_MASTERY))
        self.assertTrue(self.c.has_ability(Ability.ACTION_SURGE))
        self.assertTrue(self.c.has_ability(Ability.TACTICAL_MIND))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertEqual(self.c.level, 5)
        self.assertTrue(self.c.has_ability(Ability.TACTICAL_SHIFT))
        self.assertTrue(self.c.has_ability(Ability.EXTRA_ATTACK))

    ###################################################################
    def test_level6(self):
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 15)
        self.c.level6(hp=5, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION, self.c))
        self.assertEqual(self.c.level, 6)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 16)
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 14)
        self.assertIn("feat ability_score_improvement (1)", self.c.stats[Stat.STRENGTH].value.reason)
        self.assertIn("Base (15)", self.c.stats[Stat.STRENGTH].value.reason)

        with self.assertRaises(InvalidOption):
            self.c.level6(hp=6)

    ###################################################################
    def test_champion(self):

        self.c = FighterChampion(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERCEPTION,
            Skill.ACROBATICS,
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=8,
            wisdom=10,
            charisma=12,
        )
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_ability(Ability.IMPROVED_CRITICAL))
        self.assertTrue(self.c.has_ability(Ability.REMARKABLE_ATHLETE))


###################################################################
class TestPsiWarrior(unittest.TestCase):

    def setUp(self):
        self.c = FighterPsiWarrior(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.SURVIVAL,
            Skill.ANIMAL_HANDLING,
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=8,
            wisdom=10,
            charisma=12,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_ability(Ability.PSIONIC_POWER_FIGHTER))

        self.assertEqual(self.c.energy_dice, "4 x d6")


###################################################################
class TestEldritchKnight(unittest.TestCase):
    def setUp(self):
        self.c = FighterEldritchKnight(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ATHLETICS,
            Skill.ANIMAL_HANDLING,
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=8,
            wisdom=10,
            charisma=12,
        )
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertTrue(self.c.has_ability(Ability.WAR_BOND))

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.spell_casting_ability, Stat.INTELLIGENCE)
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\SpellSaveDC{9}", output)  # default 8 + 2 prof -1 for low int
        self.assertIn(r"\FirstLevelSpellSlotsTotal{1}", output)
        self.assertIn(r"\SpellcastingAbility{Intelligence}", output)
        self.assertIn(r"\SpellcastingClass{Eldritch Knight 3}", output)

        self.assertEqual(self.c.max_spell_level(), 1)

    ###################################################################
    def test_learn_spells(self):
        self.c.learn_spell(Spells.JUMP, Spells.FRIENDS)
        self.c.prepare_spells(Spells.JUMP, Spells.FRIENDS)
        self.assertIn(Spells.JUMP, self.c.known_spells)
        self.assertIn(Spells.JUMP, self.c.prepared_spells)
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\CantripSlotA{Friends}", output)
        self.assertIn(r"\FirstLevelSpellSlotA{Jump}", output)
        self.assertIn(r"\FirstLevelSpellSlotAPrepared{True}", output)


###################################################################
class TestBattleMaster(unittest.TestCase):
    def setUp(self):
        self.c = FighterBattleMaster(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ACROBATICS,
            Skill.ANIMAL_HANDLING,
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=8,
            wisdom=10,
            charisma=12,
            student_tool=Tool.LEATHERWORKERS_TOOLS,
            student_skill=Skill.SURVIVAL,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_ability(Ability.COMBAT_SUPERIORITY))
        self.assertIn(Tool.LEATHERWORKERS_TOOLS, self.c.tool_proficiencies)
        self.assertIn(Skill.SURVIVAL, self.c.skills)

    ###################################################################
    def test_student_of_war(self):
        self.assertTrue(self.c.has_ability(Ability.STUDENT_OF_WAR))
        # Need to specify student_tool
        with self.assertRaises(InvalidOption):
            FighterBattleMaster("name", DummyOrigin(), DummySpecies(), Skill.ACROBATICS, Skill.ANIMAL_HANDLING)
        # Need to specify student_skill
        with self.assertRaises(InvalidOption):
            FighterBattleMaster(
                "name",
                DummyOrigin(),
                DummySpecies(),
                Skill.ACROBATICS,
                Skill.ANIMAL_HANDLING,
                student_tool=Tool.LEATHERWORKERS_TOOLS,
            )
        # Need skill to be one of the base
        with self.assertRaises(InvalidOption):
            fighter = FighterBattleMaster(
                "name",
                DummyOrigin(),
                DummySpecies(),
                Skill.ACROBATICS,
                Skill.ANIMAL_HANDLING,
                student_tool=Tool.LEATHERWORKERS_TOOLS,
                student_skill=Skill.ARCANA,
            )
            print(fighter.skills)  # Need to access skills to do the validation

        # Need tool to be an artisan
        with self.assertRaises(InvalidOption):
            fighter = FighterBattleMaster(
                "name",
                DummyOrigin(),
                DummySpecies(),
                Skill.ACROBATICS,
                Skill.ANIMAL_HANDLING,
                student_tool=Tool.DISGUISE_KIT,
                student_skill=Skill.HISTORY,
            )
            print(fighter.tool_proficiencies)  # Need to access tools to do the validation

    ###################################################################
    def test_maneuvers(self):
        self.c.add_maneuver(Parry())
        print(f"DBG {self.c.maneuvers=}")
        self.assertIn("Parry", self.c.class_special)

    ###################################################################
    def test_superiority_dice(self):
        self.assertIn("Superiority Dice: 4", self.c.class_special)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
