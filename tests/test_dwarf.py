import unittest
from charsheets.species.dwarf import Dwarf
from charsheets.constants import Skill, Ability
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
        self.assertTrue(self.c.has_ability(Ability.DWARVEN_TOUGHNESS))
        self.assertTrue(self.c.has_ability(Ability.DWARVEN_RESILIANCE))
        self.assertTrue(self.c.has_ability(Ability.STONE_CUNNING))


# EOF
