from typing import cast

from charsheets.armour import Studded
from charsheets.character import Character
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.features import Crafter, Expertise, SavageAttacker, AbilityScoreImprovement
from charsheets.origins import Artisan
from charsheets.species import Human, Skillful, Versatile
from charsheets.classes import Rogue, RogueAssassin
from charsheets.weapons import Rapier, Shortbow

character = Character(
    "Footpad",
    Artisan(
        Stat.DEXTERITY,
        Stat.DEXTERITY,
        Stat.INTELLIGENCE,
        Crafter(cast(Tool, Tool.SMITHS_TOOLS), cast(Tool, Tool.THIEVES_TOOLS), cast(Tool, Tool.LEATHERWORKERS_TOOLS)),
    ),
    Human(skillful=Skillful(Skill.DECEPTION), versatile=Versatile(SavageAttacker())),
    language1=Language.DWARVISH,
    language2=Language.ORC,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=10,
    charisma=8,
)

character.add_level(
    Rogue(
        skills=[Skill.SLEIGHT_OF_HAND, Skill.STEALTH, Skill.ACROBATICS, Skill.INSIGHT],
        expertise=Expertise(Skill.SLEIGHT_OF_HAND, Skill.STEALTH),
        language=Language.ORC,
    )
)
character.add_level(Rogue(hp=5))
character.add_level(RogueAssassin(hp=6))
character.add_level(RogueAssassin(hp=6,feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))

character.add_weapon(Rapier())
character.add_weapon(Shortbow())
character.wear_armour(Studded())
