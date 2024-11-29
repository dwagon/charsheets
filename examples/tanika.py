from charsheets.constants import Origin, Weapon, Armour, Skill, CharSubclassName
from charsheets.classes.druid import Magician
from charsheets.species.elf import Elf

character = Magician(
    "Tanika",
    Origin.NOBLE,
    Elf,
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
character.set_sub_class(CharSubclassName.CIRCLE_OF_THE_LAND)
character.add_level(hp=5)


character.add_weapon(Weapon.DAGGER)
character.add_weapon(Weapon.SHORTBOW)
character.armour = Armour.LEATHER
character.shield = True
