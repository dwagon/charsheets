from charsheets.backgrounds2014 import Criminal
from charsheets.character import Character2014
from charsheets.classes2014 import DraconicSorcerer, Ancestor
from charsheets.constants import Skill
from charsheets.race2014 import Dragonborn, Ancestry14
from charsheets.weapons import Dagger

character = Character2014(
    "Salomax",
    Criminal(),
    Dragonborn(ancestry=Ancestry14.RED),
    strength=8,
    dexterity=13,
    constitution=14,
    intelligence=10,
    wisdom=12,
    charisma=15,
)

character.add_level(DraconicSorcerer(ancestry=Ancestor.RED, skills=[Skill.INTIMIDATION, Skill.NATURE]))
character.add_weapon(Dagger())
