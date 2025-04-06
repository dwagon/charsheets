from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.warlock import Warlock
from charsheets.constants import Feature, Stat
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "DARK_ONES_BLESSING", "Dark Ones Blessing")
extend_enum(Feature, "DARK_ONES_OWN_LUCK", "Dark Ones Own Luck")
extend_enum(Feature, "FIENDISH_RESILIENCE", "Fiendish Resilience")
extend_enum(Feature, "FIEND_SPELLS", "Fiend Spells")


#################################################################################
class WarlockFiend(Warlock):
    _class_name = "Warlock (Fiend)"

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(DarkOnesBlessing())
        self.add_feature(FiendSpells())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(DarkOnesOwnLuck())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(FiendishResilience())


#############################################################################
class FiendSpells(BaseFeature):
    tag = Feature.FIEND_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason(
            "Celestial Spells",
            Spell.BURNING_HANDS,
            Spell.COMMUNE,
            Spell.SCORCHING_RAY,
            Spell.SUGGESTION,
        )
        if character.level >= 5:
            spells |= Reason("Celestial Spells", Spell.FIREBALL, Spell.STINKING_CLOUD)
        if character.level >= 7:
            spells |= Reason("Celestial Spells", Spell.FIRE_SHIELD, Spell.WALL_OF_FIRE)
        if character.level >= 9:
            spells |= Reason("Celestial Spells", Spell.GEAS, Spell.INSECT_PLAGUE)
        return spells


#############################################################################
class DarkOnesBlessing(BaseFeature):
    tag = Feature.DARK_ONES_BLESSING

    @property
    def desc(self) -> str:
        bonus = max(1, self.owner.stats[Stat.CHARISMA].modifier + self.owner.level)

        return f"""When you reduce an enemy to 0 Hit Points, you gain {bonus} Temporary Hit Points. You also gain this 
    benefit if someone else reduces an enemy within 10 feet of you to 0 Hit Points."""


#############################################################################
class DarkOnesOwnLuck(BaseFeature):
    tag = Feature.DARK_ONES_OWN_LUCK

    @property
    def goes(self) -> int:
        return max(1, self.owner.stats[Stat.CHARISMA].modifier)

    @property
    def desc(self) -> str:
        return f"""You can call on your fiendish patron to alter fate in your favour. When you make an ability check or a 
    saving throw, you can use this feature to add 1d10 to your roll. You can do so after seeing the roll but before 
    any of the roll's effects occur.

    You can use this feature {self.goes} times, but you can use it 
    no more that once per roll. You regain all expended uses when you finish a Long Rest."""


#############################################################################
class FiendishResilience(BaseFeature):
    tag = Feature.FIENDISH_RESILIENCE
    _desc = """Choose one damage type, other than Force, when ever you finish a Short or Long Rest. You have 
    Resistance to that damage type until you choose a different one with this feature."""


# EOF
