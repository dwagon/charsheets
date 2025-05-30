from typing import Optional, Any, TYPE_CHECKING

from charsheets.classes.base_class import BaseClass
from charsheets.classes.sorcerer.metamagic import BaseMetamagic
from charsheets.constants import Stat, Skill, CharacterClass, Weapon
from charsheets.reason import Reason
from charsheets.spell import Spell
from charsheets.util import safe

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#################################################################################
class Sorcerer(BaseClass):
    _base_skill_proficiencies = {Skill.ARCANA, Skill.DECEPTION, Skill.INSIGHT, Skill.INTIMIDATION, Skill.PERSUASION, Skill.RELIGION}
    _base_class = CharacterClass.SORCERER
    _class_name = "Sorcerer"

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None

    #############################################################################
    def level1multi(self, **kwargs: Any):  # pragma: no coverage
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.set_saving_throw_proficiency(Stat.CONSTITUTION, Stat.CHARISMA)
        self.character.specials[CharacterClass.SORCERER] = set()

    #############################################################################
    def mod_specific_weapon_proficiency(self, character: "BaseCharacter") -> Reason[Weapon]:
        return Reason("Sorcerer", Weapon.DAGGER, Weapon.DART, Weapon.SLING, Weapon.QUARTERSTAFF, Weapon.LIGHT_CROSSBOW)

    #############################################################################
    def every_level(self, **kwargs: Any):
        if metamagics := kwargs.get("add_metamagic"):
            if not isinstance(metamagics, list):
                metamagics = [metamagics]
            for meta in metamagics:
                self.add_metamagic(meta)

        if metamagics := kwargs.get("remove_metamagic"):
            if not isinstance(metamagics, list):
                metamagics = [metamagics]
            for meta in metamagics:
                self.remove_metamagic(meta)

    #########################################################################
    def add_metamagic(self, meta: BaseMetamagic):
        assert self.character is not None
        self.character.specials[CharacterClass.SORCERER].add(meta)

    #########################################################################
    def remove_metamagic(self, meta: BaseMetamagic):
        assert self.character is not None
        tag = meta.tag
        for mm in self.character.specials[CharacterClass.SORCERER].copy():
            if mm.tag == tag:
                self.character.specials[CharacterClass.SORCERER].remove(mm)

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 6

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.CHARISMA

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
            6: [
                Spell.ARCANE_GATE,
                Spell.CHAIN_LIGHTNING,
                Spell.CIRCLE_OF_DEATH,
                Spell.DISINTEGRATE,
                Spell.EYEBITE,
                Spell.FLESH_TO_STONE,
                Spell.GLOBE_OF_INVULNERABILITY,
                Spell.MASS_SUGGESTION,
                Spell.MOVE_EARTH,
                Spell.OTILUKES_FREEZING_SPHERE,
                Spell.SUNBEAM,
                Spell.TRUE_SEEING,
            ],
            7: [
                Spell.DELAYED_BLAST_FIREBALL,
                Spell.ETHEREALNESS,
                Spell.FINGER_OF_DEATH,
                Spell.FIRE_STORM,
                Spell.PLANE_SHIFT,
                Spell.PRISMATIC_SPRAY,
                Spell.REVERSE_GRAVITY,
                Spell.TELEPORT,
            ],
            8: [
                Spell.DEMIPLANE,
                Spell.DOMINATE_MONSTER,
                Spell.EARTHQUAKE,
                Spell.INCENDIARY_CLOUD,
                Spell.POWER_WORD_STUN,
                Spell.SUNBURST,
            ],
            9: [Spell.GATE, Spell.METEOR_STORM, Spell.POWER_WORK_KILL, Spell.TIME_STOP, Spell.WISH],
        }

        known_spells: Reason[Spell] = Reason()
        for spells in sorcerer_spells.values():
            for spell in spells:
                known_spells |= Reason("Sorcerer Spell", spell)
        return known_spells

    #########################################################################
    @property
    def sorcery_points(self) -> int:
        assert self.character is not None
        assert self.character.sorcerer is not None
        lvl = self.character.sorcerer.level
        return lvl if lvl >= 2 else 0

    #########################################################################
    @property
    def class_special(self) -> str:
        assert self.character is not None
        ans = [f"Sorcery Points: {self.sorcery_points}\n"]
        if self.level >= 2:
            ans.append(f"Metamagic:\n")
            for meta in sorted(self.character.specials[CharacterClass.SORCERER], key=lambda x: x.tag):
                ans.append(f"{safe(meta.tag).title()} (Cost {meta.cost} SP):\n")
                ans.extend((meta.desc, "\n"))
        return "\n".join(ans)


# EOF
