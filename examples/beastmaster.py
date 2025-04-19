from charsheets.armour import Leather
from charsheets.character import Character
from charsheets.classes import RangerBeastMaster, DeftExplorer, Ranger
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Healer, Expertise, UnarmedFighting, MediumArmorMaster, BoonOfCombatProwess
from charsheets.origins import Entertainer
from charsheets.species import Human, Skillful, Versatile
from charsheets.weapons import Longbow, ShortSword

character = Character(
    "Dar",
    Entertainer(Stat.STRENGTH, Stat.DEXTERITY, Stat.CHARISMA),
    Human(Skillful(Skill.ANIMAL_HANDLING), Versatile(Healer())),
    Language.ELVISH,
    Language.HALFLING,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=8,
    wisdom=14,
    charisma=10,
)

character.player_name = "Gamma"
character.extras = {"hair": "patchy", "alignment": "LE"}
character.add_level(Ranger(skills=[Skill.INSIGHT, Skill.SURVIVAL, Skill.ANIMAL_HANDLING]))
character.add_level(Ranger(hp=5, deft=DeftExplorer(Language.ORC, Language.GOBLIN, Skill.MEDICINE), style=UnarmedFighting()))
character.add_level(RangerBeastMaster(hp=6))
character.add_level(RangerBeastMaster(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(RangerBeastMaster(hp=6))
character.add_level(RangerBeastMaster(hp=3))
character.add_level(RangerBeastMaster(hp=6))
character.add_level(RangerBeastMaster(hp=7, feat=MediumArmorMaster(Stat.DEXTERITY)))
character.add_level(RangerBeastMaster(hp=4, expertise=Expertise(Skill.SURVIVAL, Skill.PERCEPTION)))
character.add_level(RangerBeastMaster(hp=10))
character.add_level(RangerBeastMaster(hp=10))
character.add_level(RangerBeastMaster(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(RangerBeastMaster(hp=5))
character.add_level(RangerBeastMaster(hp=5))
character.add_level(RangerBeastMaster(hp=5))
character.add_level(RangerBeastMaster(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(RangerBeastMaster(hp=5))
character.add_level(RangerBeastMaster(hp=5))
character.add_level(RangerBeastMaster(hp=5, boon=BoonOfCombatProwess(Stat.STRENGTH)))
character.add_level(RangerBeastMaster(hp=5))


character.wear_armour(Leather())
character.add_weapon(Longbow())
character.add_weapon(ShortSword())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
