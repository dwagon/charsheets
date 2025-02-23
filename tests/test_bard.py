import unittest

from charsheets.ability_score import AbilityScore
from charsheets.classes import Bard
from charsheets.constants import Skill, Stat, Feature, Proficiency
from charsheets.exception import InvalidOption
from charsheets.features import AbilityScoreImprovement, Expertise
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Bard(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERSUASION,
            Skill.RELIGION,
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

    ###################################################################
    def test_level1(self):
        self.c.level1()
        self.assertEqual(self.c.level, 1)
        self.assertEqual(int(self.c.hp), 8 + 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertEqual(self.c.bardic_inspiration_die(), "d6")
        self.assertEqual(self.c.num_bardic_inspiration(), 2)
        self.assertIn(Spell.BANE, self.c.spells_of_level(1))

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


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
