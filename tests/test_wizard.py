import unittest

from charsheets.classes import Wizard, Abjurer, Diviner, Evoker, Illusionist
from charsheets.constants import Skill, Stat, Ability, Proficiency, Weapon
from charsheets.main import render
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestWizard(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Wizard(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.NATURE,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.add_weapon(Weapon.QUARTERSTAFF)

    ###################################################################
    def test_basic(self):
        self.assertEqual(self.c.hit_dice, 6)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)

    #############################################################################
    def test_renders(self):
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\SpellcastingAbility{Intelligence}", output)

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 6)
        self.assertIn("level 2 (5)", self.c.hp.reason)
        self.assertIn("Level 1 (6)", self.c.hp.reason)

        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_ability(Ability.SCHOLAR))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 4)

        self.assertEqual(self.c.level, 3)
        self.assertEqual(int(self.c.hp), 4 + 5 + 6)

        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)


#######################################################################
class TestAbjurer(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Abjurer(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.NATURE,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_light(self):
        self.assertTrue(self.c.has_ability(Ability.ABJURATION_SAVANT))


#######################################################################
class TestDiviner(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Diviner(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.NATURE,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_life(self):
        self.assertTrue(self.c.has_ability(Ability.DIVINATION_SAVANT))


#######################################################################
class TestEvoker(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Evoker(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.NATURE,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_trickery(self):
        self.assertTrue(self.c.has_ability(Ability.EVOCATION_SAVANT))


#######################################################################
class TestIllusionist(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Illusionist(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.NATURE,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_war(self):
        self.assertTrue(self.c.has_ability(Ability.ILLUSION_SAVANT))


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
