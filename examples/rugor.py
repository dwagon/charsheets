from charsheets.classes import PathOfTheBeserker
from charsheets.constants import Skill, Armour, Weapon
from charsheets.origins import Artisan
from charsheets.species.dwarf import Dwarf

character = PathOfTheBeserker(
    "Rugor",
    Artisan(),
    Dwarf(),
    Skill.INTIMIDATION,
    Skill.ATHLETICS,
    strength=18,
    dexterity=14,
    constitution=14,
    intelligence=10,
    wisdom=12,
    charisma=8,
)


character.player_name = "Beta"
character.add_level(8)  # Level 2
character.add_level(5)  # Level 3
character.add_level(8)  # Level 4
character.armour = Armour.SCALE
character.shield = True
character.add_weapon(Weapon.SHORTBOW)
character.add_weapon(Weapon.WARHAMMER)
character.extras = {"hair": "bushy"}
