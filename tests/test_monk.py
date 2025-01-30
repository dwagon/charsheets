import unittest

from charsheets.classes import Monk, MonkWarriorOfMercy, MonkWarriorOfTheOpenHand, MonkWarriorOfShadow, MonkWarriorOfTheElements
from charsheets.constants import Skill, Stat, Feature, Proficiency, Tool
from charsheets.features import AbilityScoreImprovement
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestMonk(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Monk(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ACROBATICS,
            Skill.RELIGION,
            strength=12,
            dexterity=15,
            constitution=13,
            intelligence=10,
            wisdom=14,
            charisma=8,
        )

    ###################################################################
    def test_basic(self):
        self.assertEqual(self.c.hit_dice, 8)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.CHARISMA))
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.spell_slots(1), 0)
        self.assertTrue(self.c.has_feature(Feature.MARTIAL_ARTS))
        self.assertTrue(self.c.has_feature(Feature.UNARMORED_DEFENSE_MONK))
        self.assertEqual(self.c.martial_arts_die, "d6")
        ma = self.c.find_feature(Feature.MARTIAL_ARTS)
        self.assertIn(f"Dexterity modifier ({self.c.dexterity.modifier})", ma.desc)

    ###################################################################
    def test_unarmored_defense(self):
        ud = self.c.find_feature(Feature.UNARMORED_DEFENSE_MONK)
        expected = 10 + self.c.dexterity.modifier + self.c.wisdom.modifier
        self.assertIn(f"Armor Class equals {expected}", ud.desc)

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8 + 2)  # 2 for CON
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.MONKS_FOCUS))
        self.assertTrue(self.c.has_feature(Feature.UNARMORED_MOVEMENT))
        self.assertTrue(self.c.has_feature(Feature.UNCANNY_METABOLISM))
        self.assertTrue(self.c.speed, 30 + 10)
        self.assertEqual(self.c.martial_arts_die, "d6")
        self.assertEqual(self.c.monk_dc, self.c.proficiency_bonus + 8 + self.c.wisdom.modifier)

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=9, force=True)

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertTrue(self.c.has_feature(Feature.DEFLECT_ATTACKS))
        self.assertEqual(self.c.martial_arts_die, "d6")

    ###################################################################
    def test_level4(self):
        self.c.level4(hp=9, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH), force=True)

        self.assertEqual(self.c.level, 4)
        self.assertEqual(self.c.martial_arts_die, "d6")

        self.assertTrue(self.c.has_feature(Feature.SLOW_FALL))
        self.assertEqual(self.c.martial_arts_die, "d6")

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=5 + 6 + 7, force=True)

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.martial_arts_die, "d8")

        self.assertTrue(self.c.has_feature(Feature.EXTRA_ATTACK))
        self.assertTrue(self.c.has_feature(Feature.STUNNING_STRIKE))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.martial_arts_die, "d8")

        self.assertTrue(self.c.has_feature(Feature.EMPOWERED_STRIKES))
        self.assertTrue(self.c.speed, 30 + 15)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)

        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 0)
        self.assertEqual(self.c.martial_arts_die, "d8")

        self.assertTrue(self.c.has_feature(Feature.EVASION))
        self.assertEqual(self.c.focus_points, 7)
        sf = self.c.find_feature(Feature.SLOW_FALL)
        self.assertIn("fall by 35 HP", sf.desc)


#######################################################################
class TestMercy(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = MonkWarriorOfMercy(
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
        self.c.level3(hp=5 + 6, force=True)
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
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.PHYSICIANS_TOUCH))
        hoharm = self.c.find_feature(Feature.HAND_OF_HARM)
        self.assertIn("Poisoned", hoharm.desc)
        hoheal = self.c.find_feature(Feature.HAND_OF_HEALING)
        self.assertIn("Poisoned", hoheal.desc)


#######################################################################
class TestElements(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = MonkWarriorOfTheElements(
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
        self.c.level3(hp=5 + 6, force=True)
        self.assertTrue(self.c.has_feature(Feature.ELEMENTAL_ATTUNEMENT))
        self.assertTrue(self.c.has_feature(Feature.MANIPULATE_ELEMENTS))
        self.assertIn(Spell.ELEMENTALISM, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.ELEMENTAL_BURST))


#######################################################################
class TestOpenHand(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = MonkWarriorOfTheOpenHand(
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
        self.c.level3(hp=5 + 6, force=True)
        self.assertTrue(self.c.has_feature(Feature.OPEN_HAND_TECHNIQUE))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.WHOLENESS_OF_BODY))
        wob = self.c.find_feature(Feature.WHOLENESS_OF_BODY)
        self.assertIn("1d8+2", wob.desc)


#######################################################################
class TestShadow(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = MonkWarriorOfShadow(
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
        self.c.level3(hp=5 + 6, force=True)
        self.assertTrue(self.c.has_feature(Feature.SHADOW_ARTS))
        self.assertIn(Spell.MINOR_ILLUSION, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertTrue(self.c.has_feature(Feature.SHADOW_STEP))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
