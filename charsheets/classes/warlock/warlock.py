import math
from typing import Optional, Any, cast, TYPE_CHECKING

from aenum import extend_enum

from charsheets.classes.base_class import BaseClass
from charsheets.classes.warlock.invocations import BaseInvocation
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery, CharacterClass
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell, spell_name
from charsheets.util import safe

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "CONTACT_PATRON", "Contact Patron")
extend_enum(Feature, "ELDRITCH_INVOCATIONS", "Eldritch Invocations")
extend_enum(Feature, "ELDRITCH_MASTER", "Eldritch Master")
extend_enum(Feature, "MAGICAL_CUNNING", "Magical Cunning")
extend_enum(Feature, "MYSTIC_ARCANUM", "Mystic Arcanum")
extend_enum(Feature, "PACT_MAGIC", "Pact Magic")


#################################################################################
class Warlock(BaseClass):
    _base_skill_proficiencies = {
        Skill.ARCANA,
        Skill.DECEPTION,
        Skill.HISTORY,
        Skill.INTIMIDATION,
        Skill.INVESTIGATION,
        Skill.NATURE,
        Skill.RELIGION,
    }
    _base_class = CharacterClass.WARLOCK
    _class_name = "Warlock"

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.set_saving_throw_proficiency(Stat.WISDOM, Stat.CHARISMA)

    #############################################################################
    def level1multi(self, **kwargs: Any):
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_armor_proficiency(Reason("Warlock", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.add_feature(EldritchInvocations())
        self.add_feature(PactMagic())
        self.character.specials[CharacterClass.WARLOCK] = []

    #########################################################################
    @property
    def class_special(self) -> str:
        assert self.character is not None
        ans = [f"Eldritch Invocations\n"]
        for invocation in sorted(self.character.specials[CharacterClass.WARLOCK], key=lambda x: x.tag):
            invoc_name = safe(invocation.tag).title()
            ans.extend((f"{invoc_name}:", invocation.desc, "\n"))
        return "\n".join(ans)

    #########################################################################
    def add_invocation(self, invocation: BaseInvocation):
        assert self.character is not None
        invocation.owner = self.character
        self.character.specials[CharacterClass.WARLOCK].append(invocation)

    #########################################################################
    def remove_invocation(self, invocation: BaseInvocation):
        assert self.character is not None
        tag = invocation.tag
        for invoc in self.character.specials[CharacterClass.WARLOCK].copy():
            if invoc.tag == tag:
                self.character.specials[CharacterClass.WARLOCK].remove(invoc)

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.CHARISMA

    #############################################################################
    def level2(self, **kwargs: Any):
        self.add_feature(MagicalCunning())

    #############################################################################
    def level9(self, **kwargs: Any):
        self.add_feature(ContactPatron())

    #############################################################################
    def level11(self, **kwargs: Any):
        if "mystic" not in kwargs:
            raise InvalidOption("Level 11 Warlocks should specify 'mystic=MysticArcanum(...)'")
        self.add_feature(kwargs["mystic"])

    #############################################################################
    def level13(self, **kwargs: Any):
        if "mystic" not in kwargs:
            raise InvalidOption("Level 13 Warlocks should specify 'mystic=MysticArcanum(...)'")
        self.add_feature(kwargs["mystic"])

    #############################################################################
    def level15(self, **kwargs: Any):
        if "mystic" not in kwargs:
            raise InvalidOption("Level 15 Warlocks should specify 'mystic=MysticArcanum(...)'")
        self.add_feature(kwargs["mystic"])

    #############################################################################
    def level17(self, **kwargs: Any):
        if "mystic" not in kwargs:
            raise InvalidOption("Level 17 Warlocks should specify 'mystic=MysticArcanum(...)'")
        self.add_feature(kwargs["mystic"])

    #############################################################################
    def level20(self, **kwargs: Any):
        self.add_feature(EldritchMaster())

    #############################################################################
    def every_level(self, **kwargs: Any):
        if invocations := kwargs.get("add_invocation"):
            if not isinstance(invocations, list):
                invocations = [invocations]
            for invocation in invocations:
                self.add_invocation(invocation)

        if invocations := kwargs.get("remove_invocation"):
            if not isinstance(invocations, list):
                invocations = [invocations]
            for invocation in invocations:
                self.remove_invocation(invocation)

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [1, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [2, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [2, 2, 0, 0, 0, 0, 0, 0, 0],
            5: [2, 2, 2, 0, 0, 0, 0, 0, 0],
            6: [2, 2, 2, 0, 0, 0, 0, 0, 0],
            7: [2, 2, 2, 2, 0, 0, 0, 0, 0],
            8: [2, 2, 2, 2, 0, 0, 0, 0, 0],
            9: [2, 2, 2, 2, 2, 0, 0, 0, 0],
            10: [2, 2, 2, 2, 2, 0, 0, 0, 0],
            11: [3, 3, 3, 3, 3, 0, 0, 0, 0],
            12: [3, 3, 3, 3, 3, 0, 0, 0, 0],
            13: [3, 3, 3, 3, 3, 0, 0, 0, 0],
            14: [3, 3, 3, 3, 3, 0, 0, 0, 0],
            15: [3, 3, 3, 3, 3, 0, 0, 0, 0],
            16: [3, 3, 3, 3, 3, 0, 0, 0, 0],
            17: [4, 4, 4, 4, 4, 0, 0, 0, 0],
            18: [4, 4, 4, 4, 4, 0, 0, 0, 0],
            19: [4, 4, 4, 4, 4, 0, 0, 0, 0],
            20: [4, 4, 4, 4, 4, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def check_modifiers(self, modifier: str) -> Reason:
        assert self.character is not None
        result = Reason[Any]()
        if CharacterClass.WARLOCK not in self.character.specials:
            return result
        for invocation in self.character.specials[CharacterClass.WARLOCK]:
            if self.character._has_modifier(invocation, modifier):
                value = getattr(invocation, modifier)(character=self)
                result.extend(self.character._handle_modifier_result(value, f"Invocation {invocation.tag}"))
        result |= super().check_modifiers(modifier)
        return result

    #########################################################################
    def spell_damage_bonus(self, spell: Spell) -> int:
        """Return modifiers to spell damage"""
        result = 0
        assert self.character is not None
        for invocation in self.character.specials[CharacterClass.WARLOCK]:
            if hasattr(invocation, "spell_damage_bonus"):
                result += getattr(invocation, "spell_damage_bonus")(spell)
        return result


#############################################################################
class EldritchInvocations(BaseFeature):
    hide = True
    tag = Feature.ELDRITCH_INVOCATIONS
    _desc = """You have unearthed Eldritch Invocations, pieces of forbidden knowledge that imbue you with an abiding
    magical ability or other lessons."""


#############################################################################
class PactMagic(BaseFeature):
    tag = Feature.PACT_MAGIC
    hide = True
    _desc = """You know two Warlock cantrips"""


#############################################################################
class MagicalCunning(BaseFeature):
    tag = Feature.MAGICAL_CUNNING
    recovery = Recovery.LONG_REST
    goes = 1

    @property
    def desc(self) -> str:
        max_level = 0
        assert self.owner.warlock is not None
        for spell_level in range(1, 6):
            if self.owner.warlock.spell_slots(spell_level) != 0:
                max_level = spell_level
        slots = math.ceil(max_level / 2)

        return f"""You can perform an esoteric rite for 1 minute. At the end of it, you regain at most {slots}
        expended Pact Magic spell slots"""


#############################################################################
class ContactPatron(BaseFeature):
    tag = Feature.CONTACT_PATRON
    recovery = Recovery.LONG_REST
    _goes = 1
    _desc = """You always have the 'Contact Other Plane' spell prepared. You can cast the spell without expending a 
    spell slot to contact your patron, and you automatically succeed on the spell’s saving throw."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Contact Patron", Spell.CONTACT_OTHER_PLANE)


#############################################################################
class MysticArcanum(BaseFeature):
    tag = Feature.MYSTIC_ARCANUM
    recovery = Recovery.LONG_REST
    _goes = 1
    _desc = """Your patron grants you a magical secret called an arcanum. Choose one level 6 Warlock spell as this 
    arcanum.

    You can cast your arcanum spell once without expending a spell slot, and you must finish a Long Rest before you 
    can cast it in this way again. As shown in the Warlock Features table, you gain another Warlock spell of your 
    choice that can be cast in this way when you reach Warlock levels 13 (level 7 spell), 15 (level 8 spell), 
    and 17 (level 9 spell). You regain all uses of your Mystic Arcanum when you finish a Long Rest.

    Whenever you gain a Warlock level, you can replace one of your arcanum spells with another Warlock spell of the 
    same level."""

    @property
    def desc(self) -> str:
        spell_str = ", ".join(f"'{spell_name(_)}'" for _ in self.spells)
        return f"You can cast {spell_str} once without expending a spell slot"

    def __init__(self, *spells: Spell):
        self.spells = spells

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Mystic Arcanum", *self.spells)


#############################################################################
class EldritchMaster(BaseFeature):
    tag = Feature.ELDRITCH_MASTER

    _desc = """When you use your Magical Cunning feature, you regain all your expended Pact Magic spell slots."""


# EOF
