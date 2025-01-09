from typing import Optional

from charsheets.abilities import InnateSorcery, FontOfMagic, MetaMagic, SorcerousRestoration
from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill
from charsheets.reason import Reason
from charsheets.spells import Spells


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
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spells]:
        sorcerer_spells = {
            0: [],
            1: [
                Spells.BURNING_HANDS,
                Spells.CHARM_PERSON,
                Spells.CHROMATIC_ORB,
                Spells.COLOR_SPRAY,
                Spells.COMPREHEND_LANGUAGES,
                Spells.DETECT_MAGIC,
                Spells.DISGUISE_SELF,
                Spells.EXPEDITIOUS_RETREAT,
                Spells.FALSE_LIFE,
                Spells.FEATHER_FALL,
                Spells.FOG_CLOUD,
                Spells.GREASE,
                Spells.ICE_KNIFE,
                Spells.JUMP,
                Spells.MAGE_ARMOR,
                Spells.MAGIC_MISSILE,
                Spells.RAY_OF_SICKNESS,
                Spells.SHIELD,
                Spells.SLEEP,
                Spells.THUNDERWAVE,
                Spells.WITCH_BOLT,
            ],
            2: [
                Spells.ALTER_SELF,
                Spells.ARCANE_VIGOR,
                Spells.BLINDNESS_DEAFNESS,
                Spells.BLUR,
                Spells.CLOUD_OF_DAGGERS,
                Spells.CROWN_OF_MADNESS,
                Spells.DARKNESS,
                Spells.DARKVISION,
                Spells.DETECT_THOUGHTS,
                Spells.DRAGONS_BREATH,
                Spells.ENHANCE_ABILITY,
                Spells.ENLARGE_REDUCE,
                Spells.FLAME_BLADE,
                Spells.FLAMING_SPHERE,
                Spells.GUST_OF_WIND,
                Spells.HOLD_PERSON,
                Spells.INVISIBILITY,
                Spells.KNOCK,
                Spells.LEVITATE,
                Spells.MAGIC_WEAPON,
                Spells.MIND_SPIKE,
                Spells.PHANTASMAL_FORCE,
                Spells.SCORCHING_RAY,
                Spells.SEE_INVISIBILITY,
                Spells.SHATTER,
                Spells.SPIDER_CLIMB,
                Spells.SUGGESTION,
                Spells.WEB,
            ],
            3: [
                Spells.BLINK,
                Spells.CLAIRVOYANCE,
                Spells.COUNTERSPELL,
                Spells.DAYLIGHT,
                Spells.DISPEL_MAGIC,
                Spells.FEAR,
                Spells.FIREBALL,
                Spells.FLY,
                Spells.GASEOUS_FORM,
                Spells.HASTE,
                Spells.HYPNOTIC_PATTERN,
                Spells.LIGHTNING_BOLT,
                Spells.MAJOR_IMAGE,
                Spells.PROTECTION_FROM_ENERGY,
                Spells.SLEET_STORM,
                Spells.SLOW,
                Spells.STINKING_CLOUD,
                Spells.TONGUES,
                Spells.VAMPIRIC_TOUCH,
                Spells.WATER_BREATHING,
                Spells.WATER_WALK,
            ],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        known_spells: Reason[Spells] = Reason()
        for spells in sorcerer_spells.values():
            for spell in spells:
                known_spells |= Reason("Sorcerer Spell", spell)
        return known_spells

    #############################################################################
    def max_spell_level(self) -> int:
        return min(9, ((self.level + 1) // 2))


# EOF
