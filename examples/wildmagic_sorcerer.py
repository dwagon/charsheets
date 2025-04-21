from charsheets.character import Character
from charsheets.classes import DistantSpell, EmpoweredSpell, TransmutedSpell, SeekingSpell, Sorcerer, SorcererWildMagic
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Resilient, BoonOfDimensionalTravel
from charsheets.origins import Soldier
from charsheets.species import Tiefling, Legacy
from charsheets.weapons import Sling, Spear

character = Character(
    "Ephinox the Giggler",
    Soldier(Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION),
    Tiefling(Legacy.CHTHONIC, Stat.CHARISMA),
    Language.INFERNAL,
    Language.UNDERCOMMON,
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
character.add_level(Sorcerer(hp=5, add_metamagic=[DistantSpell(), EmpoweredSpell()]))
character.add_level(SorcererWildMagic(hp=6))
character.add_level(SorcererWildMagic(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
character.add_level(SorcererWildMagic(hp=6))
character.add_level(SorcererWildMagic(hp=3))
character.add_level(SorcererWildMagic(hp=4))
character.add_level(SorcererWildMagic(hp=7, feat=Resilient(Stat.CHARISMA)))
character.add_level(SorcererWildMagic(hp=4))
character.add_level(SorcererWildMagic(hp=6, add_metamagic=[TransmutedSpell(), SeekingSpell()]))
character.add_level(SorcererWildMagic(hp=5))
character.add_level(SorcererWildMagic(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
character.add_level(SorcererWildMagic(hp=5))
character.add_level(SorcererWildMagic(hp=5))
character.add_level(SorcererWildMagic(hp=5))
character.add_level(SorcererWildMagic(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
character.add_level(SorcererWildMagic(hp=5))
character.add_level(SorcererWildMagic(hp=5))
character.add_level(SorcererWildMagic(hp=5, boon=BoonOfDimensionalTravel(Stat.CHARISMA)))
character.add_level(SorcererWildMagic(hp=5))


character.add_weapon(Sling())
character.add_weapon(Spear())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
