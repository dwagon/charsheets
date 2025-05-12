import unittest

from charsheets.character import Character2014
from charsheets.classes2014 import Paladin
from charsheets.constants import Skill, Stat, Proficiency, Feature
from charsheets.main import render
from charsheets.spell import Spell
from tests.dummy import DummyBackground, DummyRace


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
    def test_paladin(self):
        self.c.add_level(Paladin(skills=[Skill.ATHLETICS, Skill.MEDICINE]))
        self.assertEqual(self.c.max_hit_dice, "1d10")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CHARISMA))
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())

    ###################################################################
    def test_features(self):
        self.c.add_level(Paladin(skills=[Skill.ATHLETICS, Skill.MEDICINE]))
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.spell_slots(1), 0)
        self.assertTrue(self.c.has_feature(Feature.LAY_ON_HANDS14))
        self.assertTrue(self.c.has_feature(Feature.DIVINE_SENSE14))
        loh = self.c.find_feature(Feature.LAY_ON_HANDS14)
        self.assertIn("restore 5 hit points", loh.desc)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()
