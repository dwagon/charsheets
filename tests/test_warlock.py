import unittest


from charsheets.constants import Skill, Origin, Stat, Ability
from charsheets.classes.warlock import Warlock, EldritchSpear, PactOfTheTome
from charsheets.spells import Spells
from tests.fixtures import DummySpecies


#######################################################################
class TestWarlock(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Warlock(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
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
        self.assertEqual(self.c.max_spell_level(1), 1)
        self.assertEqual(self.c.spell_slots(1), 1)
        self.assertEqual(self.c.class_abilities(), {Ability.ELDRITCH_INVOCATIONS, Ability.PACT_MAGIC})
        self.c.learn_spell(Spells.ARMOR_OF_AGATHYS)
        self.c.learn_spell(Spells.CLOUD_OF_DAGGERS)
        self.assertEqual(self.c.spells(1), [Spells.ARMOR_OF_AGATHYS])

    ###################################################################
    def test_level2(self):
        self.c.add_level(5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(self.c.hp, 5 + 8)
        self.assertEqual(self.c.max_spell_level(1), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertEqual(self.c.class_abilities(), {Ability.ELDRITCH_INVOCATIONS, Ability.PACT_MAGIC, Ability.MAGICAL_CUNNING})

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
