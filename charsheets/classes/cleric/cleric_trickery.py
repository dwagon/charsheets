from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.cleric import Cleric
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "BLESSING_OF_THE_TRICKSTER", "Blessing of the Trickster")
extend_enum(Feature, "IMPROVED_DUPLICITY", "Improved Duplicity")
extend_enum(Feature, "INVOKE_DUPLICITY", "Invoke Duplicity")
extend_enum(Feature, "TRICKERY_DOMAIN_SPELLS", "Trickery Domain Spells")
extend_enum(Feature, "TRICKSTERS_TRANSPOSITION", "Tricksters Transposition")


#################################################################################
class ClericTrickeryDomain(Cleric):
    _class_name = "Trickery Domain Cleric"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(BlessingOfTheTrickster())
        self.add_feature(InvokeDuplicity())
        self.add_feature(TrickeryDomainSpells())
        super().level3(**kwargs)

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(TrickstersTransposition())

    #############################################################################
    def level17(self, **kwargs: Any):
        self.add_feature(ImprovedDuplicity())


#################################################################################
class BlessingOfTheTrickster(BaseFeature):
    tag = Feature.BLESSING_OF_THE_TRICKSTER
    _desc = """As a Magic action, you can choose yourself or a willing creature within 30 feet of yourself to have
    Advantage on Dexterity (Stealth) checks. This blessing lasts until you finish a Long Rest or you use this
    feature again."""


#################################################################################
class InvokeDuplicity(BaseFeature):
    tag = Feature.INVOKE_DUPLICITY
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
class TrickeryDomainSpells(BaseFeature):
    tag = Feature.TRICKERY_DOMAIN_SPELLS
    _desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the Trickery Domain Spells table, you thereafter always have the listed spells prepared."""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason(
            "Trickery Domain Spells", Spell.CHARM_PERSON, Spell.DISGUISE_SELF, Spell.INVISIBILITY, Spell.PASS_WITHOUT_TRACE
        )
        if character.level >= 5:
            spells |= Reason("Tickery Domain Spells", Spell.HYPNOTIC_PATTERN, Spell.NONDETECTION)
        if character.level >= 7:
            spells |= Reason("Tickery Domain Spells", Spell.CONFUSION, Spell.DIMENSION_DOOR)
        if character.level >= 9:
            spells |= Reason("Tickery Domain Spells", Spell.DOMINATE_PERSON, Spell.MODIFY_MEMORY)
        return spells


#################################################################################
class TrickstersTransposition(BaseFeature):
    tag = Feature.TRICKSTERS_TRANSPOSITION
    _desc = """Whenever you take the Bonus Action to create or move the illusion of your Invoke Duplicity, 
    you can teleport, swapping places with the illusion."""


#################################################################################
class ImprovedDuplicity(BaseFeature):
    tag = Feature.IMPROVED_DUPLICITY
    _desc = """The illusion of your Invoke Duplicity has grown more powerful in the following ways.
    
    Shared Distraction. When you and your allies make attack rolls against a creature within 5 feet of the illusion, 
    the attack rolls have Advantage. 
    
    Healing Illusion. When the illusion ends, you or a creature of your choice within 5 feet of it regains a number 
    of Hit Points equal to your Cleric level."""


# EOF
