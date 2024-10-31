""" Class to define a character"""

from typing import Optional

from constants import Skill, Armour, WeaponType
from char_class import CharClass
from ability_score import Ability
from skill import CharacterSkill
from weapon import Weapon


#############################################################################
class Character:
    def __init__(self):
        self.name: str = "Unknown"
        self.player_name: str = "Unknown"
        self.char_class: Optional[CharClass] = None
        self.level: int = 0
        self.strength = Ability()
        self.dexterity = Ability()
        self.constitution = Ability()
        self.intelligence = Ability()
        self.wisdom = Ability()
        self.charisma = Ability()
        self.skills: dict[Skill, CharacterSkill] = {}
        self.armour: set[Armour] = set()
        self.weapons: dict[WeaponType, Weapon] = {}
        self.hp: int = 0
        self.speed: int = 30

    #########################################################################
    @property
    def hit_dice(self) -> str:
        return f"{self.level}d{self.char_class.hit_dice}"

    #########################################################################
    @property
    def initiative(self):
        return self.dexterity.modifier

    #########################################################################
    @property
    def proficiency_bonus(self) -> int:
        return int((self.level - 1) / 4) + 2

    #########################################################################
    @property
    def ac(self) -> int:
        ac = 10
        if Armour.LEATHER in self.armour:
            ac = 11 + self.dexterity.modifier
        if Armour.SHIELD in self.armour:
            ac += 2
        return ac

    #########################################################################
    def __getattr__(self, item):

        try:
            skill = Skill(item.lower())
            return self.skills[skill]
        except ValueError:
            pass
        print(f"DBG Unknown __getattr__({item=})")

    # EOF
