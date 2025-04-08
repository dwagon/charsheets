import unittest

from charsheets.character import Character
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
from charsheets.exception import InvalidOption
from charsheets.features import AbilityScoreImprovement
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin, DummyCharClass


#######################################################################
class TestDruid(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
        )

    ###################################################################
    def test_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.c.add_level(Druid(hp=1, primal=Warden()))
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())

    ###################################################################
    def test_no_primal(self):
        with self.assertRaises(InvalidOption):
            self.c.add_level(Druid(skills=[]))

    ###################################################################
    def test_druid(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Magician()))

        self.assertEqual(self.c.max_hit_dice, "1d8")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertEqual(self.c.spell_casting_ability, Stat.WISDOM)

        # Magician
        self.assertTrue(self.c.is_proficient(Skill.ARCANA))
        self.assertEqual(self.c.arcana.modifier.reason, "stat (1) + proficiency (2) + Magician (2)")
        self.assertEqual(self.c.arcana.modifier.value, 5)
        self.assertFalse(self.c.is_proficient(Skill.NATURE))
        self.assertEqual(self.c.nature.modifier.reason, "stat (1) + Magician (2)")
        self.assertEqual(self.c.nature.modifier.value, 3)

    ###################################################################
    def test_level1(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))

        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertTrue(self.c.has_feature(Feature.DRUIDIC))

        self.c.prepare_spells(Spell.ANIMAL_FRIENDSHIP)
        self.assertIn(Spell.FAERIE_FIRE, [_[0] for _ in self.c.spells_of_level(1)])

        # Warden
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_druidic(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))

        self.assertIn(Language.DRUIDIC, self.c.languages)

    ###################################################################
    def test_level2(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))

        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8 + 4)  # +4 for CON
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_feature(Feature.WILD_SHAPE))
        self.assertTrue(self.c.has_feature(Feature.WILD_COMPANION))

    ###################################################################
    def test_level3(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(Druid(hp=1))

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertIn(Spell.HEAT_METAL, [_[0] for _ in self.c.spells_of_level(2)])

    ###################################################################
    def test_level5(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertIn(Spell.WIND_WALL, [_[0] for _ in self.c.spells_of_level(3)])

    ###################################################################
    def test_level6(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 1)
        self.assertTrue(self.c.has_feature(Feature.ELEMENTAL_FURY))

    ###################################################################
    def test_level8(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))

        self.assertEqual(self.c.level, 8)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 2)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))

        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.max_spell_level(), 5)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 1)
        self.assertIn(Spell.ANTILIFE_SHELL, [_[0] for _ in self.c.spells_of_level(5)])

    ###################################################################
    def test_level10(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertEqual(self.c.max_spell_level(), 5)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)

    ###################################################################
    def test_level11(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertEqual(self.c.max_spell_level(), 6)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertEqual(self.c.spell_slots(6), 1)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1))
        self.c.add_level(Druid(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Druid(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.max_spell_level(), 7)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertEqual(self.c.spell_slots(6), 1)
        self.assertEqual(self.c.spell_slots(7), 1)


#######################################################################
class TestCircleOfStars(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
        )

    ###################################################################
    def test_circle_of_stars(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheStars(hp=1))

        self.assertTrue(self.c.has_feature(Feature.STAR_MAP))
        self.assertTrue(self.c.has_feature(Feature.STARRY_FORM))

        self.assertIn(Spell.GUIDANCE, self.c.prepared_spells)
        sm = self.c.find_feature(Feature.STAR_MAP)
        self.assertEqual(sm.goes, 2)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheStars(hp=1))
        self.c.add_level(DruidCircleOfTheStars(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheStars(hp=1))

        self.assertIn(Spell.GUIDANCE, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheStars(hp=1))
        self.c.add_level(DruidCircleOfTheStars(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(DruidCircleOfTheStars(hp=1))
        self.c.add_level(DruidCircleOfTheStars(hp=1))

        self.assertTrue(self.c.has_feature(Feature.COSMIC_OMEN))
        co = self.c.find_feature(Feature.COSMIC_OMEN)
        self.assertEqual(co.goes, 2)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheStars(hp=1))
        self.c.add_level(DruidCircleOfTheStars(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheStars(hp=1))
        self.c.add_level(DruidCircleOfTheStars(hp=1))
        self.c.add_level(DruidCircleOfTheStars(hp=1))
        self.c.add_level(DruidCircleOfTheStars(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheStars(hp=1))
        self.c.add_level(DruidCircleOfTheStars(hp=1))

        self.assertTrue(self.c.has_feature(Feature.TWINKLING_CONSTELLATIONS))


#######################################################################
class TestCircleOfLand(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
        )

    ###################################################################
    def test_circle_of_land(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheLand(hp=1))

        self.assertTrue(self.c.has_feature(Feature.LANDS_AID))
        self.assertIn(Spell.BLUR, self.c.prepared_spells)
        self.assertIn(Spell.BURNING_HANDS, self.c.prepared_spells)
        self.assertIn(Spell.FIRE_BOLT, self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheLand(hp=1))

        self.assertIn(Spell.FIREBALL, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1))

        self.assertTrue(self.c.has_feature(Feature.NATURAL_RECOVERY))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1))

        self.assertIn(Spell.FREEDOM_OF_MOVEMENT, self.c.prepared_spells)
        self.assertIn(Spell.POLYMORPH, self.c.prepared_spells)
        self.assertIn(Spell.ICE_STORM, self.c.prepared_spells)
        self.assertIn(Spell.BLIGHT, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheLand(hp=1))

        self.assertIn(Spell.WALL_OF_STONE, self.c.prepared_spells)
        self.assertIn(Spell.CONE_OF_COLD, self.c.prepared_spells)
        self.assertIn(Spell.TREE_STRIDE, self.c.prepared_spells)
        self.assertIn(Spell.INSECT_PLAGUE, self.c.prepared_spells)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheLand(hp=1))
        self.c.add_level(DruidCircleOfTheLand(hp=1))

        self.assertTrue(self.c.has_feature(Feature.NATURES_WARD))


#######################################################################
class TestCircleOfSea(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
        )

    ###################################################################
    def test_circle_of_sea(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.assertTrue(self.c.has_feature(Feature.WRATH_OF_THE_SEA))
        self.assertIn(Spell.THUNDERWAVE, self.c.prepared_spells)

    ###################################################################
    def test_wrath_of_the_sea(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        wots = self.c.find_feature(Feature.WRATH_OF_THE_SEA)
        self.assertIn("roll 2d6", wots.desc)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheSea(hp=1))

        self.assertIn(Spell.LIGHTNING_BOLT, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1))

        self.assertTrue(self.c.has_feature(Feature.AQUATIC_AFFINITY))
        self.assertEqual(int(self.c.swim_speed), 30)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1))

        self.assertIn(Spell.CONTROL_WATER, self.c.prepared_spells)
        self.assertIn(Spell.ICE_STORM, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheSea(hp=1))

        self.assertIn(Spell.CONJURE_ELEMENTAL, self.c.prepared_spells)
        self.assertIn(Spell.HOLD_MONSTER, self.c.prepared_spells)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheSea(hp=1))
        self.c.add_level(DruidCircleOfTheSea(hp=1))

        self.assertTrue(self.c.has_feature(Feature.STORMBORN))


