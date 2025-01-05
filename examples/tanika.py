from charsheets.armour import Leather
from charsheets.classes import CircleOfTheLandDruid
from charsheets.constants import Skill, Stat, Feat
from charsheets.origins import Noble
from charsheets.species import Elf
from charsheets.weapons import Dagger, Shortbow
from charsheets.abilities import Magician


character = CircleOfTheLandDruid(
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
character.level4(hp=5)


character.add_weapon(Dagger())
character.add_weapon(Shortbow())
character.armour = Leather(character)
character.shield = True
