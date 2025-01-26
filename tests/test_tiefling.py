import unittest

from charsheets.constants import Skill, DamageType, Stat, Feature
from charsheets.species import Tiefling, Legacy
from charsheets.spell import Spell
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestTieflingAbyssal(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_tiefling",
            DummyOrigin(),
            Tiefling(Legacy.ABYSSAL, Stat.CHARISMA),
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
    def test_name(self):
        self.assertEqual("Abyssal Tiefling", self.c.species.name)

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 30)

    ###################################################################
    def test_fiendish_legacy(self):
        fl = self.c.find_feature(Feature.FIENDISH_LEGACY)
        self.assertIn(DamageType.POISON, self.c.damage_resistances)
        self.assertIn("Charisma is your", fl.desc)
        self.assertIn("You can cast Poison Spray", fl.desc)
        self.c.level3(hp=1)
        self.assertIn("Ray Of Sickness", fl.desc)
        self.assertIn(Spell.RAY_OF_SICKNESS, self.c.prepared_spells)
        self.c.level5(hp=1)
        self.assertIn(Spell.HOLD_PERSON, self.c.prepared_spells)

    ###################################################################
    def test_otherworldly(self):
        op = self.c.find_feature(Feature.OTHERWORLDLY_PRESENCE)
        self.assertIn(Spell.THAUMATURGY, self.c.known_spells)
        self.assertIn("the spell uses Charisma", op.desc)


#######################################################################
class TestTieflingChthonic(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_tiefling",
            DummyOrigin(),
            Tiefling(Legacy.CHTHONIC, Stat.INTELLIGENCE),
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
    def test_fiendish_legacy(self):
        fl = self.c.find_feature(Feature.FIENDISH_LEGACY)
        self.assertIn(DamageType.NECROTIC, self.c.damage_resistances)
        self.assertIn("Intelligence is your", fl.desc)
        self.assertIn("You can cast Chill Touch", fl.desc)
        self.c.level3(hp=1)
        self.assertIn(Spell.FALSE_LIFE, self.c.prepared_spells)
        self.c.level5(hp=1)
        self.assertIn(Spell.RAY_OF_ENFEEBLEMENT, self.c.prepared_spells)


#######################################################################
class TestTieflingInfernal(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_tiefling",
            DummyOrigin(),
            Tiefling(Legacy.INFERNAL, Stat.WISDOM),
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
    def test_fiendish_legacy(self):
        fl = self.c.find_feature(Feature.FIENDISH_LEGACY)
        self.assertIn(DamageType.FIRE, self.c.damage_resistances)
        self.assertIn("Wisdom is your", fl.desc)
        self.assertIn("You can cast Fire Bolt", fl.desc)
        self.assertNotIn(Spell.HELLISH_REBUKE, self.c.prepared_spells)
        self.c.level3(hp=1)
        self.assertIn(Spell.HELLISH_REBUKE, self.c.prepared_spells)
        self.c.level5(hp=1)
        self.assertIn(Spell.DARKNESS, self.c.prepared_spells)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
