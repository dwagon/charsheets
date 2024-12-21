#
from charsheets.classes.fighter import Champion
from charsheets.constants import Armour, Weapon, Skill, Feat, Stat
from charsheets.origins import Criminal
from charsheets.species.goliath import Goliath

character = Champion(
    "Freya",
    Criminal(Stat.CONSTITUTION, Stat.CONSTITUTION, Stat.INTELLIGENCE),
    Goliath(),
    Skill.ACROBATICS,
    Skill.INSIGHT,
    strength=16,  # base 15 + 1 for lvl 4 score
    dexterity=14,
    constitution=13,
    intelligence=8,  # base 8 + 1 for lvl 4 score
    wisdom=10,
    charisma=12,
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
character.add_level(hp=9)  # level 4
character.armour = Armour.RING
character.shield = False
character.add_weapon(Weapon.MAUL)
character.languages = {"Common", "Dwarvish"}
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# EOF
