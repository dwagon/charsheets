from charsheets.armour import Leather
from charsheets.character import Character
from charsheets.classes.ranger import Ranger, DeftExplorer, DruidicWarrior, RangerHunter
from charsheets.constants import Stat, Skill, Language
from charsheets.features import Archery, AbilityScoreImprovement, Observant, Expertise
from charsheets.origins import Guard
from charsheets.species import Human, Skillful, Versatile
from charsheets.spell import Spell
from charsheets.weapons import Longbow, ShortSword

character = Character(
    "Gregory",
    Guard(Stat.STRENGTH, Stat.STRENGTH, Stat.WISDOM),
    Human(Skillful(Skill.ANIMAL_HANDLING), Versatile(Archery())),
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
character.add_level(
    Ranger(
        hp=5,
        deft=DeftExplorer(Language.ORC, Language.GOBLIN, Skill.NATURE),
        style=DruidicWarrior(Spell.DRUIDCRAFT, Spell.SPARE_THE_DYING),
    )
)
character.add_level(RangerHunter(hp=6))  # Level 3
character.add_level(RangerHunter(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))  # Level 4
character.add_level(RangerHunter(hp=6))  # Level 5
character.add_level(RangerHunter(hp=3))  # Level 6
character.add_level(RangerHunter(hp=6))  # Level 7
character.add_level(RangerHunter(hp=7, feat=Observant(Skill.INVESTIGATION, Stat.INTELLIGENCE)))  # Level 8
character.add_level(RangerHunter(hp=4, expertise=Expertise(Skill.SURVIVAL, Skill.PERCEPTION)))  # Level 9
character.add_level(RangerHunter(hp=10))  # Level 10
character.add_level(RangerHunter(hp=10))  # Level 11
character.add_level(RangerHunter(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))  # Level 12
character.add_level(RangerHunter(hp=5))  # Level 13

character.wear_armour(Leather())
character.add_weapon(Longbow())
character.add_weapon(ShortSword())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
