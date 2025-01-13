import unittest

from charsheets.classes import Paladin, PaladinOathOfDevotion, PaladinOathOfVengeance, PaladinOathOfAncients, PaladinOathOfGlory
from charsheets.constants import Skill, Stat, Ability, Proficiency
from charsheets.feats import AbilityScoreImprovement
from charsheets.spells import Spells
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestPaladin(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Paladin(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.RELIGION,
            Skill.PERSUASION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_basic(self):
        self.assertEqual(self.c.hit_dice, 10)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CHARISMA))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertEqual(int(self.c.hp), 10)
        self.assertIn(Spells.WRATHFUL_SMITE, self.c.spells_of_level(1))

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 10)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertTrue(self.c.has_ability(Ability.PALADINS_SMITE))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertEqual(self.c.spell_slots(2), 0)
        self.assertIn(Spells.SEARING_SMITE, self.c.spells_of_level(1))

    ###################################################################
    def test_level4(self):
        self.c.level4(hp=5 + 6, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION, self.c))

        self.assertEqual(self.c.level, 4)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertEqual(self.c.spell_slots(2), 0)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertTrue(self.c.has_ability(Ability.FAITHFUL_STEED))
        self.assertTrue(self.c.has_ability(Ability.EXTRA_ATTACK))
        self.assertIn(Spells.SEARING_SMITE, self.c.spells_of_level(1))
        self.assertIn(Spells.ZONE_OF_TRUTH, self.c.spells_of_level(2))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=9)

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertTrue(self.c.has_ability(Ability.AURA_OF_PROTECTION))


#######################################################################
class TestOathOfGlory(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = PaladinOathOfGlory(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERSUASION,
            Skill.INSIGHT,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_glory(self):
        self.assertIn(Spells.GUIDING_BOLT, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.PEERLESS_ATHLETE))
        self.assertTrue(self.c.has_ability(Ability.INSPIRING_SMITE))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.MAGIC_WEAPON, self.c.prepared_spells)


#######################################################################
class TestOathOfDevotion(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = PaladinOathOfDevotion(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ATHLETICS,
            Skill.MEDICINE,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_devotion(self):
        self.assertIn(Spells.SHIELD_OF_FAITH, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.SACRED_WEAPON))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.ZONE_OF_TRUTH, self.c.prepared_spells)


#######################################################################
class TestOathOfAncients(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = PaladinOathOfAncients(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.MEDICINE,
            Skill.ATHLETICS,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_ancients(self):
        self.assertIn(Spells.ENSNARING_STRIKE, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.NATURES_WRATH))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.MOONBEAM, self.c.prepared_spells)


#######################################################################
class TestOathOfVengeance(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = PaladinOathOfVengeance(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.INSIGHT,
            Skill.RELIGION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_vengeance(self):
        self.assertIn(Spells.HUNTERS_MARK, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.VOW_OF_EMNITY))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.MISTY_STEP, self.c.prepared_spells)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
