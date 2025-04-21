import unittest

from charsheets.character import Character
from charsheets.classes import (
    Fighter,
    FighterEldritchKnight,
    FighterChampion,
    FighterPsiWarrior,
    FighterBattleMaster,
    Parry,
    StudentOfWar,
    Rally,
    BaitAndSwitch,
    Riposte,
)
from charsheets.constants import Skill, Stat, Feature, Proficiency, Tool, DamageType, Language
from charsheets.exception import InvalidOption
from charsheets.features import AbilityScoreImprovement, ThrownWeaponFighting, BlindFighting, Archery, Defense, BoonOfCombatProwess
from charsheets.main import render
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin, DummyCharClass


#######################################################################
class TestFighter(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=8,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.c.add_level(Fighter(hp=1, style=Defense()))
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())

    ###################################################################
    def test_no_style(self):
        with self.assertRaises(InvalidOption):
            self.c.add_level(Fighter(skills=[]))

    ###################################################################
    def test_fighter(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.assertEqual(self.c.level, 1)
        self.assertTrue(self.c.has_feature(Feature.SECOND_WIND))
        self.assertEqual(int(self.c.hp), 10 + 1)  # 1 for CON
        self.assertEqual(self.c.max_hit_dice, "1d10")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CONSTITUTION))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIsNone(self.c.spell_casting_ability)
        self.assertEqual(self.c.spell_slots(1), 0)

    ###################################################################
    def test_level2(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=5))
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 10 + 2)  # 2 for CON
        self.assertTrue(self.c.has_feature(Feature.WEAPON_MASTERY))
        self.assertTrue(self.c.has_feature(Feature.ACTION_SURGE))
        self.assertTrue(self.c.has_feature(Feature.TACTICAL_MIND))

    ###################################################################
    def test_level3(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.level, 3)

    ###################################################################
    def level4(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=Archery()))

    ###################################################################
    def test_level5(self):
        self.level4()
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.level, 5)
        self.assertTrue(self.c.has_feature(Feature.TACTICAL_SHIFT))
        self.assertTrue(self.c.has_feature(Feature.EXTRA_ATTACK))

    ###################################################################
    def test_level6(self):
        self.level4()
        self.c.add_level(Fighter(hp=1))
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 15)

        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))

        self.assertEqual(self.c.level, 6)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 16)
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 14)
        self.assertIn("AbilityScoreImprovement (1)", self.c.stats[Stat.STRENGTH].value.reason)
        self.assertIn("Base (15)", self.c.stats[Stat.STRENGTH].value.reason)

    ###################################################################
    def test_fighting_style(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=ThrownWeaponFighting()))
        self.assertTrue(self.c.has_feature(Feature.THROWN_WEAPON_FIGHTING))
        self.c.add_level(Fighter(hp=1, remove_style=ThrownWeaponFighting(), add_style=Defense()))
        self.assertFalse(self.c.has_feature(Feature.THROWN_WEAPON_FIGHTING))
        self.assertTrue(self.c.has_feature(Feature.DEFENSE))

    ###################################################################
    def test_weapon_mastery(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))

        self.assertEqual(self.c.fighter.num_weapon_mastery, 3)

        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=Archery()))
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.fighter.num_weapon_mastery, 4)

        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.fighter.num_weapon_mastery, 5)

    ###################################################################
    def test_level7(self):
        self.level4()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.level, 7)
        sw = self.c.find_feature(Feature.SECOND_WIND)
        self.assertEqual(sw.goes, 3)

    ###################################################################
    def level8(self):
        self.level4()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))

    ###################################################################
    def test_level9(self):
        self.level8()
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.level, 9)
        self.assertTrue(self.c.has_feature(Feature.INDOMITABLE))
        self.assertTrue(self.c.has_feature(Feature.TACTICAL_MASTER))
        i = self.c.find_feature(Feature.INDOMITABLE)
        self.assertEqual(i.goes, 1)

    ###################################################################
    def test_level10(self):
        self.level8()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.level, 10)
        sw = self.c.find_feature(Feature.SECOND_WIND)
        self.assertEqual(sw.goes, 4)

    ###################################################################
    def test_level11(self):
        self.level8()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1))
        self.assertIn("twice", self.c.extra_attacks[0])

        self.c.add_level(Fighter(hp=1))
        self.assertEqual(self.c.level, 11)
        self.assertIn("three times", self.c.extra_attacks[0])

    ###################################################################
    def level12(self):
        self.level8()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))

    ###################################################################
    def test_level13(self):
        self.level12()
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertTrue(self.c.has_feature(Feature.STUDIED_ATTACKS))
        i = self.c.find_feature(Feature.INDOMITABLE)
        self.assertEqual(i.goes, 2)

    ###################################################################
    def test_level14(self):
        self.level12()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))

        self.assertEqual(self.c.level, 14)

    ###################################################################
    def test_level15(self):
        self.level12()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.level, 15)

    ###################################################################
    def test_level16(self):
        self.level12()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))

        self.assertEqual(self.c.level, 16)

    ###################################################################
    def test_level17(self):
        self.level12()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.level, 17)
        asurge = self.c.find_feature(Feature.ACTION_SURGE)
        self.assertEqual(asurge.goes, 2)
        indom = self.c.find_feature(Feature.INDOMITABLE)
        self.assertEqual(indom.goes, 3)

    ###################################################################
    def test_level18(self):
        self.level12()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.level, 18)

    ###################################################################
    def test_level19(self):
        self.level12()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, boon=BoonOfCombatProwess(Stat.STRENGTH)))

        self.assertEqual(self.c.level, 19)

    ###################################################################
    def test_level20(self):
        self.level12()
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(Fighter(hp=1, boon=BoonOfCombatProwess(Stat.STRENGTH)))
        self.c.add_level(Fighter(hp=1))

        self.assertEqual(self.c.level, 20)
        self.assertIn("four times", self.c.extra_attacks[0])


