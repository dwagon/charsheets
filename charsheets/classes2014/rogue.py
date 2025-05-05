from typing import Optional, cast, Any, TYPE_CHECKING

from aenum import extend_enum
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, Feature, Language, CharacterClass, Weapon, Tool
from charsheets.exception import InvalidOption
from charsheets.features import Expertise
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "SNEAK_ATTACK14", "Sneak Attack")
extend_enum(Feature, "THIEVES_CANT14", "Thieves' Cant")


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
        Skill.PERFORMANCE,
        Skill.PERSUASION,
        Skill.SLEIGHT_OF_HAND,
        Skill.STEALTH,
    }
    _base_class = CharacterClass.ROGUE
    _class_name = "Rogue"

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_weapon_proficiency(Reason("Rogue", cast(Proficiency, Proficiency.SIMPLE_WEAPONS)))
        self.character.set_saving_throw_proficiency(Stat.DEXTERITY, Stat.INTELLIGENCE)

    #############################################################################
    def level1multi(self, **kwargs: Any):
        pass

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        if "expertise" not in kwargs:
            raise InvalidOption("Level 1 Rogues get Expertise: level1(expertise=Expertise(...))")
        self.character.add_armor_proficiency(Reason("Rogue", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        assert isinstance(kwargs["expertise"], Expertise)
        self.add_feature(kwargs["expertise"])
        self.add_feature(ThievesCant())
        self.add_feature(SneakAttack())

    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #########################################################################
    def mod_specific_weapon_proficiency(self, character: "BaseCharacter") -> Reason[Weapon]:
        return Reason("Rogue", Weapon.HAND_CROSSBOW, Weapon.LONGSWORD, Weapon.RAPIER, Weapon.SHORTSWORD)

    #########################################################################
    def mod_add_tool_proficiency(self, character: "BaseCharacter") -> Reason[Tool]:
        return Reason("Rogue", cast(Tool, Tool.THIEVES_TOOLS))

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
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
    tag = Feature.SNEAK_ATTACK14

    @property
    def desc(self) -> str:
        sad = cast(Rogue, self.owner.rogue).sneak_attack_dmg
        return f"""Once per turn, you can deal an extra {sad} damage to one creature you hit with an attack if you have
            advantage on the attack roll. The attack must use a finesse or a ranged weapon.

            You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, 
            and you don't have disadvantage on the attack roll."""


#############################################################################
class ThievesCant(BaseFeature):
    tag = cast(Feature, Feature.THIEVES_CANT14)
    _desc = """During your rogue training you learned thieves' cant, a secret mix of dialect, jargon, and code that
    allows you to hide messages in seemingly normal conversation."""
    hide = True

    def __init__(self):
        super().__init__()

    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Thieves' Cant", cast(Language, Language.THIEVES_CANT))


# EOF
