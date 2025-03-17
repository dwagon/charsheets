from charsheets.armour import Studded
from charsheets.classes import BarbarianPathOfTheBeserker, PrimalKnowledge
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.features import GreatWeaponMaster, Crafter
from charsheets.origins import Artisan
from charsheets.species import Dwarf
from charsheets.weapons import HeavyCrossbow
from charsheets.weapons import Warhammer

character = BarbarianPathOfTheBeserker(
    "Rugor",
    Artisan(
        Stat.STRENGTH,
        Stat.STRENGTH,
        Stat.INTELLIGENCE,
        Crafter(Tool.BREWERS_SUPPLIES, Tool.LEATHERWORKERS_TOOLS, Tool.SMITHS_TOOLS),
    ),
    Dwarf(),
    Skill.INTIMIDATION,
    Skill.ATHLETICS,
    strength=15,
    dexterity=13,
    constitution=14,
    intelligence=10,
    wisdom=12,
    charisma=8,
)
character.extras = {"image": "characters/images/rugor.jpeg"}

character.player_name = "Kurt"

character.level1()
character.level2(hp=8)
character.level3(hp=9, ability=PrimalKnowledge(Skill.SURVIVAL))
character.level4(hp=4, feat=GreatWeaponMaster())

character.add_languages(Language.DWARVISH, Language.GIANT)
character.wear_armour(Studded())
character.add_weapon(HeavyCrossbow())
character.add_weapon(Warhammer())
character.extras = {"hair": "bushy"}
