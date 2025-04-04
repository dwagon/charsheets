from charsheets.armour import Unarmoured
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, RitualCaster
from charsheets.origins import Wayfairer
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell

character = Character(
    "Ephita",
    Wayfairer(Stat.DEXTERITY, Stat.DEXTERITY, Stat.WISDOM),
    Elf(Lineages.DROW, Skill.PERCEPTION),
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
character.level8(hp=7, feat=RitualCaster(Stat.WISDOM, spells=[Spell.ALARM, Spell.FIND_FAMILIAR]))
character.level9(hp=5)
character.level10(hp=5)
character.level11(hp=8)
character.level12(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION))
character.level13(hp=5)


character.wear_armour(Unarmoured())
character.add_languages(Language.ELVISH, Language.ORC)
character.add_equipment("Packed Lunch", "Ointment")
