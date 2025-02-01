from charsheets.features.base_feature import BaseFeature
from charsheets.classes.rogue import Rogue
from charsheets.constants import Feature


#################################################################################
class RogueSoulknife(Rogue):
    #############################################################################
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Soulknife"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        features: set[BaseFeature] = {PsionicPowerRogue(), PsychicBlades()}
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
    _desc = """Any features in this subclass that use a Psionic Energy Die use only the dice from this subclass. Some of your 
    powers expend a Psionic Energy Die, as specified in a power's description, and you can't use a power if it 
    requires you to use a die when your Psionic Energy Dice are all expended.

    You regain one of your expended Psionic Energy Dice when you finish a Short Rest, and you regain all of them when 
    you finish a Long Rest.

    Psi-Bolstered Knack. If you fail an ability check using a skill or tool with which you have proficiency, 
    you can roll one Psionic Energy Die and add the number rolled to the check, potentially turning failure into 
    success. The die is expended only if the roll then succeeds.

    Psychic Whispers. You can establish telepathic communication between yourself and others. As a Magic action, 
    choose one or more creatures you can see, up to a number of creatures equal to your Proficiency Bonus, 
    and then roll one Psionic Energy Die. For a number of hours equal to the number rolled, the chosen creatures can 
    speak telepathically with you, and you can speak telepathically with them. To send or receive a message (no 
    action required), you and the other creature must be within 1 mile of each other. A creature can end the 
    telepathic connection at any time (no action required).

    The first time you use this power after each Long Rest, you don't expend the Psionic Energy Die. All other times 
    you use the power, you expend the die."""


#############################################################################
class PsychicBlades(BaseFeature):
    tag = Feature.PSYCHIC_BLADES
    _desc = """You can manifest shimmering blades of psychic energy. Whenever you take the Attack action or make an 
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


# EOF
