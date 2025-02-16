from charsheets.classes.druid import Druid
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.spell import Spell


#################################################################################
class DruidCircleOfTheMoon(Druid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Druid (Circle of the Moon)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = set()
        abilities |= super().class_features()
        abilities |= {CircleForms()}
        self.prepare_spells(Spell.CURE_WOUNDS, Spell.MOONBEAM, Spell.STARRY_WISP)
        if self.level >= 5:
            self.prepare_spells(Spell.CONJURE_ANIMALS)
        if self.level >= 6:
            abilities.add(ImprovedCircleForms())
        if self.level >= 7:
            self.prepare_spells(Spell.FOUNT_OF_MOONLIGHT)
        if self.level >= 9:
            self.prepare_spells(Spell.MASS_CURE_WOUNDS)
        if self.level >= 10:
            abilities |= {MoonlightStep()}
        return abilities


#############################################################################
class CircleForms(BaseFeature):
    tag = Feature.CIRCLE_FORMS

    @property
    def desc(self) -> str:
        return f"""You can channel lunar magic when you assume a Wild Shape form, granting you the benefits below.

    Challenge Rating. The maximum Challenge Rating for the form is {self.owner.level // 3}.

    Armor Class. Until you leave the form, your AC equals {13+self.owner.wisdom.modifier} if that total is higher than
    the Beast's AC.

    Temporary Hit Points. You gain {3*self.owner.level} Temporary Hit Points."""


#############################################################################
class ImprovedCircleForms(BaseFeature):
    tag = Feature.IMPROVED_CIRCLE_FORMS
    _desc = """While in Wild Shape form, you gain the following benefits.

    Lunar Radiance. Each of your attacks in a Wild Shape form can deal its normal damage type of Radiant damage. You
    make this choice each time you hit with those attacks.

    Increased Toughness. You can add your Wisdom modifier to your Constitution saving throws.
    """


#############################################################################
class MoonlightStep(BaseFeature):
    tag = Feature.MOONLIGHT_STEP
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return max(1, self.owner.wisdom.modifier)

    _desc = """As a Bonus Action, you teleport up to 30 feet to an unoccupied space you can see, and you have
    Advantage on the next attack roll you make before the end of this turn. 
    
    You can also regain uses by expending a level 2+ spell slot for each use you want to restore (no action required)."""


# EOF
