from typing import Optional, Any, cast

from charsheets.character import Character
from charsheets.classes.warlock.invocations import BaseInvocation
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell, spell_name
from charsheets.util import safe


#################################################################################
class Warlock(Character):
    _base_skill_proficiencies = {
        Skill.ARCANA,
        Skill.DECEPTION,
        Skill.HISTORY,
        Skill.INTIMIDATION,
        Skill.INVESTIGATION,
        Skill.NATURE,
        Skill.RELIGION,
    }

    #########################################################################
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.invocations: list[BaseInvocation] = []

    #########################################################################
    @property
    def class_special(self) -> str:
        ans = [f"Eldritch Invocations\n"]
        for invocation in sorted(self.invocations, key=lambda x: x.tag):
            invoc_name = safe(invocation.tag).title()
            ans.extend((f"{invoc_name}:", invocation.desc, "\n"))
        return "\n".join(ans)

    #########################################################################
    def add_invocation(self, invocation: BaseInvocation):
        invocation.owner = self
        self.invocations.append(invocation)

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
        return Reason("Class Proficiency", cast(Proficiency, Proficiency.SIMPLE_WEAPONS))

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Class Proficiency", cast(Proficiency, Proficiency.LIGHT_ARMOUR))

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.WISDOM, Stat.CHARISMA)

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {EldritchInvocation(), PactMagic()}
        if self.level >= 2:
            abilities.add(MagicalCunning())
        if self.level >= 9:
            abilities.add(ContactPatron())

        return abilities

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
    def max_spell_level(self) -> int:
        return min(5, (self.level + 1) // 2)

    #############################################################################
    def check_modifiers(self, modifier: str) -> Reason[Any]:
        result = Reason[Any]()
        result.extend(super().check_modifiers(modifier))
        for invocation in self.invocations:
            if self._has_modifier(invocation, modifier):
                value = getattr(invocation, modifier)(character=self)
                result.extend(self._handle_modifier_result(value, f"Invocation {invocation.tag}"))
        return result

    #############################################################################
    def level11(self, **kwargs: Any):
        if "mystic" not in kwargs:
            raise InvalidOption("Level 11 Warlocks should specify 'mystic=MysticArcanum(...)'")
        self.add_feature(kwargs["mystic"])
        self._add_level(11, **kwargs)


#############################################################################
class EldritchInvocation(BaseFeature):
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
        slots = self.owner.spell_slots(self.owner.max_spell_level()) // 2
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


# EOF
