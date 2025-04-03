from charsheets.armour import Studded
from charsheets.character import Character
from charsheets.classes import RogueSoulknife, Rogue
from charsheets.constants import Skill, Stat, Language, DamageType
from charsheets.features import AbilityScoreImprovement, Expertise, ElementalAdept
from charsheets.origins import Entertainer
from charsheets.species import Orc
from charsheets.weapons import Rapier, Shortbow

character = Character(
    "Nolam the Bastard",
    Entertainer(Stat.DEXTERITY, Stat.DEXTERITY, Stat.CHARISMA),
    Orc(),
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
        skills=[Skill.SLEIGHT_OF_HAND, Skill.STEALTH, Skill.PERCEPTION, Skill.PERSUASION],
        language=Language.DEEP_SPEECH,
        expertise=Expertise(Skill.STEALTH, Skill.HISTORY),
    )
)
character.add_level(Rogue(hp=5))
character.add_level(RogueSoulknife(hp=6))
character.add_level(RogueSoulknife(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
character.add_level(RogueSoulknife(hp=6))
character.add_level(RogueSoulknife(hp=4, expertise=Expertise(Skill.ACROBATICS, Skill.SLEIGHT_OF_HAND)))
character.add_level(RogueSoulknife(hp=4))
character.add_level(RogueSoulknife(hp=5, feat=ElementalAdept(DamageType.FIRE, Stat.CHARISMA)))
character.add_level(RogueSoulknife(hp=4))
character.add_level(RogueSoulknife(hp=6, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(RogueSoulknife(hp=8))
character.add_level(RogueSoulknife(hp=6, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(RogueSoulknife(hp=5))

character.add_weapon(Rapier(atk_bonus=1, dmg_bonus=1, name="Pointy End"))
character.add_weapon(Shortbow())
character.wear_armour(Studded(ac_bonus=1, name="Glamour"))
