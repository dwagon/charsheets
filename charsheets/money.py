"""Class to handle money treasure"""

from enum import StrEnum, auto


#############################################################################
class Coin(StrEnum):
    """Coin names"""

    PLATINUM = auto()
    GOLD = auto()
    ELECTRUM = auto()
    SILVER = auto()
    COPPER = auto()


#############################################################################
class Money:
    """Handle money for a character"""

    def __init__(self) -> None:
        self._coins: dict[Coin, int] = {Coin.PLATINUM: 0, Coin.GOLD: 0, Coin.ELECTRUM: 0, Coin.SILVER: 0, Coin.COPPER: 0}

    def add_coins(self, coin: Coin, amount: int) -> None:
        """Add coins"""
        self._coins[coin] += amount

    def remove_coins(self, coin: Coin, amount: int) -> None:
        """Remove coins"""
        self._coins[coin] -= amount

    def __getitem__(self, coin: Coin) -> int:
        return self._coins[coin]


# EOF
