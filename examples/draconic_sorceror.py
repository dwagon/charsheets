from charsheets.character import Character
from charsheets.classes import (
    ElementalAffinity,
    QuickenedSpell,
    CarefulSpell,
    DistantSpell,
    SubtleSpell,
    Sorcerer,
    SorcererDraconic,
)
from charsheets.constants import Skill, Stat, DamageType, Language
from charsheets.features import AbilityScoreImprovement, Sentinel
from charsheets.origins import Sailor
from charsheets.species import Tiefling, Legacy
from charsheets.weapons import Sling, Spear

character = Character(
    "Selenor",
    Sailor(Stat.STRENGTH, Stat.DEXTERITY, Stat.STRENGTH),
    Tiefling(Legacy.INFERNAL, Stat.CHARISMA),
    Language.UNDERCOMMON,
    Language.GIANT,
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
character.sorcerer.add_metamagic(CarefulSpell(), QuickenedSpell())
character.add_level(SorcererDraconic(hp=6))
character.add_level(SorcererDraconic(hp=7, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
character.add_level(SorcererDraconic(hp=6))
character.add_level(SorcererDraconic(hp=3, feat=ElementalAffinity(DamageType.POISON)))
character.add_level(SorcererDraconic(hp=4))
character.add_level(SorcererDraconic(hp=7, feat=Sentinel(Stat.STRENGTH)))
character.add_level(SorcererDraconic(hp=4))
character.add_level(SorcererDraconic(hp=6))
character.sorcerer.add_metamagic(DistantSpell(), SubtleSpell())
character.add_level(SorcererDraconic(hp=5))
character.add_level(SorcererDraconic(hp=7, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
character.add_level(SorcererDraconic(hp=5))


character.add_weapon(Sling())
character.add_weapon(Spear())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
