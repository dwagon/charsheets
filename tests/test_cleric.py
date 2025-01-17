import unittest

from charsheets.ability_score import AbilityScore
from charsheets.constants import Skill, Stat, Ability, Proficiency
from charsheets.classes import Cleric, ClericLifeDomain, ClericLightDomain, ClericTrickeryDomain, ClericWarDomain
from charsheets.spells import Spells
from tests.dummy import DummySpecies, DummyOrigin
from charsheets.abilities import DivineProtector, Thaumaturge


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

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(int(self.c.hp), 8 + 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertIn(Spells.BANE, self.c.spells_of_level(1))

    ###################################################################
    def test_protector(self):
        self.c.add_ability(DivineProtector())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())

    ###################################################################
    def test_thaumaturge(self):
        self.assertEqual(int(self.c.religion.modifier), 2)
        self.assertEqual(int(self.c.arcana.modifier), 0)

        self.c.add_ability(Thaumaturge())
        self.assertEqual(int(self.c.religion.modifier), 4)
        self.assertEqual(int(self.c.arcana.modifier), 2)
        self.assertIn("thaumaturge (2)", self.c.religion.modifier.reason)
        self.c.stats[Stat.WISDOM] = AbilityScore(Stat.WISDOM, self.c, 3)
        self.assertIn("thaumaturge (1)", self.c.religion.modifier.reason)

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8 + 2)  # 2 for CON
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_ability(Ability.CHANNEL_DIVINITY))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertIn(Spells.LOCATE_OBJECT, self.c.spells_of_level(2))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=5 + 6 + 7)

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertTrue(self.c.has_ability(Ability.SEAR_UNDEAD))

        self.assertIn(Spells.WATER_WALK, self.c.spells_of_level(3))

    ###################################################################
    def test_sear_undead(self):
        self.c.level5(hp=3)
        su = self.c.find_ability(Ability.SEAR_UNDEAD)
        self.assertIn("roll 2d8", su.desc)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)


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
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_light(self):
        self.assertIn(Spells.BURNING_HANDS, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.RADIANCE_OF_THE_DAWN))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.FIREBALL, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=9)
        self.assertTrue(self.c.has_ability(Ability.IMPROVED_WARDING_FLARE))


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
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_life(self):
        self.assertIn(Spells.LESSER_RESTORATION, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.PRESERVE_LIFE))

    ###################################################################
    def test_preserve_life(self):
        pl = self.c.find_ability(Ability.PRESERVE_LIFE)
        self.assertIn("restore 15 Hit Points", pl.desc)
        self.c.level6(hp=1)
        self.assertIn("restore 30 Hit Points", pl.desc)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.MASS_HEALING_WORD, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=9)
        self.assertTrue(self.c.has_ability(Ability.BLESSED_HEALER))


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
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_trickery(self):
        self.assertIn(Spells.PASS_WITHOUT_TRACE, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.BLESSING_OF_THE_TRICKSTER))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.HYPNOTIC_PATTERN, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=9)
        self.assertTrue(self.c.has_ability(Ability.TRICKSTERS_TRANSPOSITION))


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
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_war(self):
        self.assertIn(Spells.SPIRITUAL_WEAPON, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.WAR_PRIEST))

    ###################################################################
    def test_war_priest(self):
        wp = self.c.find_ability(Ability.WAR_PRIEST)
        self.assertIn("2 times", wp.desc)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.CRUSADERS_MANTLE, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=9)
        self.assertTrue(self.c.has_ability(Ability.WAR_GODS_BLESSING))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
