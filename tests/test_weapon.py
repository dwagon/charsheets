import unittest

from charsheets.constants import WeaponMasteryProperty, WeaponCategory, DamageType, WeaponProperty, Weapon, Skill
from charsheets.exception import UnhandledException
from charsheets.features import WeaponMastery
from charsheets.weapons import (
    Battleaxe,
    Flail,
    Glaive,
    Greataxe,
    Greatsword,
    Halberd,
    Lance,
    Longsword,
    Maul,
    Morningstar,
    Pike,
    Rapier,
    Scimitar,
    ShortSword,
    Trident,
    Warhammer,
    WarPick,
    Whip,
)
from charsheets.weapons import BlowGun, HandCrossbow, HeavyCrossbow, Longbow, Musket, Pistol
from charsheets.weapons import Club, Dagger, Greatclub, Handaxe, Javelin, LightHammer, Mace, Quarterstaff, Sickle, Spear
from charsheets.weapons import Dart, Shortbow, Sling, LightCrossbow
from charsheets.weapons.base_weapon import BaseWeapon
from tests.dummy import DummyCharClass, DummySpecies, DummyOrigin


#############################################################################
class WeaponTest(BaseWeapon):
    tag = Weapon.TEST

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
        self.weapon = WeaponTest()
        self.c.add_weapon(self.weapon)

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
        weapon1 = WeaponTest(dmg_bonus=3)
        self.c.add_weapon(weapon1)
        dmg_bonus = weapon1.dmg_bonus
        self.assertEqual(dmg_bonus.reason, "dmg_bonus (3) + dex mod (2)")
        self.assertEqual(dmg_bonus.value, 5)

    ###################################################################
    def test_atk_bonus(self):
        atk_bonus = self.weapon.atk_bonus
        self.assertEqual(atk_bonus.reason, "prof_bonus (2) + dex mod (2)")
        self.assertEqual(atk_bonus.value, 4)
        weapon1 = WeaponTest(atk_bonus=-2)
        self.c.add_weapon(weapon1)
        atk_bonus = weapon1.atk_bonus
        self.assertEqual(atk_bonus.reason, "prof_bonus (2) + dex mod (2) + atk_bonus (-2)")
        self.assertEqual(atk_bonus.value, 2)

    ###################################################################
    def test_mastery(self):
        self.assertEqual(self.weapon.mastery, "")
        self.c.add_feature(WeaponMastery())
        self.assertEqual(self.weapon.mastery, "SAP")

    ###################################################################
    def test_equal(self):
        weapon1 = WeaponTest()
        weapon2 = WeaponTest()
        self.assertEqual(weapon1, weapon2)
        weapon3 = Pistol()
        self.assertNotEqual(weapon1, weapon3)
        self.assertNotEqual(weapon1, "Weapon")

    ###################################################################
    def test_name(self):
        self.assertEqual(str(self.weapon), "<Weapon Test +4 1d3 + +2/Piercing>")
        weapon1 = WeaponTest(name="Fred")
        self.c.add_weapon(weapon1)
        self.assertEqual(weapon1.name, "Fred")
        self.assertEqual(str(weapon1), "<Weapon Fred +4 1d3 + +2/Piercing>")

    ###################################################################
    def test_validation(self):
        with self.assertRaises(UnhandledException):
            WeaponTest(invalid="Foo")


#######################################################################
class TestCategories(unittest.TestCase):

    ###################################################################
    def test_category(self):
        for weapon in (Club, Dagger, Greatclub, Handaxe, Javelin, LightHammer, Mace, Quarterstaff, Sickle, Spear):
            self.assertEqual(weapon().weapon_type, WeaponCategory.SIMPLE_MELEE)
        for weapon in (Dart, Shortbow, Sling, LightCrossbow):
            self.assertEqual(weapon().weapon_type, WeaponCategory.SIMPLE_RANGED)
            self.assertTrue(weapon().is_ranged())
        for weapon in (
            Battleaxe,
            Flail,
            Glaive,
            Greataxe,
            Greatsword,
            Halberd,
            Lance,
            Longsword,
            Maul,
            Morningstar,
            Pike,
            Rapier,
            Scimitar,
            ShortSword,
            Trident,
            Warhammer,
            WarPick,
            Whip,
        ):
            self.assertEqual(weapon().weapon_type, WeaponCategory.MARTIAL_MELEE)
        for weapon in (BlowGun, HandCrossbow, HeavyCrossbow, Longbow, Musket, Pistol):
            self.assertEqual(weapon().weapon_type, WeaponCategory.MARTIAL_RANGED)
            self.assertTrue(weapon().is_ranged())

    ###################################################################
    def test_mastery(self):
        for weapon in Club, Javelin, LightCrossbow, Sling, Whip, Longbow:
            self.assertEqual(weapon().weapon_mastery, WeaponMasteryProperty.SLOW)
        for weapon in Dagger, LightHammer, Sickle, Scimitar:
            self.assertEqual(weapon().weapon_mastery, WeaponMasteryProperty.NICK)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
