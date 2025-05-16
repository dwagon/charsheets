import unittest

from charsheets.character import Character
from charsheets.constants import Language, Weapon, DamageType
from charsheets.items import DemonArmor
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestItems(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.ELVISH,
            strength=10,
            dexterity=10,
            constitution=10,
            wisdom=10,
            intelligence=10,
            charisma=10,
        )

    ###################################################################
    def test_demon_armor(self):
        self.assertEqual(int(self.c.ac), 10)
        for weapon in self.c.weapons:
            if weapon.tag == Weapon.UNARMED:
                self.assertEqual(weapon.dmg_dice, "1")
                self.assertEqual(str(weapon.atk_bonus), "+2")  # Prof
                self.assertEqual(str(weapon.dmg_bonus), "")
                self.assertEqual(weapon.damage_type, DamageType.BLUDGEONING)
        self.c.use_item(DemonArmor())
        self.assertEqual(int(self.c.ac), 11)
        for weapon in self.c.weapons:
            if weapon.tag == Weapon.UNARMED:
                self.assertEqual(weapon.dmg_dice, "1d8")
                self.assertEqual(str(weapon.atk_bonus), "+3")  # Prof + DA
                self.assertEqual(str(weapon.dmg_bonus), "+1")
                self.assertEqual(weapon.damage_type, DamageType.SLASHING)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
