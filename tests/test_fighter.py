import unittest


from charsheets.constants import Skill, Origin, Stat, Ability, Proficiency
from charsheets.classes import Fighter, EldritchKnight, Champion, PsiWarrior, BattleMaster, BattleManeuver
from charsheets.spells import Spells
from tests.dummy import DummySpecies, DummyOrigin
from charsheets.main import render


#######################################################################
class TestFighter(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Fighter(
            "name",
            DummyOrigin(),
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
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_ability(Ability.SECOND_WIND))

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 10)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_ability(Ability.WEAPON_MASTERY))
        self.assertTrue(self.c.has_ability(Ability.ACTION_SURGE))
        self.assertTrue(self.c.has_ability(Ability.TACTICAL_MIND))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)

    ###################################################################
    def test_champion(self):

        self.c = Champion(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_ability(Ability.IMPROVED_CRITICAL))
        self.assertTrue(self.c.has_ability(Ability.REMARKABLE_ATHLETE))


###################################################################
class TestPsiWarrior(unittest.TestCase):

    def setUp(self):
        self.c = PsiWarrior(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_ability(Ability.PSIONIC_POWER))

        self.assertEqual(self.c.energy_dice, "4 x d6")


###################################################################
class TestEldritchKnight(unittest.TestCase):
    def setUp(self):
        self.c = EldritchKnight(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=10,
        )
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertTrue(self.c.has_ability(Ability.WAR_BOND))

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.spell_casting_ability, Stat.INTELLIGENCE)
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\SpellSaveDC{10}", output)  # default 8 + 2 prof
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
        self.c = BattleMaster(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)
        self.c.maneuvers = {BattleManeuver.AMBUSH, BattleManeuver.RALLY, BattleManeuver.PARRY}

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_ability(Ability.COMBAT_SUPERIORITY))
        self.assertTrue(self.c.has_ability(Ability.STUDENT_OF_WAR))

    ###################################################################
    def test_maneuvers(self):
        self.assertIn("Parry", self.c.class_special)

    ###################################################################
    def test_superiority_dice(self):
        self.assertIn("Superiority Dice: 4", self.c.class_special)


#######################################################################
if __name__ == "__main__":
    unittest.main()


# EOF
