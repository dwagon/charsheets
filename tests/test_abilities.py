import unittest

from charsheets.classes import Wizard
from charsheets.constants import Skill, Weapon, Stat
from tests.dummy import DummySpecies, DummyOrigin
from charsheets.abilities import AbilityScoreImprovement


#######################################################################
class TestAbility(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Wizard(
            "name",
            DummyOrigin(),
            DummySpecies(),
            Skill.ARCANA,
            Skill.NATURE,
            strength=7,
            dexterity=14,
            constitution=11,
            wisdom=20,
            intelligence=5,
            charisma=10,
        )
        self.c.add_weapon(Weapon.LONGSWORD)

    ###################################################################
    def test_ability_score_improvement(self):
        self.assertEqual(int(self.c.dexterity.value), 14)
        asi = AbilityScoreImprovement(Stat.DEXTERITY, Stat.INTELLIGENCE)
        self.c.add_ability(asi)
        self.assertEqual(int(self.c.dexterity.value), 15)
        self.assertEqual(int(self.c.intelligence.value), 6)
        self.assertEqual(int(self.c.wisdom.value), 20, "Unchanged")
        self.assertEqual(asi.desc, "Increased Dexterity and Intelligence")

        asi2 = AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)
        self.assertEqual(int(self.c.charisma.value), 10)
        self.c.add_ability(asi2)
        self.assertEqual(int(self.c.charisma.value), 12)
        self.assertEqual(asi2.desc, "Increased Charisma twice")


#######################################################################
if __name__ == "__main__":
    unittest.main()

# EOF
