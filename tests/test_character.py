import unittest

from charsheets.constants import Armour, DamageType, Language
from charsheets.constants import Skill, Stat, Ability, Weapon
from charsheets.reason import Reason
from charsheets.spells import Spells
from tests.dummy import DummyCharClass, DummySpecies, DummyOrigin
from charsheets.abilities import Alert, AbilityScoreImprovement
from charsheets.weapons import Spear
from charsheets.armour import Leather
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
        self.assertEqual(int(self.c.strength.value), 7)
        self.assertEqual(int(self.c.stats[Stat.INTELLIGENCE].value), 6)  # +1 for origin

    ###################################################################
    def test_ac(self):
        self.assertEqual(self.c.armour.tag, Armour.NONE)
        self.assertEqual(self.c.ac.value, 12)
        self.c.shield = True
        self.assertEqual(self.c.ac.value, 14)
        self.c.wear_armour(Leather())
        self.assertEqual(self.c.ac.value, 15)
        self.assertIn("shield (2)", self.c.ac.reason)
        self.assertIn("dex_modifier (2)", self.c.ac.reason)
        self.assertIn("leather (11)", self.c.ac.reason)
        self.assertEqual(len(self.c.ac), 3, self.c.ac._reasons)

    ###################################################################
    def test_known_spells(self):
        self.c.learn_spell(Spells.MAGIC_MISSILE, Spells.FIREBALL)
        spells = self.c.known_spells
        self.assertIn(Spells.MAGIC_MISSILE, spells)
        self.assertIn(Spells.FIREBALL, spells)
        self.assertNotIn(Spells.LIGHTNING_BOLT, spells)

        self.assertEqual(spells.count(Spells.FIREBALL), 1)
        self.c.prepare_spells(Spells.FIREBALL)
        self.assertEqual(spells.count(Spells.FIREBALL), 1)

    ###################################################################
    def test_abilities(self):
        self.assertTrue(self.c.has_ability(Ability.RAGE))
        self.assertTrue(self.c.has_ability(Ability.DARKVISION60))

    ###################################################################
    def test_saving_throws(self):
        self.assertEqual(self.c.intelligence.proficient, 1)
        self.assertEqual(self.c.dexterity.proficient, 0)
        self.assertEqual(self.c.wisdom.modifier, 5)
        self.assertEqual(self.c.proficiency_bonus, 2)
        self.assertEqual(self.c.wisdom.saving_throw, 5 + 2)

    ###################################################################
    def test_skills(self):
        self.assertIn(Skill.ATHLETICS, self.c.skills)  # Dummy Origin
        self.assertIn(Skill.ARCANA, self.c.skills)  # Dummy Class
        self.assertNotIn(Skill.ANIMAL_HANDLING, self.c.skills)

    ###################################################################
    def test_lookup_skill(self):
        aths = self.c.lookup_skill(Skill.ATHLETICS)
        self.assertEqual(aths.proficient, 1)
        self.assertEqual(aths.origin, "None")

        anim = self.c.lookup_skill(Skill.ANIMAL_HANDLING)
        self.assertEqual(anim.proficient, 0)
        self.assertEqual(anim.origin, "")

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
    def test_spell_attack_bonus(self):
        self.assertEqual(self.c.spell_casting_ability, Stat.STRENGTH)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 7)
        self.assertEqual(self.c.stats[Stat.STRENGTH].modifier, -2)
        self.assertEqual(self.c.spell_attack_bonus, 0)  # 2 for proficiency, -1 for strength mod

    ###################################################################
    def test_initiative(self):
        self.assertEqual(self.c.initiative.value, 3)
        self.assertIn("species_bonus (1)", self.c.initiative.reason)
        self.assertNotIn("ability alert (2)", self.c.initiative.reason)

        self.c.add_ability(Alert())
        self.assertEqual(self.c.initiative.value, 5)
        self.assertIn("species_bonus (1)", self.c.initiative.reason)
        self.assertIn("ability alert (2)", self.c.initiative.reason)

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
    def test_level_spells(self):
        self.c.learn_spell(Spells.JUMP, Spells.KNOCK, Spells.FLAME_BLADE, Spells.ELDRITCH_BLAST)
        self.assertEqual(self.c.spells_of_level(1), [Spells.JUMP])
        self.assertEqual(self.c.spells_of_level(2), [Spells.FLAME_BLADE, Spells.KNOCK])
        self.assertEqual(self.c.spells_of_level(3), [])
        self.assertEqual(self.c.spells_of_level(0), [Spells.ELDRITCH_BLAST])

    ###################################################################
    def test_level2(self):
        self.c.level2(hp=5)
        self.assertEqual(self.c.level, 2)
        self.assertEqual(int(self.c.hp), 7 + 5 - 2)  # 7 for hit dice, 5 for level, -2 for low con

    ###################################################################
    def test_level3(self):
        self.c.level3(hp=5 + 6)
        self.assertEqual(self.c.level, 3)
        self.assertEqual(int(self.c.hp), 7 + 5 + 6 - 3)  # 7 for hit dice, 5 for level2, 6 for level 3, -3 for low con

    ###################################################################
    def test_level4(self):
        self.c.level4(hp=5, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION))
        self.assertEqual(self.c.level, 4)
        self.assertEqual(int(self.c.stats[Stat.STRENGTH].value), 8)
        self.assertEqual(int(self.c.stats[Stat.CONSTITUTION].value), 9)
        self.assertIn("ability ability_score_improvement (1)", self.c.stats[Stat.STRENGTH].value.reason)
        self.assertIn("Base (7)", self.c.stats[Stat.STRENGTH].value.reason)

        with self.assertRaises(InvalidOption):
            self.c.level4(hp=6)

    ###################################################################
    def test_level5(self):
        self.c.level5(hp=5 + 6 + 7 + 2)
        self.assertEqual(self.c.level, 5)
        self.assertEqual(
            int(self.c.hp), 7 + 5 + 6 + 7 + 2 - 5
        )  # 7 for hit dice, 5 for level2, 6 for level 3, 7 for level 4, 2 for level 5, -5 for low con
        self.assertEqual(self.c.proficiency_bonus, 3)

    ###################################################################
    def test_level6(self):
        self.c.level6(hp=1)
        self.assertEqual(self.c.level, 6)
        self.assertEqual(self.c.proficiency_bonus, 3)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
