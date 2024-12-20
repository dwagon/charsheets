#
from charsheets.classes import LifeDomain
from charsheets.constants import Armour, Weapon, Skill
from charsheets.origins import Acolyte
from charsheets.species.halfling import Halfling
from charsheets.spells import Spells

character = LifeDomain(
    "Malaketh",
    Acolyte(),
    Halfling(),
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

character.armour = Armour.BREASTPLATE
character.shield = True
character.add_weapon(Weapon.MACE)

character.add_equipment("Packed lunch")

# EOF
