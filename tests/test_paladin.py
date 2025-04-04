import unittest

from charsheets.character import Character
from charsheets.classes import Paladin, PaladinOathOfDevotion, PaladinOathOfVengeance, PaladinOathOfAncients, PaladinOathOfGlory
from charsheets.constants import Skill, Stat, Feature, Proficiency, Language
from charsheets.features import AbilityScoreImprovement
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin, DummyCharClass


#######################################################################
class TestPaladin(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=10,
            constitution=13,
            intelligence=8,
            wisdom=12,
            charisma=14,
        )

    ###################################################################
    def test_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.c.add_level(Paladin(hp=1))
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_basic(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))

        self.assertEqual(self.c.max_hit_dice, "1d10")
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
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertEqual(int(self.c.hp), 10 + 1)  # +1 for CON
        self.assertIn(Spell.WRATHFUL_SMITE, [_[0] for _ in self.c.spells_of_level(1)])
        self.assertTrue(self.c.has_feature(Feature.LAY_ON_HANDS))
        self.assertTrue(self.c.has_feature(Feature.WEAPON_MASTERY))

    ###################################################################
    def test_level2(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))

        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 10 + 2)  # +2 for CON
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertTrue(self.c.has_feature(Feature.PALADINS_SMITE))
        self.assertTrue(self.c.has_feature(Feature.FIGHTING_STYLE_PALADIN))

    ###################################################################
    def test_level3(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(Paladin(hp=1))

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertEqual(self.c.spell_slots(2), 0)
        self.assertIn(Spell.SEARING_SMITE, [_[0] for _ in self.c.spells_of_level(1)])
        self.assertTrue(self.c.has_feature(Feature.CHANNEL_DIVINITY_PALADIN))
        cd = self.c.find_feature(Feature.CHANNEL_DIVINITY_PALADIN)
        self.assertEqual(cd.goes, 2)

    ###################################################################
    def test_level4(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))

        self.assertEqual(self.c.level, 4)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertEqual(self.c.spell_slots(2), 0)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertTrue(self.c.has_feature(Feature.FAITHFUL_STEED))
        self.assertTrue(self.c.has_feature(Feature.EXTRA_ATTACK))
        self.assertIn(Spell.SEARING_SMITE, [_[0] for _ in self.c.spells_of_level(1)])
        self.assertIn(Spell.ZONE_OF_TRUTH, [_[0] for _ in self.c.spells_of_level(2)])

    ###################################################################
    def test_level6(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertTrue(self.c.has_feature(Feature.AURA_OF_PROTECTION))

    ###################################################################
    def test_aura_of_protection(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))

        aop = self.c.find_feature(Feature.AURA_OF_PROTECTION)
        self.assertIn("bonus of 2", aop.desc)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))

        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertTrue(self.c.has_feature(Feature.ABJURE_FOES))
        self.assertIn(Spell.BLINDING_SMITE, [_[0] for _ in self.c.spells_of_level(3)])

    ###################################################################
    def test_level10(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertTrue(self.c.has_feature(Feature.AURA_OF_COURAGE))

    ###################################################################
    def test_level11(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertTrue(self.c.has_feature(Feature.RADIANT_STRIKES))
        cd = self.c.find_feature(Feature.CHANNEL_DIVINITY_PALADIN)
        self.assertEqual(cd.goes, 3)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1))
        self.c.add_level(Paladin(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(Paladin(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 1)

        cd = self.c.find_feature(Feature.CHANNEL_DIVINITY_PALADIN)
        self.assertEqual(cd.goes, 3)


#######################################################################
class TestOathOfGlory(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=10,
            constitution=13,
            intelligence=8,
            wisdom=12,
            charisma=14,
        )

    ###################################################################
    def test_glory(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.assertIn(Spell.GUIDING_BOLT, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.PEERLESS_ATHLETE))
        self.assertTrue(self.c.has_feature(Feature.INSPIRING_SMITE))

    ###################################################################
    def test_level5(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfGlory(hp=1))

        self.assertIn(Spell.MAGIC_WEAPON, self.c.prepared_spells)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1))

        self.assertTrue(self.c.has_feature(Feature.AURA_OF_ALACRITY))

    ###################################################################
    def test_level9(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfGlory(hp=1))

        self.assertIn(Spell.HASTE, self.c.prepared_spells)
        self.assertIn(Spell.PROTECTION_FROM_ENERGY, self.c.prepared_spells)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1))
        self.c.add_level(PaladinOathOfGlory(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfGlory(hp=1))

        self.assertIn(Spell.FREEDOM_OF_MOVEMENT, self.c.prepared_spells)
        self.assertIn(Spell.COMPULSION, self.c.prepared_spells)


#######################################################################
class TestOathOfDevotion(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=10,
            constitution=13,
            intelligence=8,
            wisdom=12,
            charisma=14,
        )

    ###################################################################
    def test_devotion(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfDevotion(hp=1))

        self.assertIn(Spell.SHIELD_OF_FAITH, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.SACRED_WEAPON))

    ###################################################################
    def test_sacred_weapon(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfDevotion(hp=1))

        sw = self.c.find_feature(Feature.SACRED_WEAPON)
        self.assertIn("add 2,", sw.desc)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfDevotion(hp=1))

        self.assertIn(Spell.ZONE_OF_TRUTH, self.c.prepared_spells)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1))

        self.assertTrue(self.c.has_feature(Feature.AURA_OF_DEVOTION))

    ###################################################################
    def test_level9(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfDevotion(hp=1))

        self.assertIn(Spell.BEACON_OF_HOPE, self.c.prepared_spells)
        self.assertIn(Spell.DISPEL_MAGIC, self.c.prepared_spells)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1))
        self.c.add_level(PaladinOathOfDevotion(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfDevotion(hp=1))

        self.assertIn(Spell.FREEDOM_OF_MOVEMENT, self.c.prepared_spells)
        self.assertIn(Spell.GUARDIAN_OF_FAITH, self.c.prepared_spells)


#######################################################################
class TestOathOfAncients(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=10,
            constitution=13,
            intelligence=8,
            wisdom=12,
            charisma=14,
        )

    ###################################################################
    def test_ancients(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfAncients(hp=1))

        self.assertIn(Spell.ENSNARING_STRIKE, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.NATURES_WRATH))

    ###################################################################
    def test_level5(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfAncients(hp=1))

        self.assertIn(Spell.MOONBEAM, self.c.prepared_spells)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1))

        self.assertTrue(self.c.has_feature(Feature.AURA_OF_WARDING))

    ###################################################################
    def test_level9(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfAncients(hp=1))

        self.assertIn(Spell.PLANT_GROWTH, self.c.prepared_spells)
        self.assertIn(Spell.PROTECTION_FROM_ENERGY, self.c.prepared_spells)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1))
        self.c.add_level(PaladinOathOfAncients(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfAncients(hp=1))

        self.assertIn(Spell.ICE_STORM, self.c.prepared_spells)
        self.assertIn(Spell.STONESKIN, self.c.prepared_spells)


#######################################################################
class TestOathOfVengeance(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=15,
            dexterity=10,
            constitution=13,
            intelligence=8,
            wisdom=12,
            charisma=14,
        )

    ###################################################################
    def test_vengeance(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.assertIn(Spell.HUNTERS_MARK, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.VOW_OF_EMNITY))

    ###################################################################
    def test_level5(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfVengeance(hp=1))

        self.assertIn(Spell.MISTY_STEP, self.c.prepared_spells)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1))

        self.assertTrue(self.c.has_feature(Feature.RELENTLESS_AVENGER))

    ###################################################################
    def test_level9(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfVengeance(hp=1))

        self.assertIn(Spell.HASTE, self.c.prepared_spells)
        self.assertIn(Spell.PROTECTION_FROM_ENERGY, self.c.prepared_spells)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Paladin(skills=[Skill.RELIGION, Skill.PERSUASION]))
        self.c.add_level(Paladin(hp=5))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1))
        self.c.add_level(PaladinOathOfVengeance(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
        self.c.add_level(PaladinOathOfVengeance(hp=1))

        self.assertIn(Spell.BANISHMENT, self.c.prepared_spells)
        self.assertIn(Spell.DIMENSION_DOOR, self.c.prepared_spells)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
