from charsheets.constants import DamageType
from charsheets.spell import Spell
from charsheets.spells.base_spell import BaseSpell


class FireBolt(BaseSpell):
    """Fire Bolt"""

    def __init__(self):
        super().__init__()
        self.damage_type = DamageType.FIRE
        self.tag = Spell.FIRE_BOLT

    def spell_range(self) -> int:
        return 120

    def damage_dice(self) -> str:
        if self.caster.level >= 17:
            return "4d10"
        if self.caster.level >= 11:
            return "3d10"
        if self.caster.level >= 5:
            return "2d10"
        return "1d10"

    def num_attacks(self) -> int:
        return 1
