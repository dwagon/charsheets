import unittest

from charsheets.constants import Skill, Ability
from charsheets.species import Goliath, GiantsAncestry
from tests.dummy import DummyCharClass, DummyOrigin


#######################################################################
class TestGoliath(unittest.TestCase):
    def setUp(self):
        self.c = DummyCharClass(
            "test_goliath",
            DummyOrigin(),
            Goliath(GiantsAncestry.CLOUD_GIANT),
            Skill.DECEPTION,
            Skill.PERCEPTION,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_ancestry(self):
        self.assertTrue(self.c.has_ability(Ability.GIANT_ANCESTRY))
        self.assertTrue(self.c.has_ability(Ability.GIANT_CLOUDS_JAUNT))
        hg = DummyCharClass(
            "hill giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.HILL_GIANT),
            Skill.DECEPTION,
            Skill.PERCEPTION,
        )
        self.assertTrue(hg.has_ability(Ability.GIANT_HILLS_TUMBLE))

        cg = DummyCharClass(
            "cloud giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.CLOUD_GIANT),
            Skill.DECEPTION,
            Skill.PERCEPTION,
        )
        self.assertTrue(cg.has_ability(Ability.GIANT_CLOUDS_JAUNT))

        fg = DummyCharClass(
            "fire giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.FIRE_GIANT),
            Skill.DECEPTION,
            Skill.PERCEPTION,
        )
        self.assertTrue(fg.has_ability(Ability.GIANT_FIRES_BURN))

        frg = DummyCharClass(
            "frost giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.FROST_GIANT),
            Skill.DECEPTION,
            Skill.PERCEPTION,
        )
        self.assertTrue(frg.has_ability(Ability.GIANT_FROSTS_CHILL))

        smg = DummyCharClass(
            "storm giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.STORM_GIANT),
            Skill.DECEPTION,
            Skill.PERCEPTION,
        )
        self.assertTrue(smg.has_ability(Ability.GIANT_STORMS_THUNDER))

        sng = DummyCharClass(
            "stone giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.STONE_GIANT),
            Skill.DECEPTION,
            Skill.PERCEPTION,
        )
        self.assertTrue(sng.has_ability(Ability.GIANT_STONES_ENDURANCE))

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 35)


# EOF
