from charsheets.classes import SorcererClockwork, TwinnedSpell, TransmutedSpell, HeightenedSpell, QuickenedSpell
from charsheets.constants import Skill, Stat
from charsheets.features import AbilityScoreImprovement, ShadowTouched
from charsheets.origins import Farmer
from charsheets.species import Tiefling, Legacy
from charsheets.spell import Spell
from charsheets.weapons import Sling, Spear

character = SorcererClockwork(
    "Selenor",
    Farmer(Stat.STRENGTH, Stat.CONSTITUTION, Stat.STRENGTH),
    Tiefling(Legacy.INFERNAL, Stat.CHARISMA),
    Skill.RELIGION,
    Skill.DECEPTION,
    strength=10,
    dexterity=13,
    constitution=14,
    intelligence=8,
    wisdom=12,
    charisma=15,
)

character.player_name = "zeta"
character.extras = {"hair": "none", "alignment": "LE", "skin": "scaly", "eyes": "yellow"}
character.level1()
character.level2(hp=5)
character.add_metamagic(TwinnedSpell(), TransmutedSpell())
character.level3(hp=6)
character.level4(hp=7, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA))
character.level5(hp=6)
character.level6(hp=3)
character.level7(hp=4)
character.level8(hp=6, feat=ShadowTouched(Spell.INFLICT_WOUNDS, Stat.CHARISMA))
character.level9(hp=4)
character.level10(hp=6)
character.add_metamagic(HeightenedSpell(), QuickenedSpell())
character.level11(hp=5)
character.level12(hp=7, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA))
character.level13(hp=5)


character.add_weapon(Sling())
character.add_weapon(Spear())
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Something Else")
