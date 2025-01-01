from charsheets.classes import CircleOfTheLandDruid, Magician
from charsheets.constants import Weapon, Armour, Skill, Stat, Feat
from charsheets.origins import Noble
from charsheets.species.elf import Elf
from charsheets.weapons import Dagger, Shortbow


class Tanika(Magician, CircleOfTheLandDruid):
    pass


character = Tanika(
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
character.feats[Feat.SKILLED].set_skills(Skill.INVESTIGATION, Skill.ATHLETICS, Skill.PERCEPTION)  # type: ignore
character.extras = {"alignment": "N", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Alpha"
character.level2(hp=5)
character.level3(hp=6)
character.level4(hp=5)


character.add_weapon(Dagger(character))
character.add_weapon(Shortbow(character))
character.armour = Armour.LEATHER
character.shield = True
