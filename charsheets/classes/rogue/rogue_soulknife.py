from charsheets.classes.rogue import Rogue
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature


#################################################################################
class RogueSoulknife(Rogue):
    #############################################################################
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Soulknife"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        features: set[BaseFeature] = {PsionicPowerRogue(), PsychicBlades()}
        if self.level >= 9:
            features |= {SoulBlades()}
        features |= super().class_features()
        return features

    #############################################################################
    @property
    def energy_dice(self) -> str:
        if self.level >= 17:
            return "12d12"
        elif self.level >= 13:
            return "10d10"
        elif self.level >= 11:
            return "8d10"
        elif self.level >= 9:
            return "8d8"
        elif self.level >= 5:
            return "6d8"
        return "4d6"

    #############################################################################
    @property
    def class_special(self) -> str:
        result = super().class_special

        result += f"\n\nEnergy Dice: {self.energy_dice}"

        return result


#############################################################################
class PsionicPowerRogue(BaseFeature):
    tag = Feature.PSIONIC_POWER_ROGUE

    @property
    def goes(self) -> int:
        return int(self.owner.energy_dice.split("d")[0])

    @property
    def desc(self) -> str:
        return f"""You regain one of your expended Psionic Energy Dice when you finish a Short Rest, and you regain all
    of them when you finish a Long Rest.

    Psi-Bolstered Knack. If you fail an ability check using a skill or tool with which you have proficiency, 
    you can roll one Psionic Energy Die and add the number rolled to the check, potentially turning failure into 
    success. The die is expended only if the roll then succeeds.

    Psychic Whispers. You can establish telepathic communication between yourself and others. As a Magic action, 
    choose one or more creatures you can see, up to a {self.owner.proficiency_bonus} creatures, 
    and then roll one Psionic Energy Die. For a number of hours equal to the number rolled, the chosen creatures can 
    speak telepathically with you, and you can speak telepathically with them. To send or receive a message (no 
    action required), you and the other creature must be within 1 mile of each other. A creature can end the 
    telepathic connection at any time (no action required).

    The first time you use this power after each Long Rest, you don't expend the Psionic Energy Die. All other times 
    you use the power, you expend the die."""


#############################################################################
class PsychicBlades(BaseFeature):
    tag = Feature.PSYCHIC_BLADES
    _desc = """Whenever you take the Attack action or make an 
    Opportunity Attack, you can manifest a Psychic Blade in your free hand and make the attack with that blade. The 
    magic blade has the following traits:

    Weapon Category: Simple Melee 

    Damage on a Hit: 1d6 Psychic plus the ability modifier used for the attack roll 

    Properties: Finesse, Thrown (range 60/120 feet) 

    Mastery: Vex (you can use this property, and it doesn't count against the number of properties you can 
    use with Weapon Mastery)

    The blade vanishes immediately after it hits or misses its target, and it leaves no mark if it deals damage.

    After you attack with the blade on your turn, you can make a melee or ranged attack with a second psychic blade 
    as a Bonus Action on the same turn if your other hand is free to create it. The damage die of this bonus attack 
    is 1d4 instead of 1d6."""


#############################################################################
class SoulBlades(BaseFeature):
    tag = Feature.SOUL_BLADES
    _desc = """Homing Strikes. If you make an attack roll with your Psychic Blade and miss the target, you can roll
    a Psychic Energy Die and add the number rolled to the attack roll. If this causes the attack to hit, the die is
    expended.
    
    Psychic Teleportation. As a Bonus Action, you manifest a Psychic Blade, expend on Psychic Energy Die and roll it,
    and throw the blade at an unoccupied space you can see up to a number of feet away equal to 10 times the number
    rolled. You then teleport to that space, and the blade vanishes."""


# EOF
