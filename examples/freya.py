from charsheets.constants import Skill, CharSpecies, CharClassName, Armour, Weapon, Feat, Origin, CharSubclassName, Ability

name = "Freya"
player_name = "Delta"
char_class = CharClassName.FIGHTER
char_subclass = CharSubclassName.CHAMPION
level = 4
species = CharSpecies.GOLIATH
strength = 16
dexterity = 14
constitution = 15
intelligence = 10
wisdom = 10
charisma = 12
hp = 43
eyes = "yellow"
hair = "purple"
height = "7'"
weight = 0
capacity = 0
alignment = "Chaotic Neutral"
origin = Origin.CRIMINAL
skill_proficiencies = {Skill.ACROBATICS, Skill.SLEIGHT_OF_HAND, Skill.STEALTH, Skill.INSIGHT}
armour = Armour.RING
shield = False
weapons = {Weapon.MAUL}
feats = {Feat.ALERT, Feat.UNARMED_FIGHTING}
abilities = {
    Ability.IMPROVED_CRITICAL,
    Ability.REMARKABLE_ATHLETE,
    Ability.WEAPON_MASTERY,
    Ability.TACTICAL_MIND,
    Ability.ACTION_SURGE,
}
equipment = ["Stuff", "More Stuff", "Something Else"]
languages = ["Common", "Dwarvish"]
other_proficiencies = ["Thieves Tools"]
