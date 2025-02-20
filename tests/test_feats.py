import unittest

from charsheets.constants import Skill, Stat, Tool, Feature, Sense, DamageType, Proficiency
from charsheets.exception import NotDefined, InvalidOption
from charsheets.features import (
    AbilityScoreImprovement,
    Skilled,
    Darkvision120,
    Darkvision60,
    Actor,
    Chef,
    ElementalAdept,
    FeyTouched,
    KeenMind,
    LightlyArmored,
    Telepathic,
    Observant,
    ModeratelyArmored,
    HeavilyArmored,
    MartialWeaponTraining,
    InspiringLeader,
)
from charsheets.main import render
from charsheets.origins import Charlatan, Artisan, Farmer, Entertainer
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyCharClass, DummyOrigin


#######################################################################
class TestSkilled(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            Charlatan(
                Stat.DEXTERITY, Stat.DEXTERITY, Stat.CONSTITUTION, Skilled(Tool.DISGUISE_KIT, Skill.ATHLETICS, Skill.INTIMIDATION)
            ),
            DummySpecies(),
            Skill.ARCANA,
            Skill.PERCEPTION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_defined(self):
        self.assertIn(Tool.FORGERY_KIT, self.c.tool_proficiencies)  # Charlatan
        self.assertIn(Tool.DISGUISE_KIT, self.c.tool_proficiencies)  # Skilled

        self.assertTrue(self.c.is_proficient(Skill.ATHLETICS))
        self.assertTrue(self.c.is_proficient(Skill.ARCANA))
        self.assertTrue(self.c.is_proficient(Skill.PERCEPTION))
        self.assertTrue(self.c.is_proficient(Skill.INTIMIDATION))

        self.assertFalse(self.c.is_proficient(Skill.ANIMAL_HANDLING))

    ###################################################################
    def test_desc(self):
        r = render(self.c, "char_sheet.jinja")
        self.assertNotIn("You have proficiency in: Disguise Kit, athletics, intimidation", r)  # Hidden
        self.assertIn("% Skilled", r)  # Hidden


#######################################################################
class TestCrafter(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            Artisan(Stat.STRENGTH, Stat.DEXTERITY, Stat.DEXTERITY),
            DummySpecies(),
            Skill.ARCANA,
            Skill.PERCEPTION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_undefined(self):
        """What happens if we don't define the tools"""
        with self.assertRaises(NotDefined):
            render(self.c, "char_sheet.jinja")

    ###################################################################
    def test_defined(self):
        self.c.find_feature(Feature.CRAFTER).set_tools(Tool.DISGUISE_KIT, Tool.CARTOGRAPHERS_TOOLS, Tool.POTTERS_TOOLS)  # type: ignore
        self.assertIn(Tool.DISGUISE_KIT, self.c.tool_proficiencies)  # Artisan
        self.assertIn(Tool.CARTOGRAPHERS_TOOLS, self.c.tool_proficiencies)  # Artisan


#######################################################################
class TestMusician(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            Entertainer(Stat.DEXTERITY, Stat.DEXTERITY, Stat.CHARISMA),
            DummySpecies(),
            Skill.ARCANA,
            Skill.PERCEPTION,
            strength=7,
            dexterity=14,
            constitution=9,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_defined(self):
        self.assertIn(Tool.MUSICAL_INSTRUMENT, self.c.tool_proficiencies)


#######################################################################
class TestTough(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            Farmer(Stat.STRENGTH, Stat.WISDOM, Stat.CONSTITUTION),
            DummySpecies(),
            Skill.ARCANA,
            Skill.PERCEPTION,
            strength=7,
            dexterity=14,
            constitution=9,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_hp(self):
        self.c.level1()
        self.assertEqual(int(self.c.hp), 7 + 2)
        self.assertIn("Tough (2)", self.c.hp.reason)
        self.assertIn("level 1 (7)", self.c.hp.reason)

    ###################################################################
    def test_desc(self):
        self.c.level = 2
        r = render(self.c, "char_sheet.jinja")
        self.assertNotIn("maximum increased by 4", r)  # Hidden
        self.assertIn("% Tough", r)


#######################################################################
class TestAbilityScoreImprovement(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.PERCEPTION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
            charisma=10,
        )

    ###################################################################
    def test_ability_score_improvement(self):
        self.assertEqual(int(self.c.dexterity.value), 14)
        asi = AbilityScoreImprovement(Stat.DEXTERITY, Stat.INTELLIGENCE)
        self.c.add_feature(asi)
        self.assertEqual(int(self.c.dexterity.value), 15)
        self.assertEqual(int(self.c.intelligence.value), 6)
        self.assertEqual(int(self.c.wisdom.value), 20, "Unchanged")

        asi2 = AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)
        self.assertEqual(int(self.c.charisma.value), 10)
        self.c.add_feature(asi2)
        self.assertEqual(int(self.c.charisma.value), 12)


#######################################################################
class TestGeneralFeats(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.PERCEPTION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
            charisma=10,
        )

    ###################################################################
    def test_darkvision(self):
        self.assertNotIn(Sense.DARKVISION60, self.c.senses)
        self.c.add_feature(Darkvision60())
        self.assertIn(Sense.DARKVISION60, self.c.senses)

        self.assertNotIn(Sense.DARKVISION120, self.c.senses)
        self.c.add_feature(Darkvision120())
        self.assertIn(Sense.DARKVISION120, self.c.senses)

    ###################################################################
    def test_actor(self):
        self.assertEqual(int(self.c.charisma.value), 10)
        self.c.add_feature(Actor())
        self.assertEqual(int(self.c.charisma.value), 11)

    ###################################################################
    def test_chef(self):
        with self.assertRaises(InvalidOption):
            self.c.add_feature(Chef(Stat.CHARISMA))
        with self.assertRaises(InvalidOption):
            self.c.add_feature(Chef())
        self.assertEqual(int(self.c.constitution.value), 11)
        self.c.add_feature(Chef(Stat.CONSTITUTION))
        self.assertEqual(int(self.c.constitution.value), 12)
        self.assertIn(Tool.COOKS_UTENSILS, self.c.tool_proficiencies)

    ###################################################################
    def test_elemental_adept(self):
        with self.assertRaises(InvalidOption):
            self.c.add_feature(ElementalAdept(DamageType.PSYCHIC, Stat.INTELLIGENCE))
        self.assertEqual(int(self.c.intelligence.value), 5)

        self.c.add_feature(ElementalAdept(DamageType.COLD, Stat.INTELLIGENCE))
        ea = self.c.find_feature(Feature.ELEMENTAL_ADEPT)
        self.assertIn("Resistance to Cold", ea.desc)
        self.assertEqual(int(self.c.intelligence.value), 6)

    ###################################################################
    def test_fey_touched(self):
        with self.assertRaises(InvalidOption):
            self.c.add_feature(FeyTouched(Stat.INTELLIGENCE))

        self.assertEqual(int(self.c.intelligence.value), 5)

        self.c.add_feature(FeyTouched(Spell.JUMP, Stat.INTELLIGENCE))
        ea = self.c.find_feature(Feature.FEY_TOUCHED)
        self.assertIn("ability is Intelligence", ea.desc)
        self.assertEqual(int(self.c.intelligence.value), 6)
        self.assertIn(Spell.MISTY_STEP, self.c.prepared_spells)
        self.assertIn(Spell.JUMP, self.c.prepared_spells)

    ###################################################################
    def test_keen_mind(self):
        with self.assertRaises(InvalidOption):
            self.c.add_feature(KeenMind(Skill.ANIMAL_HANDLING, Stat.INTELLIGENCE))
        self.assertFalse(self.c.is_proficient(Skill.HISTORY))
        self.c.add_feature(KeenMind(Skill.HISTORY, Stat.INTELLIGENCE))
        self.assertTrue(self.c.is_proficient(Skill.HISTORY))

    ###################################################################
    def test_inspiring_leader(self):
        self.c.add_feature(InspiringLeader(Stat.WISDOM))
        il = self.c.find_feature(Feature.INSPIRING_LEADER)
        self.assertIn("gain 5 Temporary", il.desc)
        self.c.level5(hp=1, force=True)
        self.assertIn("gain 10 Temporary", il.desc)

    ###################################################################
    def test_lightly_armored(self):
        self.assertNotIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.c.add_feature(LightlyArmored(Stat.STRENGTH))
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())

    ###################################################################
    def test_moderately_armored(self):
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.c.add_feature(ModeratelyArmored(Stat.STRENGTH))
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())

    ###################################################################
    def test_heavily_armored(self):
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.c.add_feature(HeavilyArmored(Stat.STRENGTH))
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())

    ###################################################################
    def test_martial_weapons(self):
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.c.add_feature(MartialWeaponTraining(Stat.DEXTERITY))
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_observant(self):
        with self.assertRaises(InvalidOption):
            self.c.add_feature(Observant(Skill.ANIMAL_HANDLING, Stat.WISDOM))
        self.assertFalse(self.c.is_proficient(Skill.INSIGHT))
        self.c.add_feature(Observant(Skill.INSIGHT, Stat.WISDOM))
        self.assertTrue(self.c.is_proficient(Skill.INSIGHT))

    ###################################################################
    def test_telepathic(self):
        self.assertNotIn(Spell.DETECT_THOUGHTS, self.c.prepared_spells)
        self.c.add_feature(Telepathic(Stat.WISDOM))
        self.assertIn(Spell.DETECT_THOUGHTS, self.c.prepared_spells)
        tp = self.c.find_feature(Feature.TELEPATHIC)
        self.assertIn("spell is Wisdom", tp.desc)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
