#
from charsheets.features import Interception, AbilityScoreImprovement
from charsheets.armour import Ring, Shield
from charsheets.classes import FighterEldritchKnight
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.origins import Criminal
from charsheets.species import Orc
from charsheets.spell import Spell
from charsheets.weapons import Longsword

character = FighterEldritchKnight(
    "Freya",
    Criminal(Stat.CONSTITUTION, Stat.CONSTITUTION, Stat.INTELLIGENCE),
    Orc(),
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
character.fighting_style(Interception())
character.level2(hp=9)
character.level3(hp=7)
character.learn_spell(Spell.FIRE_BOLT, Spell.TRUE_STRIKE, Spell.MAGIC_MISSILE, Spell.IDENTIFY, Spell.BURNING_HANDS)
character.prepare_spells(Spell.MAGIC_MISSILE, Spell.IDENTIFY)
character.level4(hp=9, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.INTELLIGENCE))
character.level5(hp=9)
character.learn_spell(Spell.SLEEP)
character.level6(hp=8, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.CONSTITUTION))
character.level7(hp=6)


character.wear_armour(Ring())
character.wear_shield(Shield())
character.add_weapon(Longsword(atk_bonus=1, dmg_bonus=1, name="Longsword +1"))
character.add_languages(Language.GIANT, Language.DWARVISH)
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# EOF
