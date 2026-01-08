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


MONEY: dict[Coin, int] = {Coin.PLATINUM: 0, Coin.GOLD: 0, Coin.ELECTRUM: 0, Coin.SILVER: 0, Coin.COPPER: 0}


#############################################################################
class MoneyMixin:
    """Mixin to help reduce class bloat in Character"""

    #########################################################################
    @staticmethod
    def add_coins(coin: Coin, amount: int):
        """Add coins"""
        MONEY[coin] += amount

    #########################################################################
    @staticmethod
    def remove_coins(coin: Coin, amount: int):
        """Remove / Spend coins"""
        MONEY[coin] -= amount

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
