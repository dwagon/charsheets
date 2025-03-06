from typing import TYPE_CHECKING

from aenum import extend_enum

from charsheets.classes.ranger import Ranger
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class RangerFeyWanderer(Ranger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Fey Wanderer"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {DreadfulStrikes(), OtherworldlyGlamour(), FeyWandererSpells()}
        abilities |= super().class_features()
        if self.level >= 7:
            abilities |= {BeguilingTwist()}
        if self.level >= 11:
            abilities |= {FeyReinforcements()}
        return abilities


extend_enum(Feature, "BEGUILING_TWIST", "Indomitable")
extend_enum(Feature, "DREADFUL_STRIKES", "Indomitable")
extend_enum(Feature, "FEY_REINFORCEMENTS", "Indomitable")
extend_enum(Feature, "FEY_WANDERER_SPELLS", "Indomitable")
extend_enum(Feature, "OTHERWORLDLY_GLAMOUR", "Indomitable")


#############################################################################
class DreadfulStrikes(BaseFeature):
    tag = Feature.DREADFUL_STRIKES
    _desc = """When you hit a creature with a weapon, you can deal an extra 1d4 Psychic damage to the target,
    which can take this extra damage only once per turn."""


#############################################################################
class OtherworldlyGlamour(BaseFeature):
    tag = Feature.OTHERWORLDLY_GLAMOUR
    _desc = """Whenever you make a Charisma check, you gain a bonus to the check equal to your Wisdom modifier (min +1).
    You also gain proficiency in one of these skills of your choice: Deception, Performance or Persuasion"""
    # TODO - select skill


#############################################################################
class FeyWandererSpells(BaseFeature):
    tag = Feature.FEY_WANDERER_SPELLS
    hide = True
    _desc = """Feywild Gifts

    1 Illusory butterflies flutter around you while you take aShort or Long Rest.

    2 Flowers bloom from your hair each dawn.

    3 You faintly smell of cinnamon, lavender, nutmeg, or another comforting herb or spice.

    4 Your shadow dances while noone is looking directly at it.

    5 Horns or antlers sprout from your head.

    6 Your skin and hair change color each dawn."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Fey Wanderer", Spell.CHARM_PERSON)
        if character.level >= 5:
            spells |= Reason("Fey Wanderer", Spell.MISTY_STEP)
        if character.level >= 9:
            spells |= Reason("Fey Wanderer", Spell.SUMMON_FEY)
        return spells


#############################################################################
class BeguilingTwist(BaseFeature):
    tag = Feature.BEGUILING_TWIST
    _desc = """You have Advantage on saving throws to avoid or end the 
    Charmed or Frightened condition.
    
    In addition, whenever you or a creature you can see within 120 feet of you succeeds on a saving throw to avoid or 
    end the Charmed or Frightened condition, you can take a Reaction to force a different creature you can see 
    withing 120 feet of yourself to make a Wisdom save against your spell save DC. On a failed save, the target is 
    Charmed or Frightened (your choice) for 1 minute. The target repeats the save at the end of each of its turns, 
    ending the effect on itself on a success."""


#############################################################################
class FeyReinforcements(BaseFeature):
    tag = Feature.FEY_REINFORCEMENTS
    _desc = """You can cast 'Summon Fey' without a Material component. You can also cast it once without a spell 
    slot, and you regain the ability to cast it in this way when you finish a Long Rest.

    Whenever you start casting the spell, you can modify it so that it doesn't require Concentration. If you do so, 
    the spell's duration becomes 1 minute for that casting."""


# EOF
