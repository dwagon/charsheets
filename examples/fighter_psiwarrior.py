#
from charsheets.armour import Ring
from charsheets.character import Character
from charsheets.classes import Fighter, FighterPsiWarrior
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.features import UnarmedFighting, AbilityScoreImprovement, MageSlayer
from charsheets.origins import Criminal
from charsheets.species import Goliath, GiantsAncestry
from charsheets.weapons import Maul

character = Character(
    "Freya",
    Criminal(Stat.CONSTITUTION, Stat.CONSTITUTION, Stat.INTELLIGENCE),
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
character.add_level(Fighter(skills=[Skill.ACROBATICS, Skill.INSIGHT]))
character.fighter.fighting_style(UnarmedFighting())

character.add_level(Fighter(hp=9))
character.add_level(FighterPsiWarrior(hp=7))
character.add_level(FighterPsiWarrior(hp=9, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.INTELLIGENCE)))
character.add_level(FighterPsiWarrior(hp=9))
character.add_level(FighterPsiWarrior(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
character.add_level(FighterPsiWarrior(hp=6))
character.add_level(FighterPsiWarrior(hp=8, feat=MageSlayer(Stat.STRENGTH)))
character.add_level(FighterPsiWarrior(hp=4))
character.add_level(FighterPsiWarrior(hp=5))
character.add_level(FighterPsiWarrior(hp=10))
character.add_level(FighterPsiWarrior(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
character.add_level(FighterPsiWarrior(hp=5))

character.wear_armour(Ring())
character.add_weapon(Maul(atk_bonus=1, dmg_bonus=1, name="Maul +1"))
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# EOF
