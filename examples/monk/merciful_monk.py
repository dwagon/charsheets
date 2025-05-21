from charsheets.armour import Unarmoured
from charsheets.character import Character
from charsheets.classes import Monk, MonkWarriorOfMercy
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, RitualCaster, BoonOfIrresistibleOffense
from charsheets.origins import Wayfairer
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell

character = Character(
    "Ephita",
    Wayfairer(Stat.DEXTERITY, Stat.DEXTERITY, Stat.WISDOM),
    Elf(Lineages.DROW, Skill.PERCEPTION, Stat.WISDOM),
    Language.ELVISH,
    Language.ORC,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=10,
    wisdom=14,
    charisma=8,
)

character.extras = {"hair": "bald", "alignment": "LG"}
character.add_level(Monk(skills=[Skill.HISTORY, Skill.RELIGION]))
character.add_level(Monk(hp=5))
character.add_level(MonkWarriorOfMercy(hp=6))
character.add_level(MonkWarriorOfMercy(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
character.add_level(MonkWarriorOfMercy(hp=6))
character.add_level(MonkWarriorOfMercy(hp=5))
character.add_level(MonkWarriorOfMercy(hp=4))
character.add_level(MonkWarriorOfMercy(hp=7, feat=RitualCaster(Stat.WISDOM, spells=[Spell.ALARM, Spell.FIND_FAMILIAR])))
character.add_level(MonkWarriorOfMercy(hp=5))
character.add_level(MonkWarriorOfMercy(hp=5))
character.add_level(MonkWarriorOfMercy(hp=8))
character.add_level(MonkWarriorOfMercy(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(MonkWarriorOfMercy(hp=5))
character.add_level(MonkWarriorOfMercy(hp=5))
character.add_level(MonkWarriorOfMercy(hp=5))
character.add_level(MonkWarriorOfMercy(hp=7, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.INTELLIGENCE)))
character.add_level(MonkWarriorOfMercy(hp=5))
character.add_level(MonkWarriorOfMercy(hp=5))
character.add_level(MonkWarriorOfMercy(hp=5, boon=BoonOfIrresistibleOffense(Stat.DEXTERITY)))
character.add_level(MonkWarriorOfMercy(hp=5))

character.wear_armour(Unarmoured())
character.add_equipment("Packed Lunch", "Ointment")
