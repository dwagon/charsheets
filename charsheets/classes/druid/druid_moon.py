from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.druid import Druid
from charsheets.constants import Ability
from charsheets.spell import Spell


#################################################################################
class DruidCircleOfTheMoon(Druid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Druid (Circle of the Moon)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {CircleForms()}
        self.prepare_spells(Spell.CURE_WOUNDS, Spell.MOONBEAM, Spell.STARRY_WISP)
        if self.level >= 5:
            self.prepare_spells(Spell.CONJURE_ANIMALS)
        if self.level >= 6:
            abilities.add(ImprovedCircleForms())
        if self.level >= 7:
            self.prepare_spells(Spell.FOUNT_OF_MOONLIGHT)
        return abilities


#############################################################################
class CircleForms(BaseAbility):
    tag = Ability.CIRCLE_FORMS
    _desc = """You can channel lunar magic when you assume a Wild Shape form, granting you the benefits below.

    Challenge Rating. The maximum Challenge Rating for the form equals your Druid level divided by 3 (round down).

    Armor Class. Until you leave the form, your AC equals 13 plus your Wisdom modifier if that total is higher than
    the Beast's AC.

    Temporary Hit Points. You gain a number of Temporary Hit Points equal to three times your Druid level."""


#############################################################################
class ImprovedCircleForms(BaseAbility):
    tag = Ability.IMPROVED_CIRCLE_FORMS
    _desc = """While in Wild Shape form, you gain the following benefits.

    Lunar Radiance. Each of your attacks in a Wild Shape form can deal its normal damage type of Radiant damage. You
    make this choice each time you hit with those attacks.

    Increased Toughness. You can add your Wisdom modifier to your Constitution saving throws.
    """


# EOF
