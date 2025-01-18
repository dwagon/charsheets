from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.paladin import Paladin
from charsheets.constants import Ability
from charsheets.spells import Spells


#################################################################################
class PaladinOathOfVengeance(Paladin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Paladin (Oath of Vengeance)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {VowOfEmnity()}
        abilities |= super().class_abilities()
        self.prepare_spells(Spells.BANE, Spells.HUNTERS_MARK)
        if self.level >= 5:
            self.prepare_spells(Spells.HOLD_PERSON, Spells.MISTY_STEP)
        return abilities


#############################################################################
class VowOfEmnity(BaseAbility):
    tag = Ability.VOW_OF_EMNITY
    _desc = """When you take the Attack action, you can expend one use of your Channel Divinity to utter a vow of
    enmity against a creature you can see within 30 feet of yourself. You have Advantage on attack rolls
    against the creature for 1 minute or until you use this feature again.

    If the creature drops to O Hit Points before the vow ends, you can transfer the vow to a different creature within 
    30 feet of yourself (no action required)."""


# EOF
