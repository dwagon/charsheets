from charsheets.features.base_feature import BaseFeature
from charsheets.classes.druid import Druid
from charsheets.constants import Feature
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
        return abilities


#############################################################################
class CircleForms(BaseFeature):
    tag = Feature.CIRCLE_FORMS

    @property
    def desc(self) -> str:
        return f"""You can channel lunar magic when you assume a Wild Shape form, granting you the benefits below.

    Challenge Rating. The maximum Challenge Rating for the form {self.owner.level //3}.

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


# EOF
