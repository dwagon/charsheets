import unittest

from charsheets.ability_score import AbilityScore
from charsheets.character import Character
from charsheets.classes import (
    Cleric,
    ClericLifeDomain,
    ClericLightDomain,
    ClericTrickeryDomain,
    ClericWarDomain,
    DivineProtector,
    Thaumaturge,
)
from charsheets.constants import Skill, Stat, Feature, Proficiency, Language
from charsheets.features import AbilityScoreImprovement
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin, DummyCharClass


#######################################################################
class TestCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.c.add_level(Cleric(hp=1))
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertEqual(self.c.max_hit_dice, "1d7 + 1d8")

    ###################################################################
    def test_basic(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))

        self.assertEqual(self.c.max_hit_dice, "1d8")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CHARISMA))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertEqual(self.c.spell_casting_ability, Stat.WISDOM)

    ###################################################################
    def test_level1(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))

        self.assertEqual(self.c.level, 1)
        self.assertEqual(int(self.c.hp), 8 + 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertIn(Spell.BANE, [_[0] for _ in self.c.spells_of_level(1)])

    ###################################################################
    def test_protector(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))

        self.c.add_feature(DivineProtector())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())

    ###################################################################
    def test_thaumaturge(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))

        self.assertEqual(int(self.c.religion.modifier), 2)
        self.assertEqual(int(self.c.arcana.modifier), 0)

        self.c.add_feature(Thaumaturge())
        self.assertEqual(int(self.c.religion.modifier), 4)
        self.assertEqual(int(self.c.arcana.modifier), 2)
        self.assertIn("thaumaturge (2)", self.c.religion.modifier.reason)
        self.c.stats[Stat.WISDOM] = AbilityScore(Stat.WISDOM, self.c, 3)
        self.assertIn("thaumaturge (1)", self.c.religion.modifier.reason)

    ###################################################################
    def test_level2(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))

        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8 + 2)  # 2 for CON
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_feature(Feature.CHANNEL_DIVINITY_CLERIC))

    ###################################################################
    def test_level3(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(Cleric(hp=1))

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertIn(Spell.LOCATE_OBJECT, [_[0] for _ in self.c.spells_of_level(2)])

    ###################################################################
    def test_level5(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertTrue(self.c.has_feature(Feature.SEAR_UNDEAD))

        self.assertIn(Spell.WATER_WALK, [_[0] for _ in self.c.spells_of_level(3)])

    ###################################################################
    def test_sear_undead(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))

        su = self.c.find_feature(Feature.SEAR_UNDEAD)
        self.assertIn("roll 2d8", su.desc)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 1)
        self.assertIn(Spell.AURA_OF_LIFE, [_[0] for _ in self.c.spells_of_level(4)])

    ###################################################################
    def test_channel_divinity(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))

        self.assertFalse(self.c.has_feature(Feature.CHANNEL_DIVINITY_CLERIC))
        self.c.add_level(Cleric(hp=5))
        self.assertTrue(self.c.has_feature(Feature.CHANNEL_DIVINITY_CLERIC))
        cd = self.c.find_feature(Feature.CHANNEL_DIVINITY_CLERIC)
        self.assertIn("Roll 1d8", cd.desc)
        self.assertEqual(cd.goes, 2)
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.assertIn("Roll 2d8", cd.desc)
        self.assertEqual(cd.goes, 3)

    ###################################################################
    def test_level8(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))

        self.assertEqual(self.c.level, 8)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 2)
        self.assertIn(Spell.AURA_OF_LIFE, [_[0] for _ in self.c.spells_of_level(4)])

    ###################################################################
    def test_level9(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))

        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.max_spell_level(), 5)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 1)
        self.assertIn(Spell.CIRCLE_OF_POWER, [_[0] for _ in self.c.spells_of_level(5)])

    ###################################################################
    def test_level10(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertEqual(self.c.max_spell_level(), 5)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertTrue(self.c.has_feature(Feature.DIVINE_INTERVENTION))

    ###################################################################
    def test_level11(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertEqual(self.c.max_spell_level(), 6)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertEqual(self.c.spell_slots(6), 1)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1))
        self.c.add_level(Cleric(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(Cleric(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.max_spell_level(), 7)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 3)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertEqual(self.c.spell_slots(6), 1)
        self.assertEqual(self.c.spell_slots(7), 1)

        cd = self.c.find_feature(Feature.CHANNEL_DIVINITY_CLERIC)
        self.assertIn("Roll 3d8", cd.desc)
        self.assertEqual(cd.goes, 3)


#######################################################################
class TestLightDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_light(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericLightDomain(hp=1))

        self.assertIn(Spell.BURNING_HANDS, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.RADIANCE_OF_THE_DAWN))
        self.assertTrue(self.c.has_feature(Feature.WARDING_FLARE))
        wf = self.c.find_feature(Feature.WARDING_FLARE)
        self.assertEqual(wf.goes, 2)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericLightDomain(hp=1))
        self.c.add_level(ClericLightDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericLightDomain(hp=1))

        self.assertIn(Spell.FIREBALL, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericLightDomain(hp=1))
        self.c.add_level(ClericLightDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericLightDomain(hp=1))
        self.c.add_level(ClericLightDomain(hp=1))

        self.assertTrue(self.c.has_feature(Feature.IMPROVED_WARDING_FLARE))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericLightDomain(hp=1))
        self.c.add_level(ClericLightDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericLightDomain(hp=1))
        self.c.add_level(ClericLightDomain(hp=1))
        self.c.add_level(ClericLightDomain(hp=1))

        self.assertIn(Spell.ARCANE_EYE, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericLightDomain(hp=1))
        self.c.add_level(ClericLightDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericLightDomain(hp=1))
        self.c.add_level(ClericLightDomain(hp=1))
        self.c.add_level(ClericLightDomain(hp=1))
        self.c.add_level(ClericLightDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericLightDomain(hp=1))

        self.assertIn(Spell.FLAME_STRIKE, self.c.prepared_spells)
        self.assertIn(Spell.SCRYING, self.c.prepared_spells)


