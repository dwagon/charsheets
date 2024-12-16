from charsheets.constants import Skill, Armour, Weapon, Origin
from charsheets.classes import Hunter
from charsheets.species.human import Human

character = Hunter(
    "Monark",
    Origin.GUARD,
    Human(Skill.ANIMAL_HANDLING),
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
character.add_level(hp=7)  # level 4

character.armour = Armour.LEATHER
character.add_weapon(Weapon.LONGBOW)
character.add_weapon(Weapon.SHORTSWORD)
character.languages = {"Common", "Elvish", "Gnomish"}
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
