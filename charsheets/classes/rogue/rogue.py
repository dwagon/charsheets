from typing import Optional, cast, Any, TYPE_CHECKING

from aenum import extend_enum

from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, Feature, Language, CharacterClass
from charsheets.exception import InvalidOption
from charsheets.features import WeaponMastery, Evasion
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "CUNNING_ACTION", "Cunning Action")
extend_enum(Feature, "CUNNING_STRIKE", "Cunning Strike")
extend_enum(Feature, "IMPROVED_CUNNING_STRIKE", "Improved Cunning Strike")
extend_enum(Feature, "RELIABLE_TALENT", "Reliable Talent")
extend_enum(Feature, "SNEAK_ATTACK", "Sneak Attack")
extend_enum(Feature, "STEADY_AIM", "Steady Aim")
extend_enum(Feature, "THIEVES_CANT", "Thieves' Cant")
extend_enum(Feature, "UNCANNY_DODGE", "Uncanny Dodge")


#################################################################################
class Rogue(BaseClass):
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
    _base_class = CharacterClass.ROGUE

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_weapon_proficiency(Reason("Rogue", cast(Proficiency, Proficiency.SIMPLE_WEAPONS)))
        self.character.add_weapon_proficiency(Reason("Rogue", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))
        self.character.set_saving_throw_proficiency(Stat.DEXTERITY, Stat.INTELLIGENCE)

    #############################################################################
    def level1multi(self, **kwargs: Any):
        if "skills" not in kwargs or len(kwargs["skills"]) != 1:
            raise InvalidOption("Level 1 Rogues multiclass one skill: skills='...'")
        kwargs["stats"] = []

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        if "expertise" not in kwargs:
            raise InvalidOption("Level 1 Rogues get Expertise: level1(expertise=Expertise(...))")
        self.character.add_armor_proficiency(Reason("Rogue", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.add_feature(kwargs["expertise"])
        self.add_feature(ThievesCant(self.kwargs["language"]))
        self.add_feature(SneakAttack())
        self.add_feature(WeaponMastery())

    #############################################################################
    def level2(self, **kwargs: Any):
        self.add_feature(CunningAction())

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(SteadyAim())

    #############################################################################
    def level5(self, **kwargs: Any):
        self.add_feature(CunningStrike())
        self.add_feature(UncannyDodge())

    #############################################################################
    def level6(self, **kwargs: Any):
        if "expertise" not in kwargs:
            raise InvalidOption("Level 6 Rogues get Expertise: level6(expertise=Expertise(...))")
        self.add_feature(kwargs["expertise"])

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(Evasion())
        self.add_feature(ReliableTalent())

    #############################################################################
    def level10(self, **kwargs: Any):
        if "feat" not in kwargs:
            raise InvalidOption("Level 10 rogues should specify a feat")

    #############################################################################
    def level11(self, **kwargs: Any):
        self.add_feature(ImprovedCunningStrike())

    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0

    #############################################################################
    @property
    def sneak_attack_dmg(self) -> int:
        assert self.character is not None
        rogue_level = self.character.highest_level(CharacterClass.ROGUE)
        if rogue_level is None:  # pragma: no coverage
            return 0
        return (rogue_level.level + 1) // 2

    #############################################################################
    @property
    def class_special(self) -> str:
        return f"Sneak Attack Dice: {self.sneak_attack_dmg}"


#############################################################################
class SneakAttack(BaseFeature):
    tag = Feature.SNEAK_ATTACK

    @property
    def desc(self) -> str:
        sad = cast(Rogue, self.owner.rogue).sneak_attack_dmg
        return f"""Once per turn, you can deal an extra
    {sad}d6 damage to one creature you hit with an attack roll if you have Advantage on the
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
    _desc = """On your turn, you can take one of the following actions as a Bonus Action: Dash, Disengage, or Hide."""


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


#############################################################################
class ImprovedCunningStrike(BaseFeature):
    tag = Feature.IMPROVED_CUNNING_STRIKE
    _desc = """You can use up to two Cunning Strike effects when you deal Sneak Attack damage, paying the die cost 
    for each effect."""


# EOF
