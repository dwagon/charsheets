import unittest


from charsheets.constants import Skill, Origin, Stat, Ability, Proficiencies
from charsheets.classes import Ranger, BeastMaster, FeyWanderer, GloomStalker, Hunter
from charsheets.spells import Spells
from tests.fixtures import DummySpecies
from charsheets.main import render


#######################################################################
class TestRanger(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Ranger(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_ranger(self):
        self.assertEqual(self.c.hit_dice, 10)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.DEXTERITY))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.INTELLIGENCE))
        self.assertIn(Proficiencies.SHIELDS, self.c.armour_proficiencies())
        self.assertNotIn(Proficiencies.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiencies.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertEqual(self.c.spell_casting_ability, Stat.WISDOM)
        self.assertIn(Spells.GOODBERRY, self.c.known_spells)

    ###################################################################
    def test_renders(self):
        output = render(self.c, "char_sheet.jinja")
        self.assertIn(r"\SpellcastingAbility{Wisdom}", output)

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertIn(Ability.FAVOURED_ENEMY, self.c.class_abilities())
        self.assertIn(Ability.WEAPON_MASTERY, self.c.class_abilities())
        self.assertEqual(self.c.spell_slots(1), 2)

    ###################################################################
    def test_level2(self):
        self.c.add_level(5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(self.c.hp, 5 + 10)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertIn(Ability.DEFT_EXPLORER, self.c.class_abilities())
        self.assertIn(Ability.FIGHTING_STYLE, self.c.class_abilities())
        self.assertEqual(self.c.spell_slots(1), 2)

    ###################################################################
    def test_level3(self):
        self.c.add_level(5)
        self.c.add_level(6)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)


###################################################################
class TestBeastMaster(unittest.TestCase):

    def setUp(self):
        self.c = BeastMaster(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.add_level(5)
        self.c.add_level(6)

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.level, 3)
        self.assertIn(Ability.PRIMAL_COMPANION, self.c.class_abilities())


###################################################################
class TestFeyWanderer(unittest.TestCase):

    def setUp(self):
        self.c = FeyWanderer(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.add_level(5)
        self.c.add_level(6)

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.level, 3)
        self.assertIn(Ability.OTHERWORLDLY_GLAMOUR, self.c.class_abilities())
        self.assertIn(Ability.DREADFUL_STRIKES, self.c.class_abilities())
        self.assertIn(Spells.CHARM_PERSON, self.c.prepared_spells)


###################################################################
class TestGloomStalker(unittest.TestCase):
    def setUp(self):
        self.c = GloomStalker(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=10,
        )
        self.c.add_level(5)
        self.c.add_level(6)

    ###################################################################
    def test_basics(self):
        self.assertIn(Ability.DREAD_AMBUSHER, self.c.class_abilities())
        self.assertIn(Spells.DISGUISE_SELF, self.c.prepared_spells)


###################################################################
class TestHunter(unittest.TestCase):
    def setUp(self):
        self.c = Hunter(
            "name",
            Origin.ACOLYTE,
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.add_level(5)
        self.c.add_level(6)

    ###################################################################
    def test_basics(self):
        self.assertIn(Ability.HUNTERS_LORE, self.c.class_abilities())
        self.assertIn(Ability.HUNTERS_PREY, self.c.class_abilities())
        self.assertEqual(self.c.spell_casting_ability, Stat.WISDOM)


# EOF
