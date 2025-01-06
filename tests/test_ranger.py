import unittest


from charsheets.constants import Skill, Origin, Stat, Ability, Proficiency
from charsheets.classes import Ranger, RangerBeastMaster, RangerFeyWanderer, RangerGloomStalker, RangerHunter
from charsheets.spells import Spells
from tests.dummy import DummySpecies, DummyOrigin
from charsheets.main import render


#######################################################################
class TestRanger(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Ranger(
            "name",
            DummyOrigin(),
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
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
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
        self.assertTrue(self.c.has_ability(Ability.FAVOURED_ENEMY))
        self.assertTrue(self.c.has_ability(Ability.WEAPON_MASTERY))
        self.assertEqual(self.c.spell_slots(1), 2)

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 10)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertTrue(self.c.has_ability(Ability.DEFT_EXPLORER))
        self.assertTrue(self.c.has_ability(Ability.FIGHTING_STYLE))

        self.assertEqual(self.c.spell_slots(1), 2)

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertEqual(int(self.c.hp), 6 + 5 + 10)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)


###################################################################
class TestBeastMaster(unittest.TestCase):

    def setUp(self):
        self.c = RangerBeastMaster(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.level, 3)
        self.assertTrue(self.c.has_ability(Ability.PRIMAL_COMPANION))


###################################################################
class TestFeyWanderer(unittest.TestCase):

    def setUp(self):
        self.c = RangerFeyWanderer(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_basics(self):
        self.assertEqual(self.c.level, 3)
        self.assertIn(Spells.CHARM_PERSON, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.OTHERWORLDLY_GLAMOUR))
        self.assertTrue(self.c.has_ability(Ability.DREADFUL_STRIKES))


###################################################################
class TestGloomStalker(unittest.TestCase):
    def setUp(self):
        self.c = RangerGloomStalker(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=10,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_ability(Ability.DREAD_AMBUSHER))

        self.assertIn(Spells.DISGUISE_SELF, self.c.prepared_spells)


###################################################################
class TestHunter(unittest.TestCase):
    def setUp(self):
        self.c = RangerHunter(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.ANIMAL_HANDLING,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_basics(self):
        self.assertTrue(self.c.has_ability(Ability.HUNTERS_PREY))
        self.assertTrue(self.c.has_ability(Ability.HUNTERS_LORE))

        self.assertEqual(self.c.spell_casting_ability, Stat.WISDOM)


#######################################################################
if __name__ == "__main__":
    unittest.main()


# EOF
