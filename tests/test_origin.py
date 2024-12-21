import unittest

from charsheets.ability_score import AbilityScore
from charsheets.constants import Stat, Skill
from charsheets.character import Character
from charsheets.reason import Reason
from tests.fixtures import DummyCharClass, DummyOrigin, DummySpecies


#######################################################################
class TestOrigin(unittest.TestCase):
    ###################################################################
    def testStatIncrease(self):
        self.char = DummyCharClass(
            "test_char",
            DummyOrigin(Stat.STRENGTH, Stat.WISDOM, Stat.WISDOM),
            DummySpecies(),
            Skill.DECEPTION,
            Skill.PERCEPTION,
            strength=10,
            wisdom=10,
            intelligence=10,
        )
        self.assertEqual(int(self.char.stats[Stat.STRENGTH].value), 11)
        self.assertEqual(int(self.char.stats[Stat.WISDOM].value), 12)
        self.assertEqual(int(self.char.stats[Stat.INTELLIGENCE].value), 10)


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
