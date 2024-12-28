import unittest

from charsheets.ability import get_ability
from charsheets.constants import Armour, DamageType
from charsheets.constants import Skill, Stat, Ability, Weapon
from charsheets.reason import Reason
from tests.dummy import DummyCharClass, DummySpecies, DummyOrigin
from charsheets.feats import Alert
from charsheets.abilities.feat import AbilityScoreImprovement


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
    def test_stats(self):
        self.assertEqual(int(self.c.strength.value), 7)
        self.assertEqual(int(self.c.stats[Stat.INTELLIGENCE].value), 6)  # +1 for origin

    ###################################################################
    def test_ac(self):
        self.assertEqual(self.c.armour, Armour.NONE)
        self.assertEqual(self.c.ac.value, 12)
        self.c.shield = True
        self.assertEqual(self.c.ac.value, 14)
        self.c.armour = Armour.LEATHER
        self.assertEqual(self.c.ac.value, 15)
        self.assertIn("shield (2)", self.c.ac.reason)
        self.assertIn("dex_modifier (2)", self.c.ac.reason)
        self.assertIn("leather (11)", self.c.ac.reason)
        self.assertEqual(len(self.c.ac), 3, self.c.ac._reasons)

    ###################################################################
    def test_abilities(self):
        self.assertEqual(self.c.abilities, {get_ability(Ability.RAGE), get_ability(Ability.DARKVISION60)})

    ###################################################################
    def test_saving_throws(self):
        self.assertEqual(self.c.intelligence.proficient, 1)
        self.assertEqual(self.c.dexterity.proficient, 0)
        self.assertEqual(self.c.wisdom.modifier, 5)
        self.assertEqual(self.c.proficiency_bonus, 2)
        self.assertEqual(self.c.wisdom.saving_throw, 5 + 2)

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
        self.assertNotIn("feat alert (2)", self.c.initiative.reason)

        self.c.add_feat(Alert(self.c))
        self.assertEqual(self.c.initiative.value, 5)
        self.assertIn("species_bonus (1)", self.c.initiative.reason)
        self.assertIn("feat alert (2)", self.c.initiative.reason)

    ###################################################################
    def test_weapons(self):
        weaps = self.c.weapons.copy()
        self.assertEqual(len(self.c.weapons), 1)  # Should start with only being unarmed
        weaps_0 = weaps.pop()
        self.assertEqual(weaps_0.tag, Weapon.UNARMED)
        self.c.add_weapon(Weapon.SPEAR)
        self.assertEqual(len(self.c.weapons), 2)

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
        self.assertIn("feat ability_score_improvement (1)", self.c.stats[Stat.STRENGTH].value.reason)
        self.assertIn("Base (7)", self.c.stats[Stat.STRENGTH].value.reason)


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
