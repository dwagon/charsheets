#
from charsheets.features import UnarmedFighting, AbilityScoreImprovement
from charsheets.armour import Ring
from charsheets.classes import FighterPsiWarrior
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.origins import Criminal
from charsheets.species import Goliath, GiantsAncestry
from charsheets.weapons import Maul

character = FighterPsiWarrior(
    "Freya",
    Criminal(Stat.CONSTITUTION, Stat.CONSTITUTION, Stat.INTELLIGENCE),
    Goliath(GiantsAncestry.HILL_GIANT),
    Skill.ACROBATICS,
    Skill.INSIGHT,
    strength=16,
    dexterity=14,
    constitution=13,
    intelligence=8,
    wisdom=10,
    charisma=12,
    student_tool=Tool.SMITHS_TOOLS,
    student_skill=Skill.PERSUASION,
)
character.player_name = "Delta"
character.extras = {
    "eyes": "yellow",
    "hair": "purple",
    "height": "7'5",
    "alignment": "CN",
    "image": "characters/images/freya.png",
    "age": "20",
    "skin": "yes",
}
character.fighting_style(UnarmedFighting())
character.level2(hp=9)
character.level3(hp=7)
character.level4(hp=9, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.INTELLIGENCE))
character.level5(hp=9)
character.level6(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION))
character.level7(hp=6)
character.level8(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION))


character.wear_armour(Ring())
character.add_weapon(Maul(atk_bonus=1, dmg_bonus=1, name="Maul +1"))
character.add_languages(Language.GIANT, Language.DWARVISH)
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# EOF
