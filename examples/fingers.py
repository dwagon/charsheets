from charsheets.armour import Studded
from charsheets.backgrounds2014 import Entertainer
from charsheets.character import Character2014
from charsheets.classes2014 import Rogue
from charsheets.constants import Skill, Stat, Language
from charsheets.features import Expertise
from charsheets.race2014 import HalfElf
from charsheets.weapons import Rapier, Shortbow

character = Character2014(
    "Fingers",
    Entertainer(),
    HalfElf(language=Language.ORC, stat1=Stat.DEXTERITY, stat2=Stat.INTELLIGENCE, skill1=Skill.ACROBATICS, skill2=Skill.ATHLETICS),
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=10,
    charisma=8,
    player_name="Phi",
)
character.extras = {"alignment": "CN", "image": "characters/images/aradim.png"}
character.add_level(
    Rogue(
        skills=[Skill.SLEIGHT_OF_HAND, Skill.STEALTH, Skill.INTIMIDATION, Skill.INSIGHT],
        expertise=Expertise(Skill.SLEIGHT_OF_HAND, Skill.STEALTH),
    )
)


character.add_weapon(Rapier())
character.add_weapon(Shortbow())
character.wear_armour(Studded())
