import unittest

from charsheets.character import Character
from charsheets.constants import Skill, Feature, DamageType, Language
from charsheets.species import Dwarf
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestDwarf(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_dwarf",
            DummyOrigin(),
            Dwarf(),
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

    ###################################################################
    def test_abilities(self):
        self.assertTrue(self.c.has_feature(Feature.DWARVEN_RESILIENCE))
        self.assertTrue(self.c.has_feature(Feature.STONE_CUNNING))

    ###################################################################
    def test_dwarven_toughness(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.assertTrue(self.c.has_feature(Feature.DWARVEN_TOUGHNESS))
        self.assertIn("Dwarven Toughness (1)", self.c.hp.reason)
        self.c.add_level(DummyCharClass(hp=5))

        self.assertIn("Dwarven Toughness (2)", self.c.hp.reason)
        self.assertEqual(int(self.c.hp), 7 + 5 + 2 + 4)  # 7=lvl1, 5=lvl2, 2=dt, 4=con

    ###################################################################
    def test_dwarven_resilience(self):
        self.assertTrue(self.c.has_feature(Feature.DWARVEN_RESILIENCE))
        self.assertIn(DamageType.POISON, self.c.damage_resistances)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
