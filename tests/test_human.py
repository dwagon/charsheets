import unittest

from charsheets.constants import Skill, Feature
from charsheets.main import render
from charsheets.species import Human, Skillful, Versatile
from tests.dummy import DummyCharClass, DummyOrigin
from charsheets.features import Alert


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

        self.assertEqual(self.c.lookup_skill(Skill.ANIMAL_HANDLING).proficient, 1)  # Skillful
        self.assertEqual(self.c.lookup_skill(Skill.DECEPTION).proficient, 1)  # Class
        self.assertEqual(self.c.lookup_skill(Skill.ARCANA).proficient, 0)

        r = render(self.c, "char_sheet.jinja")
        self.assertNotIn("You gained proficiency in animal_handling", r)
        self.assertIn("% Skillful", r)

    ###################################################################
    def test_versatile(self):
        self.assertTrue(self.c.has_feature(Feature.ALERT))


# EOF
