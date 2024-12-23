import unittest
from charsheets.species.dwarf import Dwarf
from charsheets.constants import Origin, Skill, Ability
from charsheets.ability import get_ability
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
        self.assertIn(get_ability(Ability.DWARVEN_TOUGHNESS), self.c.abilities)
        self.assertIn(get_ability(Ability.DWARVEN_RESILIANCE), self.c.abilities)
        self.assertIn(get_ability(Ability.STONE_CUNNING), self.c.abilities)


# EOF
