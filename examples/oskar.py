from charsheets.armour import Plate
from charsheets.backgrounds2014 import Urchin
from charsheets.character import Character2014
from charsheets.classes2014 import WarCleric
from charsheets.constants import Skill, Stat, Language
from charsheets.race2014 import HalfElf
from charsheets.weapons import Longsword

character = Character2014(
    "Oskar Warslave",
    Urchin(),
    HalfElf(language=Language.ORC, stat1=Stat.DEXTERITY, stat2=Stat.INTELLIGENCE, skill1=Skill.ACROBATICS, skill2=Skill.ATHLETICS),
    strength=14,
    dexterity=12,
    constitution=13,
    intelligence=11,
    wisdom=17,
    charisma=8,
    player_name="Phi",
)
character.extras = {"alignment": "LE"}
character.add_level(WarCleric(skills=[Skill.HISTORY, Skill.RELIGION]))
character.add_weapon(Longsword())
character.wear_armour(Plate())
