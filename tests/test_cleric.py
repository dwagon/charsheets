import unittest


from charsheets.constants import Skill, Stat, Ability, Proficiency
from charsheets.classes import Cleric, ClericLifeDomain, ClericLightDomain, ClericTrickeryDomain, ClericWarDomain
from charsheets.spells import Spells
from tests.dummy import DummySpecies, DummyOrigin
from charsheets.abilities import DivineProtector, Thaumaturge


#######################################################################
class TestCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Cleric(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.PERSUASION,
            Skill.RELIGION,
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
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

    ###################################################################
    def test_level1(self):
        self.assertEqual(self.c.level, 1)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertIn(Spells.BANE, self.c.spells_of_level(1))

    ###################################################################
    def test_protector(self):
        self.c.add_ability(DivineProtector())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())

    ###################################################################
    def test_thaumaturge(self):
        self.c.add_ability(Thaumaturge())

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 5 + 8)
        self.assertEqual(self.c.max_spell_level(), 1)
        self.assertEqual(self.c.spell_slots(1), 3)
        self.assertTrue(self.c.has_ability(Ability.CHANNEL_DIVINITY))

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)

        self.assertEqual(self.c.level, 3)
        self.assertEqual(self.c.max_spell_level(), 2)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 2)
        self.assertIn(Spells.LOCATE_OBJECT, self.c.spells_of_level(2))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=5 + 6 + 7)

        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 2)
        self.assertTrue(self.c.has_ability(Ability.SEAR_UNDEAD))

        self.assertIn(Spells.WATER_WALK, self.c.spells_of_level(3))

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)

        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.max_spell_level(), 3)
        self.assertEqual(self.c.spell_slots(1), 4)
        self.assertEqual(self.c.spell_slots(2), 3)
        self.assertEqual(self.c.spell_slots(3), 3)


#######################################################################
class TestLightDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = ClericLightDomain(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.MEDICINE,
            Skill.PERSUASION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_light(self):
        self.assertIn(Spells.BURNING_HANDS, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.RADIANCE_OF_THE_DAWN))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.FIREBALL, self.c.prepared_spells)


#######################################################################
class TestLifeDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = ClericLifeDomain(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.RELIGION,
            Skill.MEDICINE,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_life(self):
        self.assertIn(Spells.LESSER_RESTORATION, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.PRESERVE_LIFE))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.MASS_HEALING_WORD, self.c.prepared_spells)


#######################################################################
class TestTrickeryDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = ClericTrickeryDomain(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.INSIGHT,
            Skill.RELIGION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_trickery(self):
        self.assertIn(Spells.PASS_WITHOUT_TRACE, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.BLESSING_OF_THE_TRICKSTER))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.HYPNOTIC_PATTERN, self.c.prepared_spells)


#######################################################################
class TestWarDomain(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = ClericWarDomain(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.HISTORY,
            Skill.PERSUASION,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
        )
        self.c.level3(hp=5 + 6)

    ###################################################################
    def test_war(self):
        self.assertIn(Spells.SPIRITUAL_WEAPON, self.c.prepared_spells)
        self.assertTrue(self.c.has_ability(Ability.WAR_PRIEST))

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=9)
        self.assertIn(Spells.CRUSADERS_MANTLE, self.c.prepared_spells)


#######################################################################
if __name__ == "__main__":
    unittest.main()


# EOF
