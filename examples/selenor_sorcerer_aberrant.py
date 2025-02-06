from charsheets.classes import SorcererAberrant, ExtendedSpell, HeightenedSpell
from charsheets.constants import Skill, Stat
from charsheets.features import AbilityScoreImprovement
from charsheets.origins import Wayfairer
from charsheets.species import Tiefling, Legacy
from charsheets.weapons import Sling, Spear

character = SorcererAberrant(
    "Selenor",
    Wayfairer(Stat.WISDOM, Stat.DEXTERITY, Stat.CHARISMA),
    Tiefling(Legacy.ABYSSAL, Stat.INTELLIGENCE),
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
character.level1()
character.level2(hp=5)
character.add_metamagic(ExtendedSpell(), HeightenedSpell())
character.level3(hp=6)
character.level4(hp=7, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.INTELLIGENCE))
character.level5(hp=6)
character.level6(hp=3)
character.level7(hp=4)
character.level8(hp=7, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.INTELLIGENCE))
character.level9(hp=4)

character.add_weapon(Sling())
character.add_weapon(Spear())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
