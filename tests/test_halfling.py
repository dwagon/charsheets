import unittest

from charsheets.character import Character
from charsheets.constants import Feature, Language
from charsheets.species import Halfling
from tests.dummy import DummyOrigin


#######################################################################
class TestHalfling(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_hobbit",
            DummyOrigin(),
            Halfling(),
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
        self.assertTrue(self.c.has_feature(Feature.BRAVE))
        self.assertTrue(self.c.has_feature(Feature.LUCK))
        self.assertTrue(self.c.has_feature(Feature.NATURALLY_STEALTHY))
        self.assertTrue(self.c.has_feature(Feature.HALFLING_NIMBLENESS))


# EOF
