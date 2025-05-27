from charsheets.constants import DamageType
from charsheets.reason import SignedReason


#############################################################################
class Attack:
    def __init__(
        self,
        name: str,
        atk_bonus: SignedReason,
        dmg_dice: str,
        dmg_bonus: SignedReason,
        dmg_type: DamageType,
        atk_range: int = 0,
        notes: str = "",
    ) -> None:
        self.name: str = name
        self.atk_bonus: SignedReason = atk_bonus
        self.dmg_dice: str = dmg_dice
        self.dmg_bonus: SignedReason = dmg_bonus
        self.dmg_type: DamageType = dmg_type
        self.atk_range = atk_range
        self.notes = notes

        assert isinstance(self.name, str)
        assert isinstance(self.dmg_type, DamageType)

    def __repr__(self):
        return f"<Attack {self.name}: {self.atk_bonus} {self.dmg_dice}{self.dmg_bonus} {self.dmg_type}>"


# EOF
