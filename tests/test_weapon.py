import unittest
from typing import TYPE_CHECKING

from charsheets.constants import WeaponMasteryProperty, WeaponCategory, DamageType, WeaponProperty, Weapon, Skill
from charsheets.weapons.base_weapon import BaseWeapon
from tests.dummy import DummyCharClass, DummySpecies, DummyOrigin
from charsheets.abilities import WeaponMastery

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class WeaponTest(BaseWeapon):
    tag = Weapon.TEST

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.weapon_type = WeaponCategory.SIMPLE_MELEE
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d3"
        self.properties = [WeaponProperty.THROWN, WeaponProperty.VERSATILE, WeaponProperty.RANGE]
        self.range = (20, 60)
        self.versatile_damage_dice = "1d8"


#######################################################################
class TestWeapon(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=7,
            dexterity=14,
            constitution=8,
            wisdom=20,
            intelligence=5,
        )
        self.weapon = WeaponTest(self.c)

    ###################################################################
    def test_ranged(self):
        self.weapon.weapon_type = WeaponCategory.SIMPLE_MELEE
        self.weapon.properties = [WeaponProperty.VERSATILE]
        self.assertFalse(self.weapon.is_ranged())
        self.weapon.properties = [WeaponProperty.THROWN]
        self.assertTrue(self.weapon.is_ranged())

    ###################################################################
    def test_dmg_dice(self):
        self.weapon.damage_dice = "1d7"
        self.assertEqual(self.weapon.dmg_dice, "1d7")

    ###################################################################
    def test_dmg_type(self):
        self.weapon.damage_type = DamageType.ACID
        self.assertEqual(self.weapon.dmg_type, "ACID")

    ###################################################################
    def test_dmg_bonus(self):
        dmg_bonus = self.weapon.dmg_bonus
        self.assertEqual(dmg_bonus.value, 2)
        self.assertEqual(dmg_bonus.reason, "dex mod (2)")

    ###################################################################
    def test_atk_bonus(self):
        atk_bonus = self.weapon.atk_bonus
        self.assertEqual(atk_bonus.reason, "prof_bonus (2) + dex mod (2)")
        self.assertEqual(atk_bonus.value, 4)

    ###################################################################
    def test_mastery(self):
        self.assertEqual(self.weapon.mastery, "")
        self.c.add_ability(WeaponMastery())
        self.assertEqual(self.weapon.mastery, "SAP")


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
