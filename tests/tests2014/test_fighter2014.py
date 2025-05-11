import unittest

from charsheets.armour import Leather
from charsheets.character import Character2014
from charsheets.classes2014 import Fighter, Defense, Archery
from charsheets.constants import Skill, Stat, Feature, Proficiency, Weapon
from charsheets.exception import InvalidOption
from charsheets.weapons import Shortbow
from tests.dummy import DummyBackground, DummyRace


#######################################################################
class TestFighter(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=8,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_fighter(self):
        self.c.add_level(Fighter(skills=[Skill.INTIMIDATION, Skill.PERCEPTION], style=Defense()))
        self.assertEqual(self.c.level, 1)
        self.assertTrue(self.c.has_feature(Feature.SECOND_WIND))
        self.assertEqual(int(self.c.hp), 10 + 1)  # 1 for CON
        self.assertEqual(self.c.max_hit_dice, "1d10")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CONSTITUTION))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIsNone(self.c.spell_casting_ability)
        self.assertEqual(self.c.spell_slots(1), 0)

    ###################################################################
    def test_archery(self):
        self.c.add_level(Fighter(skills=[Skill.INTIMIDATION, Skill.PERCEPTION], style=Archery()))
        self.c.add_weapon(Shortbow())
        shortbow = None
        for weapon in self.c.weapons:
            if weapon.tag == Weapon.SHORTBOW:
                shortbow = weapon
                break
        assert shortbow is not None
        self.assertEqual(int(shortbow.atk_bonus), 6)  # dex, archery, prof
        self.assertIn("Archery (2)", shortbow.atk_bonus.reason)
        self.assertEqual(int(shortbow.dmg_bonus), 2)  # dex
        self.assertNotIn("Archery (2)", shortbow.dmg_bonus.reason)

    ###################################################################
    def test_defense(self):
        self.c.add_level(Fighter(skills=[Skill.INTIMIDATION, Skill.PERCEPTION], style=Defense()))
        self.c.wear_armour(Leather())
        self.assertEqual(int(self.c.ac), 14)
        self.assertIn("Defense (1)", self.c.ac.reason)

    ###################################################################
    def test_missing_style(self):
        with self.assertRaises(InvalidOption):
            self.c.add_level(Fighter(skills=[Skill.INTIMIDATION, Skill.PERCEPTION]))

    ###################################################################
    def test_bad_style(self):
        with self.assertRaises(AssertionError):
            self.c.add_level(Fighter(skills=[Skill.INTIMIDATION, Skill.PERCEPTION], style=None))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
