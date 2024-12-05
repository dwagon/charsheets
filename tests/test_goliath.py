import unittest
from charsheets.species.goliath import Goliath
from charsheets.constants import Origin, Skill
from tests.fixtures import DummyCharClass


#######################################################################
class TestGoliath(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_goliath",
            Origin.ACOLYTE,
            Goliath(),
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
        self.assertEqual(self.c.speed, 35)


# EOF