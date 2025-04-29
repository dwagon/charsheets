from typing import TYPE_CHECKING

from charsheets.attack import Attack
from charsheets.constants import DamageType
from charsheets.reason import SignedReason
from charsheets.spell import Spell, spell_name

if TYPE_CHECKING:
    from charsheets.character import BaseCharacter


#######################################################################
class BaseSpell:
    def __init__(self) -> None:
        self._range: int = 0
        self._num_attacks: int = 1
        self.tag: Spell = Spell.NONE
        self.damage_type: DamageType = DamageType.NONE
        self.caster: BaseCharacter
        self._damage_dice: str = ""
        self._damage_bonus: int = 0

    def range(self) -> int:
        return self._range

    def num_attacks(self) -> int:
        return self._num_attacks

    def damage_dice(self) -> str:
        return self._damage_dice

    def damage_bonus(self) -> int:
        mod = self.caster.spell_damage_bonus(self.tag)
        return self._damage_bonus + mod

    def to_attack(self) -> Attack:
        if self.num_attacks():
            dmg_dice = f"{self.num_attacks()} x {self.damage_dice()}"
        else:
            dmg_dice = f"{self.damage_dice()}"

        return Attack(
            spell_name(self.tag),
            SignedReason("Spell Attack Bonus", self.caster.spell_attack_bonus),
            dmg_dice,
            SignedReason("", self.damage_bonus()),
            self.damage_type,
        )


# EOF
