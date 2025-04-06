from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.sorcerer import Sorcerer
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "BASTION_OF_LAW", "Bastion of Law")
extend_enum(Feature, "CLOCKWORK_SPELLS", "Clockwork Spells")
extend_enum(Feature, "RESTORE_BALANCE", "Restore Balance")


#################################################################################
class SorcererClockwork(Sorcerer):
    _class_name = "Sorcerer (Clockwork)"

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(ClockworkSpells())
        self.add_feature(RestoreBalance())
        self.add_feature(ClockworkSpells())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(BastionOfLaw())


#############################################################################
class ClockworkSpells(BaseFeature):
    tag = Feature.CLOCKWORK_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Clockwork Spells", Spell.AID, Spell.ALARM, Spell.LESSER_RESTORATION, Spell.PROTECTION_FROM_EVIL_AND_GOOD)
        if character.level >= 5:
            spells |= Reason("Clockwork Spells", Spell.DISPEL_MAGIC, Spell.PROTECTION_FROM_ENERGY)
        if character.level >= 7:
            spells |= Reason("Clockwork Spells", Spell.FREEDOM_OF_MOVEMENT, Spell.SUMMON_CONSTRUCT)
        if character.level >= 9:
            spells |= Reason("Clockwork Spells", Spell.GREATER_RESTORATION, Spell.WALL_OF_FORCE)
        return spells


#############################################################################
class RestoreBalance(BaseFeature):
    tag = Feature.RESTORE_BALANCE
    _desc = """When a creature you can see within 60 feet of yourself is about to roll a d20 with Advantage or 
    Disadvantage, you can take a Reaction to prevent the roll from being affected by Advantage and Disadvantage.

    You can use this feature a number of times equal to your Charisma modifier (minimum of once), and you regain all 
    expended uses when you finish a Long Rest."""


#############################################################################
class BastionOfLaw(BaseFeature):
    tag = Feature.BASTION_OF_LAW
    _desc = """As a Magic action, you can expend 1 to 5 Sorcery Points to create a magical ward around yourself or 
    another creature you can see within 30 feet of yourself. The ward is represented by a number of d8s equal to the 
    number of Sorcery Points spent to create it. When the warded creature takes damage, it can expend a number of 
    those dice, roll them, and reduce the damage taken by the total rolled on those dice.

    The ward lasts until you finish a Long Rest or until you use this feature again."""


# EOF
