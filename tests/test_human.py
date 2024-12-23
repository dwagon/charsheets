import unittest
from charsheets.species.human import Human
from charsheets.constants import Origin, Skill, Ability
from charsheets.ability import get_ability
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestHuman(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_human",
            DummyOrigin(),
            Human(Skill.ANIMAL_HANDLING),
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
        self.assertIn(get_ability(Ability.RESOURCEFUL), self.c.abilities)
        self.assertIn(get_ability(Ability.SKILLFUL), self.c.abilities)

    ###################################################################
    def test_skillful(self):
        self.assertIn(Skill.ANIMAL_HANDLING, self.c.skills)  # From Alertness
        self.assertIn(Skill.DECEPTION, self.c.skills)  # From class


# EOF
