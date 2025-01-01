from charsheets.classes import Hunter
from charsheets.constants import Skill, Armour, Weapon, Stat
from charsheets.origins import Guard
from charsheets.species.human import Human
from charsheets.abilities import AbilityScoreImprovement
from charsheets.weapons import Longbow, ShortSword

character = Hunter(
    "Monark",
    Guard(Stat.STRENGTH, Stat.STRENGTH, Stat.WISDOM),
    Human(Skill.ANIMAL_HANDLING),
    Skill.INSIGHT,
    Skill.SURVIVAL,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=8,
    wisdom=14,
    charisma=10,
)

character.player_name = "Gamma"
character.extras = {"hair": "patchy", "alignment": "LE"}
character.level2(hp=5)
character.level3(hp=6)
character.level4(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION))

character.armour = Armour.LEATHER
character.add_weapon(Longbow(character))
character.add_weapon(ShortSword(character))
character.languages = {"Common", "Elvish", "Gnomish"}
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
