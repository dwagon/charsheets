from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.fighter import Fighter
from charsheets.constants import Feature, DamageType, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:
    from charsheets.character import Character

extend_enum(Feature, "BULWARK_OF_FORCE", "Bulwark of Force")
extend_enum(Feature, "GUARDED_MIND", "Guarded Mind")
extend_enum(Feature, "PSIONIC_POWER_FIGHTER", "Psionic Power")
extend_enum(Feature, "TELEKINETIC_ADEPT", "Telekinetic Adept")
extend_enum(Feature, "TELEKINETIC_MASTER", "Telekinetic Master")


#################################################################################
class FighterPsiWarrior(Fighter):
    _class_name = "Psiwarrior"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(PsionicPowerFighter())

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(TelekineticAdept())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(GuardedMind())

    #############################################################################
    def level15(self, **kwargs: Any):
        self.add_feature(BulwarkOfForce())

    #############################################################################
    def level18(self, **kwargs: Any):
        self.add_feature(TelekineticMaster())

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
    recovery = Recovery.PARTIAL

    @property
    def desc(self) -> str:
        int_mod = self.owner.intelligence.modifier
        bonus = max(1, int_mod)
        return f"""Protective Field. When you or another creature you can see within 30 feet of you takes damage, 
        you can take a Reaction to expend one Psionic Energy Die, roll the die, and reduce the damage taken by the 
        number rolled plus {bonus}, as you create a momentary shield of telekinetic force.
    
        Psionic Strike. You can propel your weapons with psionic force. Once on each of your turns, immediately after you
        hit a target within 30 feet of yourself with an attack and deal damage to it with a weapon, you can expend one
        Psionic Energy Die, rolling it and dealing Force damage to the target equal to the number rolled plus {int_mod}.
    
        Telekinetic Movement. You can move an object or a creature with your mind. As a Magic action, choose one target
        you can see within 30 feet of yourself; the target must be a loose object that is Large or smaller or one willing
        creature other than you. You transport the target up to 30 feet to an unoccupied space you can see.
        Alternatively, if that target is a Tiny object, you can transport it to or from your hand.
    
        Once you take this action, you can't do so again until you finish a Short or Long Rest unless you expend a
        Psionic Energy Die (no action required) to restore your use of it."""


############################################################################
class TelekineticAdept(BaseFeature):
    tag = Feature.TELEKINETIC_ADEPT

    @property
    def desc(self) -> str:
        dc = 8 + self.owner.intelligence.modifier + self.owner.proficiency_bonus
        return f"""Psi-Powered Leap. As a Bonus Action, you gain a Fly Speed equal to twice your Speed until the end
        of the current turn. Once you take this Bonus Action, you can't do so again until you finish a Short or Long
        Rest unless you expend a Psionic Energy Die (no action required) to restore your use of it.

        Telekinetic Thrust. When you deal damage to a target with your Psionic Strike, you can force the target to
        make a Strength saving throw (DC {dc}). On a failed save,
        you can give the target the Prone condition or transport it up to 10 feet horizontally."""


############################################################################
class BulwarkOfForce(BaseFeature):
    tag = Feature.BULWARK_OF_FORCE

    _desc = """You can shield yourself and others with telekinetic force. As a Bonus Action, you can choose 
    creatures, including yourself, within 30 feet of yourself, up to a number of creatures equal to your Intelligence 
    modifier (minimum of one creature). Each of the chosen creatures has Half Cover for 1 minute or until you have 
    the Incapacitated condition.

    Once you use this feature, you can't do so again until you finish a Long Rest unless you expend a Psionic Energy 
    Die (no action required) to restore your use of it."""


############################################################################
class TelekineticMaster(BaseFeature):
    tag = Feature.TELEKINETIC_MASTER

    _desc = """You always have the 'Telekinesis' spell prepared. With this feature, you can cast it without a spell 
    slot or components, and your spellcasting ability for it is Intelligence. On each of your turns while you 
    maintain Concentration on it, including the turn when you cast it, you can make one attack with a weapon as a 
    Bonus Action.

    Once you cast the spell with this feature, you can't do so in this way again until you finish a Long Rest unless 
    you expend a Psionic Energy Die (no action required) to restore your use of it."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Telekinetic Master", Spell.TELEKINESIS)


############################################################################
class GuardedMind(BaseFeature):
    tag = Feature.GUARDED_MIND
    _desc = """If you start your turn with the Charmed or Frightened condition, you can expend a Psionic Energy Die
    (no action required) and end every effect on yourself giving you those conditions."""

    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason("Guarded Mind", DamageType.PSYCHIC)


# EOF
