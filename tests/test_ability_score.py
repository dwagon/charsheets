import unittest

from charsheets.ability_score import AbilityScore
from charsheets.character import Character
from charsheets.constants import Stat, Skill
from charsheets.reason import Reason
from tests.dummy import DummyCharClass, DummyOrigin, DummySpecies


#######################################################################
class TestAbilityScore(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.char = DummyCharClass(
            "test_char",
            DummyOrigin(),
            DummySpecies(),
            Skill.DECEPTION,
            Skill.PERCEPTION,
        )

    ###################################################################
    def mod_stat_dex(self, character: "Character") -> int:
        return 2

    ###################################################################
    def mod_stat_cha(self, character: "Character") -> Reason:
        return Reason("Ugly", -2)

    ###################################################################
    def test_init(self):
        strength = AbilityScore(Stat.STRENGTH, self.char, 10)
        self.assertEqual(strength.modifier, 0)
        self.assertEqual(strength.value.value, 10)
        self.assertEqual(strength.value.reason, "Base (10)")

    ###################################################################
    def test_int_modifier(self):
        self.char.mod_stat_dex = self.mod_stat_dex
        dex = AbilityScore(Stat.DEXTERITY, self.char, 10)
        self.assertEqual(dex.value.value, 12)
        self.assertEqual(dex.modifier, 1)
        self.assertIn("Base (10)", dex.value.reason)
        self.assertIn("class mod_stat_dex (2)", dex.value.reason)

    ###################################################################
    def test_reason_modifier(self):
        self.char.mod_stat_cha = self.mod_stat_cha
        cha = AbilityScore(Stat.CHARISMA, self.char, 10)
        self.assertEqual(cha.value.value, 8)
        self.assertEqual(cha.modifier, -1)
        self.assertEqual(cha.value.reason, "Ugly (-2) + Base (10)")

    ###################################################################
    def test_modifiers(self):
        wis = AbilityScore(Stat.WISDOM, self.char, 3)
        self.assertEqual(wis.modifier, -4)
        wis = AbilityScore(Stat.WISDOM, self.char, 5)
        self.assertEqual(wis.modifier, -3)
        wis = AbilityScore(Stat.WISDOM, self.char, 6)
        self.assertEqual(wis.modifier, -2)
        wis = AbilityScore(Stat.WISDOM, self.char, 17)
        self.assertEqual(wis.modifier, 3)
        wis = AbilityScore(Stat.WISDOM, self.char, 18)
        self.assertEqual(wis.modifier, 4)


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
