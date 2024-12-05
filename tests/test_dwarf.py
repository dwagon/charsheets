import unittest
from charsheets.species.dwarf import Dwarf
from charsheets.constants import Origin, Skill, Ability
from charsheets.ability import get_ability
from tests.fixtures import DummyCharClass


#######################################################################
class TestDragonborn(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_dwarf",
            Origin.ACOLYTE,
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
        self.assertEqual(self.c.speed, 30)

    ###################################################################
    def test_abilities(self):
        self.assertIn(get_ability(Ability.DWARVEN_TOUGHNESS), self.c.abilities)
        self.assertIn(get_ability(Ability.DWARVEN_RESILIANCE), self.c.abilities)
        self.assertIn(get_ability(Ability.STONE_CUNNING), self.c.abilities)


# EOF
