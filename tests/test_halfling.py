import unittest
from charsheets.species import Halfling
from charsheets.constants import Skill, Ability
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestHalfling(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_hobbit",
            DummyOrigin(),
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
        self.assertTrue(self.c.has_ability(Ability.BRAVE))
        self.assertTrue(self.c.has_ability(Ability.LUCK))
        self.assertTrue(self.c.has_ability(Ability.NATURALLY_STEALTHY))
        self.assertTrue(self.c.has_ability(Ability.HALFLING_NIMBLENESS))


# EOF
