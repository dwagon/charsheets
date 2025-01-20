from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.sorcerer import Sorcerer
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class SorcererClockwork(Sorcerer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Clockwork Sorceror"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {ClockworkSpells(), RestoreBalance()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities |= {BastionOfLaw()}
        if self.level >= 7:
            self.prepare_spells(Spell.FREEDOM_OF_MOVEMENT, Spell.SUMMON_CONSTRUCT)
        return abilities


#############################################################################
class ClockworkSpells(BaseAbility):
    tag = Ability.CLOCKWORK_SPELLS
    _desc = """Consult the Manifestations of Order table and choose or randomly determine away your 
    connection to order manifests while you are casting any of your Sorcerer spells.

    1 Spectral cog wheels hover behind you.

    2 The hands of a clock spin in your eyes.

    3 Your skin glows with a brassy sheen.

    4 Floating equations and geometric objects overlay your body.

    5 Your Spellcasting Focus temporarily takes the form of a tiny clockwork mechanism.

    6 The ticking of gears or ringing of a clock can be heard by you and those affected by your magic."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason[Spell]()
        spells.add("Clockwork Spells", Spell.AID)
        spells.add("Clockwork Spells", Spell.LESSER_RESTORATION)
        spells.add("Clockwork Spells", Spell.PROTECTION_FROM_EVIL_AND_GOOD)
        spells.add("Clockwork Spells", Spell.ALARM)
        if character.level >= 5:
            spells.add("Clockwork Spells", Spell.DISPEL_MAGIC)
            spells.add("Clockwork Spells", Spell.PROTECTION_FROM_ENERGY)

        return spells


#############################################################################
class RestoreBalance(BaseAbility):
    tag = Ability.RESTORE_BALANCE
    _desc = """Your connection to the plane of absolute order allows you to equalize chaotic moments. When a creature 
    you can see within 60 feet of yourself is about to roll a d20 with Advantage or Disadvantage, you can take a 
    Reaction to prevent the roll from being affected by Advantage and Disadvantage.

    You can use this feature a number of times equal to your Charisma modifier (minimum of once), and you regain all 
    expended uses when you finish a Long Rest."""


#############################################################################
class BastionOfLaw(BaseAbility):
    tag = Ability.BASTION_OF_LAW
    _desc = """You can tap into the grand equation of existence to imbue a creature with a shimmering shield of 
    order. As a Magic action, you can expend 1 to 5 Sorcery Points to create a magical ward around yourself or 
    another creature you can see within 30 feet of yourself. The ward is represented by a number of d8s equal to the 
    number of Sorcery Points spent to create it. When the warded creature takes damage, it can expend a number of 
    those dice, roll them, and reduce the damage taken by the total rolled on those dice.

    The ward lasts until you finish a Long Rest or until you use this feature again."""


# EOF
