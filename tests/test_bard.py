import unittest

from charsheets.character import Character
from charsheets.classes import (
    Bard,
    BardDanceCollege,
    BardGlamourCollege,
    BardLoreCollege,
    BonusProficiencies,
    BardValorCollege,
    MagicalDiscoveries,
)
from charsheets.constants import Skill, Stat, Feature, Proficiency, Language
from charsheets.exception import InvalidOption
from charsheets.features import AbilityScoreImprovement, Expertise, Poisoner
from charsheets.main import render
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin, DummyCharClass


#######################################################################
class TestBard(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=14,
            constitution=12,
            intelligence=13,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.assertFalse(self.c.is_proficient(Skill.RELIGION))
        self.c.add_level(Bard(hp=1, skills=[Skill.RELIGION]))
        self.assertTrue(self.c.is_proficient(Skill.RELIGION))
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertEqual(self.c.max_hit_dice, "1d7 + 1d8")

    ###################################################################
    def test_invalid_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        with self.assertRaises(InvalidOption):
            self.c.add_level(Bard(hp=1))

    ###################################################################
    def test_basic(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.assertEqual(self.c.max_hit_dice, "1d8")
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
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        assert self.c.bard is not None
        self.assertEqual(self.c.level, 1)
        self.assertEqual(int(self.c.hp), 8 + 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d6")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)
        txt = render(self.c, "char_sheet.jinja")
        self.assertIn("Bardic Inspiration: 2d6", txt)
        self.assertTrue(self.c.has_feature(Feature.BARDIC_INSPIRATION))

    ###################################################################
    def test_level2(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=5, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))

        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 8 + 5 + 2)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d6")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)
        self.assertTrue(self.c.has_feature(Feature.EXPERTISE))
        self.assertTrue(self.c.has_feature(Feature.JACK_OF_ALL_TRADES))

        joat = self.c.find_feature(Feature.JACK_OF_ALL_TRADES)
        self.assertIn("add 1", joat.desc)

    ###################################################################
    def test_invalid_level2(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        with self.assertRaises(InvalidOption):
            self.c.add_level(Bard(hp=5))

    ###################################################################
    def test_level3(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(Bard(hp=1))

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d6")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)

    ###################################################################
    def test_level4(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=Poisoner(Stat.DEXTERITY)))
        self.assertEqual(self.c.level, 4)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d6")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=Poisoner(Stat.DEXTERITY)))
        self.c.add_level(Bard(hp=1))

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)

        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d8")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)
        self.assertTrue(self.c.has_feature(Feature.FONT_OF_INSPIRATION))

    ###################################################################
    def test_level6(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=Poisoner(Stat.DEXTERITY)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)

        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d8")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=Poisoner(Stat.DEXTERITY)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 1)

        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d8")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)
        self.assertTrue(self.c.has_feature(Feature.COUNTERCHARM))

    ###################################################################
    def test_level8(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=Poisoner(Stat.DEXTERITY)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))

        self.assertEqual(self.c.level, 8)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 2)

        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d8")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 3)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=Poisoner(Stat.DEXTERITY)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.PERFORMANCE, Skill.PERSUASION)))

        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.max_spell_level(), 5)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 1)

        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d8")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=Poisoner(Stat.DEXTERITY)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.PERFORMANCE, Skill.PERSUASION)))
        self.c.add_level(Bard(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertEqual(self.c.max_spell_level(), 5)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d10")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)

        self.assertTrue(self.c.has_feature(Feature.MAGICAL_SECRETS))

    ###################################################################
    def test_level11(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=Poisoner(Stat.DEXTERITY)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.PERFORMANCE, Skill.PERSUASION)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertEqual(self.c.max_spell_level(), 6)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertEqual(self.c.spell_slots(6), 1)
        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d10")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=Poisoner(Stat.DEXTERITY)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.PERFORMANCE, Skill.PERSUASION)))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1))
        self.c.add_level(Bard(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
        self.c.add_level(Bard(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.max_spell_level(), 7)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertEqual(self.c.spell_slots(6), 1)
        self.assertEqual(self.c.spell_slots(7), 1)

        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d10")
        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)

        joat = self.c.find_feature(Feature.JACK_OF_ALL_TRADES)
        self.assertIn("add 2", joat.desc)


#######################################################################
class TestDance(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=14,
            constitution=12,
            intelligence=13,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_basic(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(BardDanceCollege(hp=1))

        self.assertTrue(self.c.has_feature(Feature.DAZZLING_FOOTWORK))

    ###################################################################
    def test_level6(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(BardDanceCollege(hp=1))
        self.c.add_level(BardDanceCollege(hp=1, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
        self.c.add_level(BardDanceCollege(hp=1))
        self.c.add_level(BardDanceCollege(hp=1))

        self.assertTrue(self.c.has_feature(Feature.INSPIRING_MOVEMENT))
        self.assertTrue(self.c.has_feature(Feature.TANDEM_FOOTWORK))


#######################################################################
class TestGlamour(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=14,
            constitution=12,
            intelligence=13,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_basic(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(BardGlamourCollege(hp=1))

        self.assertTrue(self.c.has_feature(Feature.BEGUILING_MAGIC))
        self.assertTrue(self.c.has_feature(Feature.MANTLE_OF_INSPIRATION))

    ###################################################################
    def test_level6(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(BardGlamourCollege(hp=1))
        self.c.add_level(BardGlamourCollege(hp=1, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
        self.c.add_level(BardGlamourCollege(hp=1))
        self.c.add_level(BardGlamourCollege(hp=1))

        self.assertTrue(self.c.has_feature(Feature.MANTLE_OF_MAJESTY))


#######################################################################
class TestLore(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=14,
            constitution=12,
            intelligence=13,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.c.add_level(Bard(hp=1, skills=[Skill.ARCANA]))

    ###################################################################
    def test_basic(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(BardLoreCollege(hp=1, bonus=BonusProficiencies(Skill.MEDICINE, Skill.NATURE, Skill.SURVIVAL)))

        self.assertTrue(self.c.has_feature(Feature.BONUS_PROFICIENCIES))
        self.assertTrue(self.c.has_feature(Feature.CUTTING_WORDS))

        self.assertTrue(self.c.is_proficient(Skill.MEDICINE))
        self.assertTrue(self.c.is_proficient(Skill.NATURE))
        self.assertTrue(self.c.is_proficient(Skill.SURVIVAL))

    ###################################################################
    def test_level6(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(BardLoreCollege(hp=1, bonus=BonusProficiencies(Skill.MEDICINE, Skill.INSIGHT, Skill.STEALTH)))
        self.c.add_level(BardLoreCollege(hp=1, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
        self.c.add_level(BardLoreCollege(hp=1))
        self.c.add_level(BardLoreCollege(hp=1, bonus=MagicalDiscoveries(Spell.MAGIC_MISSILE, Spell.CURE_WOUNDS)))

        self.assertTrue(self.c.has_feature(Feature.MAGICAL_DISCOVERIES))
        self.assertIn(Spell.MAGIC_MISSILE, self.c.known_spells)


#######################################################################
class TestValor(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=14,
            constitution=12,
            intelligence=13,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_basic(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(BardValorCollege(hp=1))

        self.assertTrue(self.c.has_feature(Feature.COMBAT_INSPIRATION))
        self.assertTrue(self.c.has_feature(Feature.MARTIAL_TRAINING))
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())

    ###################################################################
    def test_level6(self):
        self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
        self.c.add_level(Bard(hp=1, expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING)))
        self.c.add_level(BardValorCollege(hp=1))
        self.c.add_level(BardValorCollege(hp=1, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
        self.c.add_level(BardValorCollege(hp=1))
        self.c.add_level(BardValorCollege(hp=1, bonus=MagicalDiscoveries(Spell.MAGIC_MISSILE, Spell.CURE_WOUNDS)))

        self.assertTrue(self.c.has_feature(Feature.EXTRA_ATTACK_BARD))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
