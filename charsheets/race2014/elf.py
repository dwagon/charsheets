from typing import TYPE_CHECKING

from aenum import extend_enum

from charsheets.constants import Feature, Skill, Language, Weapon
from charsheets.features import Darkvision60, Darkvision120
from charsheets.features.base_feature import BaseFeature
from charsheets.race2014.base_race import BaseRace
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:
    from charsheets.character import BaseCharacter

extend_enum(Feature, "FEY_ANCESTRY14", "Fey Ancestry")
extend_enum(Feature, "KEEN_SENSES14", "Keen Senses")
extend_enum(Feature, "TRANCE14", "Trance")
extend_enum(Feature, "MASK_OF_THE_WILD14", "Mask of the Wild")
extend_enum(Feature, "SUNLIGHT_SENSITIVITY14", "Sunlight Sensitivity")


#############################################################################
class Elf(BaseRace):
    #########################################################################
    def __init__(self):
        super().__init__()
        self.speed = 30

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        return {
            Darkvision60(),
            KeenSenses(),
            FeyAncestry(),
        }

    #########################################################################
    def mod_stat_dex(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Elf", 2)

    #########################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Elf", Language.ELVISH)


#############################################################################
class HighElf(Elf):
    #########################################################################
    def __init__(self, cantrip: Spell, language: Language):
        super().__init__()
        self._language = language
        self._cantrip = cantrip

    #########################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        lingo = super().mod_add_language(character)
        return lingo | Reason("High Elf", self._language)

    #########################################################################
    def mod_add_known_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("High Elf", self._cantrip)

    #########################################################################
    def mod_stat_int(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("High Elf", 1)

    #########################################################################
    def mod_specific_weapon_proficiency(self, character: "BaseCharacter") -> Reason[Weapon]:
        return Reason("Elf Weapon Training", Weapon.LONGSWORD, Weapon.SHORTSWORD, Weapon.LONGBOW, Weapon.SHORTBOW)


#############################################################################
class WoodElf(Elf):

    #########################################################################
    def __init__(self):
        super().__init__()
        self.speed = 35

    #########################################################################
    def mod_stat_wis(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Wood Elf", 1)

    #########################################################################
    def mod_specific_weapon_proficiency(self, character: "BaseCharacter") -> Reason[Weapon]:
        return Reason("Elf Weapon Training", Weapon.LONGSWORD, Weapon.SHORTSWORD, Weapon.LONGBOW, Weapon.SHORTBOW)

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        base = super().race_feature()
        base.add(MaskOfTheWild())
        return base


#############################################################################
class Drow(Elf):
    #########################################################################
    def mod_stat_cha(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Drow", 1)

    #########################################################################
    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        spells = Reason("Drow", Spell.DANCING_LIGHTS)
        if character.level >= 3:
            spells |= Reason("Drow", Spell.FAERIE_FIRE)
        if character.level >= 5:
            spells |= Reason("Drow", Spell.DARKNESS)
        return spells

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        base = super().race_feature()
        base |= {Darkvision120(), SunlightSensitivity()}
        return base

    #########################################################################
    def mod_specific_weapon_proficiency(self, character: "BaseCharacter") -> Reason[Weapon]:
        return Reason("Drow Weapon Training", Weapon.RAPIER, Weapon.SHORTSWORD, Weapon.HAND_CROSSBOW)


#############################################################################
class FeyAncestry(BaseFeature):
    tag = Feature.FEY_ANCESTRY14
    _desc = """You have advantage on saving throws against being charmed, and magic can't put you to sleep."""


#############################################################################
class KeenSenses(BaseFeature):
    tag = Feature.KEEN_SENSES14
    _desc = """You have proficiency in the Perception skill"""
    hide = True

    def mod_add_skill_proficiency(self, character: "BaseCharacter") -> Reason[Skill]:
        return Reason("Keen Senses", Skill.PERCEPTION)


#############################################################################
class Trance(BaseFeature):
    tag = Feature.TRANCE14
    _desc = """You don’t need to sleep. You can finish a Long Rest in 4 hours if 
    you spend those hours in a trancelike meditation, during which you retain consciousness."""


#############################################################################
class MaskOfTheWild(BaseFeature):
    tag = Feature.MASK_OF_THE_WILD14
    _desc = """You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow,
            mist, and other natural phenomena."""


#############################################################################
class SunlightSensitivity(BaseFeature):
    tag = Feature.SUNLIGHT_SENSITIVITY14
    _desc = """You have disadvantage on attacks rolls and on Wisdom (Perception) checks that rely on sight when you, 
    the target of your attack, or whatever you are trying to perceive is in direct sunlight."""


# EOF
