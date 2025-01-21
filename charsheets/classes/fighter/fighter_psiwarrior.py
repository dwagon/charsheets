from charsheets.features.base_feature import BaseFeature
from charsheets.classes.fighter import Fighter
from charsheets.constants import Feature


#################################################################################
class FighterPsiWarrior(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Psi Warrior"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = set()
        abilities |= super().class_features()
        abilities |= {PsionicPowerFighter()}
        if self.level >= 7:
            abilities |= {TelekineticAdept()}
        return abilities

    #############################################################################
    @property
    def energy_dice(self) -> str:
        if self.level >= 17:
            return "12 x d12"
        elif self.level >= 13:
            return "10 x d10"
        elif self.level >= 11:
            return "8 x d10"
        elif self.level >= 9:
            return "8 x d8"
        elif self.level >= 5:
            return "6 x d8"
        return "4 x d6"

    #############################################################################
    @property
    def class_special(self) -> str:
        return f"Psionic Energy Dice: {self.energy_dice}\n"


############################################################################
class PsionicPowerFighter(BaseFeature):
    tag = Feature.PSIONIC_POWER_FIGHTER

    @property
    def desc(self) -> str:
        int_mod = self.owner.intelligence.modifier
        bonus = max(1, int_mod)
        return f"""You harbor a wellspring of psionic energy within yourself.

    You regain one of your expended Psionic Energy Dice when you finish a Short Rest, and you regain all of them
    when you finish a Long Rest.

    Protective Field. When you or another creature you can see within 30 feet of you takes damage, you can take a 
    Reaction to expend one Psionic Energy Die, roll the die, and reduce the damage taken by the number rolled plus 
    {bonus}, as you create a momentary shield of telekinetic force.

    Psionic Strike. You can propel your weapons with psionic force. Once on each of your turns, immediately after you 
    hit a target within 30 feet of yourself with an attack and deal damage to it with a weapon, you can expend one 
    Psionic Energy Die, rolling it and dealing Force damage to the target equal to the number rolled plus
    {int_mod}.

    Telekinetic Movement. You can move an object or a creature with your mind. As a Magic action, choose one target 
    you can see within 30 feet of yourself; the target must be a loose object that is Large or smaller or one willing 
    creature other than you. You transport the target up to 30 feet to an unoccupied space you can see. 
    Alternatively, if that target is a Tiny object, you can transport it to or from your hand.

    Once you take this action, you can't do so again until you finish a Short or Long Rest unless you expend a 
    Psionic Energy Die (no action required) to restore your use of it."""


############################################################################
class TelekineticAdept(BaseFeature):
    tag = Feature.TELEKINETIC_ADEPT
    _desc = """You have mastered new ways to use your telekinetic features, detailed below.
    
    Psi-Powered Leap. As a Bonus Action, you gain a Fly Speed equal to twice your Speed until the end of the current 
    turn. Once you take this Bonus Action, you can't do so again until you finish a Short or Long Rest unless you 
    expend a Psionic Energy Die (no action required) to restore your use of it.
    
    Telekinetic Thrust. When you deal damage to a target with your Psionic Strike, you can force the trget to make a 
    Strength saving throw (DC 8 plus your Intelligence modifier and Proficiency Bonus). On a failed save, 
    you can give the target the Prone condition or transport it up to 10 feet horizontally."""


# EOF
