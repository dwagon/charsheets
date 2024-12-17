import unittest


from charsheets.constants import Skill, Origin, Stat, Ability, Proficiencies
from charsheets.classes import Cleric, LifeDomain, LightDomain, TrickeryDomain, WarDomain
from charsheets.spells import Spells
from tests.fixtures import DummySpecies


#######################################################################
class TestCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Cleric(
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
    def test_basic(self):
        self.assertEqual(self.c.hit_dice, 8)
        self.assertTrue(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CHARISMA))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertIn(Proficiencies.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiencies.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiencies.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiencies.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertNotIn(Proficiencies.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertIn(Spells.BANE, self.c.spells_of_level(1))

    ###################################################################
    def test_protector(self):
        self.c.add_ability(Ability.DIVINE_ORDER_PROTECTOR)
        print(self.c.abilities)
        self.assertIn(Proficiencies.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiencies.HEAVY_ARMOUR, self.c.armour_proficiencies())

    ###################################################################
    def test_thaumaturge(self):
        self.c.add_ability(Ability.DIVINE_ORDER_THAUMATURGE)

    ###################################################################
    def test_level2(self):
        self.c.add_level(5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(self.c.hp, 5 + 8)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertIn(Ability.CHANNEL_DIVINITY, self.c.class_abilities())

    ###################################################################
    def test_level3(self):
        self.c.add_level(5)
        self.c.add_level(6)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertIn(Spells.LOCATE_OBJECT, self.c.spells_of_level(2))


#######################################################################
class TestLightDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = LightDomain(
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
    def test_light(self):
        self.assertIn(Spells.BURNING_HANDS, self.c.prepared_spells)
        self.assertIn(Ability.RADIANCE_OF_THE_DAWN, self.c.class_abilities())


#######################################################################
class TestLifeDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = LifeDomain(
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
    def test_life(self):
        self.assertIn(Spells.LESSER_RESTORATION, self.c.prepared_spells)
        self.assertIn(Ability.PRESERVE_LIFE, self.c.class_abilities())


#######################################################################
class TestTrickeryDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = TrickeryDomain(
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
    def test_trickery(self):
        self.assertIn(Spells.PASS_WITHOUT_TRACE, self.c.prepared_spells)
        self.assertIn(Ability.BLESSING_OF_THE_TRICKSTER, self.c.class_abilities())


#######################################################################
class TestWarDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = WarDomain(
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
    def test_war(self):
        self.assertIn(Spells.SPIRITUAL_WEAPON, self.c.prepared_spells)
        self.assertIn(Ability.WAR_PRIEST, self.c.class_abilities())


# EOF
