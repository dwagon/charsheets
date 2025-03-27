import unittest

from charsheets.character import Character
from charsheets.constants import Skill, DamageType, Stat, Feature, Language
from charsheets.features import Grappler
from charsheets.species import Tiefling, Legacy
from charsheets.spell import Spell
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestTieflingAbyssal(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_tiefling",
            DummyOrigin(),
            Tiefling(Legacy.ABYSSAL, Stat.CHARISMA),
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
        self.assertIn("You can cast 'Poison Spray'", fl.desc)
        self.c.add_level(DummyCharClass(skills=[]))
        self.c.add_level(DummyCharClass(hp=1))
        self.c.add_level(DummyCharClass(hp=1))
        self.assertIn("Ray Of Sickness", fl.desc)
        self.assertIn(Spell.RAY_OF_SICKNESS, self.c.prepared_spells)
        self.c.add_level(DummyCharClass(hp=1, feat=Grappler(Stat.STRENGTH)))
        self.c.add_level(DummyCharClass(hp=1))
        self.assertIn(Spell.HOLD_PERSON, self.c.prepared_spells)

    ###################################################################
    def test_otherworldly(self):
        op = self.c.find_feature(Feature.OTHERWORLDLY_PRESENCE)
        self.assertIn(Spell.THAUMATURGY, self.c.known_spells)
        self.assertIn("the spell uses Charisma", op.desc)


#######################################################################
class TestTieflingChthonic(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_tiefling",
            DummyOrigin(),
            Tiefling(Legacy.CHTHONIC, Stat.INTELLIGENCE),
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
    def test_fiendish_legacy(self):
        fl = self.c.find_feature(Feature.FIENDISH_LEGACY)
        self.assertIn(DamageType.NECROTIC, self.c.damage_resistances)
        self.assertIn("Intelligence is your", fl.desc)
        self.assertIn("You can cast 'Chill Touch'", fl.desc)
        self.c.add_level(DummyCharClass(skills=[]))
        self.c.add_level(DummyCharClass(hp=1))
        self.c.add_level(DummyCharClass(hp=1))
        self.assertIn(Spell.FALSE_LIFE, self.c.prepared_spells)
        self.c.add_level(DummyCharClass(hp=1, feat=Grappler(Stat.STRENGTH)))
        self.c.add_level(DummyCharClass(hp=1))
        self.assertIn(Spell.RAY_OF_ENFEEBLEMENT, self.c.prepared_spells)


#######################################################################
class TestTieflingInfernal(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_tiefling",
            DummyOrigin(),
            Tiefling(Legacy.INFERNAL, Stat.WISDOM),
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
    def test_fiendish_legacy(self):
        fl = self.c.find_feature(Feature.FIENDISH_LEGACY)
        self.assertIn(DamageType.FIRE, self.c.damage_resistances)
        self.assertIn("Wisdom is your", fl.desc)
        self.assertIn("You can cast 'Fire Bolt'", fl.desc)
        self.assertNotIn(Spell.HELLISH_REBUKE, self.c.prepared_spells)
        self.c.add_level(DummyCharClass(skills=[]))
        self.c.add_level(DummyCharClass(hp=1))
        self.c.add_level(DummyCharClass(hp=1))
        self.assertIn(Spell.HELLISH_REBUKE, self.c.prepared_spells)
        self.c.add_level(DummyCharClass(hp=1, feat=Grappler(Stat.STRENGTH)))
        self.c.add_level(DummyCharClass(hp=1))
        self.assertIn(Spell.DARKNESS, self.c.prepared_spells)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
