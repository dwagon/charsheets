#
from charsheets.constants import Armour, Weapon, Origin, Skill
from charsheets.classes.wizard import Wizard
from charsheets.species.aasimar import Aasimar

character = Wizard(
    "Waznerson",
    Origin.CHARLATAN,
    Aasimar(),
    Skill.ARCANA,
    Skill.MEDICINE,
    strength=8,  # base 8
    dexterity=14,  # base 12 +2 charlatan
    constitution=14,  # base 13 +1 charlatan
    intelligence=15,  # base 15
    wisdom=14,  # base 14
    charisma=10,  # base 10
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
