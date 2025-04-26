import unittest

from charsheets.character import Character, Character2014
from charsheets.constants import Skill, Feature, DamageType, Language, Stat, Proficiency
from charsheets.species import Dwarf
from tests.dummy import DummyCharClass, DummyOrigin, DummyBackground
from charsheets.race2014 import MountainDwarf, HillDwarf


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
class TestMountainDwarf(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_dwarf",
            DummyBackground(),
            MountainDwarf(),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 25)

    ###################################################################
    def test_abilities(self):
        self.assertTrue(self.c.has_feature(Feature.DWARVEN_RESILIENCE14))
        self.assertTrue(self.c.has_feature(Feature.STONE_CUNNING14))
        self.assertIn(Language.DWARVISH, self.c.languages)
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())

    ###################################################################
    def test_stat(self):
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 12)
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 12)


#######################################################################
class TestHillDwarf(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_dwarf",
            DummyBackground(),
            HillDwarf(),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 25)

    ###################################################################
    def test_abilities(self):
        self.assertTrue(self.c.has_feature(Feature.DWARVEN_RESILIENCE14))
        self.assertTrue(self.c.has_feature(Feature.STONE_CUNNING14))
        self.assertTrue(self.c.has_feature(Feature.DWARVEN_TOUGHNESS14))
        self.c.add_level(DummyCharClass(skills=[]))
        self.assertIn("Dwarven Toughness (1)", self.c.hp.reason)

    ###################################################################
    def test_stat(self):
        self.assertEqual(int(self.c.stats[Stat.WISDOM].value), 11)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 10)
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 12)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
