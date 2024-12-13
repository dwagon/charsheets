import unittest


from charsheets.constants import Skill, Origin, Stat, Ability, CharSubclassName, Proficiencies
from charsheets.classes import Fighter, EldritchKnight, Champion, PsiWarrior, BattleMaster, BattleManeuver
from tests.fixtures import DummySpecies


#######################################################################
class TestDruid(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Fighter(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_fighter(self):
        self.assertEqual(self.c.hit_dice, 10)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CONSTITUTION))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertIn(Proficiencies.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiencies.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertIn(Ability.SECOND_WIND, self.c.class_abilities())

    ###################################################################
    def test_level2(self):
        self.c.add_level(5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(self.c.hp, 5 + 10)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(
            self.c.class_abilities(), {Ability.SECOND_WIND, Ability.WEAPON_MASTERY, Ability.ACTION_SURGE, Ability.TACTICAL_MIND}
        )

    ###################################################################
    def test_level3(self):
        self.c.add_level(5)
        self.c.add_level(6)
        self.assertEqual(self.c.level, 3)

    ###################################################################
    def test_champion(self):

        self.c = Champion(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.add_level(5)
        self.c.add_level(6)
        self.assertEqual(self.c.level, 3)
        self.assertIn(Ability.IMPROVED_CRITICAL, self.c.class_abilities())
        self.assertIn(Ability.REMARKABLE_ATHLETE, self.c.class_abilities())

    ###################################################################
    def test_eldritch_knight(self):

        self.c = EldritchKnight(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.add_level(5)
        self.c.add_level(6)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertIn(Ability.WAR_BOND, self.c.class_abilities())

    ###################################################################
    def test_psi_warrior(self):

        self.c = PsiWarrior(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.add_level(5)
        self.c.add_level(6)
        self.assertEqual(self.c.level, 3)
        self.assertIn(Ability.PSIONIC_POWER, self.c.class_abilities())


###################################################################
class TestBattleMaster(unittest.TestCase):
    def setUp(self):
        self.c = BattleMaster(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.add_level(5)
        self.c.add_level(6)
        self.c.maneuvers = {BattleManeuver.AMBUSH, BattleManeuver.RALLY, BattleManeuver.PARRY}

    def test_basics(self):
        self.assertEqual(self.c.level, 3)
        self.assertIn(Ability.COMBAT_SUPERIORITY, self.c.class_abilities())
        self.assertIn(Ability.STUDENT_OF_WAR, self.c.class_abilities())

    def test_maneuvers(self):
        self.assertIn("Parry", self.c.class_special)

    def test_superiority_dice(self):
        self.assertIn("Superiority Dice: 4", self.c.class_special)


# EOF
