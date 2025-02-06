import unittest

from charsheets.ability_score import AbilityScore
from charsheets.classes import (
    Cleric,
    ClericLifeDomain,
    ClericLightDomain,
    ClericTrickeryDomain,
    ClericWarDomain,
    DivineProtector,
    Thaumaturge,
)
from charsheets.constants import Skill, Stat, Feature, Proficiency
from charsheets.features import AbilityScoreImprovement
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Cleric(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERSUASION,
            Skill.RELIGION,
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_basic(self):
        self.assertEqual(self.c.hit_dice, 8)
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
        self.c.level1()
        self.assertEqual(self.c.level, 1)
        self.assertEqual(int(self.c.hp), 8 + 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertIn(Spell.BANE, self.c.spells_of_level(1))

    ###################################################################
    def test_protector(self):
        self.c.add_feature(DivineProtector())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())

    ###################################################################
    def test_thaumaturge(self):
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
        self.c.level1()
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8 + 2)  # 2 for CON
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_feature(Feature.CHANNEL_DIVINITY_CLERIC))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6, force=True)

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertIn(Spell.LOCATE_OBJECT, self.c.spells_of_level(2))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=5 + 6 + 7, force=True)

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertTrue(self.c.has_feature(Feature.SEAR_UNDEAD))

        self.assertIn(Spell.WATER_WALK, self.c.spells_of_level(3))

    ###################################################################
    def test_sear_undead(self):
        self.c.level5(hp=3, force=True)
        su = self.c.find_feature(Feature.SEAR_UNDEAD)
        self.assertIn("roll 2d8", su.desc)

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
        self.assertIn(Spell.AURA_OF_LIFE, self.c.spells_of_level(4))

    ###################################################################
    def test_channel_divinity(self):
        self.assertFalse(self.c.has_feature(Feature.CHANNEL_DIVINITY_CLERIC))
        self.c.level2(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.CHANNEL_DIVINITY_CLERIC))
        cd = self.c.find_feature(Feature.CHANNEL_DIVINITY_CLERIC)
        self.assertIn("Roll 1d8", cd.desc)
        self.assertEqual(cd.goes, 2)
        self.c.level7(hp=1, force=True)
        self.assertIn("Roll 2d8", cd.desc)
        self.assertEqual(cd.goes, 3)

    ###################################################################
    def test_level8(self):
        self.c.level8(hp=1, force=True, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.STRENGTH))

        self.assertEqual(self.c.level, 8)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 2)
        self.assertIn(Spell.AURA_OF_LIFE, self.c.spells_of_level(4))

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
        self.assertIn(Spell.CIRCLE_OF_POWER, self.c.spells_of_level(5))


#######################################################################
class TestLightDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = ClericLightDomain(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.MEDICINE,
            Skill.PERSUASION,
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_light(self):
        self.assertIn(Spell.BURNING_HANDS, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.RADIANCE_OF_THE_DAWN))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertIn(Spell.FIREBALL, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.IMPROVED_WARDING_FLARE))

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertIn(Spell.ARCANE_EYE, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertIn(Spell.FLAME_STRIKE, self.c.prepared_spells)
        self.assertIn(Spell.SCRYING, self.c.prepared_spells)


#######################################################################
class TestLifeDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = ClericLifeDomain(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.RELIGION,
            Skill.MEDICINE,
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_life(self):
        self.assertIn(Spell.LESSER_RESTORATION, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.PRESERVE_LIFE))

    ###################################################################
    def test_preserve_life(self):
        pl = self.c.find_feature(Feature.PRESERVE_LIFE)
        self.assertIn("restore 15 Hit Points", pl.desc)
        self.c.level6(hp=1, force=True)
        self.assertIn("restore 30 Hit Points", pl.desc)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertIn(Spell.MASS_HEALING_WORD, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.BLESSED_HEALER))

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertIn(Spell.DEATH_WARD, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.assertNotIn(Spell.GREATER_RESTORATION, self.c.prepared_spells)
        self.c.level9(hp=1, force=True)
        self.assertIn(Spell.GREATER_RESTORATION, self.c.prepared_spells)
        self.assertIn(Spell.MASS_CURE_WOUNDS, self.c.prepared_spells)


#######################################################################
class TestTrickeryDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = ClericTrickeryDomain(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.INSIGHT,
            Skill.RELIGION,
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_trickery(self):
        self.assertIn(Spell.PASS_WITHOUT_TRACE, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.BLESSING_OF_THE_TRICKSTER))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertIn(Spell.HYPNOTIC_PATTERN, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.TRICKSTERS_TRANSPOSITION))

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertIn(Spell.CONFUSION, self.c.prepared_spells)
        self.assertIn(Spell.DIMENSION_DOOR, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertIn(Spell.DOMINATE_PERSON, self.c.prepared_spells)
        self.assertIn(Spell.MODIFY_MEMORY, self.c.prepared_spells)


#######################################################################
class TestWarDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = ClericWarDomain(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.HISTORY,
            Skill.PERSUASION,
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )
        self.c.level3(hp=5 + 6, force=True)

    ###################################################################
    def test_war(self):
        self.assertIn(Spell.SPIRITUAL_WEAPON, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.WAR_PRIEST))

    ###################################################################
    def test_war_priest(self):
        wp = self.c.find_feature(Feature.WAR_PRIEST)
        self.assertIn("2 times", wp.desc)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9, force=True)
        self.assertIn(Spell.CRUSADERS_MANTLE, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=9, force=True)
        self.assertTrue(self.c.has_feature(Feature.WAR_GODS_BLESSING))

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertIn(Spell.FIRE_SHIELD, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertIn(Spell.HOLD_MONSTER, self.c.prepared_spells)
        self.assertIn(Spell.STEEL_WIND_STRIKE, self.c.prepared_spells)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
