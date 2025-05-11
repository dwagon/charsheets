from typing import Optional, cast, TYPE_CHECKING, Any

from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, CharacterClass
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#################################################################################
class Cleric(BaseClass):
    _base_skill_proficiencies = {Skill.HISTORY, Skill.INSIGHT, Skill.MEDICINE, Skill.PERSUASION, Skill.RELIGION}
    _base_class = CharacterClass.CLERIC
    _class_name = "Cleric"

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.set_saving_throw_proficiency(Stat.WISDOM, Stat.CHARISMA)

    #############################################################################
    def level1multi(self, **kwargs: Any):  # pragma: no coverage
        pass

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_armor_proficiency(Reason("Cleric", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Cleric", cast(Proficiency, Proficiency.MEDIUM_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Cleric", cast(Proficiency, Proficiency.SHIELDS)))

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.WISDOM

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
    def mod_add_known_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        cleric_spells = {
            0: [
                # Cantrips are learnt
            ],
            1: [
                Spell.BANE,
                Spell.BLESS,
                Spell.COMMAND,
                Spell.CREATE_OR_DESTROY_WATER,
                Spell.CURE_WOUNDS,
                Spell.DETECT_EVIL_AND_GOOD,
                Spell.DETECT_MAGIC,
                Spell.DETECT_POISON_AND_DISEASE,
                Spell.GUIDING_BOLT,
                Spell.HEALING_WORD,
                Spell.INFLICT_WOUNDS,
                Spell.PROTECTION_FROM_EVIL_AND_GOOD,
                Spell.PURIFY_FOOD_AND_DRINK,
                Spell.SANCTUARY,
                Spell.SHIELD_OF_FAITH,
            ],
            2: [
                Spell.AID,
                Spell.AUGURY,
                Spell.BLINDNESS_DEAFNESS,
                Spell.CALM_EMOTIONS,
                Spell.CONTINUAL_FLAME,
                Spell.ENHANCE_ABILITY,
                Spell.FIND_TRAPS,
                Spell.GENTLE_REPOSE,
                Spell.HOLD_PERSON,
                Spell.LESSER_RESTORATION,
                Spell.LOCATE_OBJECT,
                Spell.PRAYER_OF_HEALING,
                Spell.PROTECTION_FROM_POISON,
                Spell.SILENCE,
                Spell.SPIRITUAL_WEAPON,
                Spell.WARDING_BOND,
                Spell.ZONE_OF_TRUTH,
            ],
            3: [
                Spell.ANIMATE_DEAD,
                Spell.AURA_OF_VITALITY,
                Spell.BEACON_OF_HOPE,
                Spell.BESTOW_CURSE,
                Spell.CLAIRVOYANCE,
                Spell.CREATE_FOOD_AND_WATER,
                Spell.DAYLIGHT,
                Spell.DISPEL_MAGIC,
                Spell.FEIGN_DEATH,
                Spell.GLYPH_OF_WARDING,
                Spell.MAGIC_CIRCLE,
                Spell.MASS_HEALING_WORD,
                Spell.MELD_INTO_STONE,
                Spell.PROTECTION_FROM_ENERGY,
                Spell.REMOVE_CURSE,
                Spell.REVIVIFY,
                Spell.SENDING,
                Spell.SPEAK_WITH_DEAD,
                Spell.SPIRIT_GUARDIANS,
                Spell.TONGUES,
                Spell.WATER_WALK,
            ],
            4: [
                Spell.AURA_OF_LIFE,
                Spell.AURA_OF_PURITY,
                Spell.BANISHMENT,
                Spell.CONTROL_WATER,
                Spell.DEATH_WARD,
                Spell.DIVINATION,
                Spell.FREEDOM_OF_MOVEMENT,
                Spell.GUARDIAN_OF_FAITH,
                Spell.LOCATE_CREATURE,
                Spell.STONE_SHAPE,
            ],
            5: [
                Spell.CIRCLE_OF_POWER,
                Spell.COMMUNE,
                Spell.CONTAGION,
                Spell.DISPEL_EVIL_AND_GOOD,
                Spell.FLAME_STRIKE,
                Spell.GEAS,
                Spell.GREATER_RESTORATION,
                Spell.HALLOW,
                Spell.INSECT_PLAGUE,
                Spell.LEGEND_LORE,
                Spell.MASS_CURE_WOUNDS,
                Spell.PLANAR_BINDING,
                Spell.RAISE_DEAD,
                Spell.SCRYING,
                Spell.SUMMON_CELESTIAL,
            ],
            6: [
                Spell.BLADE_BARRIER,
                Spell.CREATE_UNDEAD,
                Spell.FIND_THE_PATH,
                Spell.FORBIDDANCE,
                Spell.HARM,
                Spell.HEROES_FEAST,
                Spell.PLANAR_ALLY,
                Spell.SUNBEAM,
                Spell.TRUE_SEEING,
                Spell.WORD_OF_RECALL,
            ],
            7: [
                Spell.CONJURE_CELESTIAL,
                Spell.DIVINE_WORD,
                Spell.ETHEREALNESS,
                Spell.FIRE_STORM,
                Spell.PLANE_SHIFT,
                Spell.POWER_WORD_FORTIFY,
                Spell.REGENERATE,
                Spell.RESURRECTION,
                Spell.SYMBOL,
            ],
            8: [Spell.ANTIMAGIC_FIELD, Spell.CONTROL_WEATHER, Spell.EARTHQUAKE, Spell.HOLY_AURA, Spell.SUNBURST],
            9: [Spell.ASTRAL_PROJECTION, Spell.GATE, Spell.MASS_HEAL, Spell.POWER_WORD_HEAL, Spell.TRUE_RESURRECTION],
        }

        known_spells: Reason[Spell] = Reason()
        for spells in cleric_spells.values():
            for spell in spells:
                known_spells |= Reason("Cleric Spell", spell)
        return known_spells


# EOF
