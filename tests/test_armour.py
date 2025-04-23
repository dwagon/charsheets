import unittest

from charsheets.armour import Plate, Scale, Studded, Unarmoured, Shield, Hide, ChainMail, ChainShirt, Leather, Splint
from charsheets.character import Character
from charsheets.constants import Language
from charsheets.exception import UnhandledException
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestArmour(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=7,
            dexterity=18,
            constitution=8,
            wisdom=20,
            intelligence=5,
            charisma=10,
        )

    ###################################################################
    def test_ac_no_dex(self):
        armour = Plate()
        self.c.wear_armour(armour)
        self.assertEqual(int(armour.armour_class()), 18)
        self.assertEqual(armour.armour_class().reason, "plate (18)")
        armour = Plate(ac_bonus=1)
        self.c.wear_armour(armour)
        self.assertEqual(int(armour.armour_class()), 19)
        self.assertEqual(armour.armour_class().reason, "plate (18) + ac_bonus (1)")

    ###################################################################
    def test_ac_max_dex(self):
        armour = Scale()
        self.c.wear_armour(armour)
        self.assertEqual(int(armour.armour_class()), 16)
        self.assertEqual(armour.armour_class().reason, "scale (14) + dex_modifier (2)")

    ###################################################################
    def test_ac_all_dex(self):
        armour = Studded()
        self.c.wear_armour(armour)
        self.assertEqual(int(armour.armour_class()), 16)
        self.assertEqual(armour.armour_class().reason, "studded (12) + dex_modifier (4)")

    ###################################################################
    def test_ac_unarmored(self):
        armour = Unarmoured()
        self.c.wear_armour(armour)
        self.assertEqual(int(armour.armour_class()), 14)
        self.assertEqual(armour.armour_class().reason, "none (10) + dex_modifier (4)")

    ###################################################################
    def test_ac_shield(self):
        armour = Shield()
        self.c.wear_armour(armour)
        self.assertEqual(int(armour.armour_class()), 2)
        self.assertEqual(armour.armour_class().reason, "shield (2)")

    ###################################################################
    def test_name(self):
        armour = ChainMail()
        self.assertEqual(str(armour), "Chain Mail")
        armour2 = ChainShirt(name="Gerald")
        self.assertEqual(str(armour2), "Gerald")

    ###################################################################
    def test_is_heavy(self):
        self.assertTrue(Splint().is_heavy())
        self.assertFalse(Leather().is_heavy())

    ###################################################################
    def test_validation(self):
        with self.assertRaises(UnhandledException):
            Hide(invalid="Foo")


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
