from charsheets.features import AbilityScoreImprovement, MagicInitiateWizard
from charsheets.armour import Unarmoured
from charsheets.classes import MonkWarriorOfTheOpenHand
from charsheets.constants import Skill, Stat, Language
from charsheets.origins import Sage
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell

character = MonkWarriorOfTheOpenHand(
    "Xadina",
    Sage(
        Stat.INTELLIGENCE,
        Stat.CONSTITUTION,
        Stat.WISDOM,
        MagicInitiateWizard(Stat.WISDOM, Spell.MESSAGE, Spell.MAGE_HAND, Spell.MAGIC_MISSILE),
    ),
    Elf(Lineages.HIGH_ELF, Skill.INSIGHT),
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
character.level4(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY))
character.level5(hp=6)
character.level6(hp=5)
character.level7(hp=4)


character.wear_armour(Unarmoured())
character.add_languages(Language.ELVISH, Language.GNOMISH)
character.add_equipment("Packed Lunch", "Ointment")
