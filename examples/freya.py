#
from charsheets.abilities import AbilityScoreImprovement
from charsheets.armour import Ring
from charsheets.classes.fighter import Champion
from charsheets.constants import Skill, Stat
from charsheets.feats import UnarmedFighting
from charsheets.origins import Criminal
from charsheets.species import Goliath
from charsheets.weapons import Maul

character = Champion(
    "Freya",
    Criminal(Stat.CONSTITUTION, Stat.CONSTITUTION, Stat.INTELLIGENCE),
    Goliath(),
    Skill.ACROBATICS,
    Skill.INSIGHT,
    strength=16,
    dexterity=14,
    constitution=13,
    intelligence=8,
    wisdom=10,
    charisma=12,
)
character.player_name = "Delta"
character.extras = {
    "eyes": "yellow",
    "hair": "purple",
    "height": "7'5",
    "alignment": "CN",
    "image": "characters/images/freya.png",
    "age": "20",
    "skin": "yes",
}
character.fighting_style(UnarmedFighting)
character.level2(hp=9)
character.level3(hp=7)
character.level4(hp=9, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.INTELLIGENCE))
character.armour = Ring(character)
character.shield = False
character.add_weapon(Maul(character))
character.languages = {"Common", "Dwarvish"}
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# EOF
