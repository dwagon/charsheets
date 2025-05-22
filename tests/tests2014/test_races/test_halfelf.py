import unittest

from charsheets.character import Character2014
from charsheets.constants import Feature, Language, Stat, Skill
from charsheets.race2014 import HalfElf
from tests.dummy import DummyBackground


#######################################################################
class TestHalfling(unittest.TestCase):
    def setUp(self):
        self.c = Character2014(
            "test_haleflef",
            DummyBackground(),
            HalfElf(
                language=Language.ORC,
                stat1=Stat.STRENGTH,
                stat2=Stat.DEXTERITY,
                skill1=Skill.ATHLETICS,
                skill2=Skill.ANIMAL_HANDLING,
            ),
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        )

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 30)

    ###################################################################
    def test_skills(self):
        self.assertTrue(self.c.is_proficient(Skill.ATHLETICS))
        self.assertTrue(self.c.is_proficient(Skill.ANIMAL_HANDLING))

    ###################################################################
    def test_stats(self):
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 11)
        self.assertEqual(int(self.c.stats[Stat.DEXTERITY].value), 11)
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 10)
        self.assertEqual(int(self.c.stats[Stat.INTELLIGENCE].value), 10)
        self.assertEqual(int(self.c.stats[Stat.WISDOM].value), 10)
        self.assertEqual(int(self.c.stats[Stat.CHARISMA].value), 12)

    ###################################################################
    def test_abilities(self):
        self.assertTrue(self.c.has_feature(Feature.HALFELF_FEY_ANCESTRY14))
        self.assertIn(Language.ORC, self.c.languages)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
