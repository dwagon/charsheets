from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.warlock import Warlock
from charsheets.constants import Ability
from charsheets.spells import Spells


#################################################################################
class WarlockArchFey(Warlock):
    _class_name = "Warlock (Archfey Patron)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {StepsOfTheFey()}
        self.prepare_spells(Spells.CALM_EMOTIONS, Spells.FAERIE_FIRE, Spells.MISTY_STEP, Spells.PHANTASMAL_FORCE, Spells.SLEEP)
        if self.level >= 5:
            self.prepare_spells(Spells.BLINK, Spells.PLANT_GROWTH)
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities |= {MistyEscape()}
        return abilities


#############################################################################
class StepsOfTheFey(BaseAbility):
    tag = Ability.STEPS_OF_THE_FEY
    _desc = """Your patron grants you the ability to move between the boundaries of the planes. You can cast
    Misty Step without expending a spell slot a number of times equal to your Charisma modifier (min once), and 
    you regain all expended uses when you finish a Long Rest.

    In addition, whenever you cast that spell, you can choose one of the following additional effects.

    Refreshing Step. Immediately after you teleport, you or one creature you can see within 10 feet of yourself
    gains 1d10 Temporary Hit Points.

    Taunting Step. Creatures within 5 feet of the space you left must succeed on a Wisdom saving throw against your
    spell save DC or have Disadvantage on attack rolls against creatures other than you until the start of your
    next turn."""


#############################################################################
class MistyEscape(BaseAbility):
    tag = Ability.MISTY_ESCAPE
    _desc = """You can cast Misty Step as a Reaction in response to taking damage.

    In addition, the following effects are now among your Steps of the Fey options.

    Disappearing Step. You have the Invisible condition until the start of your next turn or until immediate after 
    you make an attack roll, deal damage, or cast a spell.

    Dreadful Step. Creatures within 5 feet of the space you left or the space you appear in (your choice) must 
    succeed on a Wisdom saving throw against your spell save DC or take 2d10 Psychic damage."""


# EOF
