from charsheets.character import Character
from charsheets.classes import SorcererAberrant, ExtendedSpell, HeightenedSpell, EmpoweredSpell, TwinnedSpell, Sorcerer
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, MartialWeaponTraining
from charsheets.origins import Wayfairer
from charsheets.species import Tiefling, Legacy
from charsheets.weapons import Sling, Spear

character = Character(
    "Goff the Weird",
    Wayfairer(Stat.WISDOM, Stat.DEXTERITY, Stat.CHARISMA),
    Tiefling(Legacy.ABYSSAL, Stat.INTELLIGENCE),
    Language.ORC,
    Language.HALFLING,
    strength=10,
    dexterity=13,
    constitution=14,
    intelligence=8,
    wisdom=12,
    charisma=15,
)

character.player_name = "zeta"
character.extras = {"hair": "none", "alignment": "LE", "skin": "scaly", "eyes": "yellow"}
character.add_level(Sorcerer(skills=[Skill.RELIGION, Skill.DECEPTION]))
character.add_level(Sorcerer(hp=5))
character.sorcerer.add_metamagic(ExtendedSpell(), HeightenedSpell())
character.add_level(SorcererAberrant(hp=6))
character.add_level(SorcererAberrant(hp=7, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY)))
character.add_level(SorcererAberrant(hp=6))
character.add_level(SorcererAberrant(hp=3))
character.add_level(SorcererAberrant(hp=4))
character.add_level(SorcererAberrant(hp=7, feat=MartialWeaponTraining(Stat.DEXTERITY)))
character.add_level(SorcererAberrant(hp=4))
character.add_level(SorcererAberrant(hp=6))
character.sorcerer.add_metamagic(EmpoweredSpell(), TwinnedSpell())
character.add_level(SorcererAberrant(hp=5))
character.add_level(SorcererAberrant(hp=7, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.INTELLIGENCE)))
character.add_level(SorcererAberrant(hp=5))

character.add_weapon(Sling())
character.add_weapon(Spear())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