###################################################################
class TestBattleMaster(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "Ms Battlemaster",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
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
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, student=StudentOfWar(Tool.LEATHERWORKERS_TOOLS, Skill.HISTORY)))

        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_feature(Feature.COMBAT_SUPERIORITY))
        self.assertEqual(self.c.fighter.num_superiority_dice, 4)
        self.assertEqual(self.c.fighter.type_superiority_dice, "d8")

    ###################################################################
    def test_combat_superiorty(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, student=StudentOfWar(Tool.LEATHERWORKERS_TOOLS, Skill.HISTORY)))

        cs = self.c.find_feature(Feature.COMBAT_SUPERIORITY)
        self.assertIn("You have 4 Superiority", cs.desc)
        self.assertEqual(cs.goes, 4)

    ###################################################################
    def test_student_of_war(self):

        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, student=StudentOfWar(Tool.LEATHERWORKERS_TOOLS, Skill.HISTORY)))
        self.assertTrue(self.c.has_feature(Feature.STUDENT_OF_WAR))
        self.assertIn(Tool.LEATHERWORKERS_TOOLS, self.c.tool_proficiencies)
        self.assertIn(Skill.SURVIVAL, self.c.skills)

    ###################################################################
    def test_maneuvers(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(
            FighterBattleMaster(
                hp=1,
                student=StudentOfWar(Tool.LEATHERWORKERS_TOOLS, Skill.HISTORY),
                add_maneuver=[Parry(), Rally(), BaitAndSwitch()],
            )
        )

        self.assertIn("Parry", self.c.class_special)
        self.assertIn("Rally", self.c.class_special)

        self.c.add_level(FighterBattleMaster(hp=1, feat=Archery(), remove_maneuver=Parry()))
        self.assertNotIn("Parry", self.c.class_special)
        self.assertIn("Rally", self.c.class_special)

        with self.assertRaises(InvalidOption):
            self.c.add_level(FighterBattleMaster(hp=1, remove_maneuver=Riposte()))

    ###################################################################
    def test_superiority_dice(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, student=StudentOfWar(Tool.LEATHERWORKERS_TOOLS, Skill.HISTORY)))

        self.assertIn("Superiority Dice: 4", self.c.class_special)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, student=StudentOfWar(Tool.LEATHERWORKERS_TOOLS, Skill.HISTORY)))
        self.c.add_level(FighterBattleMaster(hp=1, feat=Archery()))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertTrue(self.c.has_feature(Feature.KNOW_YOUR_ENEMY))

    ###################################################################
    def test_level10(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterBattleMaster(hp=3, student=StudentOfWar(Tool.LEATHERWORKERS_TOOLS, Skill.HISTORY)))
        self.c.add_level(FighterBattleMaster(hp=1, feat=Archery()))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertEqual(self.c.fighter.num_superiority_dice, 5)
        self.assertEqual(self.c.fighter.type_superiority_dice, "d10")

    ###################################################################
    def test_level15(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterBattleMaster(hp=3, student=StudentOfWar(Tool.LEATHERWORKERS_TOOLS, Skill.HISTORY)))
        self.c.add_level(FighterBattleMaster(hp=1, feat=Archery()))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))

        self.assertEqual(self.c.level, 15)
        self.assertEqual(self.c.fighter.num_superiority_dice, 6)
        self.assertEqual(self.c.fighter.type_superiority_dice, "d10")
        self.assertTrue(self.c.has_feature(Feature.RELENTLESS))

    ###################################################################
    def test_level18(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterBattleMaster(hp=3, student=StudentOfWar(Tool.LEATHERWORKERS_TOOLS, Skill.HISTORY)))
        self.c.add_level(FighterBattleMaster(hp=1, feat=Archery()))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterBattleMaster(hp=1))
        self.c.add_level(FighterBattleMaster(hp=1))

        self.assertEqual(self.c.level, 18)
        self.assertEqual(self.c.fighter.num_superiority_dice, 6)
        self.assertEqual(self.c.fighter.type_superiority_dice, "d12")