#######################################################################
class TestLifeDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_life(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericLifeDomain(hp=1))

        self.assertIn(Spell.LESSER_RESTORATION, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.PRESERVE_LIFE))

    ###################################################################
    def test_preserve_life(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericLifeDomain(hp=1))

        pl = self.c.find_feature(Feature.PRESERVE_LIFE)
        self.assertIn("restore 15 Hit Points", pl.desc)
        self.c.add_level(ClericLifeDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.assertIn("restore 30 Hit Points", pl.desc)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.c.add_level(ClericLifeDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericLifeDomain(hp=1))

        self.assertIn(Spell.MASS_HEALING_WORD, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.c.add_level(ClericLifeDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.c.add_level(ClericLifeDomain(hp=1))

        self.assertTrue(self.c.has_feature(Feature.BLESSED_HEALER))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.c.add_level(ClericLifeDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.c.add_level(ClericLifeDomain(hp=1))

        self.assertIn(Spell.DEATH_WARD, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.c.add_level(ClericLifeDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.c.add_level(ClericLifeDomain(hp=1))
        self.c.add_level(ClericLifeDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.assertNotIn(Spell.GREATER_RESTORATION, self.c.prepared_spells)

        self.c.add_level(ClericLifeDomain(hp=1))
        self.assertIn(Spell.GREATER_RESTORATION, self.c.prepared_spells)
        self.assertIn(Spell.MASS_CURE_WOUNDS, self.c.prepared_spells)


#######################################################################
class TestTrickeryDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_trickery(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericTrickeryDomain(hp=1))

        self.assertIn(Spell.PASS_WITHOUT_TRACE, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.BLESSING_OF_THE_TRICKSTER))

    ###################################################################
    def test_level5(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericTrickeryDomain(hp=1))
        self.c.add_level(ClericTrickeryDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericTrickeryDomain(hp=1))

        self.assertIn(Spell.HYPNOTIC_PATTERN, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericTrickeryDomain(hp=1))
        self.c.add_level(ClericTrickeryDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericTrickeryDomain(hp=1))
        self.c.add_level(ClericTrickeryDomain(hp=1))

        self.assertTrue(self.c.has_feature(Feature.TRICKSTERS_TRANSPOSITION))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericTrickeryDomain(hp=1))
        self.c.add_level(ClericTrickeryDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericTrickeryDomain(hp=1))
        self.c.add_level(ClericTrickeryDomain(hp=1))
        self.c.add_level(ClericTrickeryDomain(hp=1))

        self.assertIn(Spell.CONFUSION, self.c.prepared_spells)
        self.assertIn(Spell.DIMENSION_DOOR, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericTrickeryDomain(hp=1))
        self.c.add_level(ClericTrickeryDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericTrickeryDomain(hp=1))
        self.c.add_level(ClericTrickeryDomain(hp=1))
        self.c.add_level(ClericTrickeryDomain(hp=1))
        self.c.add_level(ClericTrickeryDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericTrickeryDomain(hp=1))

        self.assertIn(Spell.DOMINATE_PERSON, self.c.prepared_spells)
        self.assertIn(Spell.MODIFY_MEMORY, self.c.prepared_spells)


#######################################################################
class TestWarDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_war(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericWarDomain(hp=1))

        self.assertIn(Spell.SPIRITUAL_WEAPON, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.WAR_PRIEST))

    ###################################################################
    def test_war_priest(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericWarDomain(hp=1))

        wp = self.c.find_feature(Feature.WAR_PRIEST)
        self.assertIn("2 times", wp.desc)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericWarDomain(hp=1))
        self.c.add_level(ClericWarDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericWarDomain(hp=1))

        self.assertIn(Spell.CRUSADERS_MANTLE, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericWarDomain(hp=1))
        self.c.add_level(ClericWarDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericWarDomain(hp=1))
        self.c.add_level(ClericWarDomain(hp=1))

        self.assertTrue(self.c.has_feature(Feature.WAR_GODS_BLESSING))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericWarDomain(hp=1))
        self.c.add_level(ClericWarDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericWarDomain(hp=1))
        self.c.add_level(ClericWarDomain(hp=1))
        self.c.add_level(ClericWarDomain(hp=1))

        self.assertIn(Spell.FIRE_SHIELD, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.c.add_level(Cleric(hp=5))
        self.c.add_level(ClericWarDomain(hp=1))
        self.c.add_level(ClericWarDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericWarDomain(hp=1))
        self.c.add_level(ClericWarDomain(hp=1))
        self.c.add_level(ClericWarDomain(hp=1))
        self.c.add_level(ClericWarDomain(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
        self.c.add_level(ClericWarDomain(hp=1))

        self.assertIn(Spell.HOLD_MONSTER, self.c.prepared_spells)
        self.assertIn(Spell.STEEL_WIND_STRIKE, self.c.prepared_spells)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
