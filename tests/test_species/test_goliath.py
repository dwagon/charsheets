import unittest

from charsheets.character import Character
from charsheets.constants import Feature, Language
from charsheets.species import Goliath, GiantsAncestry
from tests.dummy import DummyOrigin


#######################################################################
class TestGoliath(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_goliath",
            DummyOrigin(),
            Goliath(GiantsAncestry.CLOUD_GIANT),
            Language.ORC,
            Language.GNOMISH,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )

    ###################################################################
    def test_ancestry(self):
        self.assertTrue(self.c.has_feature(Feature.GIANT_ANCESTRY))
        self.assertTrue(self.c.has_feature(Feature.GIANT_CLOUDS_JAUNT))
        hg = Character(
            "hill giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.HILL_GIANT),
            Language.ORC,
            Language.GNOMISH,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )
        self.assertTrue(hg.has_feature(Feature.GIANT_HILLS_TUMBLE))

        cg = Character(
            "cloud giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.CLOUD_GIANT),
            Language.ORC,
            Language.GNOMISH,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )
        self.assertTrue(cg.has_feature(Feature.GIANT_CLOUDS_JAUNT))

        fg = Character(
            "fire giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.FIRE_GIANT),
            Language.ORC,
            Language.GNOMISH,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )
        self.assertTrue(fg.has_feature(Feature.GIANT_FIRES_BURN))

        frg = Character(
            "frost giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.FROST_GIANT),
            Language.ORC,
            Language.GNOMISH,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )
        self.assertTrue(frg.has_feature(Feature.GIANT_FROSTS_CHILL))

        smg = Character(
            "storm giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.STORM_GIANT),
            Language.ORC,
            Language.GNOMISH,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )
        self.assertTrue(smg.has_feature(Feature.GIANT_STORMS_THUNDER))

        sng = Character(
            "stone giant",
            DummyOrigin(),
            Goliath(GiantsAncestry.STONE_GIANT),
            Language.ORC,
            Language.GNOMISH,
            strength=16,
            dexterity=14,
            constitution=15,
            intelligence=10,
            wisdom=10,
            charisma=12,
        )
        self.assertTrue(sng.has_feature(Feature.GIANT_STONES_ENDURANCE))

    ###################################################################
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 35)


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
