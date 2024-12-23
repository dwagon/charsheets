from charsheets.classes import CircleOfTheLandDruid, Magician
from charsheets.constants import Weapon, Armour, Skill, Stat
from charsheets.origins import Noble
from charsheets.species.elf import Elf


class Tanika(Magician, CircleOfTheLandDruid):
    pass


character = Tanika(
    "Tanika",
    Noble(Stat.INTELLIGENCE, Stat.CHARISMA, Stat.CHARISMA),
    Elf(),
    Skill.INSIGHT,
    Skill.PERCEPTION,
    strength=8,
    dexterity=12,
    constitution=14,
    intelligence=13,
    wisdom=15,
    charisma=10,
)

character.extras = {"alignment": "N", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Alpha"
character.level2(hp=5)
character.level3(hp=6)
character.level4(hp=5)


character.add_weapon(Weapon.DAGGER)
character.add_weapon(Weapon.SHORTBOW)
character.armour = Armour.LEATHER
character.shield = True
