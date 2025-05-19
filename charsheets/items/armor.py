"""Magic Armor"""

from typing import TYPE_CHECKING

from charsheets.constants import Language, Weapon, DamageType
from charsheets.items.base_item import BaseItem
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#############################################################################
class DemonArmor(BaseItem):
    """While wearing this armor, you gain a +1 bonus to Armor Class, and you know Abyssal. In addition, the armor’s
    clawed gauntlets allow your Unarmed Strikes to deal 1d8 Slashing damage instead of the usual Bludgeoning damage,
    and you gain a +1 bonus to the attack and damage rolls of your Unarmed Strikes.

    Curse. Once you don this cursed armor, you can’t doff it unless you are targeted by a Remove Curse spell or similar
    magic. While wearing the armor, you have Disadvantage on attack rolls against demons and on saving throws against
    their spells and special abilities."""

    name = "Demon Armor"

    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason(self.name, Language.ABYSSAL)

    def mod_ac_bonus(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.name, 1)

    def mod_melee_dmg_bonus(self, weapon: Weapon, character: "BaseCharacter") -> Reason[int]:
        if weapon.tag == Weapon.UNARMED:
            return Reason(self.name, 1)
        return Reason()

    def mod_melee_atk_bonus(self, weapon: Weapon, character: "BaseCharacter") -> Reason[int]:
        if weapon.tag == Weapon.UNARMED:
            return Reason(self.name, 1)
        return Reason()

    def mod_dmg_dice(self, weapon: Weapon, character: "BaseCharacter") -> Reason[str]:
        if weapon.tag == Weapon.UNARMED:
            return Reason(self.name, "1d8")
        return Reason()

    def mod_dmg_type(self, weapon: Weapon, character: "BaseCharacter") -> Reason[DamageType]:
        if weapon.tag == Weapon.UNARMED:
            return Reason(self.name, DamageType.SLASHING)
        return Reason()

    def mod_desc(self, character: "BaseCharacter") -> Reason[str]:
        return Reason(
            self.name,
            """Curse. Once you don this cursed armor, you can’t doff it unless you are targeted by a 'Remove Curse' 
            spell or similar magic. While wearing the armor, you have Disadvantage on attack rolls against demons and 
            on saving throws against their spells and special abilities.""",
        )


# EOF
