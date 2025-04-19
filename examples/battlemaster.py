#
from charsheets.armour import Ring, Shield
from charsheets.character import Character
from charsheets.classes import Ambush, ManeuveringAttack, FeintingAttack, FighterBattleMaster, Fighter, StudentOfWar
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.features import TwoWeaponFighting, AbilityScoreImprovement, DualWielder, Durable, BoonOfCombatProwess
from charsheets.origins import Sailor
from charsheets.species import Goliath, GiantsAncestry
from charsheets.weapons import Greatsword, Musket

character = Character(
    "Yercana",
    Sailor(Stat.STRENGTH, Stat.STRENGTH, Stat.DEXTERITY),
    Goliath(GiantsAncestry.HILL_GIANT),
    Language.GIANT,
    Language.DWARVISH,
    strength=16,
    dexterity=14,
    constitution=13,
    intelligence=8,
    wisdom=10,
    charisma=12,
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
character.add_level(Fighter(skills=[Skill.ACROBATICS, Skill.INSIGHT], style=TwoWeaponFighting()))
character.add_level(Fighter(hp=9))
character.add_level(
    FighterBattleMaster(
        hp=7,
        student=StudentOfWar(Tool.SMITHS_TOOLS, Skill.PERSUASION),
        add_maneuver=[Ambush(), ManeuveringAttack(), FeintingAttack()],
    )
)
character.add_level(FighterBattleMaster(hp=9, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
character.add_level(FighterBattleMaster(hp=9))
character.add_level(FighterBattleMaster(hp=8, feat=Durable()))
character.add_level(FighterBattleMaster(hp=6))
character.add_level(FighterBattleMaster(hp=8, feat=DualWielder(Stat.STRENGTH)))
character.add_level(FighterBattleMaster(hp=4))
character.add_level(FighterBattleMaster(hp=5))
character.add_level(FighterBattleMaster(hp=10))
character.add_level(FighterBattleMaster(hp=9, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(FighterBattleMaster(hp=5))
character.add_level(FighterBattleMaster(hp=9, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(FighterBattleMaster(hp=5))
character.add_level(FighterBattleMaster(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(FighterBattleMaster(hp=5))
character.add_level(FighterBattleMaster(hp=5))
character.add_level(FighterBattleMaster(hp=5, boon=BoonOfCombatProwess(Stat.STRENGTH)))
character.add_level(FighterBattleMaster(hp=5))

character.wear_armour(Ring())
character.wear_shield(Shield())
character.add_weapon(Greatsword(atk_bonus=2, dmg_bonus=1, name="Manic Attack"))
character.add_weapon(Musket(atk_bonus=1, dmg_bonus=1, name="Musket +1"))

character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# EOF
