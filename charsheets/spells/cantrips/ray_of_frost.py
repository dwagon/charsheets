"""https://www.dndbeyond.com/spells/2226-ray-of-frost"""

from charsheets.constants import DamageType
from charsheets.spell import Spell
from charsheets.spells.base_spell import BaseSpell


class RayOfFrost(BaseSpell):
    """Ray of Frost"""

    def __init__(self):
        super().__init__()
        self.damage_type = DamageType.COLD
        self.tag = Spell.RAY_OF_FROST

    def spell_range(self) -> int:
        return 60

    def damage_dice(self) -> str:
        if self.caster.level >= 17:
            return "4d8"
        if self.caster.level >= 11:
            return "3d8"
        if self.caster.level >= 5:
            return "2d8"
        return "1d8"

    def num_attacks(self) -> int:
        return 1
