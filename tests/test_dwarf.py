import unittest
from charsheets.species import Dwarf
from charsheets.constants import Skill, Ability, DamageType
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestDwarf(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_dwarf",
            DummyOrigin(),
            Dwarf(),
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
    def test_abilities(self):
        self.assertTrue(self.c.has_ability(Ability.DWARVEN_RESILIENCE))
        self.assertTrue(self.c.has_ability(Ability.STONE_CUNNING))

    ###################################################################
    def test_dwarven_toughness(self):
        self.assertTrue(self.c.has_ability(Ability.DWARVEN_TOUGHNESS))
        self.assertIn("Dwarven Toughness (1)", self.c.hp.reason)
        self.c.level2(hp=5)
        self.assertIn("Dwarven Toughness (2)", self.c.hp.reason)
        self.assertEqual(int(self.c.hp), 7 + 5 + 2 + 4)  # 7=lvl1, 5=lvl2, 2=dt, 4=con

    ###################################################################
    def test_dwarven_resilience(self):
        self.assertTrue(self.c.has_ability(Ability.DWARVEN_RESILIENCE))
        self.assertIn(DamageType.POISON, self.c.damage_resistances)


# EOF
