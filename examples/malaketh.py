#
from charsheets.constants import Armour, Weapon, Origin, Skill, CharSubclassName
from charsheets.classes.cleric import Thaumaturge
from charsheets.spells import Spells
from charsheets.species.halfling import Halfling

character = Thaumaturge(
    "Malaketh",
    Origin.ACOLYTE,
    Halfling,
    Skill.MEDICINE,
    Skill.HISTORY,
    strength=14,  # base 14
    dexterity=8,  # base 8
    constitution=13,  # base 13
    intelligence=11,  # base 10 + 1 acolyte
    wisdom=17,  # base 15 + 2 acolyte
    charisma=12,  # base 12
)
character.player_name = "Phi"
character.extras = {
    "eyes": "brown",
    "hair": "black",
    "height": "3'",
    "alignment": "LE",
    "image": "characters/images/nende.png",
    "age": "20",
    "skin": "waxy",
}
character.learn_spell(Spells.GUIDANCE, Spells.SACRED_FLAME, Spells.THAUMATURGY)
character.learn_spell(Spells.LIGHT, Spells.RESISTANCE)  # Magic Initiate Cleric

character.add_level(8)  # Level 2
character.add_level(5)  # Level 3
character.set_sub_class(CharSubclassName.LIFE_DOMAIN)

character.armour = Armour.BREASTPLATE
character.shield = True
character.add_weapon(Weapon.MACE)

character.add_equipment("Packed lunch")

# EOF
