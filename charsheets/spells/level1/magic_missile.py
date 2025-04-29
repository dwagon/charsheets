from charsheets.constants import DamageType
from charsheets.spell import Spell
from charsheets.spells.base_spell import BaseSpell


class MagicMissile(BaseSpell):
    def __init__(self):
        super().__init__()
        self._range = 120
        self._damage_dice = "d4"
        self._damage_bonus = 1
        self.tag = Spell.MAGIC_MISSILE
        self.damage_type = DamageType.FORCE

    def num_attacks(self) -> int:
        return 3


# EOF
