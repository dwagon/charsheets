from charsheets.armour import Leather
from charsheets.character import Character
from charsheets.classes import RangerHunter, DeftExplorer, DruidicWarrior, Ranger
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Expertise, Archery, Observant, Lucky
from charsheets.origins import Guard
from charsheets.species import Human, Skillful, Versatile
from charsheets.spell import Spell
from charsheets.weapons import Longbow, Dagger

character = Character(
    "Monark",
    Guard(Stat.STRENGTH, Stat.STRENGTH, Stat.INTELLIGENCE),
    Human(Skillful(Skill.INVESTIGATION), Versatile(Lucky())),
    Language.ELVISH,
    Language.HALFLING,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=8,
    wisdom=14,
    charisma=10,
)

character.player_name = "Gary"
character.extras = {"hair": "patchy", "alignment": "LE"}
character.add_level(Ranger(skills=[Skill.ATHLETICS, Skill.PERCEPTION, Skill.NATURE]))
character.add_level(
    Ranger(
        hp=10,
        deft=DeftExplorer(Language.ORC, Language.GOBLIN, Skill.PERCEPTION),
        style=DruidicWarrior(Spell.STARRY_WISP, Spell.RESISTANCE),
    )
)
character.add_level(RangerHunter(hp=10))
character.add_level(RangerHunter(hp=9, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(RangerHunter(hp=6))  # Level 5

character.wear_armour(Leather())
character.add_weapon(Longbow())
character.add_weapon(Dagger())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")

character.add_level(RangerHunter(hp=3))
