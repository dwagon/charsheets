from typing import Any

from aenum import extend_enum

from charsheets.classes.rogue import Rogue
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature


extend_enum(Feature, "FAST_HANDS", "Fast Hands")
extend_enum(Feature, "SECOND_STORY_WORK", "Second Story Work")
extend_enum(Feature, "SUPREME_SNEAK", "Supreme Sneak")
extend_enum(Feature, "USE_MAGIC_DEVICE", "Use Magic Device")


#################################################################################
class RogueThief(Rogue):

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(FastHands())
        self.add_feature(SecondStoryWork())
        super().level3(**kwargs)

    #############################################################################
    def level9(self, **kwargs: Any):
        self.add_feature(SupremeSneak())
        super().level9(**kwargs)

    #############################################################################
    def level13(self, **kwargs: Any):
        self.add_feature(UseMagicDevice())
        super().level13(**kwargs)


#############################################################################
class FastHands(BaseFeature):
    tag = Feature.FAST_HANDS
    _desc = """As a Bonus Action, you can do one of the following.

    Sleight of Hand. Make a Dexterity (Sleight of Hand) check to pick a lock or disarm a trap with Thieves' Tools or 
    to pick a pocket.

    Use an Object. Take the Utilize action, or take the Magic action to use a magic item that requires that action."""


#############################################################################
class SecondStoryWork(BaseFeature):
    tag = Feature.SECOND_STORY_WORK
    _desc = """Climber. You gain a Climb Speed equal to your Speed. 

    Jumper. You can determine your jump distance using your Dexterity rather than your Strength."""


#############################################################################
class SupremeSneak(BaseFeature):
    tag = Feature.SUPREME_SNEAK
    _desc = """You gain the following Cunning Strike option.
    
    Stealth Attack (Cost: 1d6). If you have the Hide Action's Invisible condition, this attack doesn't end that 
    condition on you if you end the turn behind Three-Quarter Cover or Total Cover."""


#############################################################################
class UseMagicDevice(BaseFeature):
    tag = Feature.USE_MAGIC_DEVICE
    _desc = """You've learned how to maximize use of magic items, granting you the following benefits. Attunement. 
    You can attune to up to four magic items at once.

    Charges. Whenever you use a magic item property that expends charges, roll 1d6. On a roll of 6, you use the 
    property without expending the charges.

    Scrolls. You can use any Spell Scroll, using Intelligence as your spellcasting ability for the spell. If the 
    spell is a cantrip or a level 1 spell, you can cast it reliably. If the scroll contains a higher-level spell, 
    you must first succeed on an Intelligence (Arcana) check (DC 10 plus the spell's level). On a successful check, 
    you cast the spell from the scroll. On a failed check, the scroll disintegrates."""


# EOF
