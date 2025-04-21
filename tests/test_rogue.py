import unittest

from charsheets.character import Character
from charsheets.classes import Rogue, RogueSoulknife, RogueAssassin, RogueThief, RogueArcaneTrickster
from charsheets.constants import Skill, Stat, Feature, Proficiency, Tool, Language
from charsheets.exception import InvalidOption
from charsheets.features import Expertise, AbilityScoreImprovement, BoonOfNightSpirit
from charsheets.main import render
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin, DummyCharClass


#######################################################################
class TestRogue(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.assertFalse(self.c.is_proficient(Skill.ARCANA))

        self.c.add_level(
            Rogue(
                hp=1,
                skills=[Skill.ARCANA],
                expertise=Expertise(Skill.STEALTH, Skill.SLEIGHT_OF_HAND),
                language=Language.DEEP_SPEECH,
            )
        )
        self.assertTrue(self.c.is_proficient(Skill.ARCANA))
        self.assertIn(Language.DEEP_SPEECH, self.c.languages)

    ###################################################################
    def test_multi_fail(self):
        self.c.add_level(DummyCharClass(skills=[]))

        with self.assertRaises(InvalidOption):
            self.c.add_level(
                Rogue(
                    hp=1,
                    expertise=Expertise(Skill.STEALTH, Skill.SLEIGHT_OF_HAND),
                    language=Language.DEEP_SPEECH,
                )
            )

    ###################################################################
    def test_expertise_fail(self):
        with self.assertRaises(InvalidOption):
            self.c.add_level(
                Rogue(
                    skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                    language=Language.CELESTIAL,
                )
            )

    ###################################################################
    def test_basics(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.assertEqual(self.c.max_hit_dice, "1d8")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())

        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIsNone(self.c.spell_casting_ability)

    ###################################################################
    def test_level1(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.assertEqual(self.c.level, 1)
        self.assertTrue(self.c.has_feature(Feature.SNEAK_ATTACK))
        self.assertTrue(self.c.has_feature(Feature.THIEVES_CANT))
        self.assertTrue(self.c.has_feature(Feature.EXPERTISE))
        self.assertTrue(self.c.has_feature(Feature.WEAPON_MASTERY))
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 1)
        self.assertEqual(self.c.spell_slots(1), 0)
        self.assertIn(Language.CELESTIAL, self.c.languages)
        self.assertTrue(self.c.skills[Skill.ARCANA].expert)
        self.assertFalse(self.c.skills[Skill.HISTORY].expert)
        self.assertTrue(self.c.skills[Skill.ANIMAL_HANDLING].expert)

    ###################################################################
    def test_level2(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.c.add_level(Rogue(hp=5))
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8)
        self.assertTrue(self.c.has_feature(Feature.CUNNING_ACTION))
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 1)

    ###################################################################
    def test_level3(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.c.add_level(Rogue(hp=5))
        self.c.add_level(Rogue(hp=1))

        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_feature(Feature.STEADY_AIM))
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 2)

    ###################################################################
    def level4(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.c.add_level(Rogue(hp=5))
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))

    ###################################################################
    def test_level5(self):
        self.level4()
        self.c.add_level(Rogue(hp=1))

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 3)
        self.assertTrue(self.c.has_feature(Feature.UNCANNY_DODGE))
        self.assertTrue(self.c.has_feature(Feature.CUNNING_STRIKE))
        cs = self.c.find_feature(Feature.CUNNING_STRIKE)
        dc = 8 + self.c.dexterity.modifier + self.c.proficiency_bonus
        self.assertIn(f"DC {dc}", cs.desc)

    ###################################################################
    def test_level6(self):
        self.level4()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 3)

        self.assertTrue(self.c.has_feature(Feature.EXPERTISE))

    ###################################################################
    def test_level7(self):
        self.level4()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(Rogue(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 4)
        self.assertTrue(self.c.has_feature(Feature.EVASION))
        self.assertTrue(self.c.has_feature(Feature.RELIABLE_TALENT))

    ###################################################################
    def level8(self):
        self.level4()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))

    ###################################################################
    def test_level9(self):
        self.level8()
        self.c.add_level(Rogue(hp=1))

        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 5)

    ###################################################################
    def test_level10(self):
        self.level8()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))

        self.assertEqual(self.c.level, 10)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 5)

    ###################################################################
    def test_level11(self):
        self.level8()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(Rogue(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 6)
        self.assertTrue(self.c.has_feature(Feature.IMPROVED_CUNNING_STRIKE))

    ###################################################################
    def level12(self):
        self.level8()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))

    ###################################################################
    def test_level12(self):
        self.level12()

        self.assertEqual(self.c.level, 12)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 6)

    ###################################################################
    def test_level13(self):
        self.level12()
        self.c.add_level(Rogue(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 7)

    ###################################################################
    def test_level14(self):
        self.level12()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1))

        self.assertEqual(self.c.level, 14)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 7)
        self.assertTrue(self.c.has_feature(Feature.DEVIOUS_STRIKES))

    ###################################################################
    def test_level15(self):
        self.level12()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1))

        self.assertEqual(self.c.level, 15)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 8)
        self.assertTrue(self.c.has_feature(Feature.SLIPPERY_MIND))

    ###################################################################
    def level16(self):
        self.level12()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))

    ###################################################################
    def test_level16(self):
        self.level16()

        self.assertEqual(self.c.level, 16)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 8)

    ###################################################################
    def test_level17(self):
        self.level16()
        self.c.add_level(Rogue(hp=1))

        self.assertEqual(self.c.level, 17)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 9)

    ###################################################################
    def test_level18(self):
        self.level16()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1))

        self.assertEqual(self.c.level, 18)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 9)
        self.assertTrue(self.c.has_feature(Feature.ELUSIVE))

    ###################################################################
    def test_level19(self):
        self.level16()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, boon=BoonOfNightSpirit(Stat.DEXTERITY)))

        self.assertEqual(self.c.level, 19)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 10)

    ###################################################################
    def test_level20(self):
        self.level16()
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1))
        self.c.add_level(Rogue(hp=1, boon=BoonOfNightSpirit(Stat.DEXTERITY)))
        self.c.add_level(Rogue(hp=1))

        self.assertEqual(self.c.level, 20)
        self.assertEqual(self.c.rogue.sneak_attack_dmg, 10)
        self.assertTrue(self.c.has_feature(Feature.STROKE_OF_LUCK))


