from typing import TYPE_CHECKING, Any

from aenum import extend_enum
from charsheets.classes.bard import Bard
from charsheets.constants import Feature, Armour
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "DAZZLING_FOOTWORK", "Dazzling Footwork")
extend_enum(Feature, "INSPIRING_MOVEMENT", "Inspiring Movement")
extend_enum(Feature, "TANDEM_FOOTWORK", "Tandem Footwork")
extend_enum(Feature, "LEADING_EVASION", "Leading Evasion")


#################################################################################
class BardDanceCollege(Bard):
    _class_name = "Dance College Bard"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(DazzlingFootwork())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(InspiringMovement())
        self.add_feature(TandemFootwork())

    #############################################################################
    def level14(self, **kwargs: Any):
        self.add_feature(LeadingEvasion())


#################################################################################
class DazzlingFootwork(BaseFeature):
    tag = Feature.DAZZLING_FOOTWORK

    @property
    def desc(self) -> str:
        return f"""While you aren't wearing armor or wielding a Shield, you gain the following benefits.

        Dance Virtuoso. You have Advantage on any Charisma (Performance) check you make that involves you dancing.

        Agile Strikes. When you expend a use of your Bardic Inspiration as part of an action, a Bonus Action, 
        or a Reaction, you can make one Unarmed Strike as part of that action, Bonus Action, or Reaction.

        Bardic Damage. You can use Dexterity instead of Strength for the attack rolls of your Unarmed Strikes. When 
        you deal damage with an Unarmed Strike, you can deal Bludgeoning damage equal to 
        {self.owner.bard.bardic_inspiration_die()} + {self.owner.dexterity.modifier}, instead of the strike's normal damage.
        This roll doesn't expend the die."""

    def mod_ac_bonus(self, character: "Character") -> Reason[int]:
        if character.armour.tag == Armour.NONE and character.shield is None:
            return Reason("Dazzling Footwork", character.charisma.modifier)
        return Reason()


#################################################################################
class InspiringMovement(BaseFeature):
    tag = Feature.INSPIRING_MOVEMENT
    _desc = """When an enemy you can see ends its turn within S feet of you, you can take a Reaction and expend one 
    use of your Bardic Inspiration to move up to half your Speed. Then one ally of your choice within 30 feet of you 
    can also move up to half their Speed using their Reaction. 
    
    None of this feature's movement provokes Opportunity Attacks."""


#################################################################################
class TandemFootwork(BaseFeature):
    tag = Feature.TANDEM_FOOTWORK
    _desc = """When you roll Initiative, you can expend one use of your Bardic Inspiration if you don't have the 
    Incapacitated condition. When you do so, roll your Bardic Inspiration die; you and each ally within 30 feet of 
    you who can see or hear you gains a bonus to Initiative equal to the number rolled."""


#################################################################################
class LeadingEvasion(BaseFeature):
    tag = Feature.LEADING_EVASION
    _desc = """When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half 
    damage, you instead take no damage if you succeed on the saving throw and only half damage if you fail. If any 
    creatures within 5 feet of you are making the same Dexterity saving throw, you can share this benefit with them 
    for that save. You can't use this feature if you have the Incapacitated condition."""


# EOF
