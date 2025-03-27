import unittest

from charsheets.character import Character
from charsheets.classes import WarlockFiend, WarlockOldOne, WarlockCelestial, WarlockArchFey, MysticArcanum
from charsheets.classes.warlock import Warlock, EldritchSpear, PactOfTheTome
from charsheets.constants import Skill, Stat, Feature, DamageType, Proficiency, Language
from charsheets.exception import InvalidOption
from charsheets.features import Grappler, KeenMind, Piercer, Poisoner, AbilityScoreImprovement
from charsheets.spell import Spell
from tests.dummy import DummySpecies, DummyOrigin


class TestWarlock(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_warlock(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.assertEqual(self.c.max_hit_dice, "1d8")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.LIGHT_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.SHIELDS, self.c.armour_proficiencies())

    ###################################################################
    def test_level1(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.assertEqual(self.c.level, 1)
        self.assertIn("Eldritch Invocation", self.c.class_special)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 1)
        self.assertTrue(self.c.has_feature(Feature.ELDRITCH_INVOCATIONS))
        self.assertTrue(self.c.has_feature(Feature.PACT_MAGIC))

        self.c.learn_spell(Spell.ARMOR_OF_AGATHYS)
        self.c.learn_spell(Spell.CLOUD_OF_DAGGERS)
        self.assertIn(Spell.ARMOR_OF_AGATHYS, [_[0] for _ in self.c.spells_of_level(1)])

    ###################################################################
    def test_level2(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8 + 2)  # 2 for CON
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertTrue(self.c.has_feature(Feature.MAGICAL_CUNNING))

    ###################################################################
    def test_level3(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(Warlock(hp=1))
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(2), 2)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, feat=Grappler(Stat.STRENGTH)))
        self.c.add_level(Warlock(hp=1))

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(3), 2)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, feat=Grappler(Stat.STRENGTH)))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(3), 2)

    ###################################################################
    def test_level7(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, feat=Grappler(Stat.STRENGTH)))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))

        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.max_spell_level(), 4)
        self.assertEqual(self.c.spell_slots(3), 2)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, feat=Grappler(Stat.STRENGTH)))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, feat=KeenMind(Skill.ARCANA)))
        self.c.add_level(Warlock(hp=1))
        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.max_spell_level(), 5)
        self.assertEqual(self.c.spell_slots(5), 2)
        self.assertTrue(self.c.has_feature(Feature.CONTACT_PATRON))

    ###################################################################
    def test_level10(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, feat=Grappler(Stat.STRENGTH)))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, feat=Piercer(Stat.DEXTERITY)))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))

        self.assertEqual(self.c.level, 10)
        self.assertEqual(self.c.max_spell_level(), 5)
        self.assertEqual(self.c.spell_slots(5), 2)

    ###################################################################
    def test_level11(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, feat=Grappler(Stat.STRENGTH)))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, feat=Piercer(Stat.DEXTERITY)))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, mystic=MysticArcanum(Spell.EYEBITE)))

        self.assertEqual(self.c.level, 11)
        self.assertEqual(self.c.max_spell_level(), 5)
        self.assertEqual(self.c.spell_slots(5), 3)
        self.assertTrue(self.c.has_feature(Feature.MYSTIC_ARCANUM))

    ###################################################################
    def test_level13(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, feat=Grappler(Stat.STRENGTH)))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, feat=Piercer(Stat.DEXTERITY)))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1))
        self.c.add_level(Warlock(hp=1, mystic=MysticArcanum(Spell.EYEBITE)))
        self.c.add_level(Warlock(hp=1, feat=Poisoner(Stat.INTELLIGENCE)))
        self.c.add_level(Warlock(hp=1))

        self.assertEqual(self.c.level, 13)
        self.assertEqual(self.c.max_spell_level(), 5)
        self.assertEqual(self.c.spell_slots(5), 3)

    ###################################################################
    def test_eldritch_spear(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.warlock.add_invocation(EldritchSpear(Spell.CHILL_TOUCH))
        self.assertIn("Eldritch Spear", self.c.class_special)
        self.assertIn("Chill Touch", self.c.class_special)

    ###################################################################
    def test_pact_of_the_tome(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.warlock.add_invocation(
            PactOfTheTome(
                Spell.SPARE_THE_DYING,
                Spell.TOLL_THE_DEAD,
                Spell.FIRE_BOLT,
                Spell.UNSEEN_SERVANT,
                Spell.TENSERS_FLOATING_DISK,
            )
        )
        self.assertIn(Spell.TENSERS_FLOATING_DISK, self.c.prepared_spells)
        self.assertIn(Spell.TENSERS_FLOATING_DISK, self.c.known_spells)

        self.assertIn("Tenser", self.c.class_special)


#######################################################################
class TestArchFeyWarlock(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_archfey_patron(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockArchFey(hp=1))
        self.assertIn(Spell.SLEEP, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.STEPS_OF_THE_FEY))

    ###################################################################
    def test_level5(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockArchFey(hp=1))

        self.assertIn(Spell.BLINK, self.c.prepared_spells)
        self.assertIn(Spell.PLANT_GROWTH, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1))

        self.assertTrue(self.c.has_feature(Feature.MISTY_ESCAPE))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1))

        self.assertIn(Spell.DOMINATE_BEAST, self.c.prepared_spells)
        self.assertIn(Spell.GREATER_INVISIBILITY, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockArchFey(hp=1))

        self.assertEqual(self.c.level, 9)
        self.assertIn(Spell.DOMINATE_PERSON, self.c.prepared_spells)
        self.assertIn(Spell.SEEMING, self.c.prepared_spells)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockArchFey(hp=1))
        self.c.add_level(WarlockArchFey(hp=1))
        self.assertTrue(self.c.has_feature(Feature.BEGUILING_DEFENSES))


