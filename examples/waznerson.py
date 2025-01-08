#
from charsheets.armour import Leather
from charsheets.classes import WizardEvoker
from charsheets.constants import Stat, Feat
from charsheets.constants import Tool, Skill
from charsheets.origins import Charlatan
from charsheets.species import Aasimar
from charsheets.weapons import Quarterstaff

character = WizardEvoker(
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


character.wear_armour(Leather())
character.shield = True
character.add_weapon(Quarterstaff())

character.add_equipment("Snacks")
character.level2(hp=6)
character.level3(hp=3)

# EOF
