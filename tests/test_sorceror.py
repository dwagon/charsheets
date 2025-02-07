import unittest

from charsheets.armour import HalfPlate
from charsheets.classes import (
    Sorcerer,
    SorcererDraconic,
    SorcererClockwork,
    SorcererAberrant,
    SorcererWildMagic,
    ElementalAffinity,
    DistantSpell,
    EmpoweredSpell,
)
from charsheets.constants import Skill, Stat, Feature, Proficiency, Armour, DamageType
from charsheets.exception import NotDefined, InvalidOption
from charsheets.main import render
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestSorcerer(unittest.TestCase):
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
        self.c.level1()
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertTrue(self.c.has_feature(Feature.INNATE_SORCERY))
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\SpellcastingAbility{Charisma}", output)
        self.assertIn(r"Sorcery Points: 0", output)

    ###################################################################
    def test_level2(self):
        self.c.level1()
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 6 + 4)  # 4 for CON
        self.assertIn("level 2 (5)", self.c.hp.reason)
        self.assertIn("level 1 (6)", self.c.hp.reason)

        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_feature(Feature.FONT_OF_MAGIC))
        self.assertTrue(self.c.has_feature(Feature.METAMAGIC))

    ###################################################################
    def test_metamagic(self):
        self.c.level2(hp=1, force=True)
        self.c.add_metamagic(DistantSpell(), EmpoweredSpell())
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"Distant Spell", output)
        self.assertIn(r"Empowered Spell", output)

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=1, force=True)

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"Sorcery Points: 3", output)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)

    ###################################################################
    def test_sorcerous_restoration(self):
        self.c.level5(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.SORCEROUS_RESTORATION))
        sr = self.c.find_feature(Feature.SORCEROUS_RESTORATION)
        self.assertIn("expended up to 2 Sorcery", sr.desc)

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
        self.assertIn(Spell.VITRIOLIC_SPHERE, self.c.known_spells)

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.max_spell_level(), 5)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 1)
        self.assertEqual(self.c.sorcery_points, 9)
        self.assertIn(Spell.CLOUDKILL, self.c.known_spells)


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
        self.c.level3(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.TELEPATHIC_SPEECH))
        self.assertTrue(Spell.ARMS_OF_HADAR in self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertTrue(Spell.HUNGER_OF_HADAR in self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.PSIONIC_SORCERY))

    ###################################################################
    def test_psychic_defenses(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.PSYCHIC_DEFENSES))
        self.assertIn(DamageType.PSYCHIC, self.c.damage_resistances)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertTrue(Spell.EVARDS_BLACK_TENTACLES in self.c.prepared_spells)
        self.assertTrue(Spell.SENDING in self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertTrue(Spell.RARYS_TELEPATHIC_BOND in self.c.prepared_spells)
        self.assertTrue(Spell.TELEKINESIS in self.c.prepared_spells)


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
        self.c.level3(hp=3, force=True)
        self.assertTrue(self.c.has_feature(Feature.CLOCKWORK_SPELLS))
        self.assertTrue(Spell.ALARM in self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.RESTORE_BALANCE))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertTrue(Spell.PROTECTION_FROM_ENERGY in self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.BASTION_OF_LAW))

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertTrue(Spell.FREEDOM_OF_MOVEMENT in self.c.prepared_spells)
        self.assertTrue(Spell.SUMMON_CONSTRUCT in self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertTrue(Spell.GREATER_RESTORATION in self.c.prepared_spells)
        self.assertTrue(Spell.WALL_OF_FORCE in self.c.prepared_spells)


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
        self.c.level3(hp=3, force=True)
        self.assertTrue(Spell.CHROMATIC_ORB in self.c.prepared_spells)

    ###################################################################
    def test_draconic_resilience(self):
        self.c.level3(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.DRACONIC_RESILIENCE))
        self.assertIn("Draconic Resilience (3)", self.c.hp.reason)
        self.assertEqual(self.c.armour.tag, Armour.NONE)
        self.assertIn("Draconic Resilience (2)", self.c.ac.reason)
        self.assertEqual(int(self.c.ac), 13)
        self.c.wear_armour(HalfPlate())
        self.assertNotIn("Draconic Resilience (2)", self.c.ac.reason)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertTrue(Spell.FEAR in self.c.prepared_spells)

    ###################################################################
    def test_elemental_affinity(self):
        with self.assertRaises(NotDefined):
            self.c.level6(hp=1, force=True)
        with self.assertRaises(NotDefined):
            self.c.level6(hp=1, feature=1, force=True)
        with self.assertRaises(InvalidOption):
            self.c.level6(hp=1, feature=ElementalAffinity(DamageType.BLUDGEONING), force=True)

        self.c.level6(hp=1, feature=ElementalAffinity(DamageType.FIRE), force=True)
        self.assertTrue(self.c.has_feature(Feature.ELEMENTAL_AFFINITY))
        self.assertIn(DamageType.FIRE, self.c.damage_resistances)
        ef = self.c.find_feature(Feature.ELEMENTAL_AFFINITY)
        self.assertIn("deals Fire damage", ef.desc)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertTrue(Spell.ARCANE_EYE in self.c.prepared_spells)
        self.assertTrue(Spell.CHARM_MONSTER in self.c.prepared_spells)
        self.assertIn("Draconic Resilience (7)", self.c.hp.reason)

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertTrue(Spell.LEGEND_LORE in self.c.prepared_spells)
        self.assertTrue(Spell.SUMMON_DRAGON in self.c.prepared_spells)


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
        self.c.level3(hp=5 + 6, force=True)
        self.assertTrue(self.c.has_feature(Feature.WILD_MAGIC_SURGE))
        self.assertTrue(self.c.has_feature(Feature.TIDES_OF_CHAOS))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.BEND_LUCK))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
