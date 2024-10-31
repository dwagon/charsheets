""" Class to define a character"""

from constants import Skill, Armour, WeaponType, Stat
from char_class import CharClass
from ability_score import Ability
from skill import CharacterSkill
from weapon import Weapon


#############################################################################
class Character:
    def __init__(self, pcm):
        self.pcm = pcm
        self.char_class: CharClass = CharClass(pcm.char_class)
        self.level: int = self.pcm.level
        self.species = self.pcm.species
        self.strength = Ability(pcm.strength)
        self.dexterity = Ability(pcm.dexterity)
        self.constitution = Ability(pcm.constitution)
        self.intelligence = Ability(pcm.intelligence)
        self.wisdom = Ability(pcm.wisdom)
        self.charisma = Ability(pcm.charisma)
        self.set_class_proficiency()
        self.skills: dict[Skill, CharacterSkill] = self.fill_skills(pcm.skill_proficiencies)
        self.armour: Armour = self.pcm.armour
        self.shield: bool = getattr(self.pcm, "shield", False)
        self.weapons: dict[WeaponType, Weapon] = self.get_weapons(pcm.weapons)
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
        if self.armour == Armour.LEATHER:
            ac = 11 + self.dexterity.modifier
        if self.shield:
            ac += 2
        return ac

    #########################################################################
    def set_class_proficiency(self):
        for stat in Stat:
            ability = getattr(self, stat)
            ability.proficient = self.char_class.stat_proficiency(stat)

    #########################################################################
    def __getattr__(self, item):

        try:
            skill = Skill(item.lower())
            return self.skills[skill]
        except ValueError:
            pass
        try:
            ans = getattr(self.pcm, item)
            return ans
        except AttributeError:
            pass
        print(f"DBG Unknown __getattr__({item=})")
        return "unknown"

    #############################################################################
    def fill_skills(self, proficiencies) -> dict[Skill, CharacterSkill]:
        skills = {}
        p = proficiencies
        pb = self.proficiency_bonus
        skills[Skill.ATHLETICS] = CharacterSkill(self.strength, pb, Skill.ATHLETICS in p)

        for skill in (Skill.ACROBATICS, Skill.SLEIGHT_OF_HAND, Skill.STEALTH):
            skills[skill] = CharacterSkill(self.dexterity, pb, skill in p)

        for skill in (Skill.ARCANA, Skill.HISTORY, Skill.INVESTIGATION, Skill.NATURE, Skill.RELIGION):
            skills[skill] = CharacterSkill(self.intelligence, pb, skill in p)

        for skill in (Skill.ANIMAL_HANDLING, Skill.INSIGHT, Skill.MEDICINE, Skill.PERCEPTION, Skill.SURVIVAL):
            skills[skill] = CharacterSkill(self.wisdom, pb, skill in p)

        for skill in (Skill.DECEPTION, Skill.INTIMIDATION, Skill.PERFORMANCE, Skill.PERSUASION):
            skills[skill] = CharacterSkill(self.charisma, pb, skill in p)

        return skills

    #############################################################################
    def get_weapons(self, weapons: set[WeaponType]) -> dict[WeaponType, Weapon]:
        weaps = {}
        for weap_type in weapons:
            weaps[weap_type] = Weapon(weap_type, self)
        return weaps

    # EOF
