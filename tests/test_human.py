import unittest

from charsheets.constants import Skill, Feature
from charsheets.features import Alert
from charsheets.main import render
from charsheets.species import Human, Skillful, Versatile
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestHuman(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_human",
            DummyOrigin(),
            Human(Skillful(Skill.ANIMAL_HANDLING), Versatile(Alert())),
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
        self.assertTrue(self.c.has_feature(Feature.RESOURCEFUL))
        self.assertTrue(self.c.has_feature(Feature.SKILLFUL))

    ###################################################################
    def test_skillful(self):
        self.assertIn(Skill.ANIMAL_HANDLING, self.c.skills)  # From Alertness
        self.assertIn(Skill.DECEPTION, self.c.skills)  # From class

        self.assertTrue(self.c.is_proficient(Skill.ANIMAL_HANDLING))  # Skillful
        self.assertTrue(self.c.is_proficient(Skill.DECEPTION))  # Class
        self.assertFalse(self.c.is_proficient(Skill.ARCANA))

        r = render(self.c, "char_sheet.jinja")
        self.assertNotIn("You gained proficiency in animal_handling", r)
        self.assertIn("% Skillful", r)

    ###################################################################
    def test_versatile(self):
        self.assertTrue(self.c.has_feature(Feature.ALERT))


# EOF
