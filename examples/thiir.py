from charsheets.constants import (
    Eldritch_Invocation,
    Skill,
    CharSpecies,
    CharClassName,
    Armour,
    Weapon,
    Feat,
    Origin,
    Ability,
    CharSubclassName,
)
from charsheets.spells import Spells

name = "Thiir"
player_name = "Delta"
char_class = CharClassName.WARLOCK
char_subclass = CharSubclassName.GREAT_OLD_ONE_PATRON
level = 4
species = CharSpecies.HUMAN
strength = 8
dexterity = 15
constitution = 13
intelligence = 12
wisdom = 10
charisma = 18
hp = 24
origin = Origin.ACOLYTE
skill_proficiencies = {Skill.DECEPTION, Skill.INTIMIDATION, Skill.INSIGHT, Skill.RELIGION}
weapons = {}
hair = "Bald"
equipment = ["Stuff", "More Stuff", "Something Else"]
languages = []
other_proficiencies = ["Caligraphy"]
eldritch_invocations = {Eldritch_Invocation.AGONIZING_BLAST, Eldritch_Invocation.GIFT_OF_THE_DEPTHS}
spells = {
    Spells.ELDRITCH_BLAST,
    Spells.PRESTIGITATION,
    Spells.DETECT_THOUGHTS,
    Spells.DISSONANT_WHISPERS,
    Spells.PHANTASMAL_FORCE,
    Spells.ARMOR_OF_AGATHYS,
    Spells.HEX,
    Spells.INVISIBILITY,
    Spells.MISTY_STEP,
    Spells.SUGGESTION,
    Spells.TASHAS_HIDEOUS_LAUGHTER,
}
image = "characters/images/nende.png"
