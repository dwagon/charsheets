""" Class to define a character"""

from constants import CharClass, Skill
from ability_score import Ability
from skill import CharacterSkill


#############################################################################
class Character:
    def __init__(self):
        self.name: str = "Unknown"
        self.player_name: str = "Unknown"
        self.char_class: CharClass
        self.level: int = 0
        self.strength = Ability()
        self.dexterity = Ability()
        self.constitution = Ability()
        self.intelligence = Ability()
        self.wisdom = Ability()
        self.charisma = Ability()
        self.skills: dict[Skill, CharacterSkill] = {}

    #########################################################################
    @property
    def proficiency_bonus(self) -> int:
        return int((self.level - 1) / 4) + 2

    #########################################################################
    def __getattr__(self, item):

        try:
            skill = Skill(item.lower())
            return self.skills[skill]
        except ValueError:
            pass
        print(f"DBG Unknown __getattr__({item=})")

    # EOF
