from charsheets.armour import Splint
from charsheets.backgrounds2014 import Acolyte
from charsheets.character import Character2014
from charsheets.classes2014 import Paladin
from charsheets.constants import Skill, Stat, Language
from charsheets.race2014 import HalfElf
from charsheets.weapons import Mace

character = Character2014(
    "Smoofa the Uptight",
    Acolyte(Language.DWARVISH, Language.HALFLING),
    HalfElf(language=Language.ORC, stat1=Stat.DEXTERITY, stat2=Stat.INTELLIGENCE, skill1=Skill.ACROBATICS, skill2=Skill.ATHLETICS),
    strength=15,
    dexterity=10,
    constitution=13,
    intelligence=8,
    wisdom=12,
    charisma=14,
    player_name="Gerald",
)
character.extras = {"alignment": "LG"}
character.add_level(Paladin(skills=[Skill.MEDICINE, Skill.RELIGION]))
character.add_weapon(Mace())
character.wear_armour(Splint())
