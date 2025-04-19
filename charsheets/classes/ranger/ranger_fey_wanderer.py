from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.ranger import Ranger
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "BEGUILING_TWIST", "Beguiling Twist")
extend_enum(Feature, "DREADFUL_STRIKES", "Dreadful Strikes")
extend_enum(Feature, "FEY_REINFORCEMENTS", "Fey Reinforcements")
extend_enum(Feature, "FEY_WANDERER_SPELLS", "Fey Wanderer Spells")
extend_enum(Feature, "MISTY_WANDERER", "Misty Wanderer")
extend_enum(Feature, "OTHERWORLDLY_GLAMOUR", "Otherworldly Glamour")


#################################################################################
class RangerFeyWanderer(Ranger):
    _class_name = "Fey Wanderer"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(DreadfulStrikes())
        self.add_feature(OtherworldlyGlamour())
        self.add_feature(FeyWandererSpells())

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(BeguilingTwist())

    #############################################################################
    def level11(self, **kwargs: Any):
        self.add_feature(FeyReinforcements())

    #############################################################################
    def level15(self, **kwargs: Any):
        self.add_feature(MistyWanderer())


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
        if character.level >= 13:
            spells |= Reason("Fey Wanderer", Spell.DIMENSION_DOOR)
        if character.level >= 17:
            spells |= Reason("Fey Wanderer", Spell.MISLEAD)
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


#############################################################################
class MistyWanderer(BaseFeature):
    tag = Feature.MISTY_WANDERER
    _desc = """You can cast Misty Step without expending a spell slot. You can do so a number of times equal to your 
    Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest. In addition, 
    whenever you cast Misty Step, you can bring along one willing creature you can see within 5 feet of yourself. 
    That creature teleports to an unoccupied space of your choice within 5 feet of your destination space."""


# EOF
