import unittest

from charsheets.spell import is_cantrip, Spell, is_ritual, is_level, spell_school, spell_name, spell_flags


#######################################################################
class TestSpell(unittest.TestCase):
    def test_is_cantrip(self):
        self.assertTrue(is_cantrip(Spell.ELDRITCH_BLAST))
        self.assertFalse(is_cantrip(Spell.FIREBALL))

    def test_is_ritual(self):
        self.assertTrue(is_ritual(Spell.FIND_FAMILIAR))
        self.assertFalse(is_ritual(Spell.ELDRITCH_BLAST))

    def test_is_level(self):
        self.assertTrue(is_level(Spell.FIND_FAMILIAR, 1))
        self.assertTrue(is_level(Spell.FIREBALL, 3))
        self.assertFalse(is_level(Spell.WISH, 3))

    def test_spell_school(self):
        self.assertEqual(spell_school(Spell.FIREBALL), "Evoc")

    def test_spell_name(self):
        self.assertEqual(spell_name(Spell.FIREBALL), "Fireball")
        self.assertEqual(spell_name(Spell.MORDENKAINENS_SWORD), "Mordenkainen's Sword")

    def test_spell_flags(self):
        self.assertEqual(spell_flags(Spell.FIND_FAMILIAR), "[R, M]")


#######################################################################
if __name__ == "__main__":  # pragma: no coverage
    unittest.main()

# EOF
