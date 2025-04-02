import unittest

from charsheets.character import Character
from charsheets.constants import Feature, Language
from charsheets.main import render
from charsheets.species.homebrew.kuatoa import Kuatoa
from tests.dummy import DummyOrigin


#######################################################################
class TestKuaToa(unittest.TestCase):
    def setUp(self):
        self.c = Character(
            "test_fish",
            DummyOrigin(),
            Kuatoa(),
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
    def test_speed(self):
        self.assertEqual(self.c.speed.value, 30)
        self.assertEqual(self.c.swim_speed.value, 30)

    ###################################################################
    def test_abilities(self):
        self.assertTrue(self.c.has_feature(Feature.AMPHIBIOUS))
        self.assertTrue(self.c.has_feature(Feature.SPEAK_WITH_FISH))
        self.assertTrue(self.c.has_feature(Feature.SLIPPERY))
        self.assertTrue(self.c.has_feature(Feature.SWIM))

        swf = self.c.find_feature(Feature.SPEAK_WITH_FISH)
        self.assertEqual(swf.goes, 2)

    ###################################################################
    def test_render(self):
        r = render(self.c, "char_sheet.jinja")
        self.assertIn("Darkvision Underwater 120", r)


# EOF
