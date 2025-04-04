from charsheets.armour import Leather, Shield
from charsheets.character import Character
from charsheets.classes import Magician, Druid, DruidCircleOfTheSea
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Skilled, KeenMind
from charsheets.origins import Noble
from charsheets.species import Elf, Lineages
from charsheets.weapons import Dagger, Shortbow

character = Character(
    "Caeleophil",
    Noble(Stat.INTELLIGENCE, Stat.CHARISMA, Stat.CHARISMA, skilled=Skilled(Skill.INVESTIGATION, Skill.ATHLETICS, Skill.PERCEPTION)),
    Elf(Lineages.HIGH_ELF, Skill.SURVIVAL),
    Language.GNOMISH,
    Language.GIANT,
    strength=8,
    dexterity=12,
    constitution=14,
    intelligence=13,
    wisdom=15,
    charisma=10,
)
character.add_feature(Magician())
character.extras = {"alignment": "N", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Alpha"
character.add_level(Druid(skills=[Skill.INSIGHT, Skill.PERCEPTION]))
character.add_level(Druid(hp=5))
character.add_level(DruidCircleOfTheSea(hp=6))
character.add_level(DruidCircleOfTheSea(hp=5, feat=AbilityScoreImprovement(Stat.WISDOM, Stat.WISDOM)))
character.add_level(DruidCircleOfTheSea(hp=7))
character.add_level(DruidCircleOfTheSea(hp=5))
character.add_level(DruidCircleOfTheSea(hp=5))
character.add_level(DruidCircleOfTheSea(hp=5, feat=KeenMind(Skill.RELIGION)))
character.add_level(DruidCircleOfTheSea(hp=4))
character.add_level(DruidCircleOfTheSea(hp=6))
character.add_level(DruidCircleOfTheSea(hp=5))
character.add_level(DruidCircleOfTheSea(hp=5, feat=AbilityScoreImprovement(Stat.WISDOM, Stat.WISDOM)))
character.add_level(DruidCircleOfTheSea(hp=5))

character.add_weapon(Dagger())
character.add_weapon(Shortbow())
character.wear_armour(Leather(ac_bonus=1, name="Sparkly Leather"))
character.wear_shield(Shield())
