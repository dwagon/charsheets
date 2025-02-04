import unittest

from charsheets.constants import Armour, DamageType, Language
from charsheets.constants import Skill, Stat, Feature, Weapon
from charsheets.reason import Reason
from charsheets.spell import Spell
from tests.dummy import DummyCharClass, DummySpecies, DummyOrigin
from charsheets.features import Alert, AbilityScoreImprovement
from charsheets.weapons import Spear
from charsheets.armour import Leather, Shield, Plate
from charsheets.exception import InvalidOption


#######################################################################
class TestCharacter(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = DummyCharClass(
            "name",
            DummyOrigin(Stat.INTELLIGENCE),
            DummySpecies(),
            Skill.ARCANA,
            Skill.RELIGION,
            strength=7,
            dexterity=14,
            constitution=8,
            wisdom=20,
            intelligence=5,
        )

    ###################################################################
    def test_validation(self):
        with self.assertRaises(InvalidOption, msg="Validation failed with same skill"):
            DummyCharClass(
                "name",
                DummyOrigin(Stat.INTELLIGENCE),
                DummySpecies(),
                Skill.ARCANA,
                Skill.ARCANA,
            )
        with self.assertRaises(InvalidOption, msg="Validation failed with skill1"):
            DummyCharClass(
                "name",
                DummyOrigin(Stat.INTELLIGENCE),
                DummySpecies(),
                Skill.ANIMAL_HANDLING,
                Skill.ARCANA,
            )
        with self.assertRaises(InvalidOption, msg="Validation failed with skill2"):
            DummyCharClass(
                "name",
                DummyOrigin(Stat.INTELLIGENCE),
                DummySpecies(),
                Skill.ARCANA,
                Skill.ANIMAL_HANDLING,
            )

    ###################################################################
    def test_stats(self):
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 7)
        self.assertEqual(int(self.c.stats[Stat.INTELLIGENCE].value), 6)  # +1 for origin

    ###################################################################
    def test_ac(self):
        self.assertEqual(self.c.armour.tag, Armour.NONE)
        self.assertEqual(self.c.ac.value, 12)
        self.c.wear_shield(Shield())
        self.assertEqual(self.c.ac.value, 14)
        self.c.wear_armour(Leather())
        self.assertEqual(self.c.ac.value, 15)
        self.assertIn("shield (2)", self.c.ac.reason)
        self.assertIn("dex_modifier (2)", self.c.ac.reason)
        self.assertIn("leather (11)", self.c.ac.reason)
        self.assertEqual(len(self.c.ac), 3, self.c.ac._reasons)

    ###################################################################
    def test_magic_armour(self):
        self.assertEqual(self.c.armour.tag, Armour.NONE)
        self.assertEqual(self.c.ac.value, 12)
        self.c.wear_shield(Shield(ac_bonus=1))
        self.assertEqual(self.c.ac.value, 15)
        self.c.wear_armour(Plate(ac_bonus=2))
        self.assertEqual(self.c.ac.value, 23)
        self.assertIn("shield (2)", self.c.ac.reason)
        self.assertIn("plate (18)", self.c.ac.reason)
        self.assertIn("ac_bonus (1)", self.c.ac.reason)
        self.assertIn("ac_bonus (2)", self.c.ac.reason)

        self.assertEqual(len(self.c.ac), 4, self.c.ac._reasons)

    ###################################################################
    def test_get_spells_of_level(self):
        start, stop = self.c.spell_display_range(0, False)
        self.assertEqual(start, 0)
        self.assertEqual(stop, 11)
        start, stop = self.c.spell_display_range(0, True)
        self.assertEqual(start, 11)
        self.assertEqual(stop, 999)

    ###################################################################
    def test_half_spell_sheet(self):
        self.assertTrue(self.c.half_spell_sheet())
        self.c.spell_slots = lambda x: x
        self.assertFalse(self.c.half_spell_sheet())

    ###################################################################
    def test_spell_display_limits(self):
        self.assertEqual(self.c.spell_display_limits(0), 11)
        self.assertEqual(self.c.spell_display_limits(9), 0)
        self.c.spell_slots = lambda x: x
        self.assertEqual(self.c.spell_display_limits(0), 8)
        self.assertEqual(self.c.spell_display_limits(9), 7)

    ###################################################################
    def test_known_spells(self):
        self.c.learn_spell(Spell.MAGIC_MISSILE, Spell.FIREBALL)
        spells = self.c.known_spells
        self.assertIn(Spell.MAGIC_MISSILE, spells)
        self.assertIn(Spell.FIREBALL, spells)
        self.assertNotIn(Spell.LIGHTNING_BOLT, spells)

        self.assertEqual(spells.count(Spell.FIREBALL), 1)
        self.c.prepare_spells(Spell.FIREBALL)
        self.assertEqual(spells.count(Spell.FIREBALL), 1)

    ###################################################################
    def test_abilities(self):
        self.assertTrue(self.c.has_feature(Feature.EXTRA_ATTACK))
        self.assertTrue(self.c.has_feature(Feature.DARKVISION60))

    ###################################################################
    def test_saving_throws(self):
        self.assertEqual(self.c.stats[Stat.INTELLIGENCE].proficient, 1)
        self.assertEqual(self.c.stats[Stat.DEXTERITY].proficient, 0)
        self.assertEqual(self.c.stats[Stat.WISDOM].modifier, 5)
        self.assertEqual(self.c.proficiency_bonus, 2)
        self.assertEqual(self.c.stats[Stat.WISDOM].saving_throw, 5 + 2)

    ###################################################################
    def test_initialise_skills(self):
        skills = self.c.initialise_skills(Skill.ANIMAL_HANDLING, Skill.ARCANA)
        self.assertIn(Skill.STEALTH, skills.keys())
        self.assertTrue(skills[Skill.ANIMAL_HANDLING].proficient)
        self.assertFalse(skills[Skill.SURVIVAL].proficient)
        self.assertEqual(skills[Skill.ANIMAL_HANDLING].origin, "Class Skill")

    ###################################################################
    def test_skills(self):
        self.assertTrue(self.c.is_proficient(Skill.ATHLETICS))  # Dummy Origin
        self.assertTrue(self.c.is_proficient(Skill.ARCANA))  # Dummy Class
        self.assertFalse(self.c.is_proficient(Skill.ANIMAL_HANDLING))

    ###################################################################
    def test_is_proficient(self):
        decept = self.c.skills[Skill.DECEPTION]
        decept.proficient = True
        self.assertTrue(self.c.is_proficient(Skill.DECEPTION))
        decept.proficient = False
        self.assertFalse(self.c.is_proficient(Skill.DECEPTION))

    ###################################################################
    def test_damage_resistance(self):
        self.assertEqual(len(self.c.damage_resistances), 0)
        self.c.add_damage_resistance(Reason("Test", DamageType.NECROTIC))
        self.assertEqual(self.c.damage_resistances.reason, "Test (necrotic)")

    ###################################################################
    def test_equipment(self):
        self.assertEqual(self.c.equipment, [])
        self.c.add_equipment("Foo")
        self.assertEqual(self.c.equipment, ["Foo"])
        self.c.add_equipment("Bar", "Baz")
        self.assertEqual(self.c.equipment, ["Foo", "Bar", "Baz"])

    ###################################################################
    def test_class_name(self):
        self.assertEqual(self.c.class_name, "DummyCharClass")

    ###################################################################
    def test_extra_attack(self):
        ea = self.c.extra_attacks
        self.assertIn("Bunny Rabbit", ea)

    ###################################################################
    def test_spell_attack_bonus(self):
        self.assertEqual(self.c.spell_casting_ability, Stat.STRENGTH)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 7)
        self.assertEqual(self.c.stats[Stat.STRENGTH].modifier, -2)
        self.assertEqual(self.c.spell_attack_bonus, 0)  # 2 for proficiency, -1 for strength mod

    ###################################################################
    def test_initiative(self):
        self.assertEqual(self.c.initiative.value, 3)
        self.assertIn("species_bonus (1)", self.c.initiative.reason)
        self.assertNotIn("feature alert (2)", self.c.initiative.reason)

        self.c.add_feature(Alert())
        self.assertEqual(self.c.initiative.value, 5)
        self.assertIn("species_bonus (1)", self.c.initiative.reason)
        self.assertIn("feature alert (2)", self.c.initiative.reason)

    ###################################################################
    def test_weapons(self):
        self.assertEqual(len(self.c.weapons), 1)  # Should start with only being unarmed
        self.assertEqual(self.c.weapons[0].tag, Weapon.UNARMED)
        self.c.add_weapon(Spear())
        self.assertEqual(len(self.c.weapons), 2)
        self.assertEqual(self.c.weapons[1].tag, Weapon.SPEAR)

    ###################################################################
    def test_languages(self):
        self.assertIn(Language.COMMON, self.c.languages)
        self.c.add_languages(Language.GIANT)
        self.assertIn(Language.GIANT, self.c.languages)

    ###################################################################
    def test_spells_of_level(self):
        self.c.learn_spell(Spell.JUMP, Spell.KNOCK, Spell.FLAME_BLADE, Spell.ELDRITCH_BLAST)
        self.c.prepare_spells(Spell.VITRIOLIC_SPHERE)
        self.assertEqual(self.c.spells_of_level(0), [Spell.ELDRITCH_BLAST])
        self.assertEqual(self.c.spells_of_level(1), [Spell.JUMP])
        self.assertEqual(self.c.spells_of_level(2), [Spell.FLAME_BLADE, Spell.KNOCK])
        self.assertEqual(self.c.spells_of_level(3), [])
        self.assertEqual(self.c.spells_of_level(4), [Spell.VITRIOLIC_SPHERE])

    ###################################################################
    def test_level_spells(self):
        self.c.learn_spell(Spell.JUMP, Spell.KNOCK, Spell.FLAME_BLADE, Spell.ELDRITCH_BLAST)
        self.c.prepare_spells(Spell.VITRIOLIC_SPHERE)
        self.assertEqual(("A", False, "Flame Blade", "Evoc", "[C]"), self.c.level_spells(2, False)[0])
        self.assertEqual(("B", False, "Knock", "Trans", ""), self.c.level_spells(2, False)[1])
        self.assertEqual(("A", True, "Vitriolic Sphere", "Evoc", ""), self.c.level_spells(4, False)[0])
        self.assertEqual(len(self.c.level_spells(4, False)), self.c.spell_display_limits(4))
        self.assertEqual(len(self.c.level_spells(4, True)), self.c.spell_display_limits(4))

    ###################################################################
    def test_level1(self):
        self.c.level1(hp=5)
        self.assertEqual(self.c.level, 1)
        self.assertEqual(int(self.c.hp), 7 - 1)  # 7 for hit dice, -1 for low con

    ###################################################################
    def test_level2(self):
        self.c.level1()
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 7 + 5 - 2)  # 7 for hit dice, 5 for level, -2 for low con

    ###################################################################
    def test_level3(self):
        self.c.level1()
        self.c.level2(hp=5)
        self.c.level3(hp=6)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(int(self.c.hp), 7 + 5 + 6 - 3)  # 7 for hit dice, 5 for level2, 6 for level 3, -3 for low con

    ###################################################################
    def test_level4(self):
        self.c.level4(hp=5, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION), force=True)
        self.assertEqual(self.c.level, 4)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 8)
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 9)
        self.assertIn("feature ability_score_improvement (1)", self.c.stats[Stat.STRENGTH].value.reason)
        self.assertIn("Base (7)", self.c.stats[Stat.STRENGTH].value.reason)

        with self.assertRaises(InvalidOption):
            self.c.level4(hp=6)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=1, force=True)
        self.assertEqual(self.c.level, 5)
        self.assertEqual(self.c.proficiency_bonus, 3)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1, force=True)
        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.proficiency_bonus, 3)

    ###################################################################
    def test_level7(self):
        self.c.level7(hp=1, force=True)
        self.assertEqual(self.c.level, 7)
        self.assertEqual(self.c.proficiency_bonus, 3)

    ###################################################################
    def test_level8(self):
        with self.assertRaises(InvalidOption):
            self.c.level8(hp=1, force=True)
        cha = int(self.c.stats[Stat.CHARISMA].value)
        dex = int(self.c.stats[Stat.DEXTERITY].value)
        self.c.level8(hp=1, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY), force=True)
        self.assertEqual(self.c.level, 8)
        self.assertEqual(self.c.proficiency_bonus, 3)
        self.assertEqual(int(self.c.stats[Stat.CHARISMA].value), cha + 1)
        self.assertEqual(int(self.c.stats[Stat.DEXTERITY].value), dex + 1)

    ###################################################################
    def test_level9(self):
        self.c.level9(hp=1, force=True)
        self.assertEqual(self.c.level, 9)
        self.assertEqual(self.c.proficiency_bonus, 4)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
