from charsheets.armour import Leather
from charsheets.classes import DruidCircleOfTheLand
from charsheets.constants import Skill, Stat, Feat
from charsheets.origins import Noble
from charsheets.species import Elf
from charsheets.weapons import Dagger, Shortbow
from charsheets.abilities import Magician
from charsheets.feats import AbilityScoreImprovement

character = DruidCircleOfTheLand(
    "Tanika",
    Noble(Stat.INTELLIGENCE, Stat.CHARISMA, Stat.CHARISMA),
    Elf(),
    Skill.INSIGHT,
    Skill.PERCEPTION,
    strength=8,
    dexterity=12,
    constitution=14,
    intelligence=13,
    wisdom=15,
    charisma=10,
)
character.add_ability(Magician())
character.feats[Feat.SKILLED].set_skills(Skill.INVESTIGATION, Skill.ATHLETICS, Skill.PERCEPTION)  # type: ignore
character.extras = {"alignment": "N", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Alpha"
character.level2(hp=5)
character.level3(hp=6)
character.level4(hp=5, feat=AbilityScoreImprovement(Stat.WISDOM, Stat.WISDOM, character))
character.level5(hp=7)


character.add_weapon(Dagger())
character.add_weapon(Shortbow())
character.wear_armour(Leather())
character.shield = True
