from charsheets.armour import Leather
from charsheets.backgrounds2014 import Criminal
from charsheets.character import Character2014
from charsheets.classes2014 import Bard
from charsheets.constants import Skill
from charsheets.race2014 import HalfOrc
from charsheets.weapons import Rapier

character = Character2014(
    "Sir Robin",
    Criminal(),
    HalfOrc(),
    strength=8,
    dexterity=14,
    constitution=12,
    intelligence=13,
    wisdom=10,
    charisma=15,
)

character.add_level(Bard(skills=[Skill.INTIMIDATION, Skill.NATURE, Skill.INSIGHT]))
character.wear_armour(Leather())
character.add_weapon(Rapier())
