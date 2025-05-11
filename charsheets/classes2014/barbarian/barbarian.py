from typing import Optional, Any, cast

from aenum import extend_enum
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Skill, Feature, Recovery, CharacterClass, Proficiency
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

extend_enum(Feature, "RAGE14", "Rage")
extend_enum(Feature, "UNARMORED_DEFENSE_BARBARIAN14", "Unarmored Defense")


#################################################################################
class Barbarian(BaseClass):
    _base_skill_proficiencies = {
        Skill.ANIMAL_HANDLING,
        Skill.ATHLETICS,
        Skill.INTIMIDATION,
        Skill.NATURE,
        Skill.PERCEPTION,
        Skill.SURVIVAL,
    }
    _base_class = CharacterClass.BARBARIAN
    _class_name = "Barbarian"

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.set_saving_throw_proficiency(Stat.STRENGTH, Stat.CONSTITUTION)
        self.character.add_feature(Rage())
        self.character.add_feature(UnarmoredDefenseBarbarian())

    #############################################################################
    def level1multi(self, **kwargs: Any):
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_weapon_proficiency(Reason("Barbarian", cast(Proficiency, Proficiency.SIMPLE_WEAPONS)))
        self.character.add_weapon_proficiency(Reason("Barbarian", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))
        self.character.add_armor_proficiency(Reason("Barbarian", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Barbarian", cast(Proficiency, Proficiency.MEDIUM_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Barbarian", cast(Proficiency, Proficiency.SHIELDS)))

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 12

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0

    #############################################################################
    @property
    def num_rages(self) -> int:
        assert self.character is not None
        barb_level = self.character.highest_level(CharacterClass.BARBARIAN)
        if barb_level is None:  # pragma: no coverage
            return 0
        if barb_level.level >= 17:
            return 6
        if barb_level.level >= 12:
            return 5
        if barb_level.level >= 6:
            return 4
        if barb_level.level >= 3:
            return 3
        return 2

    #############################################################################
    @property
    def rage_dmg_bonus(self) -> int:
        assert self.character is not None
        barb_level = self.character.highest_level(CharacterClass.BARBARIAN)
        if barb_level is None:  # pragma: no coverage
            return 0
        if barb_level.level >= 16:
            return 4
        elif barb_level.level >= 9:
            return 3
        return 2


#################################################################################
class Rage(BaseFeature):
    tag = Feature.RAGE14
    recovery = Recovery.PARTIAL

    @property
    def desc(self) -> str:
        assert self.owner.barbarian is not None
        return f"""You can enter it as a Bonus Action if you aren't wearing Heavy armor.

        While active, your Rage follows the rules below. 

        Damage Resistance. You have Resistance to Bludgeoning, Piercing, and Slashing damage. 

        Rage Damage. When you make an attack using Strength - with either a weapon or an Unarmed Strike - and deal 
        damage to the target, add {self.owner.barbarian.rage_dmg_bonus} damage.

        Strength Advantage. You have Advantage on Strength checks and Strength saving throws. 

        No Concentration or Spells. You can't maintain Concentration, and you can't cast spells."""

    @property
    def goes(self) -> int:
        assert self.owner.barbarian is not None
        return self.owner.barbarian.num_rages


#############################################################################
class UnarmoredDefenseBarbarian(BaseFeature):
    tag = Feature.UNARMORED_DEFENSE_BARBARIAN14
    _desc = """While you aren't wearing any armor, your base Armor Class equals 10 plus your Constitution and Dexterity 
    modifiers. You can use a Shield and still gain this benefit."""


# EOF
