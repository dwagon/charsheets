from charsheets.armour import Unarmoured
from charsheets.character import Character
from charsheets.classes import MonkWarriorOfTheElements, Monk
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, MagicInitiateDruid, BoonOfIrresistibleOffense
from charsheets.origins import Guide
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell

character = Character(
    "Orton Overbright",
    Guide(
        Stat.DEXTERITY,
        Stat.CONSTITUTION,
        Stat.WISDOM,
        MagicInitiateDruid(Stat.WISDOM, Spell.MESSAGE, Spell.SPARE_THE_DYING, Spell.SPEAK_WITH_ANIMALS),
    ),
    Elf(Lineages.WOOD_ELF, Skill.PERCEPTION),
    Language.ELVISH,
    Language.GNOMISH,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=10,
    wisdom=14,
    charisma=8,
)

character.player_name = "Phi"
character.extras = {"hair": "bald", "alignment": "LG"}

character.add_level(Monk(skills=[Skill.HISTORY, Skill.RELIGION]))

character.add_level(Monk(hp=5))
character.add_level(MonkWarriorOfTheElements(hp=6))
character.add_level(MonkWarriorOfTheElements(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
character.add_level(MonkWarriorOfTheElements(hp=6))
character.add_level(MonkWarriorOfTheElements(hp=5))
character.add_level(MonkWarriorOfTheElements(hp=4))
character.add_level(MonkWarriorOfTheElements(hp=3, feat=AbilityScoreImprovement(Stat.CONSTITUTION, Stat.DEXTERITY)))
character.add_level(MonkWarriorOfTheElements(hp=4))
character.add_level(MonkWarriorOfTheElements(hp=4))
character.add_level(MonkWarriorOfTheElements(hp=8))
character.add_level(MonkWarriorOfTheElements(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(MonkWarriorOfTheElements(hp=5))
character.add_level(MonkWarriorOfTheElements(hp=5))
character.add_level(MonkWarriorOfTheElements(hp=5))
character.add_level(MonkWarriorOfTheElements(hp=7, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.INTELLIGENCE)))
character.add_level(MonkWarriorOfTheElements(hp=5))
character.add_level(MonkWarriorOfTheElements(hp=5))
character.add_level(MonkWarriorOfTheElements(hp=5, boon=BoonOfIrresistibleOffense(Stat.DEXTERITY)))
character.add_level(MonkWarriorOfTheElements(hp=5))


character.wear_armour(Unarmoured())
character.add_equipment("Packed Lunch", "Ointment")
