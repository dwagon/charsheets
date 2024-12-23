#
from charsheets.classes.wizard import Wizard
from charsheets.constants import Armour, Weapon, Skill, Stat
from charsheets.origins import Charlatan
from charsheets.species.aasimar import Aasimar

character = Wizard(
    "Waznerson",
    Charlatan(Stat.DEXTERITY, Stat.DEXTERITY, Stat.CONSTITUTION),
    Aasimar(),
    Skill.ARCANA,
    Skill.MEDICINE,
    strength=8,
    dexterity=12,
    constitution=13,
    intelligence=15,
    wisdom=14,
    charisma=10,
)
character.player_name = "Epsilon"
character.extras = {
    "eyes": "glowing red",
    "hair": "white",
    "height": "6'4",
    "alignment": "NE",
    "image": "characters/images/nende.png",
    "age": "80",
    "skin": "alabaster",
}


character.armour = Armour.LEATHER
character.shield = True
character.add_weapon(Weapon.QUARTERSTAFF)

character.add_equipment("Snacks")

# EOF
