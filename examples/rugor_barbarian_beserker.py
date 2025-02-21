from charsheets.armour import Scale, Shield
from charsheets.classes import BarbarianPathOfTheBeserker, PrimalKnowledge
from charsheets.constants import Skill, Stat, Tool, Language, Feature
from charsheets.features import AbilityScoreImprovement, Charger, Crafter
from charsheets.origins import Artisan
from charsheets.species import Dwarf
from charsheets.weapons import Shortbow, Warhammer

character = BarbarianPathOfTheBeserker(
    "Rugor",
    Artisan(Stat.STRENGTH, Stat.STRENGTH, Stat.STRENGTH, Crafter(Tool.TINKERS_TOOLS, Tool.LEATHERWORKERS_TOOLS, Tool.SMITHS_TOOLS)),
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

character.level1()
character.level2(hp=8)
character.level3(hp=5, ability=PrimalKnowledge(Skill.ARCANA))
character.level4(hp=8, feat=Charger(Stat.CONSTITUTION))
character.level5(hp=11)
character.level6(hp=10)
character.level7(hp=3)
character.level8(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION))
character.level9(hp=4)

character.add_languages(Language.DWARVISH, Language.GOBLIN)
character.wear_armour(Scale())
character.wear_shield(Shield())
character.add_weapon(Shortbow())
character.add_weapon(Warhammer())
character.extras = {"hair": "bushy"}
