import unittest

from charsheets.classes import Barbarian, PathOfTheBeserker, PathOfTheWildHeart, PathOfTheWorldTree, PathOfTheZealot
from charsheets.constants import Skill, Stat, Ability, Proficiency
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestFighter(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Barbarian(
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
    def test_basics(self):
        self.assertEqual(self.c.hit_dice, 12)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CONSTITUTION))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())

        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertIn(Ability.UNARMORED_DEFENSE, self.c.class_abilities())
        self.assertIn(Ability.WEAPON_MASTERY, self.c.class_abilities())

        self.assertIn(Ability.RAGE, self.c.class_abilities())

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(self.c.hp, 5 + 12)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertIn(Ability.DANGER_SENSE, self.c.class_abilities())
        self.assertIn(Ability.RECKLESS_ATTACK, self.c.class_abilities())

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)
        self.assertIn(Ability.PRIMAL_KNOWLEDGE, self.c.class_abilities())


###################################################################
class TestBeserker(unittest.TestCase):

    def setUp(self):
        self.c = PathOfTheBeserker(
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
        self.assertIn(Ability.FRENZY, self.c.class_abilities())


###################################################################
class TestWildHeart(unittest.TestCase):
    def setUp(self):
        self.c = PathOfTheWildHeart(
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

    ###################################################################
    def test_basics(self):
        self.assertIn(Ability.ANIMAL_SPEAKER, self.c.class_abilities())
        self.assertIn(Ability.RAGE_OF_THE_WILDS, self.c.class_abilities())


###################################################################
class TestWorldTree(unittest.TestCase):
    def setUp(self):
        self.c = PathOfTheWorldTree(
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
        self.assertIn(Ability.VITALITY_OF_THE_TREE, self.c.class_abilities())


###################################################################
class TestZealot(unittest.TestCase):
    def setUp(self):
        self.c = PathOfTheZealot(
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
        self.assertIn(Ability.DIVINE_FURY, self.c.class_abilities())
        self.assertIn(Ability.WARRIOR_OF_THE_GODS, self.c.class_abilities())


#######################################################################
if __name__ == "__main__":
    unittest.main()


# EOF
