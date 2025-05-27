import unittest

from charsheets.character import Character
from charsheets.constants import DamageType, Language
from charsheets.species import Dragonborn, Ancestor
from tests.dummy import DummyOrigin, DummyCharClass, DummyFeat


#######################################################################
class TestDragonborn(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_gold_dragonborn",
            DummyOrigin(),
            Dragonborn(Ancestor.GOLD),
            Language.ORC,
            Language.GNOMISH,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 30)
        self.assertEqual(self.c.fly_speed.value, 0)
        self.c.add_level(DummyCharClass(skills=[]))
        self.c.add_level(DummyCharClass(hp=1))
        self.c.add_level(DummyCharClass(hp=1))
        self.c.add_level(DummyCharClass(hp=1, feat=DummyFeat()))
        self.c.add_level(DummyCharClass(hp=1))
        self.assertEqual(self.c.fly_speed.value, 30)

    ###################################################################
    def test_breath_weapon(self):
        self.assertEqual(len(self.c.additional_attacks), 1)
        breath_weapon = self.c.additional_attacks.pop()
        self.assertEqual(breath_weapon.name, "Gold breath weapon")
        self.assertEqual(breath_weapon.dmg_dice, "1d10")
        self.assertEqual(breath_weapon.dmg_type, DamageType.FIRE)

        self.c.species.ancestor = Ancestor.GREEN
        self.c.level = 7
        breath_weapon = self.c.additional_attacks.pop()
        self.assertEqual(breath_weapon.dmg_dice, "2d10")
        self.assertEqual(breath_weapon.dmg_type, DamageType.POISON)
        self.assertEqual(breath_weapon.name, "Green breath weapon")

    ###################################################################
    def test_dmg_resistance(self):
        self.assertEqual(len(self.c.damage_resistances), 1)
        self.assertIn(DamageType.FIRE, self.c.damage_resistances)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
