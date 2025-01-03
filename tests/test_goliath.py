import unittest

from charsheets.constants import Skill
from charsheets.species import Goliath
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestGoliath(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_goliath",
            DummyOrigin(),
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
        self.assertEqual(self.c.speed.value, 35)


# EOF
