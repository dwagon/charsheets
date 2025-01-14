from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, Tool, Language
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Expertise(BaseAbility):
    tag = Ability.EXPERTISE
    _desc = """You gain Expertise in two of your skill preferences of your choice. Sleight of Hand and Stealth are 
    recommended if you have proficiency in them. 
    
    At Rogue level 6, you gain Expertise in two more of your skill proficiencies of your choice"""


#############################################################################
class SneakAttack(BaseAbility):
    tag = Ability.SNEAK_ATTACK
    _desc = """You know how to strike subtly and exploit a foe’s distraction. Once per turn, you can deal an extra 
    1d6 damage to one creature you hit with an attack roll if you have Advantage on the roll and the attack uses a 
    Finesse or a Ranged weapon. The extra damage’s type is the same as the weapon's type. 
    
    You don’t need Advantage on the attack roll if at least one of your allies is within 5 feet of the target, 
    the ally doesn't have the Incapacitated condition, and you don't have Disadvantage on the attack roll.
    
    The extra damage increases as you gain Rogue levels, as shown in the Sneak Attack column of the Rogue Features 
    table."""


#############################################################################
class ThievesCant(BaseAbility):
    tag = Ability.THIEVES_CANT
    _desc = """You picked up various languages in the communities where you plied your roguish talents. You know 
    Thieves' Cant and one other language of your choice, which you choose from the language tables in chapter 2."""

    def mod_add_language(self, character: "Character") -> Reason[Language]:
        return Reason("Thieves' Cant", Language.THIEVES_CANT)

    # TODO: Need to select another language


#############################################################################
class CunningAction(BaseAbility):
    tag = Ability.CUNNING_ACTION
    _desc = """Your quick thinking and agility allow you to move and act quickly. On your turn, you can take one of 
    the following actions as a Bonus Action: Dash, Disengage, or Hide."""


#############################################################################
class SteadyAim(BaseAbility):
    tag = Ability.STEADY_AIM
    _desc = """As a Bonus Action, you give yourself Advantage on your next attack roll on the current turn. You can 
    use this feature only if you haven’t moved during this turn, and after you use it, your Speed is 0 until the end 
    of the current turn."""


#############################################################################
class MageHandLegerdemain(BaseAbility):
    tag = Ability.MAGE_HAND_LEGERDERMAIN
    _desc = """When you cast Mage Hand, you can cast it as a Bonus Action, and you can make the spectral hand 
    Invisible. You can control the hand as a Bonus Action, and through it, you can make Dexterity (Sleight of Hand) 
    checks."""


#############################################################################
class Assassinate(BaseAbility):
    tag = Ability.ASSASSINATE
    _desc = """You're adept at ambushing a target, granting you the following benefits. 
    
    Initiative. You have Advantage on Initiative rolls. 
    
    Surprising Strikes. During the first round of each combat, you have Advantage on 
    attack rolls against any creature that hasn't taken a turn. If your Sneak Attack hits any target during that 
    round, the target takes extra damage of the weapon's type equal to your Rogue level."""


#############################################################################
class AssassinsTools(BaseAbility):
    tag = Ability.ASSASSINS_TOOLS
    _desc = """You gain a Disguise Kit and a Poisoner’s Kit, and you have proficiency with them."""

    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        return Reason("Assassins Tools", Tool.DISGUISE_KIT, Tool.POISONERS_KIT)


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


#############################################################################
class FastHands(BaseAbility):
    tag = Ability.FAST_HANDS
    _desc = """As a Bonus Action, you can do one of the following.

    Sleight of Hand. Make a Dexterity (Sleight of Hand) check to pick a lock or disarm a trap with Thieves' Tools or 
    to pick a pocket.

    Use an Object. Take the Utilize action, or take the Magic action to use a magic item that requires that action."""


#############################################################################
class SecondStoryWork(BaseAbility):
    tag = Ability.SECOND_STORY_WORK
    _desc = """You've trained to get into especially hard-to-reach places, granting you these benefits. 
    
    Climber. You gain a Climb Speed equal to your Speed. 
    
    Jumper. You can determine your jump distance using your Dexterity rather than your Strength."""


#############################################################################
class CunningStrike(BaseAbility):
    tag = Ability.CUNNING_STRIKE
    _desc = """You've developed cunning ways to use your Sneak Attack. When you deal Sneak Attack damage, you can add 
    one of the following Cunning Strike effects. Each effect has a die cost, which is the number of Sneak Attack 
    damage dice you must forgo to add the effect. You remove the die before rolling, and the effect occurs 
    immediately after the attack’s damage is dealt. For example, if you add the Poison effect, remove 1d6 from the 
    Sneak Attack’s damage before rolling.

    If a Cunning Strike effect requires a saving throw, the DC equals 8 plus your Dexterity modifier and Proficiency 
    Bonus.

    Poison (Cost: 1d6). You add a toxin to your strike, forcing the target to make a Constitution saving throw. On a 
    failed save, the target has the Poisoned condition for 1 minute. At the end of each of its turns, the Poisoned 
    target repeats the save, ending the effect on itself on a success. To use this effect, you must have a Poisoner’s 
    Kit on your person.

    Trip (Cost: 1d6). If the target is Large or smaller, it must succeed on a Dexterity saving throw or have must 
    succeed on a Dexterity saving throw or have the Prone condition.

    Withdraw (Cost: 1d6). Immediately after the attack, you move up to half your Speed without provoking Opportunity
    Attacks."""


#############################################################################
class UncannyDodge(BaseAbility):
    tag = Ability.UNCANNY_DODGE
    _desc = """When an attacker that you can see hits you with an attack roll, you can take a Reaction to halve the 
    attack’s damage against you (round down)."""


# EOF
