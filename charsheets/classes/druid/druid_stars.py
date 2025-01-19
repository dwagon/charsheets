from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.druid import Druid
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spells import Spells

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class DruidCircleOfTheStars(Druid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Druid (Circle of the Stars)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {StarMap(), StarryForm()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities.add(CosmicOmen())
        return abilities


#############################################################################
class StarMap(BaseAbility):
    tag = Ability.STAR_MAP
    _desc = """You've created a star chart as part of your heavenly studies.

    While holding the map, you have the Guidance and Guiding Blot spells prepared, and you can Guiding Bolt without
    expending a spell slot. You can cast it in that way a number of times equal to your Wisdom modifier (minumum of
    once) and you regain all expended uses when you finish a Long Rest."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason("Star Map", Spells.GUIDANCE, Spells.GUIDING_BOLT)


#############################################################################
class StarryForm(BaseAbility):
    tag = Ability.STARRY_FORM
    _desc = """As a Bonus Action you cn expend a use of your Wild Shape feature to take on a starry form rather than
    shape-shifting.

    While in your starry form, you retain your game statistics, but your body becomes luminous, your joints glimmer
    like stars, and glowing lines connect them as on a star chart. This form sheds Bright Light in a 10-foot radius
    and Dim Light for additional 10 feet. The form lasts for 10 minutes. It ends early if you dismiss it
    (no action required), have the Incapacitated condition, or use this feature again.

    Whenever you assume your starry form, choose which of the following constellations glimmers on your body;
    your choice gives you certain benefits while in the form.

    Archer. A constellation of an archer appears on you. When you activate this form and as a Bonus Action on your
    subsequent turns while it lasts, you can make a ranged spell attack, hurling a luminous arrow that targets one
    creature within 60 feet of yourself. On a hit, the attack deals Radiant damage equal to 1d8 plus your Wisdom
    modifier.

    Chalice. A constellation of a life-giving goblet appears on you. Whenever you cast a spell using a spell slot that
    restores Hit Points to a creature, you or another creature within 30 feet of you can regain Hit Points equal to
    1d8 plus your Wisdom modifier.

    Dragon. A constellation of a wise dragon appears on you. When you make an Intelligence or a Wisdom check or a
    Constitution saving throw to maintain Concentration, you can treat a roll of 9 or lower on the d20 as a 10.
    """


#############################################################################
class CosmicOmen(BaseAbility):
    tag = Ability.COSMIC_OMEN
    _desc = """Whenever you finish a Long Rest, you can consult your Star Map for omens and roll a die. Until you
    finish your next Long Rest, you gain access to a special Reaction based on whether you rolled an even or an odd
    number on the die:

    Weal (Even). Whenever a creature you can see within 30 feet of you is about to make a D20 Test, you can take a
    Reaction to roll 1d6 and add the number rolled to the total.

    Woe (Odd). Whenever a creature you can see within 30 feet of you is about to make a D20 Test, you can take a
    Reaction to roll 1d6 and subtract the number rolled to the total.

    You can use this Reaction a number of times equal to your Wisdom modifier (minimum of once), and you regain all
    expended uses when you finish a Long Rest."""
