#
from charsheets.classes import LifeDomain
from charsheets.constants import Armour, Weapon, Skill, Stat
from charsheets.origins import Acolyte
from charsheets.species.halfling import Halfling
from charsheets.spells import Spells

character = LifeDomain(
    "Malaketh",
    Acolyte(Stat.INTELLIGENCE, Stat.WISDOM, Stat.WISDOM),
    Halfling(),
    Skill.MEDICINE,
    Skill.HISTORY,
    strength=14,
    dexterity=8,
    constitution=13,
    intelligence=11,
    wisdom=17,
    charisma=12,
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
