from charsheets.armour import Unarmoured
from charsheets.character import Character
from charsheets.classes import Monk, MonkWarriorOfShadow
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, LightlyArmored, BoonOfIrresistibleOffense
from charsheets.origins import Merchant
from charsheets.species import Elf, Lineages

character = Character(
    "Vincenth the Obscure",
    Merchant(Stat.INTELLIGENCE, Stat.CONSTITUTION, Stat.CHARISMA),
    Elf(Lineages.WOOD_ELF, Skill.PERCEPTION),
    Language.ELVISH,
    Language.PRIMORDIAL,
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
character.add_level(MonkWarriorOfShadow(hp=6))
character.add_level(MonkWarriorOfShadow(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
character.add_level(MonkWarriorOfShadow(hp=6))
character.add_level(MonkWarriorOfShadow(hp=5))
character.add_level(MonkWarriorOfShadow(hp=4))
character.add_level(MonkWarriorOfShadow(hp=3, feat=LightlyArmored(Stat.DEXTERITY)))
character.add_level(MonkWarriorOfShadow(hp=5))
character.add_level(MonkWarriorOfShadow(hp=5))
character.add_level(MonkWarriorOfShadow(hp=8))
character.add_level(MonkWarriorOfShadow(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
character.add_level(MonkWarriorOfShadow(hp=5))
character.add_level(MonkWarriorOfShadow(hp=5))
character.add_level(MonkWarriorOfShadow(hp=5))
character.add_level(MonkWarriorOfShadow(hp=7, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.INTELLIGENCE)))
character.add_level(MonkWarriorOfShadow(hp=5))
character.add_level(MonkWarriorOfShadow(hp=5))
character.add_level(MonkWarriorOfShadow(hp=5, boon=BoonOfIrresistibleOffense(Stat.DEXTERITY)))
character.add_level(MonkWarriorOfShadow(hp=5))

character.wear_armour(Unarmoured())
character.add_equipment("Packed Lunch", "Ointment")
