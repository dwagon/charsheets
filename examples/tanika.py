from charsheets.armour import Leather, Shield
from charsheets.classes import DruidCircleOfTheMoon, Magician
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Skilled
from charsheets.origins import Noble
from charsheets.species import Elf, Lineages
from charsheets.weapons import Dagger, Scimitar

character = DruidCircleOfTheMoon(
    "Tanika",
    Noble(Stat.STRENGTH, Stat.INTELLIGENCE, Stat.CHARISMA, skilled=Skilled(Skill.NATURE, Skill.HISTORY, Skill.PERSUASION)),
    Elf(Lineages.HIGH_ELF, Skill.INSIGHT),
    Skill.ANIMAL_HANDLING,
    Skill.MEDICINE,
    strength=10,
    dexterity=8,
    constitution=13,
    intelligence=12,
    wisdom=15,
    charisma=14,
)
character.add_feature(Magician())
character.extras = {"alignment": "N", "image": "characters/images/tanika.png"}
character.player_name = "Alyce"
character.level1()
character.level2(hp=6)
character.level3(hp=4)
character.level4(hp=8, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.WISDOM))


character.add_languages(Language.ELVISH, Language.UNDERCOMMON)
character.add_weapon(Dagger())
character.add_weapon(Scimitar())
character.wear_armour(Leather())
character.wear_shield(Shield())
