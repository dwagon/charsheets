from charsheets.armour import Leather, Shield
from charsheets.classes import DruidCircleOfTheLand, Magician
from charsheets.constants import Skill, Stat, Language, Feature
from charsheets.features import AbilityScoreImprovement
from charsheets.origins import Noble
from charsheets.species import Elf, Lineages
from charsheets.weapons import Dagger, Shortbow

character = DruidCircleOfTheLand(
    "Tanika",
    Noble(Stat.INTELLIGENCE, Stat.CHARISMA, Stat.CHARISMA),
    Elf(Lineages.HIGH_ELF, Skill.SURVIVAL),
    Skill.INSIGHT,
    Skill.PERCEPTION,
    strength=8,
    dexterity=12,
    constitution=14,
    intelligence=13,
    wisdom=15,
    charisma=10,
)
character.add_feature(Magician())
character.find_feature(Feature.SKILLED).set_skills(Skill.INVESTIGATION, Skill.ATHLETICS, Skill.PERCEPTION)  # type: ignore
character.extras = {"alignment": "N", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Alpha"
character.level1()
character.level2(hp=5)
character.level3(hp=6)
character.level4(hp=5, feat=AbilityScoreImprovement(Stat.WISDOM, Stat.WISDOM))
character.level5(hp=7)
character.level6(hp=5)
character.level7(hp=5)
character.level8(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY))
character.level9(hp=4)


character.add_languages(Language.GNOMISH, Language.GIANT)
character.add_weapon(Dagger())
character.add_weapon(Shortbow())
character.wear_armour(Leather(ac_bonus=1, name="Sparkly Leather"))
character.wear_shield(Shield())
