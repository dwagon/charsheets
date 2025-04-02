import unittest

from charsheets.character import Character
from charsheets.classes import (
    Barbarian,
    PrimalKnowledge,
    BarbarianPathOfTheBeserker,
    BarbarianPathOfTheWildHeart,
    BarbarianPathOfTheWorldTree,
    BarbarianPathOfTheZealot,
)
from charsheets.constants import Skill, Stat, Feature, Proficiency, Language
from charsheets.features import AbilityScoreImprovement
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin, DummyCharClass


#######################################################################
class TestBarbarian(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=13,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=8,
        )

    ###################################################################
    def test_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.c.add_level(Barbarian(hp=1))
        print(f"DBG {self.c.class_levels=}")
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertEqual(self.c.max_hit_dice, "1d7 + 1d12")

    ###################################################################
    def test_basics(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))

        self.assertEqual(self.c.max_hit_dice, "1d12")
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
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))

        self.assertEqual(self.c.level, 1)
        self.assertEqual(int(self.c.hp), 12 + 2)  # +2 for CON
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.UNARMORED_DEFENSE_BARBARIAN))
        self.assertTrue(self.c.has_feature(Feature.WEAPON_MASTERY))
        self.assertTrue(self.c.has_feature(Feature.RAGE))

        assert self.c.barbarian is not None
        self.assertEqual(self.c.barbarian.num_rages, 2)
        self.assertEqual(self.c.barbarian.rage_dmg_bonus, 2)

    ###################################################################
    def test_level2(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=5))

        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 12 + 4)  # + 4 for CON
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.DANGER_SENSE))
        self.assertTrue(self.c.has_feature(Feature.RECKLESS_ATTACK))

        assert self.c.barbarian is not None
        self.assertEqual(self.c.barbarian.num_rages, 2)
        self.assertEqual(self.c.barbarian.rage_dmg_bonus, 2)

    ###################################################################
    def test_level3(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=5))
        self.c.add_level(Barbarian(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))

        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_feature(Feature.PRIMAL_KNOWLEDGE))
        self.assertTrue(self.c.arcana.proficient)

        assert self.c.barbarian is not None
        self.assertEqual(self.c.barbarian.num_rages, 3)
        self.assertEqual(self.c.barbarian.rage_dmg_bonus, 2)

    ###################################################################
    def test_level5(self):
        self.assertEqual(int(self.c.speed), 30)
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))

        self.assertTrue(self.c.has_feature(Feature.FAST_MOVEMENT))
        self.assertTrue(self.c.has_feature(Feature.EXTRA_ATTACK))
        self.assertEqual(int(self.c.speed), 40)

        assert self.c.barbarian is not None
        self.assertEqual(self.c.barbarian.num_rages, 3)
        self.assertEqual(self.c.barbarian.rage_dmg_bonus, 2)

    ###################################################################
    def test_level6(self):
        self.assertEqual(int(self.c.speed), 30)
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))

        assert self.c.barbarian is not None
        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.barbarian.num_rages, 4)
        self.assertEqual(self.c.barbarian.rage_dmg_bonus, 2)

    ###################################################################
    def test_level7(self):
        self.assertEqual(int(self.c.speed), 30)
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))

        assert self.c.barbarian is not None
        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.barbarian.num_rages, 4)
        self.assertEqual(self.c.barbarian.rage_dmg_bonus, 2)
        self.assertTrue(self.c.has_feature(Feature.FERAL_INSTINCT))
        self.assertTrue(self.c.has_feature(Feature.INSTINCTIVE_POUNCE))

    ###################################################################
    def test_level9(self):
        self.assertEqual(int(self.c.speed), 30)
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))

        assert self.c.barbarian is not None
        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.barbarian.num_rages, 4)
        self.assertEqual(self.c.barbarian.rage_dmg_bonus, 3)
        self.assertTrue(self.c.has_feature(Feature.BRUTAL_STRIKE))

    ###################################################################
    def test_level10(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))

        self.assertEqual(self.c.level, 10)

        assert self.c.barbarian is not None
        self.assertEqual(self.c.barbarian.num_rages, 4)
        self.assertEqual(self.c.barbarian.rage_dmg_bonus, 3)

    ###################################################################
    def test_level11(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))

        assert self.c.barbarian is not None
        self.assertEqual(self.c.barbarian.num_rages, 4)
        self.assertEqual(self.c.barbarian.rage_dmg_bonus, 3)
        self.assertTrue(self.c.has_feature(Feature.RELENTLESS_RAGE))

    ###################################################################
    def test_class_special(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))

        cs = self.c.class_special
        self.assertIn("Number of Rages: 2", cs)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(Barbarian(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Barbarian(hp=1))

        self.assertEqual(self.c.level, 13)
        assert self.c.barbarian is not None
        self.assertEqual(self.c.barbarian.num_rages, 5)
        self.assertEqual(self.c.barbarian.rage_dmg_bonus, 3)
        self.assertTrue(self.c.has_feature(Feature.IMPROVED_BRUTAL_STRIKE))


###################################################################
class TestBeserker(unittest.TestCase):

    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=13,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=8,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))

        self.assertTrue(self.c.has_feature(Feature.FRENZY))

    ###################################################################
    def test_frenzy(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))

        frenzy = self.c.find_feature(Feature.FRENZY)
        self.assertIn("roll 2d6s", frenzy.desc)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1))

        self.assertTrue(self.c.has_feature(Feature.MINDLESS_RAGE))

    ###################################################################
    def test_level10(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1))
        self.c.add_level(BarbarianPathOfTheBeserker(hp=1))

        self.assertTrue(self.c.has_feature(Feature.RETALIATION))


