from charsheets.armour import HalfPlate
from charsheets.character import Character
from charsheets.classes import BarbarianPathOfTheBerserker, PrimalKnowledge, Barbarian
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.features import GreatWeaponMaster, Crafter
from charsheets.origins import Artisan
from charsheets.species import Dwarf
from charsheets.weapons import HeavyCrossbow
from charsheets.weapons import Warhammer

character = Character(
    "Rugor",
    Artisan(
        Stat.STRENGTH,
        Stat.STRENGTH,
        Stat.INTELLIGENCE,
        Crafter(Tool.BREWERS_SUPPLIES, Tool.LEATHERWORKERS_TOOLS, Tool.SMITHS_TOOLS),
    ),
    Dwarf(),
    Language.DWARVISH,
    Language.GIANT,
    strength=15,
    dexterity=13,
    constitution=14,
    intelligence=10,
    wisdom=12,
    charisma=8,
    alignment="Questionable",
    player_name="Kurt",
)
character.extras = {"image": "characters/images/rugor.jpeg"}

character.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ATHLETICS]))
character.add_level(Barbarian(hp=8))
character.add_level(BarbarianPathOfTheBerserker(hp=9, ability=PrimalKnowledge(Skill.SURVIVAL)))
character.add_level(BarbarianPathOfTheBerserker(hp=4, feat=GreatWeaponMaster()))
character.add_level(BarbarianPathOfTheBerserker(hp=11))


character.wear_armour(HalfPlate())
character.add_weapon(HeavyCrossbow())
character.add_weapon(Warhammer())
character.extras = {"hair": "bushy"}

character.add_level(BarbarianPathOfTheBerserker(hp=9))  # Level 6
character.add_equipment("Spite Blade")  # TODO - details
character.add_equipment("Rubber Ducky", "Water Finding Compass", "Dragon Compass")