###################################################################
class TestArcaneTrickster(unittest.TestCase):

    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=15,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.c.add_level(Rogue(hp=5))
        self.c.add_level(RogueArcaneTrickster(hp=1))

        self.assertTrue(self.c.has_feature(Feature.MAGE_HAND_LEGERDERMAIN))
        self.assertEqual(self.c.spell_casting_ability, Stat.INTELLIGENCE)
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\FirstLevelSpellSlotsTotal{2}", output)
        self.assertIn(r"\SpellcastingAbility{Intelligence}", output)
        self.assertIn(Spell.MAGE_HAND, self.c.known_spells)

    ###################################################################
    def level4(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.c.add_level(Rogue(hp=5))
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))

    ###################################################################
    def test_level5(self):
        self.level4()
        self.c.add_level(RogueArcaneTrickster(hp=1))

        self.assertEqual(self.c.spell_slots(1), 3)

    ###################################################################
    def test_level7(self):
        self.level4()
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(RogueArcaneTrickster(hp=1))

        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)

    ###################################################################
    def level8(self):
        self.level4()
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))

    ###################################################################
    def test_level9(self):
        self.level8()
        self.c.add_level(RogueArcaneTrickster(hp=1))

        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertTrue(self.c.has_feature(Feature.MAGICAL_AMBUSH))

    ###################################################################
    def test_level11(self):
        self.level8()
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(RogueArcaneTrickster(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)

    ###################################################################
    def test_level13(self):
        self.level8()
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueArcaneTrickster(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertTrue(self.c.has_feature(Feature.VERSATILE_TRICKSTER))

    ###################################################################
    def test_level17(self):
        self.level8()
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1))
        self.c.add_level(RogueArcaneTrickster(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueArcaneTrickster(hp=1))

        self.assertEqual(self.c.level, 17)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)
        self.assertEqual(self.c.spell_slots(4), 0)

        self.assertTrue(self.c.has_feature(Feature.SPELL_THIEF))


