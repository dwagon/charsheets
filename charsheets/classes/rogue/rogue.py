from typing import Optional, cast, Any

from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Feature, Language
from charsheets.exception import InvalidOption
from charsheets.features import WeaponMastery, Evasion
from charsheets.features.base_feature import BaseFeature
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
    def level1(self, **kwargs: Any):
        if "expertise" not in kwargs:
            raise InvalidOption("Level 1 Rogues get Expertise: level1(expertise=Expertise(...))")
        self.add_feature(kwargs["expertise"])

        if "language" not in kwargs:
            raise InvalidOption("Rogues need to define an additional language with 'language=xxx'")
        self.add_feature(ThievesCant(kwargs["language"]))

        super().level1(**kwargs)

    #############################################################################
    def level6(self, **kwargs: Any):
        if "expertise" not in kwargs:
            raise InvalidOption("Level 6 Rogues get Expertise: level6(expertise=Expertise(...))")
        self.add_feature(kwargs["expertise"])
        super().level6(**kwargs)

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
        return Reason("Fighter", cast(Proficiency, Proficiency.SIMPLE_WEAPONS), cast(Proficiency, Proficiency.MARTIAL_WEAPONS))

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Fighter", cast(Proficiency, Proficiency.LIGHT_ARMOUR))

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.DEXTERITY, Stat.INTELLIGENCE)

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {SneakAttack(), WeaponMastery()}

        if self.level >= 2:
            abilities |= {CunningAction()}
        if self.level >= 3:
            abilities |= {SteadyAim()}
        if self.level >= 5:
            abilities |= {CunningStrike(), UncannyDodge()}
        if self.level >= 7:
            abilities |= {Evasion(), ReliableTalent()}

        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0

    #############################################################################
    @property
    def sneak_attack_dmg(self) -> int:
        return (self.level + 1) // 2

    #############################################################################
    @property
    def class_special(self) -> str:
        return f"Sneak Attack Dice: {self.sneak_attack_dmg}"

    #############################################################################
    def level10(self, **kwargs: Any):
        if "feat" not in kwargs:
            raise InvalidOption("Level 10 rogues should specify a feat")
        self._add_level(10, **kwargs)


#############################################################################
class SneakAttack(BaseFeature):
    tag = Feature.SNEAK_ATTACK

    @property
    def desc(self) -> str:
        return f"""Once per turn, you can deal an extra
    {self.owner.sneak_attack_dmg}d6 damage to one creature you hit with an attack roll if you have Advantage on the
    roll and the attack uses a Finesse or a Ranged weapon. The extra damage’s type is the same as the weapon's type.

    You don’t need Advantage on the attack roll if at least one of your allies is within 5 feet of the target,
    the ally doesn't have the Incapacitated condition, and you don't have Disadvantage on the attack roll."""


#############################################################################
class ThievesCant(BaseFeature):
    tag = cast(Feature, Feature.THIEVES_CANT)
    _desc = """You picked up various languages in the communities where you plied your roguish talents. You know
       Thieves' Cant and one other language of your choice, which you choose from the language tables in chapter 2."""
    hide = True

    def __init__(self, language: Language):
        super().__init__()
        self.language = language

    def mod_add_language(self, character: "Character") -> Reason[Language]:
        return Reason("Thieves' Cant", cast(Language, Language.THIEVES_CANT), self.language)


#############################################################################
class CunningAction(BaseFeature):
    tag = Feature.CUNNING_ACTION
    _desc = """On your turn, you can take one of
    the following actions as a Bonus Action: Dash, Disengage, or Hide."""


#############################################################################
class SteadyAim(BaseFeature):
    tag = Feature.STEADY_AIM
    _desc = """As a Bonus Action, you give yourself Advantage on your next attack roll on the current turn. You can
    use this feature only if you haven’t moved during this turn, and after you use it, your Speed is 0 until the end
    of the current turn."""


#############################################################################
class CunningStrike(BaseFeature):
    tag = Feature.CUNNING_STRIKE

    @property
    def desc(self) -> str:
        dc = 8 + self.owner.dexterity.modifier + self.owner.proficiency_bonus
        return f"""When you deal Sneak Attack damage, you can add one of the following Cunning Strike effects.

        Poison (Cost: 1d6). You add a toxin to your strike, forcing the target to make a Constitution saving throw
        (DC {dc}). On a failed save, the target has the Poisoned condition for 1 minute. At the end of each of its
        turns, the Poisoned target repeats the save, ending the effect on itself on a success. To use this effect,
        you must have a Poisoner’s Kit on your person.

        Trip (Cost: 1d6). If the target is Large or smaller, it must succeed on a Dexterity saving throw (DC {dc}) or
        have the Prone condition.

        Withdraw (Cost: 1d6). Immediately after the attack, you move up to half your Speed without provoking
        Opportunity Attacks."""


#############################################################################
class UncannyDodge(BaseFeature):
    tag = Feature.UNCANNY_DODGE
    _desc = """When an attacker that you can see hits you with an attack roll, you can take a Reaction to halve the
    attack’s damage against you (round down)."""


#############################################################################
class ReliableTalent(BaseFeature):
    tag = Feature.RELIABLE_TALENT
    _desc = """Whenever you make an ability check that uses on of your skill or tool proficiencies, you can treat
    d20 roll of 9 or lower as a 10."""


# EOF
