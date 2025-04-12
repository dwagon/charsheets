from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.warlock import Warlock
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "ARCHFEY_SPELLS", "Archfey Spells")
extend_enum(Feature, "BEGUILING_DEFENSES", "Beguiling Defenses")
extend_enum(Feature, "MISTY_ESCAPE", "Misty Escape")
extend_enum(Feature, "STEPS_OF_THE_FEY", "Steps of the Fey")


#################################################################################
class WarlockArchFey(Warlock):
    _class_name = "Arch Fey Warlock"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(StepsOfTheFey())
        self.add_feature(ArchfeySpells())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(MistyEscape())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(BeguilingDefenses())


#############################################################################
class ArchfeySpells(BaseFeature):
    tag = Feature.ARCHFEY_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason(
            "Archfey Spells", Spell.CALM_EMOTIONS, Spell.FAERIE_FIRE, Spell.MISTY_STEP, Spell.PHANTASMAL_FORCE, Spell.SLEEP
        )
        if character.level >= 5:
            spells |= Reason("Archfey Spells", Spell.BLINK, Spell.PLANT_GROWTH)
        if character.level >= 7:
            spells |= Reason("Archfey Spells", Spell.DOMINATE_BEAST, Spell.GREATER_INVISIBILITY)
        if character.level >= 9:
            spells |= Reason("Archfey Spells", Spell.DOMINATE_PERSON, Spell.SEEMING)
        return spells


#############################################################################
class StepsOfTheFey(BaseFeature):
    tag = Feature.STEPS_OF_THE_FEY
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return max(1, self.owner.charisma.modifier)

    @property
    def desc(self) -> str:
        return f"""You can cast 'Misty Step' without expending a spell slot {self.goes} times.

    In addition, whenever you cast that spell, you can choose one of the following additional effects.

    Refreshing Step. Immediately after you teleport, you or one creature you can see within 10 feet of yourself
    gains 1d10 Temporary Hit Points.

    Taunting Step. Creatures within 5 feet of the space you left must succeed on a Wisdom saving throw against your
    spell save DC or have Disadvantage on attack rolls against creatures other than you until the start of your
    next turn."""


#############################################################################
class MistyEscape(BaseFeature):
    tag = Feature.MISTY_ESCAPE
    _desc = """You can cast 'Misty Step' as a Reaction in response to taking damage.

    In addition, the following effects are now among your Steps of the Fey options.

    Disappearing Step. You have the Invisible condition until the start of your next turn or until immediate after 
    you make an attack roll, deal damage, or cast a spell.

    Dreadful Step. Creatures within 5 feet of the space you left or the space you appear in (your choice) must 
    succeed on a Wisdom saving throw against your spell save DC or take 2d10 Psychic damage."""


#############################################################################
class BeguilingDefenses(BaseFeature):
    tag = Feature.BEGUILING_DEFENSES
    recovery = Recovery.LONG_REST
    _goes = 1
    _desc = """You are immune to the Charmed condition.

            In addition, immediately after a creature you can see hits you with an attack roll, you can take a 
            Reaction to reduce the damage you take by half (round down), and you can force the attacker to make a 
            Wisdom saving throw against your spell save DC. On a failed save, the attacker takes Psychic damage equal 
            to the damage you take. Once you use this Reaction, you can't use it again until you finish a Long Rest 
            unless you expend a Pact Magic spell slot (no action required) to restore your use of it."""


# EOF
