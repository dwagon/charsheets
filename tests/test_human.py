import unittest

from charsheets.character import Character, Character2014
from charsheets.constants import Skill, Feature, Language, Stat
from charsheets.features import Alert
from charsheets.main import render
from charsheets.species import Human, Skillful, Versatile
from charsheets.race2014 import Human as Human14
from tests.dummy import DummyCharClass, DummyOrigin, DummyBackground


#######################################################################
class TestHuman(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_human",
            DummyOrigin(),
            Human(Skillful(Skill.ANIMAL_HANDLING), Versatile(Alert())),
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
        self.assertTrue(self.c.has_feature(Feature.RESOURCEFUL))
        self.assertTrue(self.c.has_feature(Feature.SKILLFUL))

    ###################################################################
    def test_skillful(self):
        self.assertIn(Skill.ANIMAL_HANDLING, self.c.skills)  # From Alertness

        self.assertTrue(self.c.is_proficient(Skill.ANIMAL_HANDLING))  # Skillful
        self.assertFalse(self.c.is_proficient(Skill.ARCANA))

        r = render(self.c, "char_sheet.jinja")
        self.assertNotIn("You gained proficiency in animal_handling", r)
        self.assertIn("% Skillful", r)

    ###################################################################
    def test_versatile(self):
        self.assertTrue(self.c.has_feature(Feature.ALERT))


#######################################################################
class TestHuman14(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_human",
            DummyBackground(),
            Human14(Language.ORC),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_stats(self):
        self.assertEqual(self.c.speed.value, 30)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 11)
        self.assertEqual(int(self.c.stats[Stat.DEXTERITY].value), 11)
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 11)
        self.assertEqual(int(self.c.stats[Stat.INTELLIGENCE].value), 11)
        self.assertEqual(int(self.c.stats[Stat.WISDOM].value), 11)
        self.assertEqual(int(self.c.stats[Stat.CHARISMA].value), 11)
        self.assertIn(Language.ORC, self.c.languages)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
