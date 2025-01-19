from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.paladin import Paladin
from charsheets.constants import Ability
from charsheets.spell import Spell


#################################################################################
class PaladinOathOfDevotion(Paladin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Paladin (Oath of Devotion)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {SacredWeapon()}
        abilities |= super().class_abilities()
        self.prepare_spells(Spell.PROTECTION_FROM_EVIL_AND_GOOD, Spell.SHIELD_OF_FAITH)
        if self.level >= 5:
            self.prepare_spells(Spell.AID, Spell.ZONE_OF_TRUTH)
        return abilities


#############################################################################
class SacredWeapon(BaseAbility):
    tag = Ability.SACRED_WEAPON
    _desc = ""

    @property
    def desc(self) -> str:
        bonus = max(1, self.owner.charisma.modifier)
        return f"""When you take the Attack action, you can expend one use of your Channel Divinity to imbue one 
        Melee weapon that you are holding with positive energy. For 10 minutes or until you use this feature again, 
        you add {bonus}, and each time you hit with it, you cause it to deal its normal damage type or Radiant 
        damage. The weapon also emits Bright Light in a 20-foot radius and Dim Light 20 feet beyond that. You can end 
        this effect early (no action required). This effect also ends if you aren't carrying the weapon."""


# EOF
