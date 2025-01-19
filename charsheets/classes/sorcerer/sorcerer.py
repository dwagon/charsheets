from typing import Optional

from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Ability
from charsheets.reason import Reason
from charsheets.spell import Spell


#################################################################################
class Sorcerer(Character):
    _base_skill_proficiencies = {Skill.ARCANA, Skill.DECEPTION, Skill.INSIGHT, Skill.INTIMIDATION, Skill.PERSUASION, Skill.RELIGION}

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 6

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.CHARISMA

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Sorcerer", Proficiency.SIMPLE_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason()
        # type: ignore

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.CONSTITUTION, Stat.CHARISMA)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {InnateSorcery()}
        if self.level >= 2:
            abilities.add(FontOfMagic())
            abilities.add(MetaMagic())
        if self.level >= 5:
            abilities.add(SorcerousRestoration())
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            6: [4, 3, 3, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        sorcerer_spells = {
            0: [],
            1: [
                Spell.BURNING_HANDS,
                Spell.CHARM_PERSON,
                Spell.CHROMATIC_ORB,
                Spell.COLOR_SPRAY,
                Spell.COMPREHEND_LANGUAGES,
                Spell.DETECT_MAGIC,
                Spell.DISGUISE_SELF,
                Spell.EXPEDITIOUS_RETREAT,
                Spell.FALSE_LIFE,
                Spell.FEATHER_FALL,
                Spell.FOG_CLOUD,
                Spell.GREASE,
                Spell.ICE_KNIFE,
                Spell.JUMP,
                Spell.MAGE_ARMOR,
                Spell.MAGIC_MISSILE,
                Spell.RAY_OF_SICKNESS,
                Spell.SHIELD,
                Spell.SLEEP,
                Spell.THUNDERWAVE,
                Spell.WITCH_BOLT,
            ],
            2: [
                Spell.ALTER_SELF,
                Spell.ARCANE_VIGOR,
                Spell.BLINDNESS_DEAFNESS,
                Spell.BLUR,
                Spell.CLOUD_OF_DAGGERS,
                Spell.CROWN_OF_MADNESS,
                Spell.DARKNESS,
                Spell.DARKVISION,
                Spell.DETECT_THOUGHTS,
                Spell.DRAGONS_BREATH,
                Spell.ENHANCE_ABILITY,
                Spell.ENLARGE_REDUCE,
                Spell.FLAME_BLADE,
                Spell.FLAMING_SPHERE,
                Spell.GUST_OF_WIND,
                Spell.HOLD_PERSON,
                Spell.INVISIBILITY,
                Spell.KNOCK,
                Spell.LEVITATE,
                Spell.MAGIC_WEAPON,
                Spell.MIND_SPIKE,
                Spell.PHANTASMAL_FORCE,
                Spell.SCORCHING_RAY,
                Spell.SEE_INVISIBILITY,
                Spell.SHATTER,
                Spell.SPIDER_CLIMB,
                Spell.SUGGESTION,
                Spell.WEB,
            ],
            3: [
                Spell.BLINK,
                Spell.CLAIRVOYANCE,
                Spell.COUNTERSPELL,
                Spell.DAYLIGHT,
                Spell.DISPEL_MAGIC,
                Spell.FEAR,
                Spell.FIREBALL,
                Spell.FLY,
                Spell.GASEOUS_FORM,
                Spell.HASTE,
                Spell.HYPNOTIC_PATTERN,
                Spell.LIGHTNING_BOLT,
                Spell.MAJOR_IMAGE,
                Spell.PROTECTION_FROM_ENERGY,
                Spell.SLEET_STORM,
                Spell.SLOW,
                Spell.STINKING_CLOUD,
                Spell.TONGUES,
                Spell.VAMPIRIC_TOUCH,
                Spell.WATER_BREATHING,
                Spell.WATER_WALK,
            ],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        known_spells: Reason[Spell] = Reason()
        for spells in sorcerer_spells.values():
            for spell in spells:
                known_spells |= Reason("Sorcerer Spell", spell)
        return known_spells

    #############################################################################
    def max_spell_level(self) -> int:
        return min(9, ((self.level + 1) // 2))

    #########################################################################
    @property
    def sourcery_points(self) -> int:
        return self.level if self.level >= 2 else 0

    #########################################################################
    @property
    def class_special(self) -> str:
        return f"Sourcery Points: {self.sourcery_points}"


#############################################################################
class InnateSorcery(BaseAbility):
    tag = Ability.INNATE_SORCERY
    _desc = """An event in your past left an indelible mark on you, infusing you with simmering magic. As a Bonus 
    Action, you can unleash that magic for 1 minute, during which you gain the following benefits: 

    The spell save DC of your Sorcerer spells increases by 1. 

    You have Advantage on the attack rolls of Sorcerer spells you cast. 

    You can use this feature twice, and you regain all expended uses of it when you finish a Long Rest."""


#############################################################################
class FontOfMagic(BaseAbility):
    tag = Ability.FONT_OF_MAGIC
    _desc = """You can tap into the wellspring of magic within yourself. This wellspring is represented by Sorcery 
    Points, which allow you to create a variety of magical effects."""


#############################################################################
class MetaMagic(BaseAbility):
    tag = Ability.METAMAGIC
    _desc = """Because your magic flows from within, you can alter your spells to suit your needs; you gain two 
    Metamagic options of your choice from “Metamagic Options” later in this class’s description. You use the chosen 
    options to temporarily modify spells you cast. To use an option, you must spend the number of Sorcery Points that 
    it costs.

    You can use only one Metamagic option on a spell when you cast it unless otherwise noted in one of those options.

    Whenever you gain a Sorcerer level, you can replace one of your Metamagic options with one you don’t know. You 
    gain two more options at Sorcerer level 10 and two more at Sorceror level 17"""


#############################################################################
class SorcerousRestoration(BaseAbility):
    tag = Ability.SORCEROUS_RESTORATION
    _desc = """When you finish a Short Rest, you can regain expended Sorcery Points, but no more than a number equal 
    to half your Sorcerer level (round down). Once you use this feature, you can’t do so again until you finish a 
    Long Rest."""


# EOF