#######################################################################
class TestCircleOfMoon(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=12,
            constitution=14,
            intelligence=13,
            wisdom=15,
            charisma=10,
        )

    ###################################################################
    def test_circle_of_moon(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))

        self.assertTrue(self.c.has_feature(Feature.CIRCLE_FORMS))
        self.assertIn(Spell.MOONBEAM, self.c.prepared_spells)

    ###################################################################
    def test_circle_forms(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))

        cf = self.c.find_feature(Feature.CIRCLE_FORMS)
        self.assertIn("gain 9 Temporary", cf.desc)  # Level * 3
        self.assertIn("AC equals 15", cf.desc)  # 13+wis mod
        self.assertIn("form is 1", cf.desc)  # Level / 3

        self.c.add_level(DruidCircleOfTheMoon(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))

        self.assertIn("gain 18 Temporary", cf.desc)  # Level * 3
        self.assertIn("AC equals 15", cf.desc)  # 13+wis mod
        self.assertIn("form is 2", cf.desc)  # Level / 3

    ###################################################################
    def test_level5(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))

        self.assertIn(Spell.CONJURE_ANIMALS, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))

        self.assertTrue(self.c.has_feature(Feature.IMPROVED_CIRCLE_FORMS))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))

        self.assertIn(Spell.FOUNT_OF_MOONLIGHT, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))

        self.assertIn(Spell.MASS_CURE_WOUNDS, self.c.prepared_spells)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Druid(skills=[Skill.ARCANA, Skill.ANIMAL_HANDLING], primal=Warden()))
        self.c.add_level(Druid(hp=5))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))
        self.c.add_level(DruidCircleOfTheMoon(hp=1))

        self.assertTrue(self.c.has_feature(Feature.MOONLIGHT_STEP))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
