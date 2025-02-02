import unittest

from charsheets.character import Character
from charsheets.constants import Skill, Stat
from charsheets.reason import Reason
from charsheets.skill import CharacterSkill
from tests.dummy import DummyCharClass, DummyOrigin, DummySpecies


#######################################################################
class TestSkill(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.char = DummyCharClass(
            "test_char",
            DummyOrigin(),
            DummySpecies(),
            Skill.DECEPTION,
            Skill.PERCEPTION,
            dexterity=10,
            charisma=14,
            intelligence=12,
        )

    ###################################################################
    def test_non_proficient(self):
        s = CharacterSkill(Skill.ACROBATICS, self.char, False, "test")
        self.assertEqual(s.stat, Stat.DEXTERITY)
        self.assertFalse(s.proficient)
        self.assertEqual(int(s.modifier), 0)

    ###################################################################
    def test_proficient(self):
        s = CharacterSkill(Skill.DECEPTION, self.char, True, "test")
        self.assertEqual(s.stat, Stat.CHARISMA)
        self.assertTrue(s.proficient)
        self.assertEqual(int(s.modifier), 4)
        self.assertEqual(s.modifier.reason, "stat (2) + proficiency (2)")

    ###################################################################
    def test_expert(self):
        s = CharacterSkill(Skill.DECEPTION, self.char, True, "test")
        s.expert = True
        self.assertTrue(s.expert)
        self.assertEqual(int(s.modifier), 6)
        self.assertEqual(s.modifier.reason, "stat (2) + expert (4)")

    ###################################################################
    def mod_skill_investigation(self, character: "Character") -> Reason:
        return Reason("Holmes", 2)

    ###################################################################
    def mod_stat_int(self, character: "Character") -> Reason:
        return Reason("Smart", 4)

    ###################################################################
    def test_prof(self):
        s = CharacterSkill(Skill.INVESTIGATION, self.char, False, "test")
        self.assertEqual(repr(s), "Investigation (test): ")
        s.proficient = True
        self.assertEqual(repr(s), "Investigation (test): Proficient")
        s.expert = True
        self.assertEqual(repr(s), "Investigation (test): Expert")

    ###################################################################
    def test_repr(self):
        s = CharacterSkill(Skill.INVESTIGATION, self.char, False, "test")
        self.assertEqual(s.prof, "0")
        s.proficient = True
        self.assertEqual(s.prof, "0.5")
        s.expert = True
        self.assertEqual(s.prof, "1")

    ###################################################################
    def test_modifier(self):
        s = CharacterSkill(Skill.INVESTIGATION, self.char, True, "test")
        self.char.mod_skill_investigation = self.mod_skill_investigation
        self.char.mod_stat_int = self.mod_stat_int
        self.assertEqual(s.stat, Stat.INTELLIGENCE)
        self.assertTrue(s.proficient)
        self.assertEqual(s.modifier.reason, "stat (3) + proficiency (2) + Holmes (2)")
        self.assertEqual(int(s.modifier), 7)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
