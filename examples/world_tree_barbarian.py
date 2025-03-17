from charsheets.armour import Scale, Shield
from charsheets.classes import BarbarianPathOfTheWorldTree, PrimalKnowledge
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.features import AbilityScoreImprovement, Charger, Crafter, PolearmMaster
from charsheets.origins import Artisan
from charsheets.species import Orc
from charsheets.weapons import Shortbow, Warhammer

character = BarbarianPathOfTheWorldTree(
    "Rhurg the Oaken",
    Artisan(Stat.STRENGTH, Stat.STRENGTH, Stat.STRENGTH, Crafter(Tool.TINKERS_TOOLS, Tool.LEATHERWORKERS_TOOLS, Tool.SMITHS_TOOLS)),
    Orc(),
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
character.level4(hp=8, feat=Charger(Stat.STRENGTH))
character.level5(hp=11)
character.level6(hp=10)
character.level7(hp=3)
character.level8(hp=8, feat=PolearmMaster(Stat.STRENGTH))
character.level9(hp=4)
character.level10(hp=5)
character.level11(hp=9)
character.level12(hp=11, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION))
character.level13(hp=5)

character.add_languages(Language.DWARVISH, Language.GOBLIN)
character.wear_armour(Scale())
character.wear_shield(Shield())
character.add_weapon(Shortbow())
character.add_weapon(Warhammer())
character.extras = {"hair": "bushy"}
