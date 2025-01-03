from charsheets.abilities import AbilityScoreImprovement
from charsheets.classes import PathOfTheBeserker
from charsheets.constants import Skill, Armour, Stat, Feat, Tool
from charsheets.origins import Artisan
from charsheets.species import Dwarf
from charsheets.weapons import Shortbow, Warhammer
from charsheets.armour import Scale

character = PathOfTheBeserker(
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
character.feats[Feat.CRAFTER].set_tools(Tool.TINKERS_TOOLS, Tool.LEATHERWORKERS_TOOLS, Tool.SMITHS_TOOLS)  # type: ignore

character.level2(hp=8)
character.level3(hp=5)
character.level4(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION))
character.armour = Scale(character)
character.shield = True
character.add_weapon(Shortbow(character))
character.add_weapon(Warhammer(character))
character.extras = {"hair": "bushy"}
