import unittest

from charsheets.character import Character2014
from charsheets.classes2014 import (
    Cleric,
    KnowledgeCleric,
    TempestCleric,
    LightCleric,
    LifeCleric,
    NatureCleric,
    WarCleric,
    TrickeryCleric,
    BlessingsOfKnowledge,
    AcolyteOfNature,
)
from charsheets.constants import Skill, Stat, Proficiency, Language, Feature
from charsheets.exception import InvalidOption
from charsheets.spell import Spell
from tests.dummy import DummyBackground, DummyRace


#######################################################################
class TestCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_basic(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))

        self.assertEqual(self.c.max_hit_dice, "1d8")
        self.assertTrue(self.c.saving_throw_proficiency(Stat.WISDOM))
        self.assertTrue(self.c.saving_throw_proficiency(Stat.CHARISMA))
        self.assertFalse(self.c.saving_throw_proficiency(Stat.STRENGTH))
        self.assertIn(Proficiency.MEDIUM_ARMOUR, self.c.armour_proficiencies())
        self.assertNotIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SHIELDS, self.c.armour_proficiencies())
        self.assertIn(Proficiency.SIMPLE_WEAPONS, self.c.weapon_proficiencies())
        self.assertNotIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())
        self.assertEqual(self.c.spell_casting_ability, Stat.WISDOM)

    ###################################################################
    def test_level1(self):
        self.c.add_level(Cleric(skills=[Skill.PERSUASION, Skill.RELIGION]))

        self.assertEqual(self.c.level, 1)
        self.assertEqual(int(self.c.hp), 8 + 1)
        self.assertEqual(self.c.spell_slots(1), 2)
        self.assertIn(Spell.BANE, [_[0] for _ in self.c.spells_of_level(1)])


#######################################################################
class TestKnowledgeCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_no_blessing(self):
        with self.assertRaises(InvalidOption):
            self.c.add_level(KnowledgeCleric(skills=[Skill.PERSUASION, Skill.RELIGION]))

    ###################################################################
    def test_features(self):
        self.c.add_level(
            KnowledgeCleric(
                skills=[Skill.PERSUASION, Skill.RELIGION],
                blessing=BlessingsOfKnowledge(Language.ORC, Language.GNOMISH, Skill.ARCANA, Skill.NATURE),
            )
        )
        self.assertIn(Spell.COMMAND, self.c.prepared_spells)
        self.assertIn(Spell.IDENTIFY, self.c.prepared_spells)
        self.assertTrue(self.c.is_proficient(Skill.ARCANA))
        self.assertIn(Language.ORC, self.c.languages)


#######################################################################
class TestLifeCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_features(self):
        self.c.add_level(
            LifeCleric(
                skills=[Skill.PERSUASION, Skill.RELIGION],
            )
        )
        self.assertIn(Spell.BLESS, self.c.prepared_spells)
        self.assertIn(Spell.CURE_WOUNDS, self.c.prepared_spells)
        self.assertTrue(self.c.has_feature(Feature.DISCIPLE_OF_LIFE14))
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())


#######################################################################
class TestLightCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_features(self):
        self.c.add_level(
            LightCleric(
                skills=[Skill.PERSUASION, Skill.RELIGION],
            )
        )
        self.assertIn(Spell.BURNING_HANDS, self.c.prepared_spells)
        self.assertIn(Spell.FAERIE_FIRE, self.c.prepared_spells)
        self.assertIn(Spell.LIGHT, self.c.known_spells)

        self.assertTrue(self.c.has_feature(Feature.WARDING_FLARE14))


#######################################################################
class TestNatureCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_no_acolyte(self):
        with self.assertRaises(InvalidOption):
            self.c.add_level(NatureCleric(skills=[Skill.PERSUASION, Skill.RELIGION]))

    ###################################################################
    def test_features(self):
        self.c.add_level(
            NatureCleric(
                skills=[Skill.PERSUASION, Skill.RELIGION], acolyte=AcolyteOfNature(Spell.DRUIDCRAFT, Skill.ANIMAL_HANDLING)
            )
        )
        self.assertIn(Spell.ANIMAL_FRIENDSHIP, self.c.prepared_spells)
        self.assertIn(Spell.SPEAK_WITH_ANIMALS, self.c.prepared_spells)
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Spell.DRUIDCRAFT, self.c.known_spells)
        self.assertTrue(self.c.is_proficient(Skill.ANIMAL_HANDLING))


#######################################################################
class TestTempestCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_features(self):
        self.c.add_level(TempestCleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.assertIn(Spell.FOG_CLOUD, self.c.prepared_spells)
        self.assertIn(Spell.THUNDERWAVE, self.c.prepared_spells)
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())

        self.assertTrue(self.c.has_feature(Feature.WRATH_OF_THE_STORM14))


#######################################################################
class TestTricksterCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_features(self):
        self.c.add_level(TrickeryCleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.assertIn(Spell.CHARM_PERSON, self.c.prepared_spells)
        self.assertIn(Spell.DISGUISE_SELF, self.c.prepared_spells)

        self.assertTrue(self.c.has_feature(Feature.BLESSING_OF_THE_TRICKSTER14))


#######################################################################
class TestWarCleric(unittest.TestCase):
    ###################################################################
    def setUp(self):
        self.c = Character2014(
            "name",
            DummyBackground(),
            DummyRace(),
            strength=14,
            dexterity=8,
            constitution=13,
            intelligence=10,
            wisdom=15,
            charisma=12,
        )

    ###################################################################
    def test_features(self):
        self.c.add_level(WarCleric(skills=[Skill.PERSUASION, Skill.RELIGION]))
        self.assertIn(Spell.DIVINE_FAVOR, self.c.prepared_spells)
        self.assertIn(Spell.SHIELD_OF_FAITH, self.c.prepared_spells)
        self.assertIn(Proficiency.HEAVY_ARMOUR, self.c.armour_proficiencies())
        self.assertIn(Proficiency.MARTIAL_WEAPONS, self.c.weapon_proficiencies())

        self.assertTrue(self.c.has_feature(Feature.WAR_PRIEST14))


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()


# EOF
