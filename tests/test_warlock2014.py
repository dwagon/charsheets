import unittest

from charsheets.character import Character, Character2014
from charsheets.classes2014 import Warlock, ArchFeyWarlock, FiendWarlock, GreatOldOneWarlock
from charsheets.constants import Skill, Stat, Proficiency, Language, Feature
from charsheets.main import render
from charsheets.spell import Spell
from charsheets.spells import EldritchBlast
from tests.dummy import DummySpecies, DummyOrigin, DummyBackground, DummyRace


#######################################################################
#######################################################################
#######################################################################
class TestWarlock(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_warlock(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.assertEqual(self.c.max_hit_dice, "1d8")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())

    ###################################################################
    def test_features(self):
        self.c.add_level(Warlock(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.spell_slots(1), 1)


#######################################################################
#######################################################################
#######################################################################
class TestArchFeyWarlock(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_features(self):
        self.c.add_level(ArchFeyWarlock(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.assertIn(Spell.FAERIE_FIRE, self.c.prepared_spells)
        self.assertIn(Spell.SLEEP, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.FEY_PRESENCE14))


#######################################################################
#######################################################################
#######################################################################
class TestFiendWarlock(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_features(self):
        self.c.add_level(FiendWarlock(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.assertIn(Spell.BURNING_HANDS, self.c.prepared_spells)
        self.assertIn(Spell.COMMAND, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.DARKONES_BLESSING14))


#######################################################################
#######################################################################
#######################################################################
class TestGreatOldWarlock(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_features(self):
        self.c.add_level(GreatOldOneWarlock(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.assertIn(Spell.DISSONANT_WHISPERS, self.c.prepared_spells)
        self.assertIn(Spell.TASHAS_HIDEOUS_LAUGHTER, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.AWAKENED_MIND14))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()
