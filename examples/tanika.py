from charsheets.classes import CircleOfTheLandDruid, Magician
from charsheets.constants import Weapon, Armour, Skill
from charsheets.origins import Noble
from charsheets.species.elf import Elf


class Tanika(Magician, CircleOfTheLandDruid):
    pass


character = Tanika(
    "Tanika",
    Noble(),
    Elf(),
    Skill.INSIGHT,
    Skill.PERCEPTION,
    strength=8,
    dexterity=12,
    constitution=14,
    intelligence=14,
    wisdom=16,
    charisma=12,
)

character.extras = {"alignment": "N", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Alpha"
character.add_level(hp=5)
character.add_level(hp=6)
character.add_level(hp=5)


character.add_weapon(Weapon.DAGGER)
character.add_weapon(Weapon.SHORTBOW)
character.armour = Armour.LEATHER
character.shield = True
