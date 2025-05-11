from typing import Optional, Any, cast, TYPE_CHECKING

from aenum import extend_enum
from charsheets.classes.base_class import BaseClass
from charsheets.classes.warlock.invocations import BaseInvocation
from charsheets.constants import Stat, Proficiency, Skill, Feature, CharacterClass
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell
from charsheets.util import safe

if TYPE_CHECKING:  # pragma: no coverage
    pass

extend_enum(Feature, "PACT_MAGIC14", "Pact Magic")


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
        self.character.specials[CharacterClass.WARLOCK] = []
        self.character.set_saving_throw_proficiency(Stat.WISDOM, Stat.CHARISMA)

    #############################################################################
    def level1multi(self, **kwargs: Any):  # pragma: no coverage
        pass

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_armor_proficiency(Reason("Warlock", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.add_weapon_proficiency(Reason("Warlock", cast(Proficiency, Proficiency.SIMPLE_WEAPONS)))
        self.add_feature(PactMagic())

    #########################################################################
    @property
    def class_special(self) -> str:
        assert self.character is not None
        if not self.character.specials[CharacterClass.WARLOCK]:
            return ""
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
        if not self.character.specials[CharacterClass.WARLOCK]:
            return result
        for invocation in self.character.specials[CharacterClass.WARLOCK]:
            if self.character.has_modifier(invocation, modifier):

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

    #########################################################################
    def spell_notes(self, spell: Spell) -> str:
        """Return special spell notes"""
        result = ""
        assert self.character is not None
        for invocation in self.character.specials[CharacterClass.WARLOCK]:
            if hasattr(invocation, "spell_notes"):
                result += getattr(invocation, "spell_notes")(spell)
        return result

    #########################################################################
    def spell_range(self, spell: Spell) -> int:
        """Return bonus spell range"""
        result = 0
        assert self.character is not None
        for invocation in self.character.specials[CharacterClass.WARLOCK]:
            if hasattr(invocation, "spell_range"):
                result += getattr(invocation, "spell_range")(spell)
        return result


#############################################################################
class PactMagic(BaseFeature):
    tag = Feature.PACT_MAGIC14
    hide = True
    _desc = """You know two Warlock cantrips"""


# EOF
