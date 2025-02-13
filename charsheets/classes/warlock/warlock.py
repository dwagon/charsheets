from typing import Optional, Any, cast

from charsheets.character import Character
from charsheets.classes.warlock.invocations import BaseInvocation
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell
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
            ans.extend((safe(invocation.tag).title(), invocation.desc, "\n"))
        return "\n".join(ans)

    #########################################################################
    def add_invocation(self, invocation: BaseInvocation):
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
class EldritchInvocation(BaseFeature):
    tag = Feature.ELDRITCH_INVOCATIONS
    _desc = """You have unearthed Eldritch Invocations, pieces of forbidden knowledge that imbue you with an abiding
    magical ability or other lessons."""


#############################################################################
class PactMagic(BaseFeature):
    tag = Feature.PACT_MAGIC
    _desc = """You know two Warlock cantrips"""


#############################################################################
class MagicalCunning(BaseFeature):
    tag = Feature.MAGICAL_CUNNING
    recovery = Recovery.LONG_REST
    goes = 1
    _desc = """You can perform an esoteric rite for 1 minute. At the end of it, you regain expended Pact Magic spell
    slots but no more than a numer equal to half your maximum (round up)."""


#############################################################################
class ContactPatron(BaseFeature):
    tag = Feature.CONTACT_PATRON
    recovery = Recovery.LONG_REST
    _goes = 1
    _desc = """You always have the Contact Other Plane spell prepared. With this feature, you can cast the spell 
    without expending a spell slot to contact your patron, and you automatically succeed on the spell’s saving throw."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Contact Patron", Spell.CONTACT_OTHER_PLANE)


# EOF
