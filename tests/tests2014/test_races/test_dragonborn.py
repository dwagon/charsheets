import unittest

from charsheets.character import Character2014
from charsheets.constants import DamageType, Language, Stat, Feature
from charsheets.race2014 import Ancestry14
from charsheets.race2014 import Dragonborn as Dragonborn14
from tests.dummy import DummyBackground


#######################################################################
class TestDragonborn14(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_red_dragonborn",
            DummyBackground(),
            Dragonborn14(Ancestry14.RED),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_stats(self):
        self.assertEqual(self.c.speed.value, 30)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 12)
        self.assertEqual(int(self.c.stats[Stat.CHARISMA].value), 11)
        self.assertIn(Language.DRACONIC, self.c.languages)
        self.assertTrue(self.c.find_feature(Feature.DRACONIC_ANCESTRY14))
        self.assertTrue(self.c.find_feature(Feature.BREATH_WEAPON14))
        self.assertTrue(self.c.find_feature(Feature.DAMAGE_RESISTANCE14))

    ###################################################################
    def test_breath_weapon(self):
        self.assertEqual(len(self.c.additional_attacks), 1)
        breath_weapon = self.c.additional_attacks.pop()
        self.assertEqual(breath_weapon.name, "Red breath weapon")
        self.assertEqual(breath_weapon.dmg_dice, "2d6")
        self.assertEqual(breath_weapon.dmg_type, DamageType.FIRE)
        bw = self.c.find_feature(Feature.BREATH_WEAPON14)
        self.assertIn("make a Dexterity saving throw DC 10", bw.desc)

    ###################################################################
    def test_dmg_resistance(self):
        self.assertEqual(len(self.c.damage_resistances), 1)
        self.assertIn(DamageType.FIRE, self.c.damage_resistances)
        dr = self.c.find_feature(Feature.DAMAGE_RESISTANCE14)
        self.assertIn("You have resistance to Fire", dr.desc)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
