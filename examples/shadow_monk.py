from charsheets.armour import Unarmoured
from charsheets.classes import MonkWarriorOfShadow
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, LightlyArmored
from charsheets.origins import Merchant
from charsheets.species import Elf, Lineages

character = MonkWarriorOfShadow(
    "Vincenth the Obscure",
    Merchant(Stat.INTELLIGENCE, Stat.CONSTITUTION, Stat.CHARISMA),
    Elf(Lineages.WOOD_ELF, Skill.PERCEPTION),
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
character.level1()
character.level2(hp=5)
character.level3(hp=6)
character.level4(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY))
character.level5(hp=6)
character.level6(hp=5)
character.level7(hp=4)
character.level8(hp=3, feat=LightlyArmored(Stat.DEXTERITY))
character.level9(hp=5)
character.level10(hp=5)
character.level11(hp=8)
character.level12(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY))
character.level13(hp=5)

character.wear_armour(Unarmoured())
character.add_languages(Language.ELVISH, Language.PRIMORDIAL)
character.add_equipment("Packed Lunch", "Ointment")
