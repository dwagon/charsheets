import unittest

from charsheets.character import Character
from charsheets.classes import (
    Ranger,
    RangerBeastMaster,
    RangerFeyWanderer,
    RangerGloomStalker,
    RangerHunter,
    DeftExplorer,
    DruidicWarrior,
)
from charsheets.constants import Skill, Stat, Feature, Proficiency, Language
from charsheets.exception import InvalidOption
from charsheets.features import Expertise, Archery, AbilityScoreImprovement
from charsheets.main import render
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin, DummyCharClass


#######################################################################
class TestRanger(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=8,
            wisdom=14,
            charisma=10,
        )

    ###################################################################
    def test_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.c.add_level(Ranger(hp=1, skills=[Skill.SURVIVAL]))
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_ranger(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.assertEqual(self.c.max_hit_dice, "1d10")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertEqual(self.c.spell_casting_ability, Stat.WISDOM)
        self.assertIn(Spell.GOODBERRY, self.c.known_spells)

    ###################################################################
    def test_renders(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\SpellcastingAbility{Wisdom}", output)

    ###################################################################
    def test_level1(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertTrue(self.c.has_feature(Feature.FAVOURED_ENEMY))
        self.assertTrue(self.c.has_feature(Feature.WEAPON_MASTERY))
        self.assertEqual(self.c.spell_slots(1), 2)

    ###################################################################
    def test_level2_missing_option(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))

        with self.assertRaises(InvalidOption):
            self.c.add_level(Ranger(hp=5))

    ###################################################################
    def test_level2_missing_deft(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        with self.assertRaises(InvalidOption):
            self.c.add_level(Ranger(hp=5, style=DruidicWarrior(Spell.MENDING, Spell.SHILLELAGH)))

    ###################################################################
    def test_level2_missing_style(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        with self.assertRaises(InvalidOption):
            self.c.add_level(
                Ranger(
                    hp=5,
                    deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA),
                )
            )

    ###################################################################
    def test_level2(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.assertNotIn(Spell.MENDING, self.c.known_spells)
        self.assertNotIn(Spell.SHILLELAGH, self.c.known_spells)
        self.assertFalse(self.c.skills[Skill.ARCANA].expert)
        self.assertNotIn(Language.DEEP_SPEECH, self.c.languages)
        self.assertNotIn(Language.PRIMORDIAL, self.c.languages)

        self.c.add_level(
            Ranger(
                hp=5,
                deft=DeftExplorer(Language.DEEP_SPEECH, Language.PRIMORDIAL, Skill.ARCANA),
                style=DruidicWarrior(Spell.MENDING, Spell.SHILLELAGH),
            )
        )
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 10 + 2)  # 2 for CON
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertTrue(self.c.has_feature(Feature.DEFT_EXPLORER))
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertIn(Language.DEEP_SPEECH, self.c.languages)
        self.assertIn(Language.PRIMORDIAL, self.c.languages)
        self.assertTrue(self.c.skills[Skill.ARCANA].expert)
        self.assertTrue(self.c.has_feature(Feature.DRUIDIC_WARRIOR))
        self.assertIn(Spell.MENDING, self.c.known_spells)
        self.assertIn(Spell.SHILLELAGH, self.c.known_spells)

    ###################################################################
    def test_level3(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(Ranger(hp=1))
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1))

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertTrue(self.c.has_feature(Feature.EXTRA_ATTACK))

    ###################################################################
    def test_level6(self):
        speed = int(self.c.speed)
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertTrue(self.c.has_feature(Feature.ROVING))
        self.assertEqual(int(self.c.speed), speed + 10)
        self.assertIn("Roving (10)", self.c.speed.reason)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))

        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertTrue(self.c.has_feature(Feature.EXPERTISE))

    ###################################################################
    def test_level10(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))
        self.c.add_level(Ranger(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertTrue(self.c.has_feature(Feature.TIRELESS))

    ###################################################################
    def test_level11(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1))
        self.c.add_level(Ranger(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(Ranger(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 1)
        self.assertTrue(self.c.has_feature(Feature.RELENTLESS_HUNTER))


###################################################################
class TestBeastMaster(unittest.TestCase):

    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=8,
            wisdom=14,
            charisma=10,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerBeastMaster(hp=1))

        self.assertTrue(self.c.has_feature(Feature.PRIMAL_COMPANION))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerBeastMaster(hp=1))
        self.c.add_level(RangerBeastMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerBeastMaster(hp=1))
        self.c.add_level(RangerBeastMaster(hp=1))
        self.c.add_level(RangerBeastMaster(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertTrue(self.c.has_feature(Feature.EXCEPTIONAL_TRAINING))

    ###################################################################
    def test_level11(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerBeastMaster(hp=1))
        self.c.add_level(RangerBeastMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerBeastMaster(hp=1))
        self.c.add_level(RangerBeastMaster(hp=1))
        self.c.add_level(RangerBeastMaster(hp=1))
        self.c.add_level(RangerBeastMaster(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerBeastMaster(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))
        self.c.add_level(RangerBeastMaster(hp=1))
        self.c.add_level(RangerBeastMaster(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertTrue(self.c.has_feature(Feature.BESTIAL_FURY))


###################################################################
class TestFeyWanderer(unittest.TestCase):

    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=8,
            wisdom=14,
            charisma=10,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerFeyWanderer(hp=1))

        self.assertEqual(self.c.level, 3)
        self.assertIn(Spell.CHARM_PERSON, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.OTHERWORLDLY_GLAMOUR))
        self.assertTrue(self.c.has_feature(Feature.DREADFUL_STRIKES))

    ###################################################################
    def test_level5(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerFeyWanderer(hp=1))

        self.assertIn(Spell.MISTY_STEP, self.c.prepared_spells)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertTrue(self.c.has_feature(Feature.BEGUILING_TWIST))

    ###################################################################
    def test_level9(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerFeyWanderer(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))

        self.assertEqual(self.c.level, 9)
        self.assertIn(Spell.SUMMON_FEY, self.c.prepared_spells)

    ###################################################################
    def test_level11(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerFeyWanderer(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertTrue(self.c.has_feature(Feature.FEY_REINFORCEMENTS))

    ###################################################################
    def test_level13(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerFeyWanderer(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1))
        self.c.add_level(RangerFeyWanderer(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerFeyWanderer(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertIn(Spell.DIMENSION_DOOR, self.c.prepared_spells)


###################################################################
class TestGloomStalker(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=8,
            wisdom=14,
            charisma=10,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.assertTrue(self.c.has_feature(Feature.DREAD_AMBUSHER))
        self.assertIn(Spell.DISGUISE_SELF, self.c.prepared_spells)
        self.assertIn("Dread Ambusher (2)", self.c.initiative.reason)
        da = self.c.find_feature(Feature.DREAD_AMBUSHER)
        self.assertEqual(da.goes, self.c.wisdom.modifier)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.assertIn(Spell.ROPE_TRICK, self.c.prepared_spells)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertTrue(self.c.has_feature(Feature.IRON_MIND))

    ###################################################################
    def test_level9(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerGloomStalker(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))

        self.assertEqual(self.c.level, 9)
        self.assertIn(Spell.FEAR, self.c.prepared_spells)

    ###################################################################
    def test_level11(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerGloomStalker(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertTrue(self.c.has_feature(Feature.STALKERS_FLURRY))

    ###################################################################
    def test_level13(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerGloomStalker(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1))
        self.c.add_level(RangerGloomStalker(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))

        self.assertNotIn(Spell.GREATER_INVISIBILITY, self.c.prepared_spells)
        self.c.add_level(RangerGloomStalker(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertIn(Spell.GREATER_INVISIBILITY, self.c.prepared_spells)


###################################################################
class TestHunter(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=8,
            wisdom=14,
            charisma=10,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerHunter(hp=1))

        self.assertTrue(self.c.has_feature(Feature.HUNTERS_PREY))
        self.assertTrue(self.c.has_feature(Feature.HUNTERS_LORE))

        self.assertEqual(self.c.spell_casting_ability, Stat.WISDOM)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerHunter(hp=1))
        self.c.add_level(RangerHunter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerHunter(hp=1))
        self.c.add_level(RangerHunter(hp=1))
        self.c.add_level(RangerHunter(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertTrue(self.c.has_feature(Feature.DEFENSIVE_TACTICS))

    ###################################################################
    def test_level11(self):
        self.c.add_level(Ranger(skills=[Skill.STEALTH, Skill.ANIMAL_HANDLING, Skill.INSIGHT]))
        self.c.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.PRIMORDIAL, Skill.ARCANA), style=Archery()))
        self.c.add_level(RangerHunter(hp=1))
        self.c.add_level(RangerHunter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerHunter(hp=1))
        self.c.add_level(RangerHunter(hp=1))
        self.c.add_level(RangerHunter(hp=1))
        self.c.add_level(RangerHunter(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(RangerHunter(hp=1, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.SURVIVAL)))
        self.c.add_level(RangerHunter(hp=1))
        self.c.add_level(RangerHunter(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertTrue(self.c.has_feature(Feature.SUPERIOR_HUNTERS_PREY))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
