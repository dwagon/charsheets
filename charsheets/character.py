""" Class to define a character"""

from typing import Optional

from constants import Skill, Armour, WeaponType, Stat
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
        self.age = ""
        self.height = ""
        self.weight = ""
        self.eyes = ""
        self.skin = ""
        self.hair = ""

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


#############################################################################
def get_weapons(weapons: set[WeaponType], wielder: Character) -> dict[WeaponType, Weapon]:
    weaps = {}
    for weap_type in weapons:
        weaps[weap_type] = Weapon(weap_type, wielder)
    return weaps


#############################################################################
def fill_skills(character: Character, proficiencies) -> dict[Skill, CharacterSkill]:
    skills = {}
    p = proficiencies
    pb = character.proficiency_bonus
    skills[Skill.ATHLETICS] = CharacterSkill(character.strength, pb, Skill.ATHLETICS in p)

    for skill in (Skill.ACROBATICS, Skill.SLEIGHT_OF_HAND, Skill.STEALTH):
        skills[skill] = CharacterSkill(character.dexterity, pb, skill in p)

    for skill in (Skill.ARCANA, Skill.HISTORY, Skill.INVESTIGATION, Skill.NATURE, Skill.RELIGION):
        skills[skill] = CharacterSkill(character.intelligence, pb, skill in p)

    for skill in (Skill.ANIMAL_HANDLING, Skill.INSIGHT, Skill.MEDICINE, Skill.PERCEPTION, Skill.SURVIVAL):
        skills[skill] = CharacterSkill(character.wisdom, pb, skill in p)

    for skill in (Skill.DECEPTION, Skill.INTIMIDATION, Skill.PERFORMANCE, Skill.PERSUASION):
        skills[skill] = CharacterSkill(character.charisma, pb, skill in p)

    return skills


#############################################################################
def fill_charsheet(pcm) -> Character:
    """Convert a personal character module into a filled in character"""
    character = Character()
    character.name = pcm.name
    character.player_name = pcm.player_name
    character.species = pcm.species
    character.level = pcm.level
    character.char_class = CharClass(pcm.char_class)
    character.armour = pcm.armour
    character.weapons = get_weapons(pcm.weapons, character)
    for stat in Stat:
        stated_stat = getattr(pcm, stat)
        ability = getattr(character, stat)
        ability.value = stated_stat
        ability.proficient = character.char_class.stat_proficiency(stat)
    character.hair = getattr(pcm, "hair", "undefined")
    character.eyes = getattr(pcm, "eyes", "undefined")
    character.age = getattr(pcm, "age", "undefined")
    character.weight = getattr(pcm, "weight", "undefined")
    character.height = getattr(pcm, "height", "undefined")
    character.skills = fill_skills(character, pcm.skill_proficiencies)

    return character
    # EOF
