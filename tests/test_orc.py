import unittest
from charsheets.species.orc import Orc
from charsheets.constants import Skill, Ability
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestOrc(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_orc",
            DummyOrigin(),
            Orc(),
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
        self.assertTrue(self.c.has_ability(Ability.DARKVISION120))
        self.assertTrue(self.c.has_ability(Ability.RELENTLESS_ENDURANCE))
        self.assertTrue(self.c.has_ability(Ability.ADRENALIN_RUSH))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
