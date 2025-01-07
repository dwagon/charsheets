import unittest

from charsheets.constants import Stat, Skill
from charsheets.exception import InvalidOption
from tests.dummy import DummyCharClass, DummyOrigin, DummySpecies


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

    ###################################################################
    def test_validation(self):
        with self.assertRaises(InvalidOption):
            char = DummyCharClass(
                "test_char",
                DummyOrigin(Stat.STRENGTH, Stat.DEXTERITY, Stat.WISDOM),
                DummySpecies(),
                Skill.DECEPTION,
                Skill.PERCEPTION,
            )


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
