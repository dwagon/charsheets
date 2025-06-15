# Homebrew Scimitar
# Emits bright light for 15', dim light for 15' more
# Adds proficiency for Acrobatics
from typing import TYPE_CHECKING

from charsheets.constants import Weapon, Skill
from charsheets.reason import Reason
from charsheets.weapons.scimitar import Scimitar
from charsheets.weapons.base_weapon import Modifiers

if TYPE_CHECKING:
    from charsheets.character import BaseCharacter


#############################################################################
class Featherlight(Scimitar):
    tag = Weapon.SCIMITAR

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.modifiers[Modifiers.NAME] = "Featherlight Scimitar"

    def mod_add_skill_expertise(self, character: "BaseCharacter") -> Reason[Skill]:
        return Reason("Featherlight", Skill.ACROBATICS)

    def mod_desc(self, character: "BaseCharacter") -> Reason[str]:
        return Reason(
            "Featherlight", """The weapon sheds bright light in a 15-foot radius, and dim white light for an additional 15-foot."""
        )
