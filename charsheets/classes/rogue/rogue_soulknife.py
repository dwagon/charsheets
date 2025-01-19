from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.rogue import Rogue
from charsheets.constants import Ability


#################################################################################
class RogueSoulknife(Rogue):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {PsionicPowerRogue(), PsychicBlades()}
        abilities |= super().class_abilities()
        return abilities


#############################################################################
class PsionicPowerRogue(BaseAbility):
    tag = Ability.PSIONIC_POWER_ROGUE
    _desc = """You harbor a wellspring of psionic energy within yourself. It is represented by your Psionic Energy 
    Dice, which fuel certain powers you have from this subclass. The Soulknife Energy Dice table shows the number of 
    these dice you have when you reach certain Rogue levels, and the table shows the die size.

    SOULKNIFE ENERGY DICE
    Rogue Level Die Size Number
    3 D6 4
    5 D8 6
    9 D8 8
    11 D10 8
    13 D10 10
    17 D12 12

    Any features in this subclass that use a Psionic Energy Die use only the dice from this subclass. Some of your 
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
class PsychicBlades(BaseAbility):
    tag = Ability.PSYCHIC_BLADES
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
