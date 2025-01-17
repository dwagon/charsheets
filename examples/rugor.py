from charsheets.abilities import AbilityScoreImprovement
from charsheets.abilities import PrimalKnowledge
from charsheets.armour import Scale
from charsheets.classes import BarbarianPathOfTheBeserker
from charsheets.constants import Skill, Stat, Tool, Language, Ability
from charsheets.origins import Artisan
from charsheets.species import Dwarf
from charsheets.weapons import Shortbow, Warhammer

character = BarbarianPathOfTheBeserker(
    "Rugor",
    Artisan(Stat.STRENGTH, Stat.STRENGTH, Stat.STRENGTH),
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


character.player_name = "Beta"
character.find_ability(Ability.CRAFTER).set_tools(Tool.TINKERS_TOOLS, Tool.LEATHERWORKERS_TOOLS, Tool.SMITHS_TOOLS)  # type: ignore

character.level2(hp=8)
character.level3(hp=5, ability=PrimalKnowledge(Skill.ARCANA))
character.level4(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION))
character.level5(hp=11)
character.level6(hp=10)

character.add_languages(Language.DWARVISH, Language.GOBLIN)
character.wear_armour(Scale())
character.shield = True
character.add_weapon(Shortbow())
character.add_weapon(Warhammer())
character.extras = {"hair": "bushy"}
