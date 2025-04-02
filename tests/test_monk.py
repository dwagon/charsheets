import unittest

from charsheets.character import Character
from charsheets.classes import Monk, MonkWarriorOfMercy, MonkWarriorOfTheOpenHand, MonkWarriorOfShadow, MonkWarriorOfTheElements
from charsheets.constants import Skill, Stat, Feature, Proficiency, Tool, Language
from charsheets.features import AbilityScoreImprovement
from charsheets.main import render
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin, DummyCharClass


#######################################################################
class TestMonk(unittest.TestCase):
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
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_multi(self):
        self.c.add_level(DummyCharClass(skills=[]))
        self.assertFalse(self.c.has_feature(Feature.UNARMORED_DEFENSE_MONK))

        self.c.add_level(Monk(hp=1))
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertTrue(self.c.has_feature(Feature.UNARMORED_DEFENSE_MONK))

    ###################################################################
    def test_basic(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.assertEqual(self.c.max_hit_dice, "1d8")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.CHARISMA))
        self.assertIsNone(self.c.spell_casting_ability)
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.spell_slots(1), 0)
        self.assertTrue(self.c.has_feature(Feature.MARTIAL_ARTS))
        self.assertTrue(self.c.has_feature(Feature.UNARMORED_DEFENSE_MONK))
        self.assertEqual(self.c.monk.martial_arts_die, "d6")
        ma = self.c.find_feature(Feature.MARTIAL_ARTS)
        self.assertIn(f"Dexterity modifier ({self.c.dexterity.modifier})", ma.desc)
        self.assertEqual(self.c.monk.focus_points, 0)

    ###################################################################
    def test_unarmored_defense(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))

        ud = self.c.find_feature(Feature.UNARMORED_DEFENSE_MONK)
        expected = 10 + self.c.dexterity.modifier + self.c.wisdom.modifier
        self.assertIn(f"Armor Class equals {expected}", ud.desc)

    ###################################################################
    def test_level2(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=5))
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8 + 2)  # 2 for CON
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.MONKS_FOCUS))
        self.assertTrue(self.c.has_feature(Feature.UNARMORED_MOVEMENT))
        self.assertTrue(self.c.has_feature(Feature.UNCANNY_METABOLISM))
        self.assertTrue(self.c.speed, 30 + 10)
        self.assertEqual(self.c.monk.martial_arts_die, "d6")
        self.assertEqual(self.c.monk.monk_dc, self.c.proficiency_bonus + 8 + self.c.wisdom.modifier)

    ###################################################################
    def test_level3(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.DEFLECT_ATTACKS))
        self.assertEqual(self.c.monk.martial_arts_die, "d6")
        da = self.c.find_feature(Feature.DEFLECT_ATTACKS)
        self.assertIn("Bludgeoning", da.desc)

    ###################################################################
    def test_level4(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))

        self.assertEqual(self.c.level, 4)
        self.assertEqual(self.c.monk.martial_arts_die, "d6")

        self.assertTrue(self.c.has_feature(Feature.SLOW_FALL))

        output = render(self.c, "char_sheet.jinja")
        self.assertIn("Martial Arts Die: 1d6", output)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.monk.martial_arts_die, "d8")

        self.assertTrue(self.c.has_feature(Feature.EXTRA_ATTACK))
        self.assertTrue(self.c.has_feature(Feature.STUNNING_STRIKE))

    ###################################################################
    def test_level6(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.monk.martial_arts_die, "d8")

        self.assertTrue(self.c.has_feature(Feature.EMPOWERED_STRIKES))
        self.assertTrue(self.c.speed, 30 + 15)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.monk.martial_arts_die, "d8")

        self.assertTrue(self.c.has_feature(Feature.EVASION))
        self.assertEqual(self.c.monk.focus_points, 7)
        sf = self.c.find_feature(Feature.SLOW_FALL)
        self.assertIn("fall by 35 HP", sf.desc)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))

        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.monk.martial_arts_die, "d8")

        self.assertTrue(self.c.has_feature(Feature.ACROBATIC_MOVEMENT))
        self.assertEqual(self.c.monk.focus_points, 9)
        um = self.c.find_feature(Feature.UNARMORED_MOVEMENT)
        self.assertEqual(int(um.mod_add_movement_speed(self.c)), 15)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.monk.martial_arts_die, "d8")

        self.assertTrue(self.c.has_feature(Feature.SELF_RESTORATION))
        self.assertTrue(self.c.has_feature(Feature.HIGHTENED_FOCUS))

        self.assertEqual(self.c.monk.focus_points, 10)
        um = self.c.find_feature(Feature.UNARMORED_MOVEMENT)
        self.assertEqual(int(um.mod_add_movement_speed(self.c)), 20)

    ###################################################################
    def test_level11(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))

        self.assertEqual(self.c.level, 11)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.monk.martial_arts_die, "d10")

        self.assertEqual(self.c.monk.focus_points, 11)
        um = self.c.find_feature(Feature.UNARMORED_MOVEMENT)
        self.assertEqual(int(um.mod_add_movement_speed(self.c)), 20)

    ###################################################################
    def test_level13(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(Monk(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(Monk(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.monk.martial_arts_die, "d10")

        self.assertEqual(self.c.monk.focus_points, 13)
        um = self.c.find_feature(Feature.UNARMORED_MOVEMENT)
        self.assertEqual(int(um.mod_add_movement_speed(self.c)), 20)

        da = self.c.find_feature(Feature.DEFLECT_ATTACKS)
        self.assertNotIn("Bludgeoning", da.desc)


#######################################################################
class TestMercy(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ATHLETICS,
            Skill.STEALTH,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_level3(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfMercy(hp=1))

        self.assertTrue(self.c.has_feature(Feature.HAND_OF_HARM))
        self.assertTrue(self.c.has_feature(Feature.HAND_OF_HEALING))
        self.assertIn(Tool.HERBALISM_KIT, self.c.tool_proficiencies)
        self.assertTrue(self.c.insight.proficient)
        self.assertTrue(self.c.medicine.proficient)
        hoharm = self.c.find_feature(Feature.HAND_OF_HARM)
        self.assertNotIn("Poisoned", hoharm.desc)
        hoheal = self.c.find_feature(Feature.HAND_OF_HEALING)
        self.assertNotIn("Poisoned", hoheal.desc)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfMercy(hp=1))
        self.c.add_level(MonkWarriorOfMercy(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfMercy(hp=1))
        self.c.add_level(MonkWarriorOfMercy(hp=1))

        self.assertTrue(self.c.has_feature(Feature.PHYSICIANS_TOUCH))
        hoharm = self.c.find_feature(Feature.HAND_OF_HARM)
        self.assertIn("Poisoned", hoharm.desc)
        hoheal = self.c.find_feature(Feature.HAND_OF_HEALING)
        self.assertIn("Poisoned", hoheal.desc)

    ###################################################################
    def test_level11(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfMercy(hp=1))
        self.c.add_level(MonkWarriorOfMercy(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfMercy(hp=1))
        self.c.add_level(MonkWarriorOfMercy(hp=1))
        self.c.add_level(MonkWarriorOfMercy(hp=1))
        self.c.add_level(MonkWarriorOfMercy(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfMercy(hp=1))
        self.c.add_level(MonkWarriorOfMercy(hp=1))
        self.c.add_level(MonkWarriorOfMercy(hp=1))

        self.assertTrue(self.c.has_feature(Feature.FLURRY_OF_HEALING_AND_HARM))


#######################################################################
class TestElements(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.HISTORY,
            Skill.STEALTH,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_level3(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfTheElements(hp=1))

        self.assertTrue(self.c.has_feature(Feature.ELEMENTAL_ATTUNEMENT))
        self.assertTrue(self.c.has_feature(Feature.MANIPULATE_ELEMENTS))
        self.assertIn(Spell.ELEMENTALISM, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfTheElements(hp=1))
        self.c.add_level(MonkWarriorOfTheElements(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfTheElements(hp=1))
        self.c.add_level(MonkWarriorOfTheElements(hp=1))

        self.assertTrue(self.c.has_feature(Feature.ELEMENTAL_BURST))

    ###################################################################
    def test_level11(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfTheElements(hp=1))
        self.c.add_level(MonkWarriorOfTheElements(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfTheElements(hp=1))
        self.c.add_level(MonkWarriorOfTheElements(hp=1))
        self.c.add_level(MonkWarriorOfTheElements(hp=1))
        self.c.add_level(MonkWarriorOfTheElements(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfTheElements(hp=1))
        self.c.add_level(MonkWarriorOfTheElements(hp=1))
        self.c.add_level(MonkWarriorOfTheElements(hp=1))

        self.assertTrue(self.c.has_feature(Feature.STRIDE_OF_THE_ELEMENTS))


#######################################################################
class TestOpenHand(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.INSIGHT,
            Skill.RELIGION,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_level3(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1))

        self.assertTrue(self.c.has_feature(Feature.OPEN_HAND_TECHNIQUE))

    ###################################################################
    def test_level6(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1))

        self.assertTrue(self.c.has_feature(Feature.WHOLENESS_OF_BODY))
        wob = self.c.find_feature(Feature.WHOLENESS_OF_BODY)
        self.assertIn("1d8+2", wob.desc)

    ###################################################################
    def test_level11(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1))
        self.c.add_level(MonkWarriorOfTheOpenHand(hp=1))

        self.assertTrue(self.c.has_feature(Feature.FLEET_STEP))


#######################################################################
class TestShadow(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.HISTORY,
            Skill.ACROBATICS,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_level3(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfShadow(hp=1))

        self.assertTrue(self.c.has_feature(Feature.SHADOW_ARTS))
        self.assertIn(Spell.MINOR_ILLUSION, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfShadow(hp=1))
        self.c.add_level(MonkWarriorOfShadow(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfShadow(hp=1))
        self.c.add_level(MonkWarriorOfShadow(hp=1))

        self.assertTrue(self.c.has_feature(Feature.SHADOW_STEP))

    ###################################################################
    def test_level11(self):
        self.c.add_level(Monk(skills=[Skill.ACROBATICS, Skill.RELIGION]))
        self.c.add_level(Monk(hp=1))
        self.c.add_level(MonkWarriorOfShadow(hp=1))
        self.c.add_level(MonkWarriorOfShadow(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfShadow(hp=1))
        self.c.add_level(MonkWarriorOfShadow(hp=1))
        self.c.add_level(MonkWarriorOfShadow(hp=1))
        self.c.add_level(MonkWarriorOfShadow(hp=1, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
        self.c.add_level(MonkWarriorOfShadow(hp=1))
        self.c.add_level(MonkWarriorOfShadow(hp=1))
        self.c.add_level(MonkWarriorOfShadow(hp=1))

        self.assertTrue(self.c.has_feature(Feature.IMPROVED_SHADOW_STEP))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
