from charsheets.armour import Leather
from charsheets.classes import RangerHunter, DeftExplorer, DruidicWarrior
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Expertise, Archery, Observant
from charsheets.origins import Guard
from charsheets.species import Human, Skillful, Versatile
from charsheets.spell import Spell
from charsheets.weapons import Longbow, ShortSword

character = RangerHunter(
    "Monark",
    Guard(Stat.STRENGTH, Stat.STRENGTH, Stat.WISDOM),
    Human(Skillful(Skill.ANIMAL_HANDLING), Versatile(Archery())),
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
character.level2(
    hp=5,
    deft=DeftExplorer(Language.ORC, Language.GOBLIN, Skill.NATURE),
    style=DruidicWarrior(Spell.DRUIDCRAFT, Spell.SPARE_THE_DYING),
)
character.level3(hp=6)
character.level4(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION))
character.level5(hp=6)
character.level6(hp=3)
character.level7(hp=6)
character.level8(hp=7, feat=Observant(Skill.INVESTIGATION, Stat.INTELLIGENCE))
character.level9(hp=4, expertise=Expertise(Skill.SURVIVAL, Skill.PERCEPTION))
character.level10(hp=10)
character.level11(hp=10)

character.wear_armour(Leather())
character.add_weapon(Longbow())
character.add_weapon(ShortSword())
character.add_languages(Language.ELVISH, Language.HALFLING)
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
