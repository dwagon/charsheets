import unittest

from charsheets.classes import Monk, MonkWarriorOfMercy, MonkWarriorOfTheOpenHand, MonkWarriorOfShadow, MonkWarriorOfTheElements
from charsheets.constants import Skill, Stat, Ability, Proficiency
from charsheets.abilities import AbilityScoreImprovement
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestMonk(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Monk(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ACROBATICS,
            Skill.RELIGION,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_basic(self):
        self.assertEqual(self.c.hit_dice, 8)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.CHARISMA))
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.spell_slots(1), 0)
        self.assertTrue(self.c.has_ability(Ability.MARTIAL_ARTS))
        self.assertTrue(self.c.has_ability(Ability.UNARMORED_DEFENSE_MONK))

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8 + 2)  # 2 for CON
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_ability(Ability.MONKS_FOCUS))
        self.assertTrue(self.c.has_ability(Ability.UNARMORED_MOVEMENT))
        self.assertTrue(self.c.has_ability(Ability.UNCANNY_METABOLISM))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=9)

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_ability(Ability.DEFLECT_ATTACKS))

    ###################################################################
    def test_level4(self):
        self.c.level4(hp=9, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH))

        self.assertEqual(self.c.level, 4)
        self.assertTrue(self.c.has_ability(Ability.SLOW_FALL))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=5 + 6 + 7)

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 0)

        self.assertTrue(self.c.has_ability(Ability.EXTRA_ATTACK))
        self.assertTrue(self.c.has_ability(Ability.STUNNING_STRIKE))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_ability(Ability.EMPOWERED_STRIKES))


#######################################################################
class TestMercy(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = MonkWarriorOfMercy(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ATHLETICS,
            Skill.STEALTH,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertTrue(self.c.has_ability(Ability.HAND_OF_HARM))
        self.assertTrue(self.c.has_ability(Ability.HAND_OF_HEALING))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)
        self.assertTrue(self.c.has_ability(Ability.PHYSICIANS_TOUCH))


#######################################################################
class TestElements(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = MonkWarriorOfTheElements(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.HISTORY,
            Skill.STEALTH,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertTrue(self.c.has_ability(Ability.ELEMENTAL_ATTUNEMENT))
        self.assertTrue(self.c.has_ability(Ability.MANIPULATE_ELEMENTS))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)
        self.assertTrue(self.c.has_ability(Ability.ELEMENTAL_BURST))


#######################################################################
class TestOpenHand(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = MonkWarriorOfTheOpenHand(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.INSIGHT,
            Skill.RELIGION,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertTrue(self.c.has_ability(Ability.OPEN_HAND_TECHNIQUE))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)
        self.assertTrue(self.c.has_ability(Ability.WHOLENESS_OF_BODY))


#######################################################################
class TestShadow(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = MonkWarriorOfShadow(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.HISTORY,
            Skill.ACROBATICS,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertTrue(self.c.has_ability(Ability.SHADOW_ARTS))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)
        self.assertTrue(self.c.has_ability(Ability.SHADOW_STEP))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
