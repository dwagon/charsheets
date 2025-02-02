import unittest

from charsheets.classes import Fighter, FighterEldritchKnight, FighterChampion, FighterPsiWarrior, FighterBattleMaster, Parry
from charsheets.constants import Skill, Stat, Feature, Proficiency, Tool
from charsheets.exception import InvalidOption
from charsheets.features import AbilityScoreImprovement, ThrownWeaponFighting, BlindFighting
from charsheets.main import render
from charsheets.spell import Spell
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
        self.c.level1()
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.SECOND_WIND))
        self.assertEqual(int(self.c.hp), 10 + 1)  # 1 for CON

    ###################################################################
    def test_level2(self):
        self.c.level1()
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 10 + 2)  # 2 for CON
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.WEAPON_MASTERY))
        self.assertTrue(self.c.has_feature(Feature.ACTION_SURGE))
        self.assertTrue(self.c.has_feature(Feature.TACTICAL_MIND))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=1, force=True)
        self.assertEqual(self.c.level, 3)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertEqual(self.c.level, 5)
        self.assertTrue(self.c.has_feature(Feature.TACTICAL_SHIFT))
        self.assertTrue(self.c.has_feature(Feature.EXTRA_ATTACK))

    ###################################################################
    def test_level6(self):
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 15)
        self.c.level6(hp=5, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION), force=True)
        self.assertEqual(self.c.level, 6)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 16)
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 14)
        self.assertIn("feature ability_score_improvement (1)", self.c.stats[Stat.STRENGTH].value.reason)
        self.assertIn("Base (15)", self.c.stats[Stat.STRENGTH].value.reason)

        with self.assertRaises(InvalidOption):
            self.c.level6(hp=6)

    ###################################################################
    def test_fighting_style(self):
        self.assertFalse(self.c.has_feature(Feature.THROWN_WEAPON_FIGHTING))
        self.c.fighting_style(ThrownWeaponFighting())
        self.assertTrue(self.c.has_feature(Feature.THROWN_WEAPON_FIGHTING))

    ###################################################################
    def test_weapon_mastery(self):
        self.assertEqual(self.c.num_weapon_mastery, 3)
        self.c.level5(hp=1, force=True)
        self.assertEqual(self.c.num_weapon_mastery, 4)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=9, force=True)
        self.assertEqual(self.c.level, 7)


#######################################################################
class TestChampion(unittest.TestCase):
    def setUp(self):
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

    ###################################################################
    def test_basics(self):
        self.c.level3(hp=5 + 6, force=True)
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_feature(Feature.IMPROVED_CRITICAL))
        self.assertTrue(self.c.has_feature(Feature.REMARKABLE_ATHLETE))
        self.assertTrue(self.c.has_feature(Feature.FIGHTING_STYLE_FIGHTER))

    ###################################################################
    def test_level7(self):
        with self.assertRaises(InvalidOption):
            self.c.level7(hp=9, force=True)
        self.assertFalse(self.c.has_feature(Feature.BLIND_FIGHTING))
        self.c.level7(hp=9, style=BlindFighting(), force=True)
        self.assertEqual(self.c.level, 7)
        self.assertTrue(self.c.has_feature(Feature.BLIND_FIGHTING))


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
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_feature(Feature.PSIONIC_POWER_FIGHTER))

        self.assertEqual(self.c.energy_dice, "4 x d6")

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertEqual(self.c.energy_dice, "6 x d8")

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=9, force=True)
        self.assertEqual(self.c.level, 7)
        self.assertTrue(self.c.has_feature(Feature.TELEKINETIC_ADEPT))


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
        self.c.level3(hp=5 + 6, force=True)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertTrue(self.c.has_feature(Feature.WAR_BOND))

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
        self.c.learn_spell(Spell.JUMP, Spell.FRIENDS)
        self.c.prepare_spells(Spell.JUMP, Spell.FRIENDS)
        self.assertIn(Spell.JUMP, self.c.known_spells)
        self.assertIn(Spell.JUMP, self.c.prepared_spells)
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\CantripSlotA{\myspell{Friends}{Ench}{[C]}}", output)
        self.assertIn(r"\FirstLevelSpellSlotA{\myspell{Jump}{Trans}{}}", output)
        self.assertIn(r"\FirstLevelSpellSlotAPrepared{True}", output)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.INTELLIGENCE), force=True)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=9, force=True)
        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)

        self.assertTrue(self.c.has_feature(Feature.WAR_MAGIC))


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

    ###################################################################
    def test_basics(self):
        self.c.level3(hp=1, force=True)
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_feature(Feature.COMBAT_SUPERIORITY))
        self.assertIn(Tool.LEATHERWORKERS_TOOLS, self.c.tool_proficiencies)
        self.assertIn(Skill.SURVIVAL, self.c.skills)
        self.assertEqual(self.c.num_superiority_dice, 4)

    ###################################################################
    def test_combat_superiorty(self):
        self.c.level3(hp=1, force=True)
        cs = self.c.find_feature(Feature.COMBAT_SUPERIORITY)
        self.assertIn("You have 4 Superiority", cs.desc)
        self.assertEqual(cs.goes, 4)

    ###################################################################
    def test_student_of_war(self):
        self.c.level3(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.STUDENT_OF_WAR))
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
        self.assertIn("Parry", self.c.class_special)

    ###################################################################
    def test_superiority_dice(self):
        self.assertIn("Superiority Dice: 4", self.c.class_special)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=9, force=True)
        self.assertEqual(self.c.level, 7)
        self.assertTrue(self.c.has_feature(Feature.KNOW_YOUR_ENEMY))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
