from charsheets.constants import Skill, CharSpecies, Armour, Weapon, Origin, CharSubclassName
from charsheets.classes.barbarian import Barbarian

character = Barbarian(
    "Rugor",
    Origin.ARTISAN,
    CharSpecies.DWARF,
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
character.set_sub_class(CharSubclassName.PATH_OF_THE_BESERKER)
character.add_level(8)  # Level 4
character.armour = Armour.SCALE
character.shield = True
character.add_weapon(Weapon.SHORTBOW)
character.add_weapon(Weapon.WARHAMMER)
character.extras = {"hair": "bushy"}
