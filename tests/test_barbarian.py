import unittest

from charsheets.classes import (
    Barbarian,
    PrimalKnowledge,
    BarbarianPathOfTheBeserker,
    BarbarianPathOfTheWildHeart,
    BarbarianPathOfTheWorldTree,
    BarbarianPathOfTheZealot,
)
from charsheets.constants import Skill, Stat, Feature, Proficiency
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestBarbarian(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Barbarian(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.INTIMIDATION,
            Skill.ANIMAL_HANDLING,
            strength=15,
            dexterity=13,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=8,
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
        self.assertEqual(self.c.spell_slots(1), 0)
        self.assertIsNone(self.c.spell_casting_ability)

    ###################################################################
    def test_level1(self):
        self.c.level1()
        self.assertEqual(self.c.level, 1)
        self.assertEqual(int(self.c.hp), 12 + 2)  # +2 for CON
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.UNARMORED_DEFENSE_BARBARIAN))
        self.assertTrue(self.c.has_feature(Feature.WEAPON_MASTERY))
        self.assertTrue(self.c.has_feature(Feature.RAGE))
        self.assertEqual(self.c.num_rages, 2)
        self.assertEqual(self.c.rage_dmg_bonus, 2)

    ###################################################################
    def test_level2(self):
        self.c.level1()
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 12 + 4)  # + 4 for CON
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.DANGER_SENSE))
        self.assertTrue(self.c.has_feature(Feature.RECKLESS_ATTACK))
        self.assertEqual(self.c.num_rages, 2)
        self.assertEqual(self.c.rage_dmg_bonus, 2)

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=1, feature=PrimalKnowledge(Skill.ARCANA), force=True)
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_feature(Feature.PRIMAL_KNOWLEDGE))
        self.assertTrue(self.c.arcana.proficient)
        self.assertEqual(self.c.num_rages, 3)
        self.assertEqual(self.c.rage_dmg_bonus, 2)

    ###################################################################
    def test_level5(self):
        self.assertEqual(int(self.c.speed), 30)
        self.c.level5(hp=5 + 6, force=True)
        self.assertEqual(self.c.level, 5)
        self.assertTrue(self.c.has_feature(Feature.FAST_MOVEMENT))
        self.assertTrue(self.c.has_feature(Feature.EXTRA_ATTACK))
        self.assertEqual(int(self.c.speed), 40)
        self.assertEqual(self.c.num_rages, 3)
        self.assertEqual(self.c.rage_dmg_bonus, 2)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.num_rages, 4)
        self.assertEqual(self.c.rage_dmg_bonus, 2)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.num_rages, 4)
        self.assertEqual(self.c.rage_dmg_bonus, 2)
        self.assertTrue(self.c.has_feature(Feature.FERAL_INSTINCT))
        self.assertTrue(self.c.has_feature(Feature.INSTINCTIVE_POUNCE))

    ###################################################################
    def test_class_special(self):
        cs = self.c.class_special
        self.assertIn("Number of Rages: 2", cs)


###################################################################
class TestBeserker(unittest.TestCase):

    def setUp(self):
        self.c = BarbarianPathOfTheBeserker(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ATHLETICS,
            Skill.ANIMAL_HANDLING,
            strength=15,
            dexterity=13,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=8,
        )
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_feature(Feature.FRENZY))

    ###################################################################
    def test_frenzy(self):
        frenzy = self.c.find_feature(Feature.FRENZY)
        self.assertIn("roll 2d6s", frenzy.desc)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.MINDLESS_RAGE))


###################################################################
class TestWildHeart(unittest.TestCase):
    def setUp(self):
        self.c = BarbarianPathOfTheWildHeart(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.SURVIVAL,
            Skill.ANIMAL_HANDLING,
            strength=15,
            dexterity=13,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=8,
        )
        self.c.level3(hp=5 + 6, force=True)
        self.assertEqual(self.c.level, 3)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_feature(Feature.ANIMAL_SPEAKER))

    ###################################################################
    def test_animal_speaker(self):
        self.assertIn(Spell.SPEAK_WITH_ANIMALS, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.ASPECTS_OF_THE_WILDS))


###################################################################
class TestWorldTree(unittest.TestCase):
    def setUp(self):
        self.c = BarbarianPathOfTheWorldTree(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.NATURE,
            Skill.ANIMAL_HANDLING,
            strength=15,
            dexterity=13,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=8,
        )
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_feature(Feature.VITALITY_OF_THE_TREE))

    ###################################################################
    def test_vitality(self):
        vott = self.c.find_feature(Feature.VITALITY_OF_THE_TREE)
        self.assertIn("2d6s", vott.desc)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.BRANCHES_OF_THE_TREE))

    ###################################################################
    def test_branches_of_the_tree(self):
        self.c.level6(hp=1, force=True)
        bott = self.c.find_feature(Feature.BRANCHES_OF_THE_TREE)
        self.assertIn("DC 13", bott.desc)


###################################################################
class TestZealot(unittest.TestCase):
    def setUp(self):
        self.c = BarbarianPathOfTheZealot(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERCEPTION,
            Skill.ANIMAL_HANDLING,
            strength=15,
            dexterity=13,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=8,
        )
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_feature(Feature.DIVINE_FURY))
        self.assertTrue(self.c.has_feature(Feature.WARRIOR_OF_THE_GODS))

    ###################################################################
    def test_divine_fury(self):
        df = self.c.find_feature(Feature.DIVINE_FURY)
        self.assertIn("1d6 plus 1", df.desc)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.FANATICAL_FOCUS))

    ###################################################################
    def test_fanatical_focus(self):
        self.c.level6(hp=1, force=True)
        ff = self.c.find_feature(Feature.FANATICAL_FOCUS)
        self.assertIn("bonus of 2", ff.desc)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
