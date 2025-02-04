from typing import Optional, Any

from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Feature
from charsheets.exception import InvalidOption
from charsheets.features import WeaponMastery, ExtraAttack
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell


#################################################################################
class Ranger(Character):
    _base_skill_proficiencies = {
        Skill.ANIMAL_HANDLING,
        Skill.ATHLETICS,
        Skill.INSIGHT,
        Skill.INVESTIGATION,
        Skill.NATURE,
        Skill.PERCEPTION,
        Skill.STEALTH,
        Skill.SURVIVAL,
    }

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.WISDOM

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Ranger", Proficiency.SIMPLE_WEAPONS, Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Ranger", Proficiency.SHIELDS, Proficiency.LIGHT_ARMOUR, Proficiency.MEDIUM_ARMOUR)
        # type: ignore

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.STRENGTH, Stat.DEXTERITY)

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {FavoredEnemy(), WeaponMastery()}
        if self.level >= 2:
            abilities.add(DeftExplorer())
            abilities.add(FightingStyleRanger())
        if self.level >= 5:
            abilities.add(ExtraAttack())
        if self.level >= 5:
            abilities.add(Roving())
        return abilities

    #############################################################################
    def level9(self, **kwargs: Any):
        if "expertise" not in kwargs:
            raise InvalidOption("Level 9 Rogues get Expertise: level9(expertise=Expertise(...))")
        self.add_feature(kwargs["expertise"])
        super().level9(**kwargs)

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            6: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            7: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            8: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            9: [4, 3, 2, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        ranger_spells = {
            0: [],
            1: [
                Spell.ALARM,
                Spell.ANIMAL_FRIENDSHIP,
                Spell.CURE_WOUNDS,
                Spell.DETECT_MAGIC,
                Spell.DETECT_POISON_AND_DISEASE,
                Spell.ENSNARING_STRIKE,
                Spell.ENTANGLE,
                Spell.FOG_CLOUD,
                Spell.GOODBERRY,
                Spell.HAIL_OF_THORNS,
                Spell.HUNTERS_MARK,
                Spell.JUMP,
                Spell.LONGSTRIDER,
                Spell.SPEAK_WITH_ANIMALS,
            ],
            2: [
                Spell.AID,
                Spell.ANIMAL_MESSENGER,
                Spell.BARKSKIN,
                Spell.BEAST_SENSE,
                Spell.CORDON_OF_ARROWS,
                Spell.DARKVISION,
                Spell.ENHANCE_ABILITY,
                Spell.FIND_TRAPS,
                Spell.GUST_OF_WIND,
                Spell.LESSER_RESTORATION,
                Spell.LOCATE_ANIMALS_OR_PLANTS,
                Spell.MAGIC_WEAPON,
                Spell.PASS_WITHOUT_TRACE,
                Spell.PROTECTION_FROM_POISON,
                Spell.SILENCE,
                Spell.SPIKE_GROWTH,
                Spell.SUMMON_BEAST,
            ],
            3: [
                Spell.CONJURE_ANIMALS,
                Spell.CONJURE_BARRAGE,
                Spell.DAYLIGHT,
                Spell.DISPEL_MAGIC,
                Spell.ELEMENTAL_WEAPON,
                Spell.LIGHTNING_ARROW,
                Spell.MELD_INTO_STONE,
                Spell.NONDETECTION,
                Spell.PLANT_GROWTH,
                Spell.PROTECTION_FROM_ENERGY,
                Spell.REVIVIFY,
                Spell.SPEAK_WITH_PLANTS,
                Spell.SUMMON_FEY,
                Spell.WATER_BREATHING,
                Spell.WATER_WALK,
                Spell.WIND_WALL,
            ],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        known_spells: Reason[Spell] = Reason()
        for spells in ranger_spells.values():
            for spell in spells:
                known_spells |= Reason("Ranger Spell", spell)
        return known_spells

    #############################################################################
    def max_spell_level(self) -> int:
        if self.level >= 17:
            return 5
        elif self.level >= 13:
            return 4
        elif self.level >= 9:
            return 3
        elif self.level >= 5:
            return 2
        return 1


#############################################################################
class FavoredEnemy(BaseFeature):
    tag = Feature.FAVOURED_ENEMY
    _desc = """You always have the Hunter's Mark spell prepared. You can cast it twice without expending a spell slot
    and you regain all expended uses of this ability when you finish a Long Rest.
    """

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Favoured Enemy", Spell.HUNTERS_MARK)


#############################################################################
class FightingStyleRanger(BaseFeature):
    tag = Feature.FIGHTING_STYLE_RANGER
    _desc = """You gain a Fighting Style fear of your choice. Instead of choosing one of those feats you can choose the
    option below.

    Druidic Warrior. You learn two Druid cantrips of your choice. The chosen cantrips count as Ranger spells for you,
    and Wisdom is your spellcasting ability for them. Whenever you gain a Ranger level, you can replace one of these
    cantrips with another Druid cantrip."""


#############################################################################
class DeftExplorer(BaseFeature):
    tag = Feature.DEFT_EXPLORER
    _desc = """Thanks to your travels, you gain the following benefits.

    Expertise. Choose one of your skill proficiencies with which you lack Expertise. You gain Expertise in that skill.

    Languages. You know two languages of your choice"""
    # TODO - select languages
    # TODO - select skill


#############################################################################
class FeywildGifts(BaseFeature):
    tag = Feature.FEYWILD_GIFTS
    _desc = """You possess a fey blessing."""


#############################################################################
class Roving(BaseFeature):
    tag = Feature.ROVING
    _desc = """Your speed increases by 10 feet if you aren't wearing Heavy armor. You also have a Climb Speed
    and Swim Speed equal to your Speed."""


# EOF
