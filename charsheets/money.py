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


MONEY = Money()


#############################################################################
class MoneyMixin:
    """Mixin to help reduce class bloat in Character"""

    #########################################################################
    def add_coins(self, coin: Coin, amount: int):
        """Add coins"""
        MONEY.add_coins(coin, amount)

    #########################################################################
    def remove_coins(self, coin: Coin, amount: int):
        """Remove / Spend coins"""
        MONEY.remove_coins(coin, amount)

    #########################################################################
    @property
    def pp(self) -> int:
        """Platinum pieces"""
        return MONEY[Coin.PLATINUM]

    #########################################################################
    @property
    def gp(self) -> int:
        """Gold pieces"""
        return MONEY[Coin.GOLD]

    #########################################################################
    @property
    def ep(self) -> int:
        """Electrum pieces"""
        return MONEY[Coin.ELECTRUM]

    #########################################################################
    @property
    def sp(self) -> int:
        """Silver pieces"""
        return MONEY[Coin.SILVER]

    #########################################################################
    @property
    def cp(self) -> int:
        """Copper pieces"""
        return MONEY[Coin.COPPER]


# EOF
