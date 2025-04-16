import unittest
from typing import cast

from charsheets.armour import HalfPlate
from charsheets.character import Character
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
from charsheets.classes.sorcerer.metamagic import MetamagicNames, QuickenedSpell, BaseMetamagic
from charsheets.classes.sorcerer.sorcerer import MetaMagic
from charsheets.constants import Skill, Stat, Feature, Proficiency, Armour, DamageType, Language, CharacterClass
from charsheets.exception import NotDefined, InvalidOption
from charsheets.features import AbilityScoreImprovement
from charsheets.main import render
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin, DummyCharClass


#######################################################################
class TestSorcerer(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=10,
            dexterity=13,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=15,
        )

    ###################################################################
    def test_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.c.add_level(Sorcerer(hp=1))
        self.assertEqual(self.c.max_hit_dice, "1d7 + 1d6")

    ###################################################################
    def test_basic(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.assertEqual(self.c.max_hit_dice, "1d6")
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
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))

        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertTrue(self.c.has_feature(Feature.INNATE_SORCERY))
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\SpellcastingAbility{Charisma}", output)
        self.assertIn(r"Sorcery Points: 0", output)

    ###################################################################
    def test_level2(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=5))

        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 6 + 4)  # 4 for CON
        self.assertIn("level 2 (5)", self.c.hp.reason)
        self.assertIn("level 1 (6)", self.c.hp.reason)

        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_feature(Feature.FONT_OF_MAGIC))
        self.assertTrue(self.c.has_feature(Feature.METAMAGIC))

    ###################################################################
    def test_metamagic(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1, add_metamagic=[DistantSpell(), EmpoweredSpell()]))

        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"Distant Spell", output)
        self.assertIn(r"Empowered Spell", output)
        mm = cast(MetaMagic, self.c.find_feature(Feature.METAMAGIC))
        self.assertEqual(mm.num_options, 2)
        self.assertIn("gain 2 Metamagic options", mm.desc)

    ###################################################################
    def test_add_metamagic(self):
        self.c.add_level(Sorcerer(skills=[]))
        self.assertEqual(len(self.c.specials[CharacterClass.SORCERER]), 0)
        self.c.add_level(Sorcerer(hp=1, add_metamagic=[DistantSpell(), EmpoweredSpell()]))
        self.assertEqual(len(self.c.specials[CharacterClass.SORCERER]), 2)
        tags = [_.tag for _ in self.c.specials[CharacterClass.SORCERER]]
        self.assertIn(MetamagicNames.DISTANT_SPELL, tags)
        self.assertIn(MetamagicNames.EMPOWERED_SPELL, tags)
        self.c.add_level(Sorcerer(hp=1, add_metamagic=QuickenedSpell()))
        self.assertEqual(len(self.c.specials[CharacterClass.SORCERER]), 3)

    ###################################################################
    def test_remove_metamagic(self):
        self.c.add_level(Sorcerer(skills=[]))
        self.c.add_level(Sorcerer(hp=1, add_metamagic=[DistantSpell(), EmpoweredSpell()]))
        self.assertEqual(len(self.c.specials[CharacterClass.SORCERER]), 2)
        tags = [_.tag for _ in self.c.specials[CharacterClass.SORCERER]]
        self.assertIn(MetamagicNames.DISTANT_SPELL, tags)
        self.assertIn(MetamagicNames.EMPOWERED_SPELL, tags)

        self.c.add_level(Sorcerer(hp=1, remove_metamagic=[EmpoweredSpell()]))
        tags = [_.tag for _ in self.c.specials[CharacterClass.SORCERER]]
        self.assertEqual(len(self.c.specials[CharacterClass.SORCERER]), 1)
        self.assertNotIn(MetamagicNames.EMPOWERED_SPELL, tags)
        self.assertIn(MetamagicNames.DISTANT_SPELL, tags)

    ###################################################################
    def test_level3(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"Sorcery Points: 3", output)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)

    ###################################################################
    def test_sorcerous_restoration(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))

        self.assertTrue(self.c.has_feature(Feature.SORCEROUS_RESTORATION))
        sr = self.c.find_feature(Feature.SORCEROUS_RESTORATION)
        self.assertIn("expended up to 2 Sorcery", sr.desc)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 1)
        self.assertIn(Spell.VITRIOLIC_SPHERE, self.c.known_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))

        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 1)
        self.assertEqual(self.c.sorcerer.sorcery_points, 9)
        self.assertIn(Spell.CLOUDKILL, self.c.known_spells)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertEqual(self.c.sorcerer.sorcery_points, 10)
        mm = cast(MetaMagic, self.c.find_feature(Feature.METAMAGIC))
        self.assertEqual(mm.num_options, 4)

    ###################################################################
    def test_level11(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertEqual(self.c.spell_slots(6), 1)
        self.assertEqual(self.c.sorcerer.sorcery_points, 11)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(Sorcerer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(Sorcerer(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertEqual(self.c.spell_slots(6), 1)
        self.assertEqual(self.c.spell_slots(7), 1)
        self.assertEqual(self.c.sorcerer.sorcery_points, 13)


#######################################################################
class TestAberrant(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=10,
            dexterity=13,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=15,
        )

    ###################################################################
    def test_level3(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))
        self.assertTrue(self.c.has_feature(Feature.TELEPATHIC_SPEECH))
        self.assertTrue(Spell.ARMS_OF_HADAR in self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererAberrant(hp=1))

        self.assertTrue(Spell.HUNGER_OF_HADAR in self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))

        self.assertTrue(self.c.has_feature(Feature.PSIONIC_SORCERY))

    ###################################################################
    def test_psychic_defenses(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))
        self.assertTrue(self.c.has_feature(Feature.PSYCHIC_DEFENSES))
        self.assertIn(DamageType.PSYCHIC, self.c.damage_resistances)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))

        self.assertTrue(Spell.EVARDS_BLACK_TENTACLES in self.c.prepared_spells)
        self.assertTrue(Spell.SENDING in self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1))
        self.c.add_level(SorcererAberrant(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererAberrant(hp=1))

        self.assertTrue(Spell.RARYS_TELEPATHIC_BOND in self.c.prepared_spells)
        self.assertTrue(Spell.TELEKINESIS in self.c.prepared_spells)


#######################################################################
class TestClockwork(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=10,
            dexterity=13,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=15,
        )

    ###################################################################
    def test_level3(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererClockwork(hp=1))

        self.assertTrue(self.c.has_feature(Feature.CLOCKWORK_SPELLS))
        self.assertTrue(Spell.ALARM in self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.RESTORE_BALANCE))

    ###################################################################
    def test_level5(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererClockwork(hp=1))
        self.c.add_level(SorcererClockwork(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererClockwork(hp=1))

        self.assertTrue(Spell.PROTECTION_FROM_ENERGY in self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererClockwork(hp=1))
        self.c.add_level(SorcererClockwork(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererClockwork(hp=1))
        self.c.add_level(SorcererClockwork(hp=1))

        self.assertTrue(self.c.has_feature(Feature.BASTION_OF_LAW))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererClockwork(hp=1))
        self.c.add_level(SorcererClockwork(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererClockwork(hp=1))
        self.c.add_level(SorcererClockwork(hp=1))
        self.c.add_level(SorcererClockwork(hp=1))

        self.assertIn(Spell.FREEDOM_OF_MOVEMENT, self.c.prepared_spells)
        self.assertIn(Spell.SUMMON_CONSTRUCT, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererClockwork(hp=1))
        self.c.add_level(SorcererClockwork(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererClockwork(hp=1))
        self.c.add_level(SorcererClockwork(hp=1))
        self.c.add_level(SorcererClockwork(hp=1))
        self.c.add_level(SorcererClockwork(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererClockwork(hp=1))

        self.assertTrue(Spell.GREATER_RESTORATION in self.c.prepared_spells)
        self.assertTrue(Spell.WALL_OF_FORCE in self.c.prepared_spells)


#######################################################################
class TestDraconic(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=10,
            dexterity=13,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=15,
        )

    ###################################################################
    def test_level3(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererDraconic(hp=1))

        self.assertTrue(Spell.CHROMATIC_ORB in self.c.prepared_spells)

    ###################################################################
    def test_draconic_resilience(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererDraconic(hp=1))

        self.assertTrue(self.c.has_feature(Feature.DRACONIC_RESILIENCE))
        self.assertIn("Draconic Resilience (3)", self.c.hp.reason)
        self.assertEqual(self.c.armour.tag, Armour.NONE)
        self.assertIn("Draconic Resilience (2)", self.c.ac.reason)
        self.assertEqual(int(self.c.ac), 13)
        self.c.wear_armour(HalfPlate())
        self.assertNotIn("Draconic Resilience (2)", self.c.ac.reason)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererDraconic(hp=1))
        self.c.add_level(SorcererDraconic(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererDraconic(hp=1))

        self.assertTrue(Spell.FEAR in self.c.prepared_spells)

    ###################################################################
    def test_elemental_affinity(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererDraconic(hp=1))
        self.c.add_level(SorcererDraconic(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererDraconic(hp=1))
        self.c.add_level(SorcererDraconic(hp=1, feat=ElementalAffinity(DamageType.FIRE)))

        self.assertTrue(self.c.has_feature(Feature.ELEMENTAL_AFFINITY))
        self.assertIn(DamageType.FIRE, self.c.damage_resistances)
        ef = self.c.find_feature(Feature.ELEMENTAL_AFFINITY)
        self.assertIn("deals Fire damage", ef.desc)

    ###################################################################
    def test_elemental_affinity_errors(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererDraconic(hp=1))
        self.c.add_level(SorcererDraconic(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererDraconic(hp=1))

        with self.assertRaises(NotDefined):
            self.c.add_level(SorcererDraconic(hp=1))

        with self.assertRaises(InvalidOption):
            self.c.add_level(SorcererDraconic(hp=1, feat=ElementalAffinity(DamageType.BLUDGEONING)))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererDraconic(hp=1))
        self.c.add_level(SorcererDraconic(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererDraconic(hp=1))
        self.c.add_level(SorcererDraconic(hp=1, feat=ElementalAffinity(DamageType.FIRE)))
        self.c.add_level(SorcererDraconic(hp=1))

        self.assertTrue(Spell.ARCANE_EYE in self.c.prepared_spells)
        self.assertTrue(Spell.CHARM_MONSTER in self.c.prepared_spells)
        self.assertIn("Draconic Resilience (7)", self.c.hp.reason)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererDraconic(hp=1))
        self.c.add_level(SorcererDraconic(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererDraconic(hp=1))
        self.c.add_level(SorcererDraconic(hp=1, feat=ElementalAffinity(DamageType.FIRE)))
        self.c.add_level(SorcererDraconic(hp=1))
        self.c.add_level(SorcererDraconic(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererDraconic(hp=1))

        self.assertTrue(Spell.LEGEND_LORE in self.c.prepared_spells)
        self.assertTrue(Spell.SUMMON_DRAGON in self.c.prepared_spells)


#######################################################################
class TestWildMagic(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=10,
            dexterity=13,
            constitution=14,
            intelligence=8,
            wisdom=12,
            charisma=15,
        )

    ###################################################################
    def test_level3(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererWildMagic(hp=1))

        self.assertTrue(self.c.has_feature(Feature.WILD_MAGIC_SURGE))
        self.assertTrue(self.c.has_feature(Feature.TIDES_OF_CHAOS))

    ###################################################################
    def test_level6(self):
        self.c.add_level(Sorcerer(skills=[Skill.ARCANA, Skill.INTIMIDATION]))
        self.c.add_level(Sorcerer(hp=1))
        self.c.add_level(SorcererWildMagic(hp=1))
        self.c.add_level(SorcererWildMagic(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
        self.c.add_level(SorcererWildMagic(hp=1))
        self.c.add_level(SorcererWildMagic(hp=1))

        self.assertTrue(self.c.has_feature(Feature.BEND_LUCK))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
