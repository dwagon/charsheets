import unittest

from charsheets.abilities import Warden, Magician
from charsheets.classes import (
    Druid,
    DruidCircleOfTheStars,
    DruidCircleOfTheMoon,
    DruidCircleOfTheSea,
    DruidCircleOfTheLand,
)
from charsheets.constants import Skill, Stat, Ability, Proficiency, Language
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
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
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
    def test_druidic(self):
        self.assertIn(Language.DRUIDIC, self.c.languages)

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8 + 4)  # +4 for CON
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

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=5 + 6 + 1)
        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertIn(Spells.WIND_WALL, self.c.spells_of_level(3))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)
        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)


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
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_circle_of_stars(self):
        self.assertTrue(self.c.has_ability(Ability.STAR_MAP))
        self.assertTrue(self.c.has_ability(Ability.STARRY_FORM))

        self.assertIn(Spells.GUIDANCE, self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=4)
        self.assertIn(Spells.GUIDANCE, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=4)
        self.assertTrue(self.c.has_ability(Ability.COSMIC_OMEN))


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
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_circle_of_land(self):
        self.assertTrue(self.c.has_ability(Ability.LANDS_AID))
        self.assertIn(Spells.BLUR, self.c.prepared_spells)
        self.assertIn(Spells.BURNING_HANDS, self.c.prepared_spells)
        self.assertIn(Spells.FIRE_BOLT, self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=4)
        self.assertIn(Spells.FIREBALL, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=4)
        self.assertTrue(self.c.has_ability(Ability.NATURAL_RECOVERY))


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
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_circle_of_sea(self):
        self.assertTrue(self.c.has_ability(Ability.WRATH_OF_THE_SEA))
        self.assertIn(Spells.THUNDERWAVE, self.c.prepared_spells)

    ###################################################################
    def test_wrath_of_the_sea(self):
        wots = self.c.find_ability(Ability.WRATH_OF_THE_SEA)
        self.assertIn("roll 2d6", wots.desc)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=4)
        self.assertIn(Spells.LIGHTNING_BOLT, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=4)
        self.assertTrue(self.c.has_ability(Ability.AQUATIC_AFFINITY))

    ###################################################################
    def test_aquatic_affinity(self):
        self.c.level6(hp=1)
        self.assertEqual(int(self.c.swim_speed), 30)


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
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_circle_of_moon(self):
        self.assertTrue(self.c.has_ability(Ability.CIRCLE_FORMS))
        self.assertIn(Spells.MOONBEAM, self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=4)
        self.assertIn(Spells.CONJURE_ANIMALS, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=4)
        self.assertTrue(self.c.has_ability(Ability.IMPROVED_CIRCLE_FORMS))


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
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
        )
        self.c.add_ability(Magician())

    ###################################################################
    def test_skills(self):
        self.assertEqual(self.c.arcana.modifier.value, 5)
        self.assertEqual(self.c.arcana.modifier.reason, "stat (1) + proficiency (2) + Magician (2)")
        self.assertEqual(self.c.nature.modifier.value, 3)
        self.assertEqual(self.c.nature.modifier.reason, "stat (1) + Magician (2)")


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
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
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
