from charsheets.armour import Leather, Shield
from charsheets.character import Character
from charsheets.classes import Magician, Druid, DruidCircleOfTheMoon
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Skilled, SkillExpert
from charsheets.origins import Noble
from charsheets.species import Elf, Lineages
from charsheets.weapons import Dagger, Shortbow

character = Character(
    "Selue the Spacey",
    Noble(Stat.INTELLIGENCE, Stat.CHARISMA, Stat.CHARISMA, skilled=Skilled(Skill.INVESTIGATION, Skill.ATHLETICS, Skill.PERCEPTION)),
    Elf(Lineages.HIGH_ELF, Skill.SURVIVAL, Stat.CHARISMA),
    Language.GNOMISH,
    Language.GIANT,
    strength=8,
    dexterity=12,
    constitution=14,
    intelligence=13,
    wisdom=15,
    charisma=10,
    player_name="Alpha",
)
character.extras = {"alignment": "N", "image": "characters/images/aaliyah.jpg"}
character.add_level(Druid(skills=[Skill.INSIGHT, Skill.PERCEPTION], primal=Magician()))
character.add_level(Druid(hp=5))
character.add_level(DruidCircleOfTheMoon(hp=6))
character.add_level(DruidCircleOfTheMoon(hp=5, feat=AbilityScoreImprovement(Stat.WISDOM, Stat.WISDOM)))
character.add_level(DruidCircleOfTheMoon(hp=7))
character.add_level(DruidCircleOfTheMoon(hp=5))
character.add_level(DruidCircleOfTheMoon(hp=5))
character.add_level(DruidCircleOfTheMoon(hp=5, feat=SkillExpert(Skill.NATURE, Skill.SURVIVAL, Stat.CHARISMA)))
character.add_level(DruidCircleOfTheMoon(hp=4))
character.add_level(DruidCircleOfTheMoon(hp=6))
character.add_level(DruidCircleOfTheMoon(hp=5))
character.add_level(DruidCircleOfTheMoon(hp=5, feat=AbilityScoreImprovement(Stat.WISDOM, Stat.WISDOM)))
character.add_level(DruidCircleOfTheMoon(hp=5))

character.add_weapon(Dagger())
character.add_weapon(Shortbow())
character.wear_armour(Leather(ac_bonus=1, name="Sparkly Leather"))
character.wear_shield(Shield())
