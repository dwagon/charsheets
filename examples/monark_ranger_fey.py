from charsheets.armour import Leather
from charsheets.classes import RangerFeyWanderer, DeftExplorer
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Tough, Expertise, MagicInitiateDruid, Archery, ShieldMaster
from charsheets.origins import Guide
from charsheets.species import Human, Skillful, Versatile
from charsheets.spell import Spell
from charsheets.weapons import Longbow, ShortSword

character = RangerFeyWanderer(
    "Monark",
    Guide(
        Stat.DEXTERITY,
        Stat.CONSTITUTION,
        Stat.WISDOM,
        initiate=MagicInitiateDruid(Stat.WISDOM, Spell.MESSAGE, Spell.SPARE_THE_DYING, Spell.SPEAK_WITH_ANIMALS),
    ),
    Human(Skillful(Skill.ANIMAL_HANDLING), Versatile(Tough())),
    Skill.INSIGHT,
    Skill.SURVIVAL,
    Skill.ANIMAL_HANDLING,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=8,
    wisdom=14,
    charisma=10,
)

character.player_name = "Gamma"
character.extras = {"hair": "patchy", "alignment": "LE"}
character.level1()
character.level2(hp=5, deft=DeftExplorer(Language.ABYSSAL, Language.DEEP_SPEECH, Skill.MEDICINE), style=Archery())
character.level3(hp=6)
character.level4(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION))
character.level5(hp=6)
character.level6(hp=3)
character.level7(hp=6)
character.level8(hp=7, feat=ShieldMaster())
character.level9(hp=4, expertise=Expertise(Skill.SURVIVAL, Skill.PERCEPTION))
character.level10(hp=10)
character.level11(hp=10)

character.wear_armour(Leather())
character.add_weapon(Longbow())
character.add_weapon(ShortSword())
character.add_languages(Language.ELVISH, Language.HALFLING)
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
