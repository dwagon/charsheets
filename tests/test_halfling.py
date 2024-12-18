import unittest
from charsheets.species.halfling import Halfling
from charsheets.constants import Origin, Skill, Ability
from charsheets.ability import get_ability
from tests.fixtures import DummyCharClass


#######################################################################
class TestDragonborn(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_hobbit",
            Origin.ACOLYTE,
            Halfling(),
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
        self.assertIn(get_ability(Ability.BRAVE), self.c.abilities)
        self.assertIn(get_ability(Ability.LUCK), self.c.abilities)
        self.assertIn(get_ability(Ability.NATURALLY_STEALTHY), self.c.abilities)
        self.assertIn(get_ability(Ability.HALFLING_NIMBLENESS), self.c.abilities)


# EOF
