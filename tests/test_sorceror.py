import unittest

from charsheets.classes import Sorcerer, SorcererDraconic, SorcererClockwork, SorcererAberrant, SorcererWildMagic
from charsheets.constants import Skill, Stat, Ability, Proficiency
from charsheets.main import render
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestWizard(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Sorcerer(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.INTIMIDATION,
            strength=10,
            dexterity=13,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=15,
        )

    ###################################################################
    def test_basic(self):
        self.assertEqual(self.c.hit_dice, 6)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CONSTITUTION))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CHARISMA))
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
        self.assertTrue(self.c.has_ability(Ability.INNATE_SORCERY))
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\SpellcastingAbility{Charisma}", output)
        self.assertIn(r"Sourcery Points: 0", output)

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 6 + 4)  # 4 for CON
        self.assertIn("level 2 (5)", self.c.hp.reason)
        self.assertIn("Level 1 (6)", self.c.hp.reason)

        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_ability(Ability.FONT_OF_MAGIC))
        self.assertTrue(self.c.has_ability(Ability.METAMAGIC))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=9)

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"Sourcery Points: 3", output)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertTrue(self.c.has_ability(Ability.SORCEROUS_RESTORATION))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=9)
        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=9)
        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 1)


#######################################################################
class TestAberrant(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = SorcererAberrant(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.PERSUASION,
            strength=10,
            dexterity=13,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=15,
        )

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=1)
        self.assertTrue(self.c.has_ability(Ability.TELEPATHIC_SPEECH))
        self.assertTrue(Spell.ARMS_OF_HADAR in self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1)
        self.assertTrue(Spell.HUNGER_OF_HADAR in self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)
        self.assertTrue(self.c.has_ability(Ability.PSIONIC_SORCERY))
        self.assertTrue(self.c.has_ability(Ability.PSYCHIC_DEFENSES))

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1)
        self.assertTrue(Spell.EVARDS_BLACK_TENTACLES in self.c.prepared_spells)
        self.assertTrue(Spell.SENDING in self.c.prepared_spells)


#######################################################################
class TestClockwork(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = SorcererClockwork(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.DECEPTION,
            strength=10,
            dexterity=13,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=15,
        )

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=3)
        self.assertTrue(self.c.has_ability(Ability.CLOCKWORK_SPELLS))
        self.assertTrue(Spell.ALARM in self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.RESTORE_BALANCE))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1)
        self.assertTrue(Spell.PROTECTION_FROM_ENERGY in self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)
        self.assertTrue(self.c.has_ability(Ability.BASTION_OF_LAW))

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1)
        self.assertTrue(Spell.FREEDOM_OF_MOVEMENT in self.c.prepared_spells)
        self.assertTrue(Spell.SUMMON_CONSTRUCT in self.c.prepared_spells)


#######################################################################
class TestDraconic(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = SorcererDraconic(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.INSIGHT,
            strength=10,
            dexterity=13,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=15,
        )

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=3)
        self.assertTrue(self.c.has_ability(Ability.DRACONIC_RESILIENCE))
        self.assertTrue(Spell.CHROMATIC_ORB in self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1)
        self.assertTrue(Spell.FEAR in self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)
        self.assertTrue(self.c.has_ability(Ability.ELEMENTAL_AFFINITY))

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1)
        self.assertTrue(Spell.ARCANE_EYE in self.c.prepared_spells)
        self.assertTrue(Spell.CHARM_MONSTER in self.c.prepared_spells)


#######################################################################
class TestWildMagic(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = SorcererWildMagic(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=10,
            dexterity=13,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=15,
        )

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertTrue(self.c.has_ability(Ability.WILD_MAGIC_SURGE))
        self.assertTrue(self.c.has_ability(Ability.TIDES_OF_CHAOS))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)
        self.assertTrue(self.c.has_ability(Ability.BEND_LUCK))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
