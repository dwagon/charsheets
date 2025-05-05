import unittest

from charsheets.armour import Shield
from charsheets.character import Character2014
from charsheets.classes2014 import Monk
from charsheets.constants import Skill, Stat, Feature, Proficiency, Weapon
from tests.dummy import DummyRace, DummyBackground


#######################################################################
class TestMonk(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_basic(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.assertEqual(self.c.max_hit_dice, "1d8")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.CHARISMA))
        self.assertIsNone(self.c.spell_casting_ability)
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.spell_slots(1), 0)
        self.assertTrue(self.c.has_feature(Feature.MARTIAL_ARTS14))
        self.assertTrue(self.c.has_feature(Feature.UNARMORED_DEFENSE_MONK14))
        self.assertEqual(self.c.monk.martial_arts_die, "d4")
        ma = self.c.find_feature(Feature.MARTIAL_ARTS)
        self.assertIn(f"Dexterity ({self.c.dexterity.modifier})", ma.desc)
        self.assertEqual(self.c.monk.ki_points, 0)

    ###################################################################
    def test_martial_arts(self):
        for weapon in self.c.weapons:
            if weapon.tag == Weapon.UNARMED:
                self.assertEqual(weapon.dmg_dice, "1")
                self.assertEqual(str(weapon.atk_bonus), "+3")  # Str Mod + Prof
                self.assertEqual(str(weapon.dmg_bonus), "+1")  # Str Mod
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        for weapon in self.c.weapons:
            if weapon.tag == Weapon.UNARMED:
                self.assertEqual(weapon.dmg_dice, "d4")
                self.assertEqual(str(weapon.atk_bonus), "+4")  # Dex Mod + Prof
                self.assertEqual(str(weapon.dmg_bonus), "+2")  # Dex Mod

    ###################################################################
    def test_unarmored_defense(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))

        ud = self.c.find_feature(Feature.UNARMORED_DEFENSE_MONK)
        expected = 10 + self.c.dexterity.modifier + self.c.wisdom.modifier
        self.assertIn(f"AC is {expected}", ud.desc)
        self.assertEqual(int(self.c.ac), expected)
        self.assertIn("Unarmored Defense (2)", self.c.ac.reason)
        self.c.wear_shield(Shield())
        self.assertEqual(int(self.c.ac), expected)
        self.assertNotIn("Unarmored Defense (2)", self.c.ac.reason)
        self.assertNotIn("Shield (2)", self.c.ac.reason)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
