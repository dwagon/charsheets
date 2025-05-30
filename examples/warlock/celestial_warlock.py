from charsheets.character import Character
from charsheets.classes import MysticArcanum, Warlock, WarlockCelestial
from charsheets.classes.warlock import AgonizingBlast, ArmorOfShadows, GiftOfTheDepths
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, MagicInitiateCleric, Skulker, BoonOfFate
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
character.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
character.add_level(Warlock(hp=4, add_invocation=AgonizingBlast(Spell.ELDRITCH_BLAST)))
character.add_level(WarlockCelestial(hp=6))
character.add_level(WarlockCelestial(hp=3, feat=AbilityScoreImprovement(Stat.CONSTITUTION, Stat.CHARISMA)))
character.add_level(WarlockCelestial(hp=6, add_invocation=ArmorOfShadows()))
character.add_level(WarlockCelestial(hp=4, add_invocation=GiftOfTheDepths()))
character.add_level(WarlockCelestial(hp=4))
character.add_level(WarlockCelestial(hp=3, feat=Skulker()))
character.add_level(WarlockCelestial(hp=4))
character.add_level(WarlockCelestial(hp=4))
character.add_level(WarlockCelestial(hp=5, mystic=MysticArcanum(Spell.ARCANE_GATE)))
character.add_level(WarlockCelestial(hp=6, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY)))
character.add_level(WarlockCelestial(hp=5, mystic=MysticArcanum(Spell.FORCECAGE)))
character.add_level(WarlockCelestial(hp=5))
character.add_level(WarlockCelestial(hp=5, mystic=MysticArcanum(Spell.DEMIPLANE)))
character.add_level(WarlockCelestial(hp=4, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
character.add_level(WarlockCelestial(hp=5, mystic=MysticArcanum(Spell.GATE)))
character.add_level(WarlockCelestial(hp=5))
character.add_level(WarlockCelestial(hp=5, boon=BoonOfFate(Stat.CHARISMA)))
character.add_level(WarlockCelestial(hp=5))

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
