from charsheets.constants import DamageType
from charsheets.spell import Spell
from charsheets.spells.base_spell import BaseSpell


class EldritchBlast(BaseSpell):
    def __init__(self):
        super().__init__()
        self.damage_type = DamageType.FORCE
        self.tag = Spell.ELDRITCH_BLAST

    def range(self) -> int:
        return 120

    def damage_dice(self) -> str:
        return "1d10"

    def num_attacks(self) -> int:
        if self.caster.level >= 17:
            return 4
        elif self.caster.level >= 11:
            return 3
        elif self.caster.level >= 5:
            return 2
        return 1