###################################################################
class TestWildHeart(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=13,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=8,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.assertTrue(self.c.has_feature(Feature.ANIMAL_SPEAKER))
        self.assertIn(Spell.SPEAK_WITH_ANIMALS, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1))

        self.assertTrue(self.c.has_feature(Feature.ASPECTS_OF_THE_WILDS))

    ###################################################################
    def test_level10(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1))
        self.c.add_level(BarbarianPathOfTheWildHeart(hp=1))

        self.assertTrue(self.c.has_feature(Feature.NATURE_SPEAKER))


###################################################################
class TestWorldTree(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=13,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=8,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))

        self.assertTrue(self.c.has_feature(Feature.VITALITY_OF_THE_TREE))
        vott = self.c.find_feature(Feature.VITALITY_OF_THE_TREE)
        self.assertIn("2d6s", vott.desc)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1))

        self.assertTrue(self.c.has_feature(Feature.BRANCHES_OF_THE_TREE))
        bott = self.c.find_feature(Feature.BRANCHES_OF_THE_TREE)
        self.assertIn("DC 13", bott.desc)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1))
        self.c.add_level(BarbarianPathOfTheWorldTree(hp=1))

        self.assertTrue(self.c.has_feature(Feature.BATTERING_ROOTS))


###################################################################
class TestZealot(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=13,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=8,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))

        self.assertTrue(self.c.has_feature(Feature.DIVINE_FURY))
        self.assertTrue(self.c.has_feature(Feature.WARRIOR_OF_THE_GODS))

    ###################################################################
    def test_divine_fury(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))

        df = self.c.find_feature(Feature.DIVINE_FURY)
        self.assertIn("1d6 plus 1", df.desc)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1))

        self.assertTrue(self.c.has_feature(Feature.FANATICAL_FOCUS))
        ff = self.c.find_feature(Feature.FANATICAL_FOCUS)
        self.assertIn("bonus of 2", ff.desc)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Barbarian(hp=1))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1, feat=PrimalKnowledge(Skill.ARCANA)))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1))
        self.c.add_level(BarbarianPathOfTheZealot(hp=1))

        self.assertTrue(self.c.has_feature(Feature.ZEALOUS_PRESENCE))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
