import unittest

from charsheets.constants import Skill, Feature
from charsheets.species import Halfling
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
        self.assertTrue(self.c.has_feature(Feature.BRAVE))
        self.assertTrue(self.c.has_feature(Feature.LUCK))
        self.assertTrue(self.c.has_feature(Feature.NATURALLY_STEALTHY))
        self.assertTrue(self.c.has_feature(Feature.HALFLING_NIMBLENESS))


# EOF
