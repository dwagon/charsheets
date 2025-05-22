import unittest

from charsheets.character import Character2014
from charsheets.classes2014 import Ranger, FavoredEnemy, NaturalExplorer
from charsheets.constants import Skill, Stat, Feature, Proficiency, Language
from charsheets.exception import InvalidOption
from tests.dummy import DummyBackground, DummyRace


#######################################################################
class TestRanger(unittest.TestCase):
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
    def test_level1_explorer_fail(self):
        with self.assertRaises(InvalidOption):
            self.c.add_level(
                Ranger(
                    skills=[Skill.ANIMAL_HANDLING, Skill.ATHLETICS],
                    favored=FavoredEnemy("Elves", Language.ELVISH),
                )
            )

    ###################################################################
    def test_level1_favoured_fail(self):
        with self.assertRaises(InvalidOption):
            self.c.add_level(
                Ranger(
                    skills=[Skill.ANIMAL_HANDLING, Skill.ATHLETICS],
                    explorer=NaturalExplorer("Shops"),
                )
            )

    ###################################################################
    def test_level1(self):
        self.c.add_level(
            Ranger(
                skills=[Skill.ANIMAL_HANDLING, Skill.ATHLETICS],
                explorer=NaturalExplorer("Shops"),
                favored=FavoredEnemy("Elves", Language.ELVISH),
            )
        )
        self.assertEqual(self.c.level, 1)

        self.assertEqual(self.c.max_hit_dice, "1d10")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())

        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertEqual(self.c.spell_slots(1), 0)
        self.assertEqual(Stat.WISDOM, self.c.spell_casting_ability)
        self.assertEqual(int(self.c.hp), 10 + 2)  # +2 for CON
        self.assertTrue(self.c.has_feature(Feature.FAVOURED_ENEMY14))
        self.assertTrue(self.c.has_feature(Feature.NATURAL_EXPLORER14))

        fe = self.c.find_feature(Feature.FAVOURED_ENEMY14)
        self.assertIn("Elves", fe.desc)
        self.assertIn(Language.ELVISH, self.c.languages)

        ne = self.c.find_feature(Feature.NATURAL_EXPLORER14)
        self.assertIn("Shops", ne.desc)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
