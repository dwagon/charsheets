from typing import Optional, cast, Any, TYPE_CHECKING

from aenum import extend_enum
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery, CharacterClass
from charsheets.exception import InvalidOption
from charsheets.features import ExtraAttack, WeaponMastery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "LAY_ON_HANDS14", "Lay on Hands")
extend_enum(Feature, "DIVINE_SENSE14", "Divine Sense")


#################################################################################
class Paladin(BaseClass):
    _base_skill_proficiencies = {
        Skill.ATHLETICS,
        Skill.INSIGHT,
        Skill.MEDICINE,
        Skill.PERSUASION,
        Skill.RELIGION,
    }
    _base_class = CharacterClass.PALADIN
    _class_name = "Paladin"

    #############################################################################
    def level1init(self, **kwargs: Any):  # pragma: no coverage
        assert self.character is not None

    #############################################################################
    def level1multi(self, **kwargs: Any):  # pragma: no coverage
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_weapon_proficiency(Reason("Paladin", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))
        self.character.add_armor_proficiency(Reason("Paladin", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Paladin", cast(Proficiency, Proficiency.MEDIUM_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Paladin", cast(Proficiency, Proficiency.HEAVY_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Paladin", cast(Proficiency, Proficiency.SHIELDS)))
        self.character.set_saving_throw_proficiency(Stat.WISDOM, Stat.CHARISMA)

        self.add_feature(LayOnHands())
        self.add_feature(DivineSense())

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.CHARISMA

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.WISDOM, Stat.CHARISMA)

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            6: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            7: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            8: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            9: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            10: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            11: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            12: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            13: [4, 3, 3, 1, 0, 0, 0, 0, 0],
            14: [4, 3, 3, 1, 0, 0, 0, 0, 0],
            15: [4, 3, 3, 2, 0, 0, 0, 0, 0],
            16: [4, 3, 3, 2, 0, 0, 0, 0, 0],
            17: [4, 3, 3, 3, 1, 0, 0, 0, 0],
            18: [4, 3, 3, 3, 1, 0, 0, 0, 0],
            19: [4, 3, 3, 3, 2, 0, 0, 0, 0],
            20: [4, 3, 3, 3, 2, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        paladin_spells = {
            0: [
                # Cantrips are learnt
            ],
            1: [
                Spell.BLESS,
                Spell.COMMAND,
                Spell.COMPELLED_DUEL,
                Spell.CURE_WOUNDS,
                Spell.DETECT_EVIL_AND_GOOD,
                Spell.DETECT_MAGIC,
                Spell.DETECT_POISON_AND_DISEASE,
                Spell.DIVINE_FAVOR,
                Spell.DIVINE_SMITE,
                Spell.HEROISM,
                Spell.PROTECTION_FROM_EVIL_AND_GOOD,
                Spell.PURIFY_FOOD_AND_DRINK,
                Spell.SEARING_SMITE,
                Spell.SHIELD_OF_FAITH,
                Spell.THUNDEROUS_SMITE,
                Spell.WRATHFUL_SMITE,
            ],
            2: [
                Spell.AID,
                Spell.FIND_STEED,
                Spell.GENTLE_REPOSE,
                Spell.LESSER_RESTORATION,
                Spell.LOCATE_OBJECT,
                Spell.MAGIC_WEAPON,
                Spell.PRAYER_OF_HEALING,
                Spell.PROTECTION_FROM_POISON,
                Spell.SHINING_SMITE,
                Spell.WARDING_BOND,
                Spell.ZONE_OF_TRUTH,
            ],
            3: [
                Spell.AURA_OF_VITALITY,
                Spell.BLINDING_SMITE,
                Spell.CREATE_FOOD_AND_WATER,
                Spell.CRUSADERS_MANTLE,
                Spell.DAYLIGHT,
                Spell.DISPEL_MAGIC,
                Spell.ELEMENTAL_WEAPON,
                Spell.MAGIC_CIRCLE,
                Spell.REMOVE_CURSE,
                Spell.REVIVIFY,
            ],
            4: [
                Spell.AURA_OF_LIFE,
                Spell.AURA_OF_PURITY,
                Spell.BANISHMENT,
                Spell.DEATH_WARD,
                Spell.LOCATE_CREATURE,
                Spell.STAGGERING_SMITE,
            ],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        known_spells: Reason[Spell] = Reason()
        for spells in paladin_spells.values():
            for spell in spells:
                known_spells |= Reason("Paladin Spell", spell)
        return known_spells


#############################################################################
class LayOnHands(BaseFeature):
    tag = Feature.LAY_ON_HANDS14

    @property
    def desc(self) -> str:
        assert self.owner.paladin is not None
        points = self.owner.paladin.level * 5
        return f"""Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you 
        take a long rest. With that pool, you can restore {points} hit points.

        As an action, you can touch a creature and draw power from the pool to restore a number of hit points to that 
        creature, up to the maximum amount remaining in your pool.

        Alternatively, you can expend 5 hit points from your pool of healing to cure the target of one disease or 
        neutralize one poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a 
        single use of Lay on Hands, expending hit points separately for each one.

        This feature has no effect on undead and constructs."""


#############################################################################
class DivineSense(BaseFeature):
    tag = Feature.DIVINE_SENSE14
    recovery = Recovery.LONG_REST
    _desc = """As an action, you can open your awareness to detect such forces. Until the end of your next turn, 
    you know the location of any celestial, fiend, or undead within 60 feet of you that is not behind total cover. 
    You know the type (celestial, fiend, or undead) of any being whose presence you sense, but not its identity (the 
    vampire Count Strahd von Zarovich, for instance). Within the same radius, you also detect the presence of any 
    place or object that has been consecrated or desecrated, as with the hallow spell."""

    @property
    def goes(self) -> int:
        return max(1, self.owner.stats[Stat.CHARISMA].modifier)


# EOF
