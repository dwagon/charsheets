from typing import Optional

from charsheets.abilities import WeaponMastery
from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Ability, Language
from charsheets.reason import Reason


#################################################################################
class Rogue(Character):
    _base_skill_proficiencies = {
        Skill.ACROBATICS,
        Skill.ATHLETICS,
        Skill.DECEPTION,
        Skill.INSIGHT,
        Skill.INTIMIDATION,
        Skill.INVESTIGATION,
        Skill.PERCEPTION,
        Skill.PERSUASION,
        Skill.SLEIGHT_OF_HAND,
        Skill.STEALTH,
    }

    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Fighter", Proficiency.SIMPLE_WEAPONS, Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Fighter", Proficiency.LIGHT_ARMOUR)

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.DEXTERITY, Stat.INTELLIGENCE)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {Expertise(), SneakAttack(), ThievesCant(), WeaponMastery()}

        if self.level >= 2:
            abilities.add(CunningAction())
        if self.level >= 3:
            abilities.add(SteadyAim())
        if self.level >= 5:
            abilities.add(CunningStrike())
            abilities.add(UncannyDodge())
        if self.level >= 6:
            abilities.add(Expertise())
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0


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
