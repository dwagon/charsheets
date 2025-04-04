from charsheets.armour import Studded
from charsheets.character import Character
from charsheets.classes import RogueAssassin, Rogue
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Expertise, Actor, Athlete
from charsheets.origins import Criminal
from charsheets.species import Halfling
from charsheets.weapons import Rapier, Shortbow

character = Character(
    "Aradim",
    Criminal(Stat.DEXTERITY, Stat.DEXTERITY, Stat.INTELLIGENCE),
    Halfling(),
    Language.DWARVISH,
    Language.ORC,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=10,
    charisma=8,
)
character.extras = {"alignment": "CN", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Phi"
character.add_level(
    Rogue(
        language=Language.GIANT,
        skills=[Skill.SLEIGHT_OF_HAND, Skill.STEALTH, Skill.ATHLETICS, Skill.DECEPTION],
        expertise=Expertise(Skill.SLEIGHT_OF_HAND, Skill.STEALTH),
    )
)
character.add_level(Rogue(hp=5))
character.add_level(RogueAssassin(hp=6))
character.add_level(RogueAssassin(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
character.add_level(RogueAssassin(hp=6))
character.add_level(RogueAssassin(hp=4, expertise=Expertise(Skill.ANIMAL_HANDLING, Skill.ARCANA)))
character.add_level(RogueAssassin(hp=4))
character.add_level(RogueAssassin(hp=5, feat=Actor()))
character.add_level(RogueAssassin(hp=4))
character.add_level(RogueAssassin(hp=6, feat=Athlete(Stat.DEXTERITY)))
character.add_level(RogueAssassin(hp=8))
character.add_level(RogueAssassin(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
character.add_level(RogueAssassin(hp=5))

character.add_weapon(Rapier(atk_bonus=1, dmg_bonus=1, name="Pointy End"))
character.add_weapon(Shortbow())
character.wear_armour(Studded(ac_bonus=1, name="Glamour"))
