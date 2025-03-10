from charsheets.armour import Leather
from charsheets.classes import RangerHunter, DeftExplorer, DruidicWarrior
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Expertise, Archery, Observant, Lucky
from charsheets.origins import Guard
from charsheets.species import Human, Skillful, Versatile
from charsheets.spell import Spell
from charsheets.weapons import Longbow, Dagger

character = RangerHunter(
    "Monark",
    Guard(Stat.STRENGTH, Stat.STRENGTH, Stat.INTELLIGENCE),
    Human(Skillful(Skill.INVESTIGATION), Versatile(Lucky())),
    Skill.ATHLETICS,
    Skill.PERCEPTION,
    Skill.NATURE,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=8,
    wisdom=14,
    charisma=10,
)

character.player_name = "Gary"
character.extras = {"hair": "patchy", "alignment": "LE"}
character.level1()
character.level2(
    hp=10,
    deft=DeftExplorer(Language.ORC, Language.GOBLIN, Skill.PERCEPTION),
    style=DruidicWarrior(Spell.STARRY_WISP, Spell.RESISTANCE),
)
character.level3(hp=10)
character.level4(hp=9, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION))


character.wear_armour(Leather())
character.add_weapon(Longbow())
character.add_weapon(Dagger())
character.add_languages(Language.ELVISH, Language.HALFLING)
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
