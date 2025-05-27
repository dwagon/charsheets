from charsheets.backgrounds2014 import Criminal
from charsheets.character import Character2014
from charsheets.classes2014 import Monk
from charsheets.constants import Skill
from charsheets.race2014 import Dragonborn, Ancestry14

character = Character2014(
    "Spaniker",
    Criminal(),
    Dragonborn(Ancestry14.BRONZE),
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=10,
    wisdom=14,
    charisma=8,
)

character.add_level(Monk(skills=[Skill.ACROBATICS, Skill.ATHLETICS]))
