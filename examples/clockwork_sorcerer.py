from charsheets.character import Character
from charsheets.classes import TwinnedSpell, TransmutedSpell, HeightenedSpell, QuickenedSpell, Sorcerer, SorcererClockwork
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, ShadowTouched
from charsheets.origins import Farmer
from charsheets.species import Tiefling, Legacy
from charsheets.spell import Spell
from charsheets.weapons import Sling, Spear

character = Character(
    "Selenor",
    Farmer(Stat.STRENGTH, Stat.CONSTITUTION, Stat.STRENGTH),
    Tiefling(Legacy.INFERNAL, Stat.CHARISMA),
    Language.ELVISH,
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
character.add_level(SorcererClockwork(hp=5))
character.sorcerer.add_metamagic(TwinnedSpell(), TransmutedSpell())
character.add_level(SorcererClockwork(hp=6))
character.add_level(SorcererClockwork(hp=7, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
character.add_level(SorcererClockwork(hp=6))
character.add_level(SorcererClockwork(hp=3))
character.add_level(SorcererClockwork(hp=4))
character.add_level(SorcererClockwork(hp=6, feat=ShadowTouched(Spell.INFLICT_WOUNDS, Stat.CHARISMA)))
character.add_level(SorcererClockwork(hp=4))
character.add_level(SorcererClockwork(hp=6))
character.sorcerer.add_metamagic(HeightenedSpell(), QuickenedSpell())
character.add_level(SorcererClockwork(hp=5))
character.add_level(SorcererClockwork(hp=7, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
character.add_level(SorcererClockwork(hp=5))


character.add_weapon(Sling())
character.add_weapon(Spear())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
