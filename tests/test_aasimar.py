import unittest

from charsheets.constants import Skill, DamageType
from charsheets.species.aasimar import Aasimar
from charsheets.spells import Spells
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestAasimar(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_aasimar",
            DummyOrigin(),
            Aasimar(),
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
    def test_dmg_resistance(self):
        self.assertIn(DamageType.NECROTIC, self.c.damage_resistances)
        self.assertIn(DamageType.RADIANT, self.c.damage_resistances)

    ###################################################################
    def test_known_spells(self):
        self.assertIn(Spells.LIGHT, self.c.known_spells)
        self.assertEqual(len(self.c.known_spells), 1)


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