###################################################################
class TestAssassin(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=10,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.c.add_level(Rogue(hp=5))
        self.c.add_level(RogueAssassin(hp=1))

        self.assertTrue(self.c.has_feature(Feature.ASSASSINATE))
        self.assertTrue(self.c.has_feature(Feature.ASSASSINS_TOOLS))
        self.assertIn(Tool.POISONERS_KIT, self.c.tool_proficiencies)

    ###################################################################
    def level8(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.c.add_level(Rogue(hp=5))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))

    ###################################################################
    def test_level9(self):
        self.level8()
        self.c.add_level(RogueAssassin(hp=1))

        self.assertTrue(self.c.has_feature(Feature.INFILTRATION_EXPERTISE))

    ###################################################################
    def test_level13(self):
        self.level8()
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueAssassin(hp=1))

        self.assertTrue(self.c.has_feature(Feature.ENVENOM_WEAPONS))

    ###################################################################
    def test_level17(self):
        self.level8()
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueAssassin(hp=1))

        self.assertTrue(self.c.has_feature(Feature.DEATH_STRIKE))

    ###################################################################
    def test_level20(self):
        self.level8()
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1))
        self.c.add_level(RogueAssassin(hp=1, boon=BoonOfNightSpirit(Stat.DEXTERITY)))
        self.c.add_level(RogueAssassin(hp=1))

        self.assertEqual(self.c.level, 20)
        self.assertTrue(self.c.has_feature(Feature.STROKE_OF_LUCK))
        self.assertTrue(self.c.has_feature(Feature.ELUSIVE))
        self.assertTrue(self.c.has_feature(Feature.SLIPPERY_MIND))
        self.assertTrue(self.c.has_feature(Feature.DEVIOUS_STRIKES))
        self.assertTrue(self.c.has_feature(Feature.IMPROVED_CUNNING_STRIKE))
        self.assertTrue(self.c.has_feature(Feature.EVASION))
        self.assertTrue(self.c.has_feature(Feature.RELIABLE_TALENT))
        self.assertTrue(self.c.has_feature(Feature.EXPERTISE))
        self.assertTrue(self.c.has_feature(Feature.CUNNING_STRIKE))
        self.assertTrue(self.c.has_feature(Feature.UNCANNY_DODGE))
        self.assertTrue(self.c.has_feature(Feature.ASSASSINATE))
        self.assertTrue(self.c.has_feature(Feature.INFILTRATION_EXPERTISE))
        self.assertTrue(self.c.has_feature(Feature.ENVENOM_WEAPONS))
        self.assertTrue(self.c.has_feature(Feature.DEATH_STRIKE))


###################################################################
class TestSoulKnife(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.c.add_level(Rogue(hp=5))
        self.c.add_level(RogueSoulknife(hp=1))

        self.assertTrue(self.c.has_feature(Feature.PSYCHIC_BLADES))
        self.assertTrue(self.c.has_feature(Feature.PSIONIC_POWER_ROGUE))
        self.assertEqual(self.c.rogue.energy_dice, "4d6")
        self.assertIn("4d6", self.c.class_special)
        ppr = self.c.find_feature(Feature.PSIONIC_POWER_ROGUE)
        self.assertEqual(ppr.goes, 4)

    ###################################################################
    def level4(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.c.add_level(Rogue(hp=5))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))

    ###################################################################
    def test_level5(self):
        self.level4()
        self.c.add_level(RogueSoulknife(hp=1))

        self.assertEqual(self.c.rogue.energy_dice, "6d8")

    ###################################################################
    def test_level9(self):
        self.level4()
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueSoulknife(hp=1))

        self.assertEqual(self.c.rogue.energy_dice, "8d8")
        self.assertTrue(self.c.has_feature(Feature.SOUL_BLADES))

    ###################################################################
    def test_level11(self):
        self.level4()
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(RogueSoulknife(hp=1))

        self.assertEqual(self.c.rogue.energy_dice, "8d10")

    ###################################################################
    def test_level13(self):
        self.level4()
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueSoulknife(hp=1))

        self.assertEqual(self.c.rogue.energy_dice, "10d10")
        self.assertTrue(self.c.has_feature(Feature.PSYCHIC_VEIL))

    ###################################################################
    def test_level17(self):
        self.level4()
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1))
        self.c.add_level(RogueSoulknife(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueSoulknife(hp=1))

        self.assertEqual(self.c.rogue.energy_dice, "12d12")
        self.assertTrue(self.c.has_feature(Feature.REND_MIND))


###################################################################
class TestThief(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_basics(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.c.add_level(Rogue(hp=5))
        self.c.add_level(RogueThief(hp=1))
        self.assertTrue(self.c.has_feature(Feature.SECOND_STORY_WORK))
        self.assertTrue(self.c.has_feature(Feature.FAST_HANDS))

    ###################################################################
    def level4(self):
        self.c.add_level(
            Rogue(
                skills=[Skill.ATHLETICS, Skill.PERSUASION, Skill.INVESTIGATION, Skill.PERCEPTION],
                expertise=Expertise(Skill.ARCANA, Skill.ANIMAL_HANDLING),
                language=Language.CELESTIAL,
            )
        )
        self.c.add_level(Rogue(hp=5))
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))

    ###################################################################
    def test_level9(self):
        self.level4()
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueThief(hp=1))

        self.assertTrue(self.c.has_feature(Feature.SUPREME_SNEAK))

    ###################################################################
    def test_level13(self):
        self.level4()
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueThief(hp=1))

        self.assertTrue(self.c.has_feature(Feature.USE_MAGIC_DEVICE))

    ###################################################################
    def test_level17(self):
        self.level4()
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, expertise=Expertise(Skill.SURVIVAL, Skill.MEDICINE)))
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1))
        self.c.add_level(RogueThief(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
        self.c.add_level(RogueThief(hp=1))

        self.assertTrue(self.c.has_feature(Feature.THIEFS_REFLEXES))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
