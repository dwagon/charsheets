#
from charsheets.armour import Plate, Shield
from charsheets.character import Character
from charsheets.classes import Fighter, FighterChampion
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.features import Interception, AbilityScoreImprovement, MagicInitiateCleric, GreatWeaponFighting, DefensiveDuelist
from charsheets.origins import Soldier
from charsheets.species import Human, Skillful, Versatile
from charsheets.spell import Spell
from charsheets.weapons import Maul

character = Character(
    "Impala the Impaler",
    Soldier(Stat.CONSTITUTION, Stat.STRENGTH, Stat.STRENGTH),
    Human(
        Skillful(Skill.ARCANA),
        Versatile(MagicInitiateCleric(Stat.WISDOM, Spell.SPARE_THE_DYING, Spell.LIGHT, Spell.CURE_WOUNDS)),
    ),
    Language.HALFLING,
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
character.fighter.fighting_style(Interception())
character.add_level(Fighter(hp=9))
character.add_level(FighterChampion(hp=7))
character.add_level(FighterChampion(hp=9, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
character.add_level(FighterChampion(hp=9))
character.add_level(FighterChampion(hp=8, feat=AbilityScoreImprovement(Stat.CONSTITUTION, Stat.CONSTITUTION)))
character.add_level(FighterChampion(hp=6, style=GreatWeaponFighting()))
character.add_level(FighterChampion(hp=8, feat=DefensiveDuelist()))
character.add_level(FighterChampion(hp=4))
character.add_level(FighterChampion(hp=5))
character.add_level(FighterChampion(hp=10))
character.add_level(FighterChampion(hp=8, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.INTELLIGENCE)))
character.add_level(FighterChampion(hp=5))

character.wear_armour(Plate(ac_bonus=1, name="+1 Plate"))
character.wear_shield(Shield())
character.add_weapon(Maul(atk_bonus=1, dmg_bonus=1, name="Maul +1"))
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# EOF
