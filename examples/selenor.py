from charsheets.feats import AbilityScoreImprovement
from charsheets.classes import SorcererDraconic
from charsheets.constants import Skill, Stat
from charsheets.origins import Sailor
from charsheets.species import Tiefling, Legacy
from charsheets.weapons import Sling, Spear

character = SorcererDraconic(
    "Selenor",
    Sailor(Stat.STRENGTH, Stat.DEXTERITY, Stat.STRENGTH),
    Tiefling(Legacy.INFERNAL),
    Skill.RELIGION,
    Skill.DECEPTION,
    strength=10,
    dexterity=13,
    constitution=14,
    intelligence=8,
    wisdom=12,
    charisma=15,
)

character.player_name = "zeta"
character.extras = {"hair": "none", "alignment": "LE", "skin": "scaly", "eyes": "yellow"}
character.level2(hp=5)
character.level3(hp=6)
character.level4(hp=7, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA, character))
character.level5(hp=6)
character.level6(hp=3)

character.add_weapon(Sling())
character.add_weapon(Spear())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
