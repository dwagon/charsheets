from charsheets.character import Character
from charsheets.classes import MysticArcanum, Warlock, WarlockOldOne
from charsheets.classes.warlock import AgonizingBlast, ArmorOfShadows, EldritchSpear
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, MagicInitiateCleric, WarCaster
from charsheets.origins import Acolyte
from charsheets.species.homebrew.kuatoa import Kuatoa
from charsheets.spell import Spell

character = Character(
    "Kanaat",
    Acolyte(
        Stat.CHARISMA,
        Stat.CHARISMA,
        Stat.CHARISMA,
        MagicInitiateCleric(Stat.CHARISMA, Spell.SPARE_THE_DYING, Spell.THAUMATURGY, Spell.CURE_WOUNDS),
    ),
    Kuatoa(),
    Language.GOBLIN,
    Language.UNDERCOMMON,
    strength=8,
    dexterity=14,
    constitution=13,
    intelligence=12,
    wisdom=10,
    charisma=15,
)
character.player_name = "Delta"
character.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION], add_invocation=AgonizingBlast(Spell.ELDRITCH_BLAST)))
character.add_level(Warlock(hp=4, add_invocation=[ArmorOfShadows(), EldritchSpear(Spell.ELDRITCH_BLAST)]))
character.add_level(WarlockOldOne(hp=6))
character.add_level(WarlockOldOne(hp=3, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY)))
character.add_level(WarlockOldOne(hp=6))
character.add_level(WarlockOldOne(hp=4))
character.add_level(WarlockOldOne(hp=4))
character.add_level(WarlockOldOne(hp=3, feat=WarCaster(Stat.CHARISMA)))
character.add_level(WarlockOldOne(hp=4))
character.add_level(WarlockOldOne(hp=4))
character.add_level(WarlockOldOne(hp=5, mystic=MysticArcanum(Spell.ARCANE_GATE)))
character.add_level(WarlockOldOne(hp=6, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CONSTITUTION)))
character.add_level(WarlockOldOne(hp=5))

character.extras = {"hair": "bald", "alignment": "CE", "image": "characters/images/nende.png"}
character.add_equipment("Stuff", "More Stuff", "Something Else")

character.learn_spell(
    Spell.ELDRITCH_BLAST,
    Spell.PRESTIGITATION,
    Spell.ARMOR_OF_AGATHYS,
    Spell.HEX,
    Spell.INVISIBILITY,
    Spell.MISTY_STEP,
    Spell.SUGGESTION,
)
