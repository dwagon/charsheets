from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.sorcerer import Sorcerer
from charsheets.constants import Ability
from charsheets.spell import Spell


#################################################################################
class SorcererDraconic(Sorcerer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Draconic Sorceror"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DraconicResilience()}
        abilities |= super().class_abilities()
        self.prepare_spells(Spell.ALTER_SELF, Spell.CHROMATIC_ORB, Spell.COMMAND)
        if self.level >= 5:
            self.prepare_spells(Spell.FEAR, Spell.FLY)
        if self.level >= 6:
            abilities |= {ElementalAffinity()}

        return abilities


#############################################################################
class DraconicResilience(BaseAbility):
    tag = Ability.DRACONIC_RESILIENCE
    _desc = """The magic in your body manifests physical traits of your draconic gift. Your Hit Point maximum 
    increases by 3, and it increases by 1 whenever you gain another Sorcerer level. Parts of you are also covered by 
    dragon-like scales. While you aren’t wearing armor, your base Armor Class equals 10 plus your Dexterity and 
    Charisma modifiers."""


#############################################################################
class ElementalAffinity(BaseAbility):
    tag = Ability.ELEMENTAL_AFFINITY
    _desc = """Your draconic magic has an affinity with a damage type associated with dragons. Choose one of those 
    types: Acid, Cold, Fire, Lightning or Poison.

    You have Resistance to that damage type, and when you cast a spell that deals damage of that type you can add 
    your Charisma modifier to one damage roll of that spell."""

    # TODO - select damage type


# EOF
