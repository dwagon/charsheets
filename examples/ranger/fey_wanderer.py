from charsheets.armour import Leather
from charsheets.character import Character
from charsheets.classes import DeftExplorer, Ranger, RangerFeyWanderer
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Tough, Expertise, MagicInitiateDruid, Archery, ShieldMaster, BoonOfFate
from charsheets.items import ManualOfBodilyHealth
from charsheets.origins import Guide
from charsheets.species import Human, Skillful, Versatile
from charsheets.spell import Spell
from charsheets.weapons import Longbow, ShortSword

character = Character(
    "Geoffrey",
    Guide(
        Stat.DEXTERITY,
        Stat.CONSTITUTION,
        Stat.WISDOM,
        initiate=MagicInitiateDruid(Stat.WISDOM, Spell.MESSAGE, Spell.SPARE_THE_DYING, Spell.SPEAK_WITH_ANIMALS),
    ),
    Human(Skillful(Skill.ANIMAL_HANDLING), Versatile(Tough())),
    Language.ELVISH,
    Language.HALFLING,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=8,
    wisdom=14,
    charisma=10,
    player_name="Gamma",
)

character.extras = {"hair": "patchy", "alignment": "LE"}
character.add_level(Ranger(skills=[Skill.INSIGHT, Skill.SURVIVAL, Skill.ANIMAL_HANDLING]))
character.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ABYSSAL, Language.DEEP_SPEECH, Skill.MEDICINE), style=Archery()))
character.add_level(RangerFeyWanderer(hp=6))
character.add_level(RangerFeyWanderer(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
character.add_level(RangerFeyWanderer(hp=6))
character.add_level(RangerFeyWanderer(hp=3))
character.add_level(RangerFeyWanderer(hp=6))
character.add_level(RangerFeyWanderer(hp=7, feat=ShieldMaster()))
character.add_level(RangerFeyWanderer(hp=4, expertise=Expertise(Skill.SURVIVAL, Skill.PERCEPTION)))
character.add_level(RangerFeyWanderer(hp=10))
character.add_level(RangerFeyWanderer(hp=10))
character.add_level(RangerFeyWanderer(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(RangerFeyWanderer(hp=5))
character.add_level(RangerFeyWanderer(hp=5))
character.add_level(RangerFeyWanderer(hp=5))
character.add_level(RangerFeyWanderer(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(RangerFeyWanderer(hp=5))
character.add_level(RangerFeyWanderer(hp=5))
character.add_level(RangerFeyWanderer(hp=5, boon=BoonOfFate(Stat.DEXTERITY)))
character.add_level(RangerFeyWanderer(hp=5))
character.use_item(ManualOfBodilyHealth())

character.wear_armour(Leather())
character.add_weapon(Longbow())
character.add_weapon(ShortSword())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
