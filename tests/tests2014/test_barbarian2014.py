import unittest

from charsheets.character import Character2014
from charsheets.classes2014 import Barbarian
from charsheets.constants import Skill, Stat, Feature, Proficiency
from tests.dummy import DummyBackground, DummyRace


#######################################################################
class TestBarbarian2014(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=15,
            dexterity=13,
            constitution=14,
            intelligence=10,
            wisdom=12,
            charisma=8,
        )

    ###################################################################
    def test_level1(self):
        self.c.add_level(Barbarian(skills=[Skill.ANIMAL_HANDLING, Skill.ATHLETICS]))
        self.assertEqual(self.c.level, 1)

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
        self.assertEqual(int(self.c.hp), 12 + 2)  # +2 for CON
        self.assertTrue(self.c.has_feature(Feature.UNARMORED_DEFENSE_BARBARIAN14))
        self.assertTrue(self.c.has_feature(Feature.RAGE14))

        assert self.c.barbarian is not None
        self.assertEqual(self.c.barbarian.num_rages, 2)
        self.assertEqual(self.c.barbarian.rage_dmg_bonus, 2)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
