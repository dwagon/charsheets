from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.wizard import Wizard
from charsheets.constants import Ability


#################################################################################
class WizardEvoker(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {EvocationSavant(), PotentCantrip()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities |= {SculptSpells()}
        return abilities


#############################################################################
class EvocationSavant(BaseAbility):
    tag = Ability.EVOCATION_SAVANT
    _desc = """Choose two Wizard spells from the Evocation school, each of which must be no higher than level 2, 
    and add them to your spellbook for free. In addition, whenever you gain access to a new level of spell slots in 
    this class, you can add one Wizard spell from the Evocation school to your spellbook for free. The chosen spell 
    must be of a level for which you have spell slots."""


#############################################################################
class PotentCantrip(BaseAbility):
    tag = Ability.POTENT_CANTRIP
    _desc = """Your damaging cantrips affect even creatures that avoid the brunt of the effect. When you cast a 
    cantrip at a creature and you miss with the attack roll or the target succeeds on a saving throw against the 
    cantrip, the target takes half the cantrip’s damage (if any) but suffers no additional effect from the cantrip."""


#############################################################################
class SculptSpells(BaseAbility):
    tag = Ability.SCULPT_SPELLS
    _desc = """You can create pockets of relative safety within the effects of your evocations. When you cast an 
    Evocation spell that affects other creatures that you can see, you can choose a number of them equal to 1 plus 
    the spell's level. The chosen creatures automatically succeed on their saving throws against the spell, 
    and they take no damage if they would normally take half damage on a successful save."""


# EOF
