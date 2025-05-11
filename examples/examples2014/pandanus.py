from charsheets.armour import Leather
from charsheets.backgrounds2014 import Urchin
from charsheets.character import Character2014
from charsheets.classes2014 import LightCleric
from charsheets.constants import Skill, Stat, Language
from charsheets.race2014 import HalfElf
from charsheets.weapons import ShortSword

character = Character2014(
    "Pandanus",
    Urchin(),
    HalfElf(language=Language.ORC, stat1=Stat.DEXTERITY, stat2=Stat.INTELLIGENCE, skill1=Skill.ACROBATICS, skill2=Skill.ATHLETICS),
    strength=14,
    dexterity=8,
    constitution=13,
    intelligence=11,
    wisdom=17,
    charisma=12,
    player_name="Phi",
)
character.extras = {"alignment": "LG", "image": "characters/images/aradim.png"}
character.add_level(LightCleric(skills=[Skill.HISTORY, Skill.RELIGION]))
character.add_weapon(ShortSword())
character.wear_armour(Leather())
