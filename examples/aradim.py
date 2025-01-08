from charsheets.feats import AbilityScoreImprovement
from charsheets.armour import Studded
from charsheets.classes import RogueThief
from charsheets.constants import Skill, Stat, Tool, Feat
from charsheets.origins import Artisan
from charsheets.species import Dwarf
from charsheets.weapons import Rapier, Shortbow

character = RogueThief(
    "Aradim",
    Artisan(Stat.DEXTERITY, Stat.DEXTERITY, Stat.INTELLIGENCE),
    Dwarf(),
    Skill.SLEIGHT_OF_HAND,
    Skill.STEALTH,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=10,
    charisma=8,
)
character.extras = {"alignment": "CN", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Phi"
character.feats[Feat.CRAFTER].set_tools(Tool.SMITHS_TOOLS, Tool.THIEVES_TOOLS, Tool.LEATHERWORKERS_TOOLS)
character.level2(hp=5)
character.level3(hp=6)
character.level4(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA, character))
character.level5(hp=6)


character.add_weapon(Rapier())
character.add_weapon(Shortbow())
character.wear_armour(Studded())
