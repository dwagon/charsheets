from charsheets.armour import Studded
from charsheets.classes import RogueSoulknife
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Expertise
from charsheets.origins import Entertainer
from charsheets.species import Orc
from charsheets.weapons import Rapier, Shortbow

character = RogueSoulknife(
    "Aradim",
    Entertainer(Stat.DEXTERITY, Stat.DEXTERITY, Stat.CHARISMA),
    Orc(),
    Skill.SLEIGHT_OF_HAND,
    Skill.STEALTH,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=10,
    charisma=8,
)
character.extras = {"alignment": "CN", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Phi"
character.level1(language=Language.DEEP_SPEECH, expertise=Expertise(Skill.STEALTH, Skill.HISTORY))
character.level2(hp=5)
character.level3(hp=6)
character.level4(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA))
character.level5(hp=6)
character.level6(hp=4, expertise=Expertise(Skill.ACROBATICS, Skill.SLEIGHT_OF_HAND))
character.level7(hp=4)
character.level8(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA))
character.level9(hp=4)
character.level10(hp=6, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION))


character.add_languages(Language.DWARVISH, Language.ORC)
character.add_weapon(Rapier(atk_bonus=1, dmg_bonus=1, name="Pointy End"))
character.add_weapon(Shortbow())
character.wear_armour(Studded(ac_bonus=1, name="Glamour"))
