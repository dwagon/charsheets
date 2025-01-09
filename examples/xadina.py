from charsheets.feats import AbilityScoreImprovement
from charsheets.armour import Unarmoured
from charsheets.classes import MonkWarriorOfTheOpenHand
from charsheets.constants import Skill, Stat
from charsheets.origins import Guide
from charsheets.species import Elf, Lineages

character = MonkWarriorOfTheOpenHand(
    "Xadina",
    Guide(Stat.DEXTERITY, Stat.CONSTITUTION, Stat.WISDOM),
    Elf(Lineages.WOOD_ELF),
    Skill.HISTORY,
    Skill.RELIGION,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=10,
    wisdom=14,
    charisma=8,
)

character.player_name = "Phi"
character.extras = {"hair": "bald", "alignment": "LG"}
character.level2(hp=5)
character.level3(hp=6)
character.level4(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY, character))
character.level5(hp=6)

character.wear_armour(Unarmoured())
character.languages = {"Common", "Elvish", "Gnomish"}
character.add_equipment("Packed Lunch", "Ointment")
