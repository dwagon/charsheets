import unittest

from charsheets.character import Character
from charsheets.constants import Skill, Feature, Language
from charsheets.species import Orc
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestOrc(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_orc",
            DummyOrigin(),
            Orc(),
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
        self.assertTrue(self.c.has_feature(Feature.DARKVISION120))
        self.assertTrue(self.c.has_feature(Feature.RELENTLESS_ENDURANCE))
        self.assertTrue(self.c.has_feature(Feature.ADRENALIN_RUSH))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
