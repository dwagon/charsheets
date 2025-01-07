import unittest

from charsheets.constants import Skill, DamageType
from charsheets.species import Tiefling, Legacy
from charsheets.spells import Spells
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestTieflingAbyssal(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_tiefling",
            DummyOrigin(),
            Tiefling(Legacy.ABYSSAL),
            Skill.ARCANA,
            Skill.HISTORY,
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
        self.assertIn(DamageType.POISON, self.c.damage_resistances)

    ###################################################################
    def test_prepared_spells(self):
        self.assertIn(Spells.POISON_SPRAY, self.c.known_spells)
        self.assertIn(Spells.THAUMATURGY, self.c.known_spells)


#######################################################################
class TestTieflingChthonic(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_tiefling",
            DummyOrigin(),
            Tiefling(Legacy.CHTHONIC),
            Skill.INSIGHT,
            Skill.INVESTIGATION,
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

    ###################################################################
    def test_prepared_spells(self):
        self.assertIn(Spells.CHILL_TOUCH, self.c.known_spells)
        self.assertIn(Spells.THAUMATURGY, self.c.known_spells)


#######################################################################
class TestTieflingInfernal(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_tiefling",
            DummyOrigin(),
            Tiefling(Legacy.INFERNAL),
            Skill.MEDICINE,
            Skill.NATURE,
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
        self.assertIn(DamageType.FIRE, self.c.damage_resistances)

    ###################################################################
    def test_prepared_spells(self):
        self.assertIn(Spells.FIRE_BOLT, self.c.known_spells)
        self.assertIn(Spells.THAUMATURGY, self.c.known_spells)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
