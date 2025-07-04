from charsheets.armour import Leather, Shield
from charsheets.character import Character
from charsheets.classes import DruidCircleOfTheMoon, Magician, Druid
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Skilled
from charsheets.origins import Noble
from charsheets.species import Elf, Lineages
from charsheets.weapons import Dagger, Scimitar
from charsheets.weapons.homebrew import Featherlight

character = Character(
    "Tanika",
    Noble(Stat.STRENGTH, Stat.INTELLIGENCE, Stat.CHARISMA, skilled=Skilled(Skill.NATURE, Skill.HISTORY, Skill.PERSUASION)),
    Elf(Lineages.HIGH_ELF, Skill.INSIGHT, Stat.WISDOM),
    Language.ELVISH,
    Language.UNDERCOMMON,
    strength=10,
    dexterity=8,
    constitution=13,
    intelligence=12,
    wisdom=15,
    charisma=14,
    player_name="Alyce",
)
character.extras = {"alignment": "N", "image": "characters/images/tanika.png"}
character.add_level(Druid(skills=[Skill.ANIMAL_HANDLING, Skill.MEDICINE], primal=Magician()))
character.add_level(Druid(hp=6))
character.add_level(DruidCircleOfTheMoon(hp=4))
character.add_level(DruidCircleOfTheMoon(hp=8, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.WISDOM)))
character.add_level(DruidCircleOfTheMoon(hp=6))

character.add_weapon(Dagger())
character.add_weapon(Featherlight())
character.wear_armour(Leather())
character.wear_shield(Shield())

# Featherlight - Guiding (White light), Proficient (Acrobatics)
