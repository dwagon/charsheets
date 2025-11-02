#
from charsheets.armour import Ring
from charsheets.character import Character
from charsheets.classes import Fighter, FighterChampion
from charsheets.constants import Skill, Stat, Language
from charsheets.features import (
    Interception,
    AbilityScoreImprovement,
)
from charsheets.origins import Criminal
from charsheets.species import Goliath, GiantsAncestry
from charsheets.weapons import Maul

character = Character(
    "Freya",
    Criminal(Stat.CONSTITUTION, Stat.DEXTERITY, Stat.INTELLIGENCE),
    Goliath(ancestry=GiantsAncestry.STONE_GIANT),
    Language.HALFLING,
    Language.DWARVISH,
    strength=16,
    dexterity=14,
    constitution=13,
    intelligence=8,
    wisdom=10,
    charisma=12,
)
character.extras = {
    "eyes": "yellow",
    "hair": "purple",
    "height": "7'5",
    "alignment": "CN",
    "image": "characters/images/freya.png",
    "age": "20",
    "skin": "yes",
}
character.add_level(Fighter(skills=[Skill.ACROBATICS, Skill.INSIGHT], style=Interception()))
character.add_level(Fighter(hp=9))
character.add_level(FighterChampion(hp=7))
character.add_level(FighterChampion(hp=9, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
character.add_level(FighterChampion(hp=9))  # Lvl 5

character.wear_armour(Ring())
character.add_weapon(Maul())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

character.add_level(FighterChampion(hp=9))

# EOF
