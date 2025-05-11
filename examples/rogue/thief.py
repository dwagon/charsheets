from typing import cast

from charsheets.armour import Studded
from charsheets.character import Character
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.features import Crafter, Expertise, AbilityScoreImprovement, BoonOfNightSpirit
from charsheets.origins import Artisan
from charsheets.species import Dwarf
from charsheets.classes import Rogue, RogueThief
from charsheets.weapons import Rapier, Shortbow

character = Character(
    "Fingers",
    Artisan(
        Stat.DEXTERITY,
        Stat.DEXTERITY,
        Stat.INTELLIGENCE,
        Crafter(cast(Tool, Tool.SMITHS_TOOLS), cast(Tool, Tool.THIEVES_TOOLS), cast(Tool, Tool.LEATHERWORKERS_TOOLS)),
    ),
    Dwarf(),
    language1=Language.DWARVISH,
    language2=Language.ORC,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=10,
    charisma=8,
)
character.extras = {"alignment": "CN", "image": "characters/images/aradim.jpg"}
character.player_name = "Phi"
character.add_level(
    Rogue(
        skills=[Skill.SLEIGHT_OF_HAND, Skill.STEALTH, Skill.INTIMIDATION, Skill.INSIGHT],
        expertise=Expertise(Skill.SLEIGHT_OF_HAND, Skill.STEALTH),
        language=Language.ABYSSAL,
    )
)

character.add_level(Rogue(hp=5))  # Level 2
character.add_level(RogueThief(hp=6))  # Level 3
character.add_level(RogueThief(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))  # Level 4
character.add_level(RogueThief(hp=6))  # Level 5
character.add_level(RogueThief(hp=4, expertise=Expertise(Skill.PERCEPTION, Skill.INVESTIGATION)))  # Level 6
character.add_level(RogueThief(hp=4))  # Level 7
character.add_level(RogueThief(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))  # Level 8
character.add_level(RogueThief(hp=4))  # Level 9
character.add_level(RogueThief(hp=6, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))  # Level 10
character.add_level(RogueThief(hp=8))  # Level 11
character.add_level(RogueThief(hp=7, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.CONSTITUTION)))  # Level 12
character.add_level(RogueThief(hp=5))  # Level 13
character.add_level(RogueThief(hp=7, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.CONSTITUTION)))
character.add_level(RogueThief(hp=5))
character.add_level(RogueThief(hp=5, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.CONSTITUTION)))
character.add_level(RogueThief(hp=5))
character.add_level(RogueThief(hp=5))
character.add_level(RogueThief(hp=5, boon=BoonOfNightSpirit(Stat.DEXTERITY)))
character.add_level(RogueThief(hp=5))

character.add_weapon(Rapier(atk_bonus=1, dmg_bonus=1, name="Pointy End"))
character.add_weapon(Shortbow())
character.wear_armour(Studded(ac_bonus=1, name="Glamour"))
