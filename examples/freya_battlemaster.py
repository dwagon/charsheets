#
from charsheets.armour import Ring
from charsheets.classes import FighterBattleMaster, Ambush, ManeuveringAttack, FeintingAttack
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.abilities import TwoWeaponFighting, AbilityScoreImprovement
from charsheets.origins import Sailor
from charsheets.species import Goliath, GiantsAncestry
from charsheets.weapons import Greatsword, Musket

character = FighterBattleMaster(
    "Freya",
    Sailor(Stat.STRENGTH, Stat.STRENGTH, Stat.DEXTERITY),
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
character.fighting_style(TwoWeaponFighting())
character.level2(hp=9)
character.level3(hp=7)
character.add_maneuver(Ambush(), ManeuveringAttack(), FeintingAttack())
character.level4(hp=9, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION))
character.level5(hp=9)
character.level6(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY))


character.wear_armour(Ring())
character.shield = False
character.add_weapon(Greatsword(atk_bonus=2, dmg_bonus=1, name="Manic Attack"))
character.add_weapon(Musket(atk_bonus=1, dmg_bonus=1, name="Musket +1"))

character.add_languages(Language.GIANT, Language.DWARVISH)
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# EOF
