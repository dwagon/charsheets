import unittest

from charsheets.constants import Skill, Stat, Tool, Feat
from charsheets.main import render
from charsheets.origins import Charlatan, Artisan, Farmer, Entertainer
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
        self.c.feats[Feat.SKILLED].set_skills(Tool.DISGUISE_KIT, Skill.ATHLETICS, Skill.INTIMIDATION)
        self.assertIn(Tool.FORGERY_KIT, self.c.tool_proficiencies)  # Charlatan
        self.assertIn(Tool.DISGUISE_KIT, self.c.tool_proficiencies)  # Skilled

        self.assertEqual(self.c.lookup_skill(Skill.ATHLETICS).proficient, 1)
        self.assertEqual(self.c.lookup_skill(Skill.ARCANA).proficient, 1)
        self.assertEqual(self.c.lookup_skill(Skill.RELIGION).proficient, 1)
        self.assertEqual(self.c.lookup_skill(Skill.INTIMIDATION).proficient, 1)

        self.assertEqual(self.c.lookup_skill(Skill.ANIMAL_HANDLING).proficient, 0)

    ###################################################################
    def test_desc(self):
        self.c.feats[Feat.SKILLED].set_skills(Tool.DISGUISE_KIT, Skill.ATHLETICS, Skill.INTIMIDATION)
        r = render(self.c, "char_sheet.jinja")
        self.assertIn("You have proficiency in: Disguise Kit, athletics, intimidation", r)


#######################################################################
class TestCrafter(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            Artisan(Stat.DEXTERITY, Stat.DEXTERITY, Stat.CONSTITUTION),
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
        """What happens if we don't define the tools"""
        with self.assertRaises(NotDefined):
            render(self.c, "char_sheet.jinja")

    ###################################################################
    def test_defined(self):
        self.c.feats[Feat.CRAFTER].set_tools(Tool.DISGUISE_KIT, Tool.CARTOGRAPHERS_TOOLS, Tool.POTTERS_TOOLS)  # type: ignore
        self.assertIn(Tool.DISGUISE_KIT, self.c.tool_proficiencies)  # Artisan
        self.assertIn(Tool.CARTOGRAPHERS_TOOLS, self.c.tool_proficiencies)  # Artisan

    ###################################################################
    def test_desc(self):
        self.c.feats[Feat.CRAFTER].set_tools(Tool.DISGUISE_KIT, Tool.CARTOGRAPHERS_TOOLS, Tool.POTTERS_TOOLS)  # type: ignore
        r = render(self.c, "char_sheet.jinja")
        self.assertIn("You gained proficiency with Cartographer's Tools, Disguise Kit, Potter's Tools", r)


#######################################################################
class TestMusician(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            Entertainer(Stat.DEXTERITY, Stat.DEXTERITY, Stat.CONSTITUTION),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=7,
            dexterity=14,
            constitution=9,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_defined(self):
        self.assertIn(Tool.MUSICAL_INSTRUMENT, self.c.tool_proficiencies)


#######################################################################
class TestTough(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            Farmer(Stat.DEXTERITY, Stat.DEXTERITY, Stat.CONSTITUTION),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=7,
            dexterity=14,
            constitution=9,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_hp(self):
        self.assertEqual(int(self.c.hp), 7 + 2)
        self.assertIn("feat tough (2)", self.c.hp.reason)
        self.assertIn("Level 1 (7)", self.c.hp.reason)

    ###################################################################
    def test_desc(self):
        self.c.level = 2
        r = render(self.c, "char_sheet.jinja")
        self.assertIn("maximum increased by 4", r)


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
