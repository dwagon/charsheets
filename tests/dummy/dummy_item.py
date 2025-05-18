from typing import TYPE_CHECKING

from charsheets.items.base_item import BaseItem
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#############################################################################
class DummyItem(BaseItem):
    name = "Dummy Item"

    def mod_desc(self, character: "BaseCharacter") -> Reason[str]:
        return Reason("Dummy Item", """Curse. Makes you a dummy.""")

    def mod_stat_str_set(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Dummy Item", 21)


# EOF
