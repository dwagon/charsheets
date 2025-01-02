#
from charsheets.classes import Evoker
from charsheets.constants import Armour, Stat, Feat
from charsheets.constants import Tool, Skill
from charsheets.origins import Charlatan
from charsheets.species import Aasimar
from charsheets.weapons import Quarterstaff

character = Evoker(
    "Waznerson",
    Charlatan(Stat.DEXTERITY, Stat.DEXTERITY, Stat.CONSTITUTION),
    Aasimar(),
    Skill.ARCANA,
    Skill.MEDICINE,
    strength=8,
    dexterity=12,
    constitution=13,
    intelligence=15,
    wisdom=14,
    charisma=10,
)
character.feats[Feat.SKILLED].set_skills(Tool.DISGUISE_KIT, Skill.ATHLETICS, Skill.INTIMIDATION)  # type: ignore
character.player_name = "Epsilon"
character.extras = {
    "eyes": "glowing red",
    "hair": "white",
    "height": "6'4",
    "alignment": "NE",
    "image": "characters/images/nende.png",
    "age": "80",
    "skin": "alabaster",
}


character.armour = Armour.LEATHER
character.shield = True
character.add_weapon(Quarterstaff(character))

character.add_equipment("Snacks")
character.level2(hp=6)
character.level3(hp=3)

# EOF
