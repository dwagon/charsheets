from typing import Optional, Any

from charsheets.character import Character
from charsheets.classes.sorcerer.metamagic import BaseMetamagic
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell
from charsheets.util import safe


#################################################################################
class Sorcerer(Character):
    _base_skill_proficiencies = {Skill.ARCANA, Skill.DECEPTION, Skill.INSIGHT, Skill.INTIMIDATION, Skill.PERSUASION, Skill.RELIGION}

    #########################################################################
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.metamagic: set[BaseMetamagic] = set()

    #########################################################################
    def add_metamagic(self, *meta: BaseMetamagic):
        for m in meta:
            self.metamagic.add(m)

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
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {InnateSorcery()}
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
            7: [4, 3, 3, 1, 0, 0, 0, 0, 0],
            8: [4, 3, 3, 2, 0, 0, 0, 0, 0],
            9: [4, 3, 3, 3, 1, 0, 0, 0, 0],
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
            4: [
                Spell.BANISHMENT,
                Spell.BLIGHT,
                Spell.CHARM_MONSTER,
                Spell.CONFUSION,
                Spell.DIMENSION_DOOR,
                Spell.DOMINATE_BEAST,
                Spell.FIRE_SHIELD,
                Spell.GREATER_INVISIBILITY,
                Spell.ICE_STORM,
                Spell.POLYMORPH,
                Spell.STONESKIN,
                Spell.VITRIOLIC_SPHERE,
                Spell.WALL_OF_FIRE,
            ],
            5: [
                Spell.ANIMATE_OBJECT,
                Spell.BIGBYS_HAND,
                Spell.CLOUDKILL,
                Spell.CONE_OF_COLD,
                Spell.CREATION,
                Spell.DOMINATE_PERSON,
                Spell.HOLD_MONSTER,
                Spell.INSECT_PLAGUE,
                Spell.SEEMING,
                Spell.SYNAPTIC_STATIC,
                Spell.TELEKINESIS,
                Spell.TELEPORTATION_CIRCLE,
                Spell.WALL_OF_STONE,
            ],
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
    def sorcery_points(self) -> int:
        return self.level if self.level >= 2 else 0

    #########################################################################
    @property
    def class_special(self) -> str:
        ans = [f"Sorcery Points: {self.sorcery_points}\n"]
        if self.level >= 2:
            ans.append(f"Metamagic:\n")
            for meta in self.metamagic:
                ans.append(f"{safe(meta.tag).title()} (Cost {meta.cost} SP):\n")
                ans.extend((meta.desc, "\n"))
        return "\n".join(ans)


#############################################################################
class InnateSorcery(BaseFeature):
    tag = Feature.INNATE_SORCERY
    goes = 2
    recovery = Recovery.LONG_REST
    _desc = """As a Bonus Action, you can unleash simmering magic for 1 minute, during which you gain the following
    benefits: 

    The spell save DC of your Sorcerer spells increases by 1. 

    You have Advantage on the attack rolls of Sorcerer spells you cast."""


#############################################################################
class FontOfMagic(BaseFeature):
    tag = Feature.FONT_OF_MAGIC
    hide = True
    _desc = """You can tap into the wellspring of magic within yourself. This wellspring is represented by Sorcery 
    Points, which allow you to create a variety of magical effects."""


#############################################################################
class MetaMagic(BaseFeature):
    tag = Feature.METAMAGIC
    hide = True
    _desc = """Because your magic flows from within, you can alter your spells to suit your needs; you gain two 
    Metamagic options of your choice from “Metamagic Options” later in this class’s description. You use the chosen 
    options to temporarily modify spells you cast. To use an option, you must spend the number of Sorcery Points that 
    it costs.

    You can use only one Metamagic option on a spell when you cast it unless otherwise noted in one of those options.

    Whenever you gain a Sorcerer level, you can replace one of your Metamagic options with one you don’t know. You 
    gain two more options at Sorcerer level 10 and two more at Sorceror level 17"""


#############################################################################
class SorcerousRestoration(BaseFeature):
    tag = Feature.SORCEROUS_RESTORATION
    goes = 1
    recovery = Recovery.LONG_REST

    @property
    def desc(self) -> str:
        points = self.owner.level // 2
        return f"""When you finish a Short Rest, you can regain expended up to {points} Sorcery Points."""


#############################################################################
class SorceryIncarnate(BaseFeature):
    tag = Feature.SORCERY_INCARNATE
    _desc = """If you have no uses of Innate Sorcery left, you can use it if you spend 2 Sorcery Points when you take 
    the Bonus Action to activate it.
    
    In addition, while your Innate Sorcery feature is active, you can use up to two of your Metamagic options on each 
    spell you cast."""


# EOF
