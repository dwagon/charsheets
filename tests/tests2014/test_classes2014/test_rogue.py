import unittest

from charsheets.character import Character2014
from charsheets.classes2014 import Rogue
from charsheets.constants import Skill, Stat, Feature, Proficiency, Language, Weapon
from charsheets.exception import InvalidOption
from charsheets.features import Expertise
from tests.dummy import DummyBackground, DummyRace


#######################################################################
class TestRogue(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
            charisma=10,
        )

    ###################################################################
    def test_expertise_fail(self):
        with self.assertRaises(InvalidOption):
            self.c.add_level(Rogue(skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION]))

    ###################################################################
    def test_level1(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
            )
        )
        self.assertEqual(self.c.level, 1)

        self.assertEqual(self.c.max_hit_dice, "1d8")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Weapon.RAPIER, self.c.specific_weapon_proficiencies())
        self.assertTrue(self.c.has_feature(Feature.SNEAK_ATTACK14))
        self.assertTrue(self.c.has_feature(Feature.THIEVES_CANT14))
        self.assertTrue(self.c.has_feature(Feature.EXPERTISE))
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 1)
        self.assertTrue(self.c.skills[Skill.ARCANA].expert)
        self.assertFalse(self.c.skills[Skill.HISTORY].expert)
        self.assertTrue(self.c.skills[Skill.ANIMAL_HANDLING].expert)
        self.assertIsNone(self.c.spell_casting_ability)
        self.assertEqual(self.c.spell_slots(1), 0)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
