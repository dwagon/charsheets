from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class ClericLightDomain(Cleric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Cleric (Light Domain)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {RadianceOfTheDawn(), LightDomainSpells(), WardingFlare()}
        if self.level >= 6:
            abilities |= {ImprovedWardingFlare()}
        return abilities


#################################################################################
class RadianceOfTheDawn(BaseAbility):
    tag = Ability.RADIANCE_OF_THE_DAWN
    _desc = """As a Magic action, you present your Holy Symbol and expend a use of your Channel Divinity to emit a 
    flash of light in a 30-foot Emanation originating from yourself. Any magical Darkness - such as that created by
    the Darkness spell - in that area is dispelled. Additionally, each creature of your choice in that area must
    make a Constitution saving throw, taking Radiant damage equal to 2d10 plus your Cleric level on a failed save or
    half as much damage on a successful one."""


#############################################################################
class LightDomainSpells(BaseAbility):
    tag = Ability.LIGHT_DOMAIN_SPELLS
    _desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the Light Domain Spells table, you thereafter always have the listed spells prepared."""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Light Domain Spells", Spell.BURNING_HANDS, Spell.FAERIE_FIRE, Spell.SCORCHING_RAY, Spell.SEE_INVISIBILITY)
        if character.level >= 5:
            spells |= Reason("Light Domain Spells", Spell.DAYLIGHT, Spell.FIREBALL)
        if character.level >= 7:
            spells |= Reason("Light Domain Spells", Spell.ARCANE_EYE, Spell.WALL_OF_FIRE)
        return spells


#################################################################################
class WardingFlare(BaseAbility):
    tag = Ability.WARDING_FLARE
    _desc = """When a creature that you can see within 30 feet of yourself makes an attack roll, you can take
    a Reaction to impose Disadvantage on the attack roll, causing light to flare before it hits or misses.

    You can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended
    uses when you finish a Long Rest."""


#################################################################################
class ImprovedWardingFlare(BaseAbility):
    tag = Ability.IMPROVED_WARDING_FLARE
    _desc = """You regain all expended uses of your Warding Flare when you finish a Short or Long Rest.

    In addition, whenever you use Warding Flare, you can give the target of the triggering attack a number of 
    Temporary Hit Points equal to 2d6 plus your Wisdom modifier."""


# EOF
