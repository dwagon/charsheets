import unittest

from charsheets.classes import (
    Druid,
    Warden,
    Magician,
    DruidCircleOfTheStars,
    DruidCircleOfTheMoon,
    DruidCircleOfTheSea,
    DruidCircleOfTheLand,
)
from charsheets.constants import Skill, Stat, Feature, Proficiency, Language
from charsheets.spell import Spell
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
        self.c.level1()
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertTrue(self.c.has_feature(Feature.DRUIDIC))

        self.c.prepare_spells(Spell.ANIMAL_FRIENDSHIP)
        self.assertIn(Spell.FAERIE_FIRE, self.c.spells_of_level(1))

    ###################################################################
    def test_druidic(self):
        self.assertIn(Language.DRUIDIC, self.c.languages)

    ###################################################################
    def test_level2(self):
        self.c.level1()
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8 + 4)  # +4 for CON
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_feature(Feature.WILD_SHAPE))
        self.assertTrue(self.c.has_feature(Feature.WILD_COMPANION))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6, force=True)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertIn(Spell.HEAT_METAL, self.c.spells_of_level(2))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=5 + 6 + 1, force=True)
        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertIn(Spell.WIND_WALL, self.c.spells_of_level(3))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 1)
        self.assertTrue(self.c.has_feature(Feature.ELEMENTAL_FURY))


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
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_circle_of_stars(self):
        self.assertTrue(self.c.has_feature(Feature.STAR_MAP))
        self.assertTrue(self.c.has_feature(Feature.STARRY_FORM))

        self.assertIn(Spell.GUIDANCE, self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=4, force=True)
        self.assertIn(Spell.GUIDANCE, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=4, force=True)
        self.assertTrue(self.c.has_feature(Feature.COSMIC_OMEN))


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
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_circle_of_land(self):
        self.assertTrue(self.c.has_feature(Feature.LANDS_AID))
        self.assertIn(Spell.BLUR, self.c.prepared_spells)
        self.assertIn(Spell.BURNING_HANDS, self.c.prepared_spells)
        self.assertIn(Spell.FIRE_BOLT, self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=4, force=True)
        self.assertIn(Spell.FIREBALL, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=4, force=True)
        self.assertTrue(self.c.has_feature(Feature.NATURAL_RECOVERY))

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=4, force=True)
        self.assertIn(Spell.FREEDOM_OF_MOVEMENT, self.c.prepared_spells)
        self.assertIn(Spell.POLYMORPH, self.c.prepared_spells)
        self.assertIn(Spell.ICE_STORM, self.c.prepared_spells)
        self.assertIn(Spell.BLIGHT, self.c.prepared_spells)


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
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_circle_of_sea(self):
        self.assertTrue(self.c.has_feature(Feature.WRATH_OF_THE_SEA))
        self.assertIn(Spell.THUNDERWAVE, self.c.prepared_spells)

    ###################################################################
    def test_wrath_of_the_sea(self):
        wots = self.c.find_feature(Feature.WRATH_OF_THE_SEA)
        self.assertIn("roll 2d6", wots.desc)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=4, force=True)
        self.assertIn(Spell.LIGHTNING_BOLT, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=4, force=True)
        self.assertTrue(self.c.has_feature(Feature.AQUATIC_AFFINITY))

    ###################################################################
    def test_aquatic_affinity(self):
        self.c.level6(hp=1, force=True)
        self.assertEqual(int(self.c.swim_speed), 30)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=4, force=True)
        self.assertIn(Spell.CONTROL_WATER, self.c.prepared_spells)
        self.assertIn(Spell.ICE_STORM, self.c.prepared_spells)


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
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_circle_of_moon(self):
        self.assertTrue(self.c.has_feature(Feature.CIRCLE_FORMS))
        self.assertIn(Spell.MOONBEAM, self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=4, force=True)
        self.assertIn(Spell.CONJURE_ANIMALS, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=4, force=True)
        self.assertTrue(self.c.has_feature(Feature.IMPROVED_CIRCLE_FORMS))

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=4, force=True)
        self.assertIn(Spell.FOUNT_OF_MOONLIGHT, self.c.prepared_spells)


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
        self.c.add_feature(Magician())

    ###################################################################
    def test_skills(self):
        self.assertTrue(self.c.is_proficient(Skill.ARCANA))
        self.assertEqual(self.c.arcana.modifier.reason, "stat (1) + proficiency (2) + Magician (2)")
        self.assertEqual(self.c.arcana.modifier.value, 5)
        self.assertFalse(self.c.is_proficient(Skill.NATURE))
        self.assertEqual(self.c.nature.modifier.reason, "stat (1) + Magician (2)")
        self.assertEqual(self.c.nature.modifier.value, 3)


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
        self.c.add_feature(Warden())

    ###################################################################
    def test_extra_proficiency(self):
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
