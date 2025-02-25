from typing import Optional, cast, Any

from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery
from charsheets.exception import InvalidOption
from charsheets.features import Expertise
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell


#################################################################################
class Bard(Character):
    _base_skill_proficiencies = {
        Skill.ACROBATICS,
        Skill.ANIMAL_HANDLING,
        Skill.ARCANA,
        Skill.ATHLETICS,
        Skill.DECEPTION,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INTIMIDATION,
        Skill.INVESTIGATION,
        Skill.MEDICINE,
        Skill.NATURE,
        Skill.PERCEPTION,
        Skill.PERFORMANCE,
        Skill.PERSUASION,
        Skill.RELIGION,
        Skill.SLEIGHT_OF_HAND,
        Skill.STEALTH,
        Skill.SURVIVAL,
    }

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.CHARISMA

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason(
            "Bard",
            cast(Proficiency, Proficiency.SIMPLE_WEAPONS),
        )

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason(
            "Bard",
            cast(Proficiency, Proficiency.LIGHT_ARMOUR),
        )

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.DEXTERITY, Stat.CHARISMA)

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {BardicInspiration()}
        if self.level >= 2:
            abilities |= {JackOfAllTrades()}
        if self.level >= 5:
            abilities |= {FontOfInspiration()}
        return abilities

    #############################################################################
    def level2(self, **kwargs: Any):
        if "expertise" not in kwargs:
            raise InvalidOption("Level 2 Bards get Expertise: level2(expertise=Expertise(...))")
        self.add_feature(kwargs["expertise"])
        self._add_level(2, **kwargs)

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
            10: [4, 3, 3, 3, 2, 0, 0, 0, 0],
            11: [4, 3, 3, 3, 2, 1, 0, 0, 0],
            12: [4, 3, 3, 3, 2, 1, 0, 0, 0],
            13: [4, 3, 3, 3, 2, 1, 1, 0, 0],
            14: [4, 3, 3, 3, 2, 1, 1, 0, 0],
            15: [4, 3, 3, 3, 2, 1, 1, 1, 0],
            16: [4, 3, 3, 3, 2, 1, 1, 1, 0],
            17: [4, 3, 3, 3, 2, 1, 1, 1, 1],
            18: [4, 3, 3, 3, 3, 1, 1, 1, 1],
            19: [4, 3, 3, 3, 3, 2, 1, 1, 1],
            20: [4, 3, 3, 3, 3, 2, 2, 1, 1],
        }[self.level][spell_level - 1]

    #############################################################################
    def max_spell_level(self) -> int:
        return min(9, ((self.level + 1) // 2))

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        bard_spells = {
            0: [
                # Cantrips are learnt
            ],
            1: [
                Spell.ANIMAL_FRIENDSHIP,
                Spell.BANE,
                Spell.CHARM_PERSON,
                Spell.COLOR_SPRAY,
                Spell.COMMAND,
                Spell.COMPREHEND_LANGUAGES,
                Spell.CURE_WOUNDS,
                Spell.DETECT_MAGIC,
                Spell.DISGUISE_SELF,
                Spell.DISSONANT_WHISPERS,
                Spell.FAERIE_FIRE,
                Spell.FEATHER_FALL,
                Spell.HEALING_WORD,
                Spell.HEROISM,
                Spell.IDENTIFY,
                Spell.ILLUSORY_SCRIPT,
                Spell.LONGSTRIDER,
                Spell.SILENT_IMAGE,
                Spell.SLEEP,
                Spell.SPEAK_WITH_ANIMALS,
                Spell.TASHAS_HIDEOUS_LAUGHTER,
                Spell.THUNDERWAVE,
                Spell.UNSEEN_SERVANT,
            ],
            2: [
                Spell.AID,
                Spell.ANIMAL_MESSENGER,
                Spell.BLINDNESS_DEAFNESS,
                Spell.CALM_EMOTIONS,
                Spell.CLOUD_OF_DAGGERS,
                Spell.CROWN_OF_MADNESS,
                Spell.DETECT_THOUGHTS,
                Spell.ENHANCE_ABILITY,
                Spell.ENTHRALL,
                Spell.HEAT_METAL,
                Spell.HOLD_PERSON,
                Spell.INVISIBILITY,
                Spell.KNOCK,
                Spell.LESSER_RESTORATION,
                Spell.LOCATE_ANIMALS_OR_PLANTS,
                Spell.LOCATE_OBJECT,
                Spell.MAGIC_MOUTH,
                Spell.MIRROR_IMAGE,
                Spell.PHANTASMAL_FORCE,
                Spell.SEE_INVISIBILITY,
                Spell.SHATTER,
                Spell.SILENCE,
                Spell.SUGGESTION,
                Spell.ZONE_OF_TRUTH,
            ],
            3: [
                Spell.BESTOW_CURSE,
                Spell.CLAIRVOYANCE,
                Spell.DISPEL_MAGIC,
                Spell.FEAR,
                Spell.FEIGN_DEATH,
                Spell.GLYPH_OF_WARDING,
                Spell.HYPNOTIC_PATTERN,
                Spell.LEOMUNDS_TINY_HUT,
                Spell.MAJOR_IMAGE,
                Spell.MASS_HEALING_WORD,
                Spell.NONDETECTION,
                Spell.PLANT_GROWTH,
                Spell.SENDING,
                Spell.SLOW,
                Spell.SPEAK_WITH_DEAD,
                Spell.STINKING_CLOUD,
                Spell.TONGUES,
            ],
            4: [
                Spell.CHARM_MONSTER,
                Spell.COMPULSION,
                Spell.CONFUSION,
                Spell.DIMENSION_DOOR,
                Spell.FOUNT_OF_MOONLIGHT,
                Spell.FREEDOM_OF_MOVEMENT,
                Spell.GREATER_INVISIBILITY,
                Spell.HALLUCINATORY_TERRAIN,
                Spell.LOCATE_CREATURE,
                Spell.PHANTASMAL_KILLER,
                Spell.POLYMORPH,
            ],
            5: [
                Spell.ANIMATE_OBJECT,
                Spell.AWAKEN,
                Spell.DOMINATE_PERSON,
                Spell.DREAM,
                Spell.GEAS,
                Spell.GREATER_RESTORATION,
                Spell.HOLD_MONSTER,
                Spell.LEGEND_LORE,
                Spell.MASS_CURE_WOUNDS,
                Spell.MISLEAD,
                Spell.MODIFY_MEMORY,
                Spell.PLANAR_BINDING,
                Spell.RAISE_DEAD,
                Spell.RARYS_TELEPATHIC_BOND,
                Spell.SCRYING,
                Spell.SEEMING,
                Spell.SYNAPTIC_STATIC,
                Spell.TELEPORTATION_CIRCLE,
                Spell.YOLANDES_REGAL_PRESENCE,
            ],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        known_spells: Reason[Spell] = Reason()
        for level in range(self.max_spell_level()):
            for spell in bard_spells[level]:
                known_spells |= Reason("Bard Spell", spell)
        return known_spells

    #############################################################################
    def num_bardic_inspiration(self) -> int:
        return max(1, self.charisma.modifier)

    #############################################################################
    def bardic_inspiration_die(self) -> str:
        if self.level >= 15:
            return "d12"
        elif self.level >= 10:
            return "d10"
        elif self.level >= 5:
            return "d8"
        return "d6"

    #############################################################################
    @property
    def class_special(self) -> str:
        return f"Bardic Inspiration: {self.num_bardic_inspiration()}{self.bardic_inspiration_die()}"


#############################################################################
class BardicInspiration(BaseFeature):
    tag = Feature.BARDIC_INSPIRATION
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return self.owner.num_bardic_inspiration()

    _desc = """As a Bonus Action, you can inspire another creature within 60 feet of yourself who can see or hear 
    you. That creature gains one of your Bardic Inspiration dice. A creature can have only one Bardic Inspiration die 
    at a time.
    
    Once within the next hour when the creature fails a D20 Test, the creature can roll the Bardic Inspiration die 
    and add the number rolled to the d20, potentially turning the failure into a success."""


#############################################################################
class JackOfAllTrades(BaseFeature):
    tag = Feature.JACK_OF_ALL_TRADES

    @property
    def desc(self) -> str:
        bonus = self.owner.proficiency_bonus // 2
        return f"""You can add {bonus} to any ability check you make that uses a skill proficiency you lack and that 
        doesn't otherwise use your Proficiency Bonus."""


#############################################################################
class FontOfInspiration(BaseFeature):
    tag = Feature.FONT_OF_INSPIRATION
    _desc = """You now regain all your expended uses of Bardic Inspiration when you finish a Short or Long Rest. You 
    can expend a spell slot (no action required) to regain one expended use of Bardic Inspiration."""


# EOF