#######################################################################
class TestChampion(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=8,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterChampion(hp=1))

        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_feature(Feature.IMPROVED_CRITICAL))
        self.assertTrue(self.c.has_feature(Feature.REMARKABLE_ATHLETE))
        self.assertTrue(self.c.has_feature(Feature.FIGHTING_STYLE_FIGHTER))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=Archery()))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.assertFalse(self.c.has_feature(Feature.BLIND_FIGHTING))

        self.c.add_level(FighterChampion(hp=1, style=BlindFighting()))

        self.assertEqual(self.c.level, 7)
        self.assertTrue(self.c.has_feature(Feature.BLIND_FIGHTING))
        self.assertTrue(self.c.has_feature(Feature.DEFENSE))

    ###################################################################
    def test_level10(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=Archery()))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterChampion(hp=1, style=BlindFighting()))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertTrue(self.c.has_feature(Feature.HEROIC_WARRIOR))

    ###################################################################
    def test_level15(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=Archery()))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterChampion(hp=1, style=BlindFighting()))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterChampion(hp=1))

        self.assertEqual(self.c.level, 15)
        self.assertTrue(self.c.has_feature(Feature.SUPERIOR_CRITICAL))

    ###################################################################
    def test_level18(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=Archery()))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterChampion(hp=1, style=BlindFighting()))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterChampion(hp=1))
        self.c.add_level(FighterChampion(hp=1))

        self.assertEqual(self.c.level, 18)
        self.assertTrue(self.c.has_feature(Feature.SURVIVOR))


###################################################################
class TestEldritchKnight(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=8,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))

        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_feature(Feature.WAR_BOND))
        self.assertEqual(self.c.spell_casting_ability, Stat.INTELLIGENCE)
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\SpellSaveDC{9}", output)  # default 8 + 2 prof -1 for low int
        self.assertIn(r"\FirstLevelSpellSlotsTotal{1}", output)
        self.assertIn(r"\SpellcastingAbility{Intelligence}", output)

    ###################################################################
    def test_learn_spells(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))

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
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=Archery()))
        self.c.add_level(FighterEldritchKnight(hp=1))

        self.assertEqual(self.c.spell_slots(1), 3)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=Archery()))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.assertEqual(self.c.spell_slots(1), 3)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=Archery()))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)

        self.assertTrue(self.c.has_feature(Feature.WAR_MAGIC))

    ###################################################################
    def test_level10(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=Archery()))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)

        self.assertTrue(self.c.has_feature(Feature.ELDRITCH_STRIKE))

    ###################################################################
    def test_level13(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=Archery()))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)

    ###################################################################
    def test_level15(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=Archery()))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))

        self.assertEqual(self.c.level, 15)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)

        self.assertTrue(self.c.has_feature(Feature.ARCANE_CHARGE))

    ###################################################################
    def test_level18(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=Archery()))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterEldritchKnight(hp=1))
        self.c.add_level(FighterEldritchKnight(hp=1))

        self.assertEqual(self.c.level, 18)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)

        self.assertTrue(self.c.has_feature(Feature.IMPROVED_WAR_MAGIC))


###################################################################
class TestPsiWarrior(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=8,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_feature(Feature.PSIONIC_POWER_FIGHTER))

        self.assertEqual(self.c.fighter.energy_dice, "4 x d6")

    ###################################################################
    def test_level5(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=Archery()))
        self.c.add_level(FighterPsiWarrior(hp=1))

        self.assertEqual(self.c.fighter.energy_dice, "6 x d8")

    ###################################################################
    def test_level7(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=Archery()))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertTrue(self.c.has_feature(Feature.TELEKINETIC_ADEPT))
        ta = self.c.find_feature(Feature.TELEKINETIC_ADEPT)
        expected_dc = 8 + self.c.intelligence.modifier + self.c.proficiency_bonus
        self.assertIn(f"DC {expected_dc}", ta.desc)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=Archery()))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))

        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.fighter.energy_dice, "8 x d8")

    ###################################################################
    def test_level10(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=Archery()))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertTrue(self.c.has_feature(Feature.GUARDED_MIND))
        self.assertIn(DamageType.PSYCHIC, self.c.damage_resistances)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=Archery()))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.fighter.energy_dice, "10 x d10")

    ###################################################################
    def test_level15(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=Archery()))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))

        self.assertEqual(self.c.level, 15)
        self.assertTrue(self.c.has_feature(Feature.BULWARK_OF_FORCE))

    ###################################################################
    def test_level18(self):
        self.c.add_level(Fighter(skills=[Skill.PERSUASION, Skill.ANIMAL_HANDLING], style=Defense()))
        self.c.add_level(Fighter(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=Archery()))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(FighterPsiWarrior(hp=1))
        self.c.add_level(FighterPsiWarrior(hp=1))

        self.assertEqual(self.c.level, 18)
        self.assertTrue(self.c.has_feature(Feature.TELEKINETIC_MASTER))
        self.assertEqual(self.c.fighter.energy_dice, "12 x d12")


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
