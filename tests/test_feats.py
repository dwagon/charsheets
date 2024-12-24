import unittest

from charsheets.constants import Skill, Stat, Tool, Feat
from charsheets.main import render
from charsheets.origins import Charlatan
from charsheets.exception import NotDefined
from tests.dummy import DummySpecies, DummyCharClass


#######################################################################
class TestSkilled(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            Charlatan(Stat.DEXTERITY, Stat.DEXTERITY, Stat.CONSTITUTION),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_undefined(self):
        """What happens if we don't define the skills"""
        with self.assertRaises(NotDefined):
            render(self.c, "char_sheet.jinja")

    ###################################################################
    def test_defined(self):
        self.c.feats[Feat.SKILLED].set_skills(Tool.DISGUISE_KIT, Skill.ATHLETICS, Skill.INTIMIDATION)  # type: ignore
        self.assertIn(Tool.FORGERY_KIT, self.c.tool_proficiencies)  # Charlatan
        self.assertIn(Tool.DISGUISE_KIT, self.c.tool_proficiencies)  # Skilled

        self.assertEqual(self.c.lookup_skill(Skill.ATHLETICS).proficient, 1)
        self.assertEqual(self.c.lookup_skill(Skill.ARCANA).proficient, 1)
        self.assertEqual(self.c.lookup_skill(Skill.RELIGION).proficient, 1)
        self.assertEqual(self.c.lookup_skill(Skill.INTIMIDATION).proficient, 1)

        self.assertEqual(self.c.lookup_skill(Skill.ANIMAL_HANDLING).proficient, 0)


#######################################################################
if __name__ == "__main__":
    unittest.main()
