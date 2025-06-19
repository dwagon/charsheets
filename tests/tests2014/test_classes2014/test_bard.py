import unittest

from charsheets.character import Character2014
from charsheets.classes2014 import Bard
from charsheets.constants import Skill, Stat, Proficiency, Language, Feature
from charsheets.exception import InvalidOption
from charsheets.spell import Spell
from tests.dummy import DummyBackground, DummyRace


#######################################################################
class TestBard(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=8,
            dexterity=14,
            constitution=12,
            intelligence=13,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_level1(self):
        self.c.add_level(Bard(skills=[Skill.INVESTIGATION, Skill.RELIGION, Skill.INSIGHT]))

        self.assertEqual(self.c.max_hit_dice, "1d8")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CHARISMA))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertEqual(self.c.spell_casting_ability, Stat.CHARISMA)

        self.assertEqual(self.c.level, 1)
        self.assertEqual(int(self.c.hp), 8 + 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertIn(Spell.ANIMAL_FRIENDSHIP, [_[0] for _ in self.c.spells_of_level(1)])

        self.assertEqual(self.c.bard.num_bardic_inspiration(), 2)
        self.assertEqual(self.c.bard.bardic_inspiration_die(), "d6")
        self.assertIn(self.c.bard.class_special, "2d6")

    ###################################################################
    def test_level1_skills(self):
        with self.assertRaises(InvalidOption):
            self.c.add_level(Bard(skills=[Skill.PERSUASION, Skill.RELIGION]))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
