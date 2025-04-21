#
from charsheets.armour import Ring, Shield
from charsheets.character import Character
from charsheets.classes import Fighter, FighterEldritchKnight
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.features import Interception, AbilityScoreImprovement, CrossbowExpert, Crusher, BoonOfCombatProwess
from charsheets.origins import Criminal
from charsheets.species import Orc
from charsheets.spell import Spell
from charsheets.weapons import Longsword

character = Character(
    "Freya",
    Criminal(Stat.CONSTITUTION, Stat.CONSTITUTION, Stat.INTELLIGENCE),
    Orc(),
    Language.GIANT,
    Language.DWARVISH,
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
character.add_level(Fighter(skills=[Skill.ACROBATICS, Skill.INSIGHT], style=Interception()))
character.add_level(Fighter(hp=9))
character.add_level(FighterEldritchKnight(hp=7))
character.learn_spell(Spell.FIRE_BOLT, Spell.TRUE_STRIKE, Spell.MAGIC_MISSILE, Spell.IDENTIFY, Spell.BURNING_HANDS)
character.prepare_spells(Spell.MAGIC_MISSILE, Spell.IDENTIFY)
character.add_level(FighterEldritchKnight(hp=9, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.INTELLIGENCE)))
character.add_level(FighterEldritchKnight(hp=9))
character.learn_spell(Spell.SLEEP)
character.add_level(FighterEldritchKnight(hp=8, feat=CrossbowExpert()))
character.add_level(FighterEldritchKnight(hp=6))
character.add_level(FighterEldritchKnight(hp=8, feat=Crusher(Stat.CONSTITUTION)))
character.add_level(FighterEldritchKnight(hp=4))
character.add_level(FighterEldritchKnight(hp=5))
character.learn_spell(Spell.SPIDER_CLIMB, Spell.MAGIC_WEAPON, Spell.MELFS_ACID_ARROW)
character.prepare_spells(Spell.SPIDER_CLIMB, Spell.MAGIC_WEAPON)
character.add_level(FighterEldritchKnight(hp=10))
character.add_level(FighterEldritchKnight(hp=9, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
character.add_level(FighterEldritchKnight(hp=5))
character.add_level(FighterEldritchKnight(hp=5, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
character.add_level(FighterEldritchKnight(hp=5))
character.add_level(FighterEldritchKnight(hp=5, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.INTELLIGENCE)))
character.add_level(FighterEldritchKnight(hp=5))
character.add_level(FighterEldritchKnight(hp=5))
character.add_level(FighterEldritchKnight(hp=5, boon=BoonOfCombatProwess(Stat.STRENGTH)))
character.add_level(FighterEldritchKnight(hp=5))


character.wear_armour(Ring())
character.wear_shield(Shield())
character.add_weapon(Longsword(atk_bonus=1, dmg_bonus=1, name="Longsword +1"))
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# EOF
