""" Ability Score"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class AbilityScore:
    def __init__(self, character: "Character", value: int = 0):
        self.value: int = value
        self.proficient = 0
        self.character: "Character" = character

    #########################################################################
    @property
    def saving_throw(self) -> int:
        if self.proficient:
            return self.modifier + self.character.proficiency_bonus
        return self.modifier

    #########################################################################
    @property
    def modifier(self):
        return int((self.value - 10) / 2)

    #########################################################################
    def __str__(self):
        return f"{self.value} {self.modifier} {self.proficient}"
