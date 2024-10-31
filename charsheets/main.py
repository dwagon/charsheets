""" Character sheet renderer"""

import argparse
import importlib.util
import sys

from jinja2 import FileSystemLoader, Environment

from constants import Stat, Skill, WeaponType
from character import Character
from skill import CharacterSkill
from weapon import Weapon
from char_class import CharClass


#############################################################################
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="CharSheets")
    parser.add_argument("charfile", type=argparse.FileType("r"))
    args = parser.parse_args()
    return args


#############################################################################
def import_sheet(file_handle, module_name="charsheet"):
    spec = importlib.util.spec_from_file_location(module_name, file_handle.name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


#############################################################################
def render(charsheet: Character) -> str:
    # LateX uses lots of {{ }} - so change delimeter
    env = Environment(
        loader=FileSystemLoader("templates"),
        block_start_string="[%",
        block_end_string="%]",
        variable_start_string="[[",
        variable_end_string="]]",
    )
    template = env.get_template("char_sheet.jinja")
    tex = template.render(X=charsheet)
    return tex


#############################################################################
def compile(input_str: str):
    """Compile into PDF"""


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

    character.skills = fill_skills(character, pcm.skill_proficiencies)

    return character


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
def main():
    args = parse_args()
    character_module = import_sheet(args.charfile)
    charsheet = fill_charsheet(character_module)
    tex_output = render(charsheet)
    compile(tex_output)
    print(tex_output)


#############################################################################
if __name__ == "__main__":
    main()
