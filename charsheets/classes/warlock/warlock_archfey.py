from aenum import extend_enum

from charsheets.classes.warlock import Warlock
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.spell import Spell


#################################################################################
class WarlockArchFey(Warlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Archfey Warlock"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {StepsOfTheFey()}
        self.prepare_spells(Spell.CALM_EMOTIONS, Spell.FAERIE_FIRE, Spell.MISTY_STEP, Spell.PHANTASMAL_FORCE, Spell.SLEEP)
        if self.level >= 5:
            self.prepare_spells(Spell.BLINK, Spell.PLANT_GROWTH)
        abilities |= super().class_features()
        if self.level >= 6:
            abilities |= {MistyEscape()}
        if self.level >= 7:
            self.prepare_spells(Spell.DOMINATE_BEAST, Spell.GREATER_INVISIBILITY)
        if self.level >= 9:
            self.prepare_spells(Spell.DOMINATE_PERSON, Spell.SEEMING)
        if self.level >= 10:
            abilities |= {BeguilingDefenses()}
        return abilities


extend_enum(Feature, "STEPS_OF_THE_FEY", "Steps of the Fey")
extend_enum(Feature, "MISTY_ESCAPE", "Misty Escape")
extend_enum(Feature, "BEGUILING_DEFENSES", "Beguiling Defenses")


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
