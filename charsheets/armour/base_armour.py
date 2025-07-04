from enum import StrEnum, auto
from typing import TYPE_CHECKING, Any, Optional

from charsheets.constants import Armour, Stat, ArmourCategory
from charsheets.exception import UnhandledException, NotDefined
from charsheets.reason import Reason
from charsheets.util import safe
from charsheets.items.base_item import BaseItem

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Modifiers(StrEnum):
    AC_BONUS = auto()
    NAME = auto()


#############################################################################
class BaseArmour(BaseItem):
    tag: Armour
    category: ArmourCategory

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.wearer: Optional["Character"] = None
        self.name = self.tag.title()
        self.ac: int = 0
        self.stealth_disadvantage: bool = False
        self.dex_mod: bool = False
        self.dex_max = 2
        self.ac_mod = 0
        self.modifiers: dict[Modifiers, Any] = self.validate_kwargs(kwargs)

    #########################################################################
    def validate_kwargs(self, kwargs) -> dict[Modifiers, Any]:
        """Ensure that all the kwargs are spelt correctly etc."""
        modifiers: dict[Modifiers, Any] = {}

        for key, value in kwargs.items():
            try:
                modifiers[Modifiers(key)] = value
            except ValueError:
                raise UnhandledException(f"{key} not handled by Armour")
        return modifiers

    ########################################################################
    def __str__(self):
        if self.modifiers.get(Modifiers.NAME):
            return self.modifiers.get(Modifiers.NAME)
        return safe(self.tag.title())

    ########################################################################
    def is_heavy(self) -> bool:
        return self.category == ArmourCategory.HEAVY

    ########################################################################
    def armour_class(self) -> Reason[int]:
        if self.wearer is None:  # pragma: no coverage
            raise NotDefined("Armour needs to be added to character")
        arm = Reason(self.tag, max(self.ac, self.ac_mod))
        if self.dex_mod:
            arm.add("dex_modifier", min(self.dex_max, self.wearer.stats[Stat.DEXTERITY].modifier))
        if self.modifiers.get(Modifiers.AC_BONUS):
            arm.add("ac_bonus", self.modifiers.get(Modifiers.AC_BONUS))

        return arm


# EOF
