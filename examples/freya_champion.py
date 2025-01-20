#
from charsheets.abilities import Interception, AbilityScoreImprovement, MagicInitiateCleric, GreatWeaponFighting
from charsheets.armour import Plate, Shield
from charsheets.classes import FighterChampion
from charsheets.constants import Skill, Stat, Tool, Language
from charsheets.origins import Soldier
from charsheets.species import Human, Skillful, Versatile
from charsheets.spell import Spell
from charsheets.weapons import Maul

character = FighterChampion(
    "Freya",
    Soldier(Stat.CONSTITUTION, Stat.STRENGTH, Stat.STRENGTH),
    Human(
        Skillful(Skill.ARCANA),
        Versatile(MagicInitiateCleric(Stat.WISDOM, Spell.SPARE_THE_DYING, Spell.LIGHT, Spell.CURE_WOUNDS)),
    ),
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
character.level4(hp=9, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH))
character.level5(hp=9)
character.level6(hp=8, feat=AbilityScoreImprovement(Stat.CONSTITUTION, Stat.CONSTITUTION))
character.level7(hp=6, style=GreatWeaponFighting())


character.wear_armour(Plate(ac_bonus=1, name="+1 Plate"))
character.wear_shield(Shield())
character.add_weapon(Maul(atk_bonus=1, dmg_bonus=1, name="Maul +1"))
character.add_languages(Language.HALFLING, Language.DWARVISH)
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# EOF
