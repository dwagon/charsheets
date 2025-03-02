from charsheets.armour import Studded
from charsheets.classes import RogueThief
from charsheets.constants import Skill, Stat, Tool, Feature, Language
from charsheets.features import AbilityScoreImprovement, Expertise, Crafter
from charsheets.origins import Artisan
from charsheets.species import Dwarf
from charsheets.weapons import Rapier, Shortbow

character = RogueThief(
    "Aradim",
    Artisan(
        Stat.DEXTERITY,
        Stat.DEXTERITY,
        Stat.INTELLIGENCE,
        Crafter(Tool.SMITHS_TOOLS, Tool.THIEVES_TOOLS, Tool.LEATHERWORKERS_TOOLS),
    ),
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
character.level1(expertise=Expertise(Skill.SLEIGHT_OF_HAND, Skill.STEALTH), language=Language.ABYSSAL)
character.level2(hp=5)
character.level3(hp=6)
character.level4(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA))
character.level5(hp=6)
character.level6(hp=4, expertise=Expertise(Skill.PERCEPTION, Skill.INVESTIGATION))
character.level7(hp=4)
character.level8(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA))
character.level9(hp=4)
character.level10(hp=6, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION))
character.level11(hp=8)

character.add_languages(Language.DWARVISH, Language.ORC)
character.add_weapon(Rapier(atk_bonus=1, dmg_bonus=1, name="Pointy End"))
character.add_weapon(Shortbow())
character.wear_armour(Studded(ac_bonus=1, name="Glamour"))
