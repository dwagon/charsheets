import unittest


from charsheets.constants import Skill, Origin, Stat, Ability, Proficiencies
from charsheets.classes import Barbarian, PathOfTheBeserker, PathOfTheWildHeart, PathOfTheWorldTree, PathOfTheZealot
from charsheets.spells import Spells
from tests.fixtures import DummySpecies
from charsheets.main import render


#######################################################################
class TestFighter(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Barbarian(
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
    def test_basics(self):
        self.assertEqual(self.c.hit_dice, 12)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CONSTITUTION))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertNotIn(Proficiencies.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiencies.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiencies.SHIELDS, self.c.armour_proficiencies())

        self.assertIn(Proficiencies.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiencies.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertIn(Ability.UNARMORED_DEFENSE, self.c.class_abilities())
        self.assertIn(Ability.WEAPON_MASTERY, self.c.class_abilities())

        self.assertIn(Ability.RAGE, self.c.class_abilities())

    ###################################################################
    def test_level2(self):
        self.c.add_level(5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(self.c.hp, 5 + 12)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertIn(Ability.DANGER_SENSE, self.c.class_abilities())
        self.assertIn(Ability.RECKLESS_ATTACK, self.c.class_abilities())

    ###################################################################
    def test_level3(self):
        self.c.add_level(5)
        self.c.add_level(6)
        self.assertEqual(self.c.level, 3)
        self.assertIn(Ability.PRIMAL_KNOWLEDGE, self.c.class_abilities())


###################################################################
class TestBeserker(unittest.TestCase):

    def setUp(self):
        self.c = PathOfTheBeserker(
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

    ###################################################################
    def test_basics(self):
        self.assertIn(Ability.FRENZY, self.c.class_abilities())


###################################################################
class TestWildHeart(unittest.TestCase):
    def setUp(self):
        self.c = PathOfTheWildHeart(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=10,
        )
        self.c.add_level(5)
        self.c.add_level(6)
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

    ###################################################################
    def test_basics(self):
        self.assertIn(Ability.VITALITY_OF_THE_TREE, self.c.class_abilities())


###################################################################
class TestZealot(unittest.TestCase):
    def setUp(self):
        self.c = PathOfTheZealot(
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

    ###################################################################
    def test_basics(self):
        self.assertIn(Ability.DIVINE_FURY, self.c.class_abilities())
        self.assertIn(Ability.WARRIOR_OF_THE_GODS, self.c.class_abilities())


# EOF
