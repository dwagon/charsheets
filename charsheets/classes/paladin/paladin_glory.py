from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.paladin import Paladin
from charsheets.constants import Ability
from charsheets.spell import Spell


#################################################################################
class PaladinOathOfGlory(Paladin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Paladin (Oath of Glory)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {PeerlessAthlete(), InspiringSmite()}
        abilities |= super().class_abilities()
        self.prepare_spells(Spell.GUIDING_BOLT, Spell.HEROISM)
        if self.level >= 5:
            self.prepare_spells(Spell.ENHANCE_ABILITY, Spell.MAGIC_WEAPON)
        return abilities


#############################################################################
class PeerlessAthlete(BaseAbility):
    tag = Ability.PEERLESS_ATHLETE
    _desc = """As a Bonus Action, you can expend one use of your Channel Divinity to augment your athleticism. For 1 
    hour, you have Advantage on Strength (Athletics) and Dexterity (Acrobatics) checks, and the distance of your Long 
    and High Jumps increases by 10 feet

    In addition, whenever an ally enters your Aura of Protection for the first time on a turn or starts their turn
    there, the ally's Speed increases by 10 feet until the end of their next turn."""


#############################################################################
class InspiringSmite(BaseAbility):
    tag = Ability.INSPIRING_SMITE
    _desc = """Immediately after you cast Divine Smite, you can expend one use of your Channel Divinity and 
    distribute Temporary Hit Points to creatures of your choice within 30 feet of yourself, which can include you. 
    The total number of Temporary Hit Points equals 2d8 plus your Paladin level, divided among the chosen creatures 
    however you like."""


# EOF
