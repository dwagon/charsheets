#
from charsheets.armour import Plate, Shield
from charsheets.backgrounds2014 import Soldier
from charsheets.character import Character2014
from charsheets.classes2014 import Fighter, Protection
from charsheets.constants import Skill, Language
from charsheets.race2014 import Human
from charsheets.weapons import Longsword

character = Character2014(
    "Erebrak",
    Soldier(),
    Human(Language.GIANT),
    strength=16,
    dexterity=14,
    constitution=13,
    intelligence=8,
    wisdom=10,
    charisma=12,
    player_name="Delta",
)

character.add_level(Fighter(skills=[Skill.ACROBATICS, Skill.INSIGHT], style=Protection()))

character.wear_armour(Plate())
character.wear_shield(Shield())
character.add_weapon(Longsword())
character.add_equipment("Packed lunch")

# EOF
