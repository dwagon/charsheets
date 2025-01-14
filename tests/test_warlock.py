import unittest

from charsheets.classes import WarlockFiend, WarlockOldOne, WarlockCelestial, WarlockArchFey
from charsheets.classes.warlock import Warlock, EldritchSpear, PactOfTheTome
from charsheets.constants import Skill, Stat, Ability
from charsheets.spells import Spells
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestWarlock(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Warlock(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

    ###################################################################
    def test_warlock(self):
        self.assertEqual(self.c.hit_dice, 8)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertIn("Eldritch Invocation", self.c.class_special)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 1)
        self.assertTrue(self.c.has_ability(Ability.ELDRITCH_INVOCATIONS))
        self.assertTrue(self.c.has_ability(Ability.PACT_MAGIC))

        self.c.learn_spell(Spells.ARMOR_OF_AGATHYS)
        self.c.learn_spell(Spells.CLOUD_OF_DAGGERS)
        self.assertEqual(self.c.spells_of_level(1), [Spells.ARMOR_OF_AGATHYS])

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8 + 2)  # 2 for CON
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertTrue(self.c.has_ability(Ability.MAGICAL_CUNNING))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(2), 2)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=11)
        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(3), 2)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=11)
        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(3), 2)

    ###################################################################
    def test_eldritch_spear(self):
        self.c.add_invocation(EldritchSpear(Spells.CHILL_TOUCH))
        self.assertIn("Eldritch Spear", self.c.class_special)
        self.assertIn("Chill Touch", self.c.class_special)

    ###################################################################
    def test_pact_of_the_tome(self):
        self.c.add_invocation(
            PactOfTheTome(
                Spells.SPARE_THE_DYING,
                Spells.TOLL_THE_DEAD,
                Spells.FIRE_BOLT,
                Spells.UNSEEN_SERVANT,
                Spells.TENSERS_FLOATING_DISK,
            )
        )
        self.assertIn(Spells.TENSERS_FLOATING_DISK, self.c.prepared_spells)
        self.assertIn(Spells.TENSERS_FLOATING_DISK, self.c.known_spells)

        self.assertIn("Tenser", self.c.class_special)


#######################################################################
class TestArchFeyWarlock(unittest.TestCase):
    def setUp(self):
        self.c = WarlockArchFey(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)

    ###################################################################
    def test_archfey_patron(self):
        self.assertIn(Spells.SLEEP, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.STEPS_OF_THE_FEY))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=11)
        self.assertIn(Spells.BLINK, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=10)
        self.assertTrue(self.c.has_ability(Ability.MISTY_ESCAPE))


#######################################################################
class TestCelestialWarlock(unittest.TestCase):
    def setUp(self):
        self.c = WarlockCelestial(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)

    ###################################################################
    def test_celestial_patron(self):
        self.assertIn(Spells.LESSER_RESTORATION, self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=11)
        self.assertIn(Spells.REVIVIFY, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=11)
        self.assertTrue(self.c.has_ability(Ability.RADIANT_SOUL))


#######################################################################
class TestFiendWarlock(unittest.TestCase):
    def setUp(self):
        self.c = WarlockFiend(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)

    ###################################################################
    def test_fiend_patron(self):
        self.assertTrue(self.c.has_ability(Ability.DARK_ONES_BLESSING))
        self.assertIn(Spells.BURNING_HANDS, self.c.prepared_spells)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=11)
        self.assertIn(Spells.FIREBALL, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=11)
        self.assertTrue(self.c.has_ability(Ability.DARK_ONES_OWN_LUCK))


#######################################################################
class TestOldOneWarlock(unittest.TestCase):
    def setUp(self):
        self.c = WarlockOldOne(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=8,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=15,
        )

        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)

    ###################################################################
    def test_old_patron(self):
        self.assertIn(Spells.DISSONANT_WHISPERS, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.PSYCHIC_SPELLS))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=11)
        self.assertIn(Spells.HUNGER_OF_HADAR, self.c.prepared_spells)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=10)
        self.assertTrue(self.c.has_ability(Ability.CLAIRVOYANT_COMBATANT))


#######################################################################
if __name__ == "__main__":
    unittest.main()
