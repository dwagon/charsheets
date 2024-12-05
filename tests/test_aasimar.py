import unittest
from charsheets.species.aasimar import Aasimar
from charsheets.constants import Origin, Skill, DamageType
from tests.fixtures import DummyCharClass
from charsheets.spells import Spells


#######################################################################
class TestAasimar(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_aasimar",
            Origin.ACOLYTE,
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
        self.assertEqual(self.c.damage_resistances, {DamageType.NECROTIC, DamageType.RADIANT})

    ###################################################################
    def test_known_spells(self):
        self.assertEqual(self.c.known_spells, {Spells.LIGHT})


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
