from charsheets.armour import Scale, Shield
from charsheets.character import Character
from charsheets.classes import Barbarian, PrimalKnowledge, BarbarianPathOfTheBeserker, Rogue
from charsheets.constants import Stat, Tool, Language, Skill
from charsheets.features import Crafter, Charger, PolearmMaster, AbilityScoreImprovement, Expertise
from charsheets.origins import Artisan
from charsheets.species import Dwarf
from charsheets.weapons import Shortbow, Warhammer

character = Character(
    "Mhurg the Shieldbiter",
    Artisan(Stat.STRENGTH, Stat.STRENGTH, Stat.STRENGTH, Crafter(Tool.TINKERS_TOOLS, Tool.LEATHERWORKERS_TOOLS, Tool.SMITHS_TOOLS)),
    Dwarf(),
    language1=Language.DWARVISH,
    language2=Language.GOBLIN,
    strength=15,
    dexterity=13,
    constitution=14,
    intelligence=10,
    wisdom=12,
    charisma=8,
)

character.player_name = "Beta"

character.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.ATHLETICS]))  # Level 1
character.add_level(Barbarian(hp=8))  # Level 2
character.add_level(BarbarianPathOfTheBeserker(hp=5, ability=PrimalKnowledge(Skill.ARCANA)))  # Level 3
character.add_level(BarbarianPathOfTheBeserker(hp=8, feat=Charger(Stat.STRENGTH)))  # Level 4
character.add_level(BarbarianPathOfTheBeserker(hp=11))  # Level 5
character.add_level(BarbarianPathOfTheBeserker(hp=10))  # Level 6
character.add_level(BarbarianPathOfTheBeserker(hp=3))  # Level 7
character.add_level(BarbarianPathOfTheBeserker(hp=8, feat=PolearmMaster(Stat.STRENGTH)))  # Level 8
character.add_level(BarbarianPathOfTheBeserker(hp=4))  # Level 9
character.add_level(BarbarianPathOfTheBeserker(hp=5))  # Level 10
character.add_level(BarbarianPathOfTheBeserker(hp=9))  # Level 11
character.add_level(BarbarianPathOfTheBeserker(hp=11, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))  # Level 12
# character.add_level(BarbarianPathOfTheBeserker(hp=5))  # Level 13
character.add_level(
    Rogue(hp=5, language=Language.ORC, skills=[Skill.SLEIGHT_OF_HAND], expertise=Expertise(Skill.STEALTH, Skill.SLEIGHT_OF_HAND))
)

character.wear_armour(Scale())
character.wear_shield(Shield())
character.add_weapon(Shortbow())
character.add_weapon(Warhammer())
character.extras = {"hair": "bushy"}
