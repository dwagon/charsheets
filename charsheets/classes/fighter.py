from typing import Optional

from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Ability, Feat
from charsheets.reason import Reason
from charsheets.abilities import WeaponMastery, ActionSurge, SecondWind, ImprovedCritical, RemarkableAthlete, TacticalMind


#################################################################################
class Fighter(Character):
    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    def fighting_style(self, style: Feat):
        self.add_feat(style)

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Fighter", Proficiency.SIMPLE_WEAPONS, Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Fighter", Proficiency.LIGHT_ARMOUR, Proficiency.MEDIUM_ARMOUR, Proficiency.HEAVY_ARMOUR, Proficiency.SHIELDS)

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.STRENGTH, Stat.CONSTITUTION)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {WeaponMastery(), ActionSurge(), SecondWind()}

        if self.level >= 2:
            abilities.add(TacticalMind())
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0


#################################################################################
class Champion(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {ImprovedCritical(), RemarkableAthlete()}
        abilities |= super().class_abilities()
        return abilities


# EOF
