#
from charsheets.constants import Armour, Weapon, Origin, Skill, Feat, CharSubclassName
from charsheets.classes.fighter import Fighter
from charsheets.species.goliath import Goliath

character = Fighter(
    "Freya",
    Origin.CRIMINAL,
    Goliath(),
    Skill.ACROBATICS,
    Skill.INSIGHT,
    strength=16,  # base 15 + 1 for lvl 4 score
    dexterity=14,  # base 14
    constitution=15,  # base 13 + 2 for criminal
    intelligence=10,  # base 8 + 1 for criminal + 1 for lvl 4 score
    wisdom=10,  # base 10
    charisma=12,  # base 12
)
character.player_name = "Delta"
character.extras = {
    "eyes": "yellow",
    "hair": "purple",
    "height": "7'5",
    "alignment": "CN",
    "image": "characters/images/freya.png",
    "age": "20",
    "skin": "yes",
}
character.fighting_style(Feat.UNARMED_FIGHTING)
character.add_level(hp=9)  # level 2
character.add_level(hp=7)  # level 3
character.set_sub_class(CharSubclassName.CHAMPION)
character.add_level(hp=9)  # level 4
character.armour = Armour.RING
character.shield = False
character.add_weapon(Weapon.MAUL)
character.languages = {"Common", "Dwarvish"}
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# EOF
