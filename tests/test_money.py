"""Tests for money"""
import unittest
from charsheets.character import Character
from charsheets.money import Coin
from charsheets.constants import Language, Stat
from tests.dummy import DummySpecies, DummyOrigin


#######################################################################
class TestMoney(unittest.TestCase):
    """Test money"""

    ###################################################################
    def setUp(self):
        self.c = Character(
            "name",
            DummyOrigin(Stat.INTELLIGENCE),
            DummySpecies(),
            Language.ORC,
            Language.GNOMISH,
            strength=7,
            dexterity=14,
            constitution=8,
            wisdom=20,
            intelligence=5,
            charisma=11,
        )

    ###################################################################
    def test_adding(self) -> None:
        """Test Adding Coins"""
        self.assertEqual(self.c.ep, 0)
        self.c.add_coins(Coin.ELECTRUM, 73)
        self.assertEqual(self.c.ep, 73)
        self.c.add_coins(Coin.ELECTRUM, 3)
        self.assertEqual(self.c.ep, 76)

    ###################################################################
    def test_removing(self) -> None:
        """Test Removing Coins"""
        self.assertEqual(self.c.cp, 0)
        self.c.add_coins(Coin.COPPER, 73)
        self.assertEqual(self.c.cp, 73)
        self.c.remove_coins(Coin.COPPER, 3)
        self.assertEqual(self.c.cp, 70)


#######################################################################
if __name__ == "__main__":
    unittest.main()
