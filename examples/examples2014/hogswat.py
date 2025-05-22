from charsheets.armour import Studded
from charsheets.backgrounds2014 import Criminal
from charsheets.character import Character2014
from charsheets.classes2014 import Ranger
from charsheets.constants import Skill
from charsheets.race2014 import HalfOrc
from charsheets.weapons import Longsword, Longbow

character = Character2014(
    "Hogswat the Lost",
    Criminal(),
    HalfOrc(),
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=10,
    wisdom=14,
    charisma=8,
)

character.add_level(Ranger(skills=[Skill.ANIMAL_HANDLING, Skill.NATURE, Skill.SURVIVAL]))
character.wear_armour(Studded())
character.add_weapon(Longsword())
character.add_weapon(Longbow())

# EOF
