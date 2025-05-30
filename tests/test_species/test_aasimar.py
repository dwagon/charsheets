import unittest

from charsheets.character import Character
from charsheets.constants import DamageType, Language
from charsheets.species import Aasimar
from charsheets.spell import Spell
from tests.dummy import DummyOrigin


#######################################################################
class TestAasimar(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_aasimar",
            DummyOrigin(),
            Aasimar(),
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
    def test_dmg_resistance(self):
        self.assertIn(DamageType.NECROTIC, self.c.damage_resistances)
        self.assertIn(DamageType.RADIANT, self.c.damage_resistances)

    ###################################################################
    def test_known_spells(self):
        self.assertIn(Spell.LIGHT, self.c.known_spells)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
