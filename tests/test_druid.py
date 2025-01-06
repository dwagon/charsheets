import unittest


from charsheets.constants import Skill, Stat, Ability, Proficiency
from charsheets.classes import (
    Druid,
    DruidCircleOfTheStars,
    DruidCircleOfTheMoon,
    DruidCircleOfTheSea,
    DruidCircleOfTheLand,
)
from charsheets.abilities import Warden, Magician
from charsheets.spells import Spells
from tests.dummy import DummySpecies, DummyOrigin


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
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertEqual(self.c.spell_casting_ability, Stat.WISDOM)

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertTrue(self.c.has_ability(Ability.DRUIDIC))

        self.c.prepare_spells(Spells.ANIMAL_FRIENDSHIP)
        self.assertIn(Spells.FAERIE_FIRE, self.c.spells_of_level(1))

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_ability(Ability.WILD_SHAPE))
        self.assertTrue(self.c.has_ability(Ability.WILD_COMPANION))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertIn(Spells.HEAT_METAL, self.c.spells_of_level(2))


#######################################################################
class TestCircleOfStars(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DruidCircleOfTheStars(
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
    def test_circle_of_stars(self):
        self.assertTrue(self.c.has_ability(Ability.STAR_MAP))
        self.assertTrue(self.c.has_ability(Ability.STARRY_FORM))

        self.assertIn(Spells.GUIDANCE, self.c.prepared_spells)


#######################################################################
class TestCircleOfLand(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DruidCircleOfTheLand(
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
    def test_circle_of_land(self):
        self.assertTrue(self.c.has_ability(Ability.LANDS_AID))


#######################################################################
class TestCircleOfSea(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DruidCircleOfTheSea(
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
    def test_circle_of_sea(self):

        self.assertTrue(self.c.has_ability(Ability.WRATH_OF_THE_SEA))

        self.assertIn(Spells.THUNDERWAVE, self.c.prepared_spells)


#######################################################################
class TestCircleOfMoon(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DruidCircleOfTheMoon(
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
    def test_circle_of_moon(self):
        self.assertTrue(self.c.has_ability(Ability.CIRCLE_FORMS))
        self.assertIn(Spells.MOONBEAM, self.c.prepared_spells)


#######################################################################
class TestMagician(unittest.TestCase):
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
            intelligence=10,
        )
        self.c.add_ability(Magician())

    ###################################################################
    def test_skills(self):
        self.assertEqual(self.c.arcana.modifier.value, 7)
        self.assertEqual(self.c.arcana.modifier.reason, "proficiency (2) + Magician (5)")
        self.assertEqual(self.c.nature.modifier.value, 5)
        self.assertEqual(self.c.nature.modifier.reason, "Magician (5)")


#######################################################################
class TestWarden(unittest.TestCase):
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
        self.c.add_ability(Warden())

    ###################################################################
    def test_extra_proficiency(self):
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
