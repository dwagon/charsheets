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


extend_enum(Feature, "ABJURE_FOES", "Abjure Foes")
extend_enum(Feature, "AURA_OF_COURAGE", "Aura of Courage")
extend_enum(Feature, "AURA_OF_PROTECTION", "Aura of Protection")
extend_enum(Feature, "CHANNEL_DIVINITY_PALADIN", "Channel Divinity")
extend_enum(Feature, "FAITHFUL_STEED", "Faithful Steed")
extend_enum(Feature, "FIGHTING_STYLE_PALADIN", "Fighting Style")
extend_enum(Feature, "BLESSED_WARRIOR", "Blessed Warrior")
extend_enum(Feature, "LAY_ON_HANDS", "Lay on Hands")
extend_enum(Feature, "PALADINS_SMITE", "Paladins Smite")
extend_enum(Feature, "RADIANT_STRIKES", "Radiant Strikes")
extend_enum(Feature, "RESTORING_TOUCH", "Restoring Touch")
extend_enum(Feature, "AURA_EXPANSION", "Aura Expansion")


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
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_armor_proficiency(Reason("Paladin", cast(Proficiency, Proficiency.HEAVY_ARMOUR)))
        self.character.set_saving_throw_proficiency(Stat.WISDOM, Stat.CHARISMA)

    #############################################################################
    def level1multi(self, **kwargs: Any):
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_weapon_proficiency(Reason("Paladin", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))
        self.character.add_armor_proficiency(Reason("Paladin", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Paladin", cast(Proficiency, Proficiency.MEDIUM_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Paladin", cast(Proficiency, Proficiency.SHIELDS)))
        self.add_feature(LayOnHands())
        self.add_feature(WeaponMastery())

    #############################################################################
    def level2(self, **kwargs: Any):
        if "style" not in kwargs:
            raise InvalidOption("Level 2 Paladins need to define a fighting style, or blessed warrior, with 'style=...'")
        self.add_feature(kwargs["style"])
        self.add_feature(PaladinsSmite())

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(ChannelDivinityPaladin())

    #############################################################################
    def level5(self, **kwargs: Any):
        self.add_feature(ExtraAttack())
        self.add_feature(FaithfulSteed())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(AuraOfProtection())

    #############################################################################
    def level9(self, **kwargs: Any):
        self.add_feature(AbjureFoes())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(AuraOfCourage())

    #############################################################################
    def level11(self, **kwargs: Any):
        self.add_feature(RadiantStrikes())

    #############################################################################
    def level14(self, **kwargs: Any):
        self.add_feature(RestoringTouch())

    #############################################################################
    def level18(self, **kwargs: Any):
        self.add_feature(AuraExpansion())

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
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
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
    tag = Feature.LAY_ON_HANDS

    @property
    def desc(self) -> str:
        assert self.owner.paladin is not None
        points = self.owner.paladin.level * 5
        return f"""Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you finish 
    a Long Rest. With that pool, you can restore {points} Hit Points.

    As a Bonus Action, you can touch a creature (which could be yourself) and draw power from the pool of healing to 
    restore a number of Hit Points to that creature, up to the maximum amount remaining in the pool.

    You can also expend 5 Hit Points from the pool of healing power to remove the Poisoned condition from the creature; 
    those points don’t also restore Hit Points to the creature."""


#############################################################################
class BlessedWarrior(BaseFeature):
    tag = Feature.BLESSED_WARRIOR
    hide = True

    def __init__(self, cantrip1: Spell, cantrip2: Spell):
        super().__init__()
        self._spells = (cantrip1, cantrip2)

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Blessed Warrior", *self._spells)

    _desc = """You learn two Cleric cantrips of your choice. The chosen cantrips count as Paladin spells for you,
    and Charisma is your spellcasting ability for them. Whenever you gain a Paladin level, you can replace one of these
    cantrips with another Druid cantrip."""


#############################################################################
class PaladinsSmite(BaseFeature):
    tag = Feature.PALADINS_SMITE
    goes = 1
    recovery = Recovery.LONG_REST
    _desc = """You always have the 'Divine Smite' spell prepared. In addition, you can cast it without expending a 
    spell slot."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Paladin's Smite", Spell.DIVINE_SMITE)


#############################################################################
class FaithfulSteed(BaseFeature):
    tag = Feature.FAITHFUL_STEED
    goes = 1
    recovery = Recovery.LONG_REST

    _desc = """You always have the 'Find Steed' spell prepared. You can also cast the spell once without expending a 
    spell slot."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Faithful Steed", Spell.FIND_STEED)


#############################################################################
class ChannelDivinityPaladin(BaseFeature):
    tag = Feature.CHANNEL_DIVINITY_PALADIN
    recovery = Recovery.PARTIAL

    @property
    def goes(self) -> int:
        return 3 if self.owner.level >= 11 else 2

    _desc = """Divine Sense. As a Bonus Action, you can open your awareness to detect Celestials, Fiends, and Undead. 
    For the next 10 minutes or until you have the Incapacitated condition, you know the location of any creature of 
    those types within 60 geet of yourself, and you know its creature type. Within the same radius, you also detect 
    the presence of any place or object that has been consecrated or desecrated, as with the Hallow spell."""


#############################################################################
class AuraOfProtection(BaseFeature):
    tag = Feature.AURA_OF_PROTECTION
    _desc = ""

    @property
    def desc(self) -> str:
        bonus = max(1, self.owner.charisma.modifier)
        return f"""You radiate a protective, unseeable aura in a 10-foot Emanation that originates from you. The aura is 
    inactive while you have the Incapacitated condition.

    You and your allies in the aura gain a bonus of {bonus} to saving throws.

    If another Paladin is present, a creature can benefit from only one Aura of Protection at a time; the creature 
    chooses which aura while in them."""


#############################################################################
class AbjureFoes(BaseFeature):
    tag = Feature.ABJURE_FOES

    @property
    def desc(self) -> str:
        num = max(1, self.owner.charisma.modifier)
        return f"""As a Magic action, you can expend one use of this class’s Channel Divinity to overwhelm foes with 
        awe. As you present your Holy Symbol or weapon, you can target {num} creatures that you can see within 60 
        feet of yourself. Each target must succeed on a Wisdom saving throw or have the Frightened condition for 1 
        minute or until it takes any damage. While Frightened in this way, a target can do only one of the following 
        on its turns: move, take an action, or take a Bonus Action."""


#############################################################################
class AuraOfCourage(BaseFeature):
    tag = Feature.AURA_OF_COURAGE
    _desc = """You and your allies have Immunity to the Frightened condition while in your Aura of Protection. If a 
    Frightened ally enters the aura, that condition has no effect on that ally while there."""


#############################################################################
class RadiantStrikes(BaseFeature):
    tag = Feature.RADIANT_STRIKES
    _desc = """Your strikes now carry supernatural power. When you hit a target with an attack roll using a Melee 
    weapon or an Unarmed Strike, the target takes an extra 1d8 Radiant damage."""


#############################################################################
class RestoringTouch(BaseFeature):
    tag = Feature.RESTORING_TOUCH
    _desc = """When you use Lay On Hands on a creature, you can also remove one or more of the following conditions 
    from the creature: Blinded, Charmed, Deafened, Frightened, Paralyzed, or Stunned. You must expend 5 Hit Points 
    from the healing pool of Lay On Hands for each of these conditions you remove; those points don't also restore 
    Hit Points to the creature."""


#############################################################################
class AuraExpansion(BaseFeature):
    tag = Feature.AURA_EXPANSION
    _desc = """Your Aura of Protection is now a 30-foot Emanation."""


# EOF
