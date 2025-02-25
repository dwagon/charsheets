import unittest

from charsheets.ability_score import AbilityScore
from charsheets.classes import (
    Bard,
    BardDanceCollege,
    BardGlamourCollege,
    BardLoreCollege,
    BonusProficiencies,
    BardValorCollege,
    MagicalDiscoveries,
)
from charsheets.constants import Skill, Stat, Feature, Proficiency
from charsheets.exception import InvalidOption
from charsheets.features import AbilityScoreImprovement, Expertise, Poisoner
from charsheets.main import render
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestBard(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Bard(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERSUASION,
            Skill.RELIGION,
            Skill.ANIMAL_HANDLING,
            strength=8,
            dexterity=14,
            constitution=12,
            intelligence=13,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_basic(self):
        self.assertEqual(self.c.hit_dice, 8)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CHARISMA))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertEqual(self.c.spell_casting_ability, Stat.CHARISMA)
        self.assertTrue(self.c.is_proficient(Skill.ANIMAL_HANDLING))
        self.assertTrue(self.c.is_proficient(Skill.PERSUASION))
        self.assertTrue(self.c.is_proficient(Skill.RELIGION))

    ###################################################################
    def test_level1(self):
        self.c.level1()
        self.assertEqual(self.c.level, 1)
        self.assertEqual(int(self.c.hp), 8 + 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertEqual(self.c.bardic_inspiration_die(), "d6")
        self.assertEqual(self.c.num_bardic_inspiration(), 2)
        txt = render(self.c, "char_sheet.jinja")
        self.assertIn("Bardic Inspiration: 2d6", txt)
        self.assertTrue(self.c.has_feature(Feature.BARDIC_INSPIRATION))

    ###################################################################
    def test_level2(self):
        with self.assertRaises(InvalidOption):
            self.c.level2(hp=2, force=True)
        self.c.level1()
        self.c.level2(hp=5, expertise=Expertise(Skill.PERFORMANCE, Skill.PERSUASION))
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 8 + 5 + 2)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertEqual(self.c.bardic_inspiration_die(), "d6")
        self.assertEqual(self.c.num_bardic_inspiration(), 2)
        self.assertTrue(self.c.has_feature(Feature.EXPERTISE))
        self.assertTrue(self.c.has_feature(Feature.JACK_OF_ALL_TRADES))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=1, force=True)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertEqual(self.c.bardic_inspiration_die(), "d6")
        self.assertEqual(self.c.num_bardic_inspiration(), 2)

    ###################################################################
    def test_level4(self):
        self.c.level4(hp=1, force=True, feat=Poisoner(Stat.DEXTERITY))
        self.assertEqual(self.c.level, 4)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.bardic_inspiration_die(), "d6")
        self.assertEqual(self.c.num_bardic_inspiration(), 2)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)

        self.assertEqual(self.c.bardic_inspiration_die(), "d8")
        self.assertEqual(self.c.num_bardic_inspiration(), 2)
        self.assertTrue(self.c.has_feature(Feature.FONT_OF_INSPIRATION))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)

        self.assertEqual(self.c.bardic_inspiration_die(), "d8")
        self.assertEqual(self.c.num_bardic_inspiration(), 2)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 1)

        self.assertEqual(self.c.bardic_inspiration_die(), "d8")
        self.assertEqual(self.c.num_bardic_inspiration(), 2)
        self.assertTrue(self.c.has_feature(Feature.COUNTERCHARM))

    ###################################################################
    def test_level8(self):
        self.c.level8(hp=1, force=True, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA))
        self.assertEqual(self.c.level, 8)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 2)

        self.assertEqual(self.c.bardic_inspiration_die(), "d8")
        self.assertEqual(self.c.num_bardic_inspiration(), 3)


#######################################################################
class TestDance(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = BardDanceCollege(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERSUASION,
            Skill.RELIGION,
            Skill.ANIMAL_HANDLING,
            strength=8,
            dexterity=14,
            constitution=12,
            intelligence=13,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_basic(self):
        self.c.level3(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.DAZZLING_FOOTWORK))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.INSPIRING_MOVEMENT))
        self.assertTrue(self.c.has_feature(Feature.TANDEM_FOOTWORK))


#######################################################################
class TestGlamour(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = BardGlamourCollege(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERSUASION,
            Skill.RELIGION,
            Skill.ANIMAL_HANDLING,
            strength=8,
            dexterity=14,
            constitution=12,
            intelligence=13,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_basic(self):
        self.c.level3(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.BEGUILING_MAGIC))
        self.assertTrue(self.c.has_feature(Feature.MANTLE_OF_INSPIRATION))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.MANTLE_OF_MAJESTY))


#######################################################################
class TestLore(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = BardLoreCollege(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERSUASION,
            Skill.RELIGION,
            Skill.ANIMAL_HANDLING,
            strength=8,
            dexterity=14,
            constitution=12,
            intelligence=13,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_basic(self):
        with self.assertRaises(InvalidOption):
            self.c.level3(hp=1, force=True)
        self.c.level3(hp=1, force=True, bonus=BonusProficiencies(Skill.MEDICINE, Skill.NATURE, Skill.SURVIVAL))

        self.assertTrue(self.c.has_feature(Feature.BONUS_PROFICIENCIES))
        self.assertTrue(self.c.has_feature(Feature.CUTTING_WORDS))

        self.assertTrue(self.c.is_proficient(Skill.MEDICINE))
        self.assertTrue(self.c.is_proficient(Skill.NATURE))
        self.assertTrue(self.c.is_proficient(Skill.SURVIVAL))

    ###################################################################
    def test_level6(self):
        with self.assertRaises(InvalidOption):
            self.c.level6(hp=1, force=True)
        self.c.level6(hp=1, force=True, bonus=MagicalDiscoveries(Spell.MAGIC_MISSILE, Spell.CURE_WOUNDS))

        self.assertTrue(self.c.has_feature(Feature.MAGICAL_DISCOVERIES))
        self.assertIn(Spell.MAGIC_MISSILE, self.c.known_spells)


#######################################################################
class TestValor(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = BardValorCollege(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERSUASION,
            Skill.RELIGION,
            Skill.ANIMAL_HANDLING,
            strength=8,
            dexterity=14,
            constitution=12,
            intelligence=13,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_basic(self):
        self.c.level3(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.COMBAT_INSPIRATION))
        self.assertTrue(self.c.has_feature(Feature.MARTIAL_TRAINING))
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.EXTRA_ATTACK))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
