from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.warlock import Warlock
from charsheets.constants import Ability
from charsheets.spell import Spell


#################################################################################
class WarlockFiend(Warlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Warlock (Fiend Patron)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DarkOnesBlessing()}
        abilities |= super().class_abilities()

        self.prepare_spells(Spell.BURNING_HANDS, Spell.COMMAND, Spell.SCORCHING_RAY, Spell.SUGGESTION)
        if self.level >= 5:
            self.prepare_spells(Spell.FIREBALL, Spell.STINKING_CLOUD)
        if self.level >= 6:
            abilities |= {DarkOnesOwnLuck()}
        if self.level >= 5:
            self.prepare_spells(Spell.FIRE_SHIELD, Spell.WALL_OF_FIRE)
        return abilities


#############################################################################
class DarkOnesBlessing(BaseAbility):
    tag = Ability.DARK_ONES_BLESSING

    @property
    def desc(self) -> str:
        bonus = max(1, self.owner.charisma.modifier + self.owner.level)

        return f"""When you reduce an enemy to 0 Hit Points, you gain {bonus} Temporary Hit Points. You also gain this 
    benefit if someone else reduces an enemy within 10 feet of you to 0 Hit Points."""


#############################################################################
class DarkOnesOwnLuck(BaseAbility):
    tag = Ability.DARK_ONES_OWN_LUCK

    @property
    def goes(self) -> int:
        return max(1, self.owner.charisma.modifier)

    @property
    def desc(self) -> str:
        return f"""You can call on your fiendish patron to alter fate in your favour. When you make an ability check or a 
    saving throw, you can use this feature to add 1d10 to your roll. You can do so after seeing the roll but before 
    any of the roll's effects occur.

    You can use this feature {self.goes} times, but you can use it 
    no more that once per roll. You regain all expended uses when you finish a Long Rest."""


# EOF
