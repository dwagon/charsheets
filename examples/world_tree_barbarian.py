from charsheets.armour import Scale, Shield
from charsheets.character import Character
from charsheets.classes import PrimalKnowledge, Barbarian, BarbarianPathOfTheWorldTree
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.features import AbilityScoreImprovement, Charger, Crafter, PolearmMaster, BoonOfCombatProwess
from charsheets.origins import Artisan
from charsheets.species import Orc
from charsheets.weapons import Shortbow, Warhammer

character = Character(
    "Rhurg the Oaken",
    Artisan(Stat.STRENGTH, Stat.STRENGTH, Stat.STRENGTH, Crafter(Tool.TINKERS_TOOLS, Tool.LEATHERWORKERS_TOOLS, Tool.SMITHS_TOOLS)),
    Orc(),
    Language.DWARVISH,
    Language.GOBLIN,
    strength=15,
    dexterity=13,
    constitution=14,
    intelligence=10,
    wisdom=12,
    charisma=8,
)

character.player_name = "Beta"

character.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ATHLETICS]))
character.add_level(Barbarian(hp=8))
character.add_level(BarbarianPathOfTheWorldTree(hp=5, ability=PrimalKnowledge(Skill.ARCANA)))
character.add_level(BarbarianPathOfTheWorldTree(hp=8, feat=Charger(Stat.STRENGTH)))
character.add_level(BarbarianPathOfTheWorldTree(hp=11))
character.add_level(BarbarianPathOfTheWorldTree(hp=10))
character.add_level(BarbarianPathOfTheWorldTree(hp=3))
character.add_level(BarbarianPathOfTheWorldTree(hp=8, feat=PolearmMaster(Stat.STRENGTH)))
character.add_level(BarbarianPathOfTheWorldTree(hp=4))
character.add_level(BarbarianPathOfTheWorldTree(hp=5))
character.add_level(BarbarianPathOfTheWorldTree(hp=9))
character.add_level(BarbarianPathOfTheWorldTree(hp=11, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(BarbarianPathOfTheWorldTree(hp=5))
character.add_level(BarbarianPathOfTheWorldTree(hp=5))
character.add_level(BarbarianPathOfTheWorldTree(hp=5))
character.add_level(BarbarianPathOfTheWorldTree(hp=11, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(BarbarianPathOfTheWorldTree(hp=5))
character.add_level(BarbarianPathOfTheWorldTree(hp=5))
character.add_level(BarbarianPathOfTheWorldTree(hp=5, boon=BoonOfCombatProwess(Stat.CONSTITUTION)))
character.add_level(BarbarianPathOfTheWorldTree(hp=5))

character.wear_armour(Scale())
character.wear_shield(Shield())
character.add_weapon(Shortbow())
character.add_weapon(Warhammer())
character.extras = {"hair": "bushy"}