#######################################################################
class TestCelestialWarlock(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_celestial_patron(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockCelestial(hp=1))
        self.assertIn(Spell.LESSER_RESTORATION, self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockCelestial(hp=1))

        self.assertIn(Spell.REVIVIFY, self.c.prepared_spells)
        self.assertIn(Spell.DAYLIGHT, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1))

        self.assertTrue(self.c.has_feature(Feature.RADIANT_SOUL))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1))

        self.assertIn(Spell.GUARDIAN_OF_FAITH, self.c.prepared_spells)
        self.assertIn(Spell.REVIVIFY, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockCelestial(hp=1))

        self.assertEqual(self.c.level, 9)
        self.assertIn(Spell.GREATER_RESTORATION, self.c.prepared_spells)
        self.assertIn(Spell.SUMMON_CELESTIAL, self.c.prepared_spells)

    ###################################################################
    def test_radiant_soul(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1))
        self.assertIn(DamageType.RADIANT, self.c.damage_resistances)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockCelestial(hp=1))
        self.c.add_level(WarlockCelestial(hp=1))

        self.assertTrue(self.c.has_feature(Feature.CELESTIAL_RESILIENCE))


#######################################################################
class TestFiendWarlock(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_fiend_patron(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockFiend(hp=1))
        self.assertTrue(self.c.has_feature(Feature.DARK_ONES_BLESSING))
        self.assertIn(Spell.BURNING_HANDS, self.c.prepared_spells)

    ###################################################################
    def test_dark_ones_blessing(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockFiend(hp=1))
        dob = self.c.find_feature(Feature.DARK_ONES_BLESSING)
        self.assertIn("gain 5 Temporary", dob.desc)

    ###################################################################
    def test_level5(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockFiend(hp=1))

        self.assertIn(Spell.FIREBALL, self.c.prepared_spells)
        self.assertIn(Spell.STINKING_CLOUD, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1))

        self.assertTrue(self.c.has_feature(Feature.DARK_ONES_OWN_LUCK))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1))

        self.assertIn(Spell.FIRE_SHIELD, self.c.prepared_spells)
        self.assertIn(Spell.WALL_OF_FIRE, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockFiend(hp=1))
        self.assertEqual(self.c.level, 9)
        self.assertIn(Spell.GEAS, self.c.prepared_spells)
        self.assertIn(Spell.INSECT_PLAGUE, self.c.prepared_spells)

    ###################################################################
    def test_dark_ones_own_luck(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1))
        dool = self.c.find_feature(Feature.DARK_ONES_OWN_LUCK)
        self.assertEqual(dool.goes, 2)
        self.assertIn("feature 2 times", dool.desc)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockFiend(hp=1))
        self.c.add_level(WarlockFiend(hp=1))

        self.assertTrue(self.c.has_feature(Feature.FIENDISH_RESILIENCE))


#######################################################################
class TestOldOneWarlock(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_old_patron(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockOldOne(hp=1))
        self.assertIn(Spell.DISSONANT_WHISPERS, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.PSYCHIC_SPELLS))

    ###################################################################
    def test_level5(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockOldOne(hp=1))

        self.assertIn(Spell.CLAIRVOYANCE, self.c.prepared_spells)
        self.assertIn(Spell.HUNGER_OF_HADAR, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1))

        self.assertTrue(self.c.has_feature(Feature.CLAIRVOYANT_COMBATANT))

    ###################################################################
    def test_level7(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1))

        self.assertIn(Spell.CONFUSION, self.c.prepared_spells)
        self.assertIn(Spell.SUMMON_ABERRATION, self.c.prepared_spells)

    ###################################################################
    def test_level9(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockOldOne(hp=1))
        self.assertEqual(self.c.level, 9)
        self.assertIn(Spell.MODIFY_MEMORY, self.c.prepared_spells)
        self.assertIn(Spell.TELEKINESIS, self.c.prepared_spells)

    ###################################################################
    def test_level10(self):
        self.c.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
        self.c.add_level(Warlock(hp=5))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
        self.c.add_level(WarlockOldOne(hp=1))
        self.c.add_level(WarlockOldOne(hp=1))

        self.assertTrue(self.c.has_feature(Feature.ELDRITCH_HEX))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()
