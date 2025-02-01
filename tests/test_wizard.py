import unittest

from charsheets.classes import Wizard, WizardAbjurer, WizardDiviner, WizardEvoker, WizardIllusionist
from charsheets.constants import Skill, Stat, Feature, Proficiency
from charsheets.main import render
from charsheets.spell import Spell
from charsheets.weapons import Quarterstaff
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
            strength=8,
            dexterity=12,
            constitution=13,
            intelligence=15,
            wisdom=14,
            charisma=10,
        )
        self.c.add_weapon(Quarterstaff())

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
        self.c.level1()
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertEqual(int(self.c.hp), 6 + 1)  # 1 for CON

    #############################################################################
    def test_renders(self):
        self.c.level1()
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\SpellcastingAbility{Intelligence}", output)

    ###################################################################
    def test_level2(self):
        self.c.level1()
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 6 + 2)  # 2 for CON
        self.assertIn("level 2 (5)", self.c.hp.reason)
        self.assertIn("level 1 (6)", self.c.hp.reason)

        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_feature(Feature.SCHOLAR))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=1, force=True)

        self.assertEqual(self.c.level, 3)

        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 1)


#######################################################################
class TestAbjurer(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = WizardAbjurer(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.NATURE,
            strength=8,
            dexterity=12,
            constitution=13,
            intelligence=15,
            wisdom=14,
            charisma=10,
        )

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.ABJURATION_SAVANT))
        self.assertTrue(self.c.has_feature(Feature.ARCANE_WARD))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.PROJECTED_WARD))


#######################################################################
class TestDiviner(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = WizardDiviner(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.NATURE,
            strength=8,
            dexterity=12,
            constitution=13,
            intelligence=15,
            wisdom=14,
            charisma=10,
        )

    ###################################################################
    def test_level3(self):
        self.c.level = 2
        self.c.level3(hp=1)
        self.assertTrue(self.c.has_feature(Feature.DIVINATION_SAVANT))
        self.assertTrue(self.c.has_feature(Feature.PORTENT))

    ###################################################################
    def test_level6(self):
        self.c.level = 5
        self.c.level6(hp=1)
        self.assertTrue(self.c.has_feature(Feature.EXPERT_DIVINATION))


#######################################################################
class TestEvoker(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = WizardEvoker(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.NATURE,
            strength=8,
            dexterity=12,
            constitution=13,
            intelligence=15,
            wisdom=14,
            charisma=10,
        )

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.EVOCATION_SAVANT))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.SCULPT_SPELLS))


#######################################################################
class TestIllusionist(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = WizardIllusionist(
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

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.ILLUSION_SAVANT))
        self.assertTrue(self.c.has_feature(Feature.IMPROVED_ILLUSIONS))

    ###################################################################
    def test_improved_illusions(self):
        self.c.level3(hp=1, force=True)
        self.assertIn(Spell.MINOR_ILLUSION, self.c.known_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.PHANTASMAL_CREATURES))

    ###################################################################
    def test_phantasmal_creatures(self):
        self.c.level6(hp=1, force=True)
        self.assertIn(Spell.SUMMON_FEY, self.c.prepared_spells)
        self.assertIn(Spell.SUMMON_BEAST, self.c.prepared_spells)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
