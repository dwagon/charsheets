from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class ClericTrickeryDomain(Cleric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Cleric (Trickery Domain)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {BlessingOfTheTrickster(), InvokeDuplicity(), TrickeryDomainSpells()}
        if self.level >= 6:
            abilities |= {TrickstersTransposition()}
        return abilities


#################################################################################
class BlessingOfTheTrickster(BaseAbility):
    tag = Ability.BLESSING_OF_THE_TRICKSTER
    _desc = """As a Magic action, you can choose yourself or a willing creature within 30 feet of yourself to have
    Advantage on Dexterity (Stealth) checks. This blessing lasts until you finish a Long Rest or you use this
    feature again."""


#################################################################################
class InvokeDuplicity(BaseAbility):
    tag = Ability.INVOKE_DUPLICITY
    _desc = """As a Bonus Action, you can expend one use of your Channel Divinity to create a perfect visual illusion
    of yourself in an unoccupied space you can see within 30 feet of yourself. The illusion is intangible and
    doesn't occupy its space. It lasts for 1 minute, but it ends early if you dismiss it (no action required) or have
    the Incapacitated condition. The illusion is animated and mimics your expressions and gestures. While it persists,
    you gain the following benefits.

    Cast Spells. You can cast spells as though were in the illusion's space, but you must use your own senses.

    Distract. When both you and your illusion are with 5 feet of a creature that can see the illusion, you have
    Advantage on attack rolls against that creature, given how distracting the illusion is to the target.

    Move. As a Bonus Action, you can move the illusion up to 30 feet to an unoccupied space you can see that is within
    120 feet of yourself."""


#############################################################################
class TrickeryDomainSpells(BaseAbility):
    tag = Ability.TRICKERY_DOMAIN_SPELLS
    _desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the Trickery Domain Spells table, you thereafter always have the listed spells prepared."""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason(
            "Trickery Domain Spells", Spell.CHARM_PERSON, Spell.DISGUISE_SELF, Spell.INVISIBILITY, Spell.PASS_WITHOUT_TRACE
        )
        if character.level >= 5:
            spells |= Reason("Tickery Domain Spells", Spell.HYPNOTIC_PATTERN, Spell.NONDETECTION)
        return spells


#################################################################################
class TrickstersTransposition(BaseAbility):
    tag = Ability.TRICKSTERS_TRANSPOSITION
    _desc = """Whenever you take the Bonus Action to create or move the illusion of your Invoke Duplicity, 
    you can teleport, swapping places with the illusion."""


# EOF
