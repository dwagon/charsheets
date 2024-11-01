""" Class to define a character"""

from typing import Any

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
        self.stats = {
            Stat.STRENGTH: Ability(pcm.strength),
            Stat.DEXTERITY: Ability(pcm.dexterity),
            Stat.CONSTITUTION: Ability(pcm.constitution),
            Stat.INTELLIGENCE: Ability(pcm.intelligence),
            Stat.WISDOM: Ability(pcm.wisdom),
            Stat.CHARISMA: Ability(pcm.charisma),
        }
        self.set_class_proficiency()
        self.skills: dict[Skill, CharacterSkill] = self.fill_skills(pcm.skill_proficiencies)
        self.armour: Armour = self.pcm.armour
        self.shield: bool = getattr(self.pcm, "shield", False)
        self.equipment: list[str] = getattr(self.pcm, "equipment", [])
        self.weapons: dict[WeaponType, Weapon] = self.get_weapons(self.pcm.weapons)
        self.hp: int = 0
        self.speed: int = 30

    #########################################################################
    @property
    def hit_dice(self) -> str:
        return f"{self.level}d{self.char_class.hit_dice}"

    #########################################################################
    @property
    def spell_save_dc(self) -> int:
        return 8 + self.spell_attack_bonus

    #########################################################################
    @property
    def spell_attack_bonus(self) -> int:
        bonus = self.proficiency_bonus
        bonus += self.stats[self.spell_casting_ability].modifier
        return bonus

    #########################################################################
    @property
    def spell_casting_ability(self) -> Stat:
        return self.char_class.spell_casting_ability

    #########################################################################
    @property
    def initiative(self):
        return self.stats[Stat.DEXTERITY].modifier

    #########################################################################
    @property
    def proficiency_bonus(self) -> int:
        return int((self.level - 1) / 4) + 2

    #########################################################################
    @property
    def ac(self) -> int:
        ac = 10
        if self.armour == Armour.LEATHER:
            ac = 11 + self.stats[Stat.DEXTERITY].modifier
        if self.shield:
            ac += 2
        return ac

    #########################################################################
    def set_class_proficiency(self):
        for stat in Stat:
            self.stats[stat].proficient = self.char_class.stat_proficiency(stat)

    #########################################################################
    def __getattr__(self, item: str) -> Any:
        """Guess what they are asking for"""
        # Try a skill
        try:
            skill = Skill(item.lower())
            return self.skills[skill]
        except ValueError:
            pass

        # Try Stat
        try:
            return self.stats[Stat(item.lower())]
        except ValueError:
            pass

        # Try anything mentioned in the pcm
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
        skills[Skill.ATHLETICS] = CharacterSkill(self.stats[Stat.STRENGTH], pb, Skill.ATHLETICS in p)

        for skill in (Skill.ACROBATICS, Skill.SLEIGHT_OF_HAND, Skill.STEALTH):
            skills[skill] = CharacterSkill(self.stats[Stat.DEXTERITY], pb, skill in p)

        for skill in (Skill.ARCANA, Skill.HISTORY, Skill.INVESTIGATION, Skill.NATURE, Skill.RELIGION):
            skills[skill] = CharacterSkill(self.stats[Stat.INTELLIGENCE], pb, skill in p)

        for skill in (Skill.ANIMAL_HANDLING, Skill.INSIGHT, Skill.MEDICINE, Skill.PERCEPTION, Skill.SURVIVAL):
            skills[skill] = CharacterSkill(self.stats[Stat.WISDOM], pb, skill in p)

        for skill in (Skill.DECEPTION, Skill.INTIMIDATION, Skill.PERFORMANCE, Skill.PERSUASION):
            skills[skill] = CharacterSkill(self.stats[Stat.CHARISMA], pb, skill in p)

        return skills

    #############################################################################
    def get_weapons(self, weapons: set[WeaponType]) -> dict[WeaponType, Weapon]:
        weaps = {}
        for weap_type in weapons:
            weaps[weap_type] = Weapon(weap_type, self)
        return weaps

    # EOF
