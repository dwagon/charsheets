from charsheets.character import Character
from charsheets.classes import MysticArcanum, Warlock, WarlockFiend
from charsheets.classes.warlock import AgonizingBlast, ArmorOfShadows, GiftOfTheDepths
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, MagicInitiateCleric, Sharpshooter, BoonOfFate
from charsheets.origins import Acolyte
from charsheets.species import Orc
from charsheets.spell import Spell

character = Character(
    "Thiir",
    Acolyte(
        Stat.CHARISMA,
        Stat.CHARISMA,
        Stat.CHARISMA,
        MagicInitiateCleric(Stat.CHARISMA, Spell.SPARE_THE_DYING, Spell.THAUMATURGY, Spell.CURE_WOUNDS),
    ),
    Orc(),
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
character.add_level(Warlock(hp=4, add_invocation=ArmorOfShadows()))
character.add_level(WarlockFiend(hp=6))
character.add_level(WarlockFiend(hp=3, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
character.add_level(WarlockFiend(hp=6, add_invocation=GiftOfTheDepths()))
character.add_level(WarlockFiend(hp=4))
character.add_level(WarlockFiend(hp=4))
character.add_level(WarlockFiend(hp=3, feat=Sharpshooter()))
character.add_level(WarlockFiend(hp=4))
character.add_level(WarlockFiend(hp=4))
character.add_level(WarlockFiend(hp=5, mystic=MysticArcanum(Spell.ARCANE_GATE)))
character.add_level(WarlockFiend(hp=6, feat=AbilityScoreImprovement(Stat.CONSTITUTION, Stat.DEXTERITY)))
character.add_level(WarlockFiend(hp=5, mystic=MysticArcanum(Spell.ETHEREALNESS)))
character.add_level(WarlockFiend(hp=4))
character.add_level(WarlockFiend(hp=5, mystic=MysticArcanum(Spell.BEFUDDLEMENT)))
character.add_level(WarlockFiend(hp=6, feat=AbilityScoreImprovement(Stat.CONSTITUTION, Stat.DEXTERITY)))
character.add_level(WarlockFiend(hp=4, mystic=MysticArcanum(Spell.ASTRAL_PROJECTION)))
character.add_level(WarlockFiend(hp=4))
character.add_level(WarlockFiend(hp=4, boon=BoonOfFate(Stat.CHARISMA)))
character.add_level(WarlockFiend(hp=4))


character.extras = {"hair": "bald", "alignment": "CE", "image": "characters/images/nende.png"}
character.add_equipment("Stuff", "More Stuff", "Something Else")

character.learn_spell(
    Spell.ELDRITCH_BLAST,
    Spell.PRESTIGITATION,
    Spell.DETECT_THOUGHTS,
    Spell.DISSONANT_WHISPERS,
    Spell.PHANTASMAL_FORCE,
    Spell.ARMOR_OF_AGATHYS,
    Spell.HEX,
    Spell.INVISIBILITY,
    Spell.MISTY_STEP,
    Spell.SUGGESTION,
    Spell.TASHAS_HIDEOUS_LAUGHTER,
)
