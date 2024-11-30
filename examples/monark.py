from charsheets.constants import Skill, Armour, Weapon, Origin, CharSubclassName
from charsheets.classes.ranger import Ranger
from charsheets.species.human import Human

character = Ranger(
    "Monark",
    Origin.GUARD,
    Human(),
    Skill.INSIGHT,
    Skill.SURVIVAL,
    strength=14,
    dexterity=17,
    constitution=13,
    intelligence=8,
    wisdom=14,
    charisma=10,
)

character.player_name = "Gamma"
character.extras = {"hair": "patchy", "alignment": "LE"}
character.add_level(hp=5)  # level 2
character.add_level(hp=6)  # level 3
character.set_sub_class(CharSubclassName.HUNTER)
character.add_level(hp=7)  # level 4

character.armour = Armour.LEATHER
character.add_weapon(Weapon.LONGBOW)
character.add_weapon(Weapon.SHORTSWORD)
character.languages = {"Common", "Elvish", "Gnomish"}
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")

# class_skill_proficiencies = {Skill.INVESTIGATION, Skill.INSIGHT, Skill.SURVIVAL}
