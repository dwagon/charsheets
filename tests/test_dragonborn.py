import unittest
from charsheets.species.dragonborn import Dragonborn, Ancestor
from charsheets.constants import Skill, DamageType
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestDragonborn(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_gold_dragonborn",
            DummyOrigin(),
            Dragonborn(Ancestor.GOLD),
            Skill.DECEPTION,
            Skill.PERCEPTION,
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

    ###################################################################
    def test_breath_weapon(self):
        self.assertEqual(len(self.c.additional_attacks), 1)
        breath_weapon = self.c.additional_attacks.copy().pop()
        self.assertEqual(breath_weapon.name, "Gold breath weapon")
        self.assertEqual(breath_weapon.dmg_dice, "1d10")
        self.assertEqual(breath_weapon.dmg_type, DamageType.FIRE)

        self.c.species.ancestor = Ancestor.GREEN
        self.c.level = 7
        breath_weapon = self.c.additional_attacks.copy().pop()
        self.assertEqual(breath_weapon.dmg_dice, "2d10")
        self.assertEqual(breath_weapon.dmg_type, DamageType.POISON)
        self.assertEqual(breath_weapon.name, "Green breath weapon")

    ###################################################################
    def test_dmg_resistance(self):
        self.assertEqual(len(self.c.damage_resistances), 1)
        dmg_res = self.c.damage_resistances.pop()
        self.assertEqual(dmg_res, DamageType.FIRE)

    ###################################################################


# EOF
