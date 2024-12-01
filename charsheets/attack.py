from charsheets.reason import Reason
from charsheets.constants import DamageType


#############################################################################
class Attack:
    def __init__(self, name: str, atk_bonus: Reason, dmg_dice: str, dmg_bonus: Reason, dmg_type: DamageType) -> None:
        self.name: str = name
        self.atk_bonus: Reason = atk_bonus
        self.dmg_dice: str = dmg_dice
        self.dmg_bonus: Reason = dmg_bonus
        self.dmg_type: DamageType = dmg_type


# EOF
