import unittest


from charsheets.constants import Skill, Stat, Ability, Proficiencies
from charsheets.classes import (
    Druid,
    Magician,
    Warden,
    CircleOfTheStarsDruid,
    CircleOfTheMoonDruid,
    CircleOfTheSeaDruid,
    CircleOfTheLandDruid,
)
from charsheets.spells import Spells
from tests.fixtures import DummySpecies, DummyOrigin


#######################################################################
class TestDruid(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Druid(
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
    def test_druid(self):
        self.assertEqual(self.c.hit_dice, 8)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertNotIn(Proficiencies.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiencies.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertIn(Ability.DRUIDIC, self.c.class_abilities())
        self.c.prepare_spells(Spells.ANIMAL_FRIENDSHIP)
        self.assertIn(Spells.FAERIE_FIRE, self.c.spells_of_level(1))

    ###################################################################
    def test_level2(self):
        self.c.add_level(5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(self.c.hp, 5 + 8)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertEqual(self.c.class_abilities(), {Ability.DRUIDIC, Ability.WILD_SHAPE, Ability.WILD_COMPANION})

    ###################################################################
    def test_level3(self):
        self.c.add_level(5)
        self.c.add_level(6)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertIn(Spells.HEAT_METAL, self.c.spells_of_level(2))


#######################################################################
class TestCircleOfStars(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = CircleOfTheStarsDruid(
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
        self.c.add_level(5)
        self.c.add_level(6)

    ###################################################################
    def test_circle_of_stars(self):
        self.assertIn(Ability.STAR_MAP, self.c.class_abilities())
        self.assertIn(Ability.STARRY_FORM, self.c.class_abilities())
        self.assertIn(Spells.GUIDANCE, self.c.prepared_spells)


#######################################################################
class TestCircleOfLand(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = CircleOfTheLandDruid(
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
        self.c.add_level(5)
        self.c.add_level(6)

    ###################################################################
    def test_circle_of_land(self):
        self.assertIn(Ability.LANDS_AID, self.c.class_abilities())


#######################################################################
class TestCircleOfSea(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = CircleOfTheSeaDruid(
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
        self.c.add_level(5)
        self.c.add_level(6)

    ###################################################################
    def test_circle_of_sea(self):

        self.assertIn(Ability.WRATH_OF_THE_SEA, self.c.class_abilities())
        self.assertIn(Spells.THUNDERWAVE, self.c.prepared_spells)


#######################################################################
class TestCircleOfMoon(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = CircleOfTheMoonDruid(
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
        self.c.add_level(5)
        self.c.add_level(6)

    ###################################################################
    def test_circle_of_moon(self):
        self.assertIn(Ability.CIRCLE_FORMS, self.c.class_abilities())
        self.assertIn(Spells.MOONBEAM, self.c.prepared_spells)


#######################################################################
class TestMagician(unittest.TestCase):
    ###################################################################
    def setUp(self):
        class StarMagician(Magician, CircleOfTheStarsDruid):
            pass

        self.c = StarMagician(
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

    ###################################################################
    def test_skills(self):
        self.assertEqual(self.c.arcana.modifier.value, 3)
        self.assertEqual(self.c.arcana.modifier.reason, "proficiency (2) + magician (1)")
        self.assertEqual(self.c.nature.modifier.value, 1)
        self.assertEqual(self.c.nature.modifier.reason, "magician (1)")


#######################################################################
class TestWarden(unittest.TestCase):
    ###################################################################
    def setUp(self):
        class DruidWarden(Warden, Druid):
            pass

        self.c = DruidWarden(
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
    def test_extra_proficiency(self):
        self.assertIn(Proficiencies.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiencies.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
