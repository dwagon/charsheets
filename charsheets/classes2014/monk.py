from typing import Optional, Any, TYPE_CHECKING, cast

from aenum import extend_enum
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Skill, Feature, CharacterClass, Proficiency, Armour, Weapon
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "UNARMORED_DEFENSE_MONK14", "Unarmored Defense")
extend_enum(Feature, "MARTIAL_ARTS14", "Martial Arts")


#################################################################################
class Monk(BaseClass):
    _base_skill_proficiencies = {
        Skill.ACROBATICS,
        Skill.ATHLETICS,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.RELIGION,
        Skill.STEALTH,
    }
    _base_class = CharacterClass.MONK
    _class_name = "Monk"

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.set_saving_throw_proficiency(Stat.STRENGTH, Stat.DEXTERITY)
        self.character.add_feature(UnarmoredDefenseMonk())
        self.character.add_feature(MartialArts())

    #############################################################################
    def level1multi(self, **kwargs: Any):  # pragma: no coverage
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_weapon_proficiency(Reason("Monk", cast(Proficiency, Proficiency.SIMPLE_WEAPONS)))

    #########################################################################
    def mod_specific_weapon_proficiency(self, character: "BaseCharacter") -> Reason[Weapon]:
        return Reason("Monk", Weapon.SHORTSWORD)

    #########################################################################
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
    @property
    def class_special(self) -> str:
        ans = []
        if self.ki_points:
            ans.append("Ki Points: {self.ki_points}")
        ans.append(f"Martial Arts Die: 1{self.martial_arts_die}")
        return "\n".join(ans)

    #############################################################################
    @property
    def ki_points(self) -> int:
        return self.level if self.level >= 2 else 0

    #############################################################################
    @property
    def martial_arts_die(self) -> str:
        if self.level >= 17:
            return "d10"
        elif self.level >= 11:
            return "d8"
        elif self.level >= 5:
            return "d6"
        return "d4"


#############################################################################
class UnarmoredDefenseMonk(BaseFeature):
    tag = cast(Feature, Feature.UNARMORED_DEFENSE_MONK14)
    hide = True

    @property
    def desc(self) -> str:
        ac = 10 + self.owner.dexterity.modifier + self.owner.wisdom.modifier
        return f"""While you are wearing no armor and not wielding a shield, you AC is {ac}"""

    def mod_ac_bonus(self, character: "BaseCharacter") -> Reason[int]:
        if self.owner.shield or self.owner.armour.tag != Armour.NONE:
            return Reason("", 0)
        ac = self.owner.wisdom.modifier
        return Reason("Unarmored Defense", ac)


#############################################################################
class MartialArts(BaseFeature):
    tag = Feature.MARTIAL_ARTS14

    @property
    def desc(self) -> str:
        assert self.owner.monk is not None
        return f"""You gain the following benefits while you are unarmed or wielding only Monk weapons and you aren't 
        wearing armor or wielding a Shield.
        
        You can use Dexterity ({self.owner.dexterity.modifier}) instead of Strength ({self.owner.strength.modifier}) 
        for the attack and damage rolls of your Unarmed Strike and Monk weapons.

        You can roll 1{self.owner.monk.martial_arts_die} in place of the normal damage of your Unarmed Strike or Monk 
        weapons.
        
        When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed 
        strike as a bonus action."""

    def mod_melee_dmg_bonus(self, weapon: Weapon, character: "BaseCharacter") -> Reason[int]:
        if weapon.tag == Weapon.UNARMED and self.owner.stats[Stat.DEXTERITY].modifier > self.owner.stats[Stat.STRENGTH].modifier:
            return Reason("Martial Arts", self.owner.stats[Stat.DEXTERITY].modifier - self.owner.stats[Stat.STRENGTH].modifier)
        return Reason()

    def mod_melee_atk_bonus(self, weapon: Weapon, character: "BaseCharacter") -> Reason[int]:
        if weapon.tag == Weapon.UNARMED and self.owner.stats[Stat.DEXTERITY].modifier > self.owner.stats[Stat.STRENGTH].modifier:
            return Reason("Martial Arts", self.owner.stats[Stat.DEXTERITY].modifier - self.owner.stats[Stat.STRENGTH].modifier)
        return Reason()

    #############################################################################
    def mod_dmg_dice(self, weapon: Weapon, character: "BaseCharacter") -> Reason[str]:
        assert self.owner.monk is not None
        if weapon.tag == Weapon.UNARMED:
            return Reason("Martial Arts", self.owner.monk.martial_arts_die)
        return Reason()


# EOF
