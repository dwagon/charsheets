import unittest

from charsheets.armour import Plate, Scale, Studded, Unarmoured, Shield
from charsheets.constants import Skill
from tests.dummy import DummyCharClass, DummySpecies, DummyOrigin


#######################################################################
class TestArmour(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=7,
            dexterity=18,
            constitution=8,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_ac_no_dex(self):
        armour = Plate(self.c)
        self.assertEqual(int(armour.armour_class()), 18)
        self.assertEqual(armour.armour_class().reason, "plate (18)")

    ###################################################################
    def test_ac_max_dex(self):
        armour = Scale(self.c)
        self.assertEqual(int(armour.armour_class()), 16)
        self.assertEqual(armour.armour_class().reason, "scale (14) + dex_modifier (2)")

    ###################################################################
    def test_ac_all_dex(self):
        armour = Studded(self.c)
        self.assertEqual(int(armour.armour_class()), 16)
        self.assertEqual(armour.armour_class().reason, "studded (12) + dex_modifier (4)")

    ###################################################################
    def test_ac_unarmored(self):
        armour = Unarmoured(self.c)
        self.assertEqual(int(armour.armour_class()), 14)
        self.assertEqual(armour.armour_class().reason, "none (10) + dex_modifier (4)")

    ###################################################################
    def test_ac_shield(self):
        armour = Shield(self.c)
        self.assertEqual(int(armour.armour_class()), 2)
        self.assertEqual(armour.armour_class().reason, "shield (2)")


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
