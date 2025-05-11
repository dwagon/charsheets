from charsheets.armour import Shield, Scale
from charsheets.backgrounds2014 import Criminal
from charsheets.character import Character2014
from charsheets.classes2014 import Barbarian
from charsheets.constants import Skill
from charsheets.race2014 import HalfOrc
from charsheets.weapons import Battleaxe

character = Character2014(
    "Gromley",
    Criminal(),
    HalfOrc(),
    strength=15,
    dexterity=13,
    constitution=14,
    intelligence=10,
    wisdom=12,
    charisma=8,
)

character.add_level(Barbarian(skills=[Skill.INTIMIDATION, Skill.NATURE]))
character.wear_shield(Shield())
character.wear_armour(Scale())
character.add_weapon(Battleaxe())
