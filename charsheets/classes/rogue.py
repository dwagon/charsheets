from typing import Optional

from charsheets.abilities import WeaponMastery, SteadyAim
from charsheets.abilities.base_ability import BaseAbility
from charsheets.abilities.rogue import Expertise, SneakAttack, ThievesCant, CunningAction, UncannyDodge, CunningStrike
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill
from charsheets.reason import Reason


#################################################################################
class Rogue(Character):
    _base_skill_proficiencies = {
        Skill.ACROBATICS,
        Skill.ATHLETICS,
        Skill.DECEPTION,
        Skill.INSIGHT,
        Skill.INTIMIDATION,
        Skill.INVESTIGATION,
        Skill.PERCEPTION,
        Skill.PERSUASION,
        Skill.SLEIGHT_OF_HAND,
        Skill.STEALTH,
    }

    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Fighter", Proficiency.SIMPLE_WEAPONS, Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Fighter", Proficiency.LIGHT_ARMOUR)

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.DEXTERITY, Stat.INTELLIGENCE)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {Expertise(), SneakAttack(), ThievesCant(), WeaponMastery()}

        if self.level >= 2:
            abilities.add(CunningAction())
        if self.level >= 3:
            abilities.add(SteadyAim())
        if self.level >= 5:
            abilities.add(CunningStrike())
            abilities.add(UncannyDodge())
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0


# EOF
