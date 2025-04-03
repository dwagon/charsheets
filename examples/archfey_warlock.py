from charsheets.character import Character
from charsheets.classes import WarlockArchFey, MysticArcanum, Warlock
from charsheets.classes.warlock import AgonizingBlast, PactOfTheBlade, EldritchSpear, EldritchSmite, ThirstingBlade, Lifedrinker
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Slasher
from charsheets.origins import Hermit
from charsheets.species import Orc
from charsheets.spell import Spell

character = Character(
    "Thiir",
    Hermit(Stat.CONSTITUTION, Stat.CHARISMA, Stat.CHARISMA),
    Orc(),
    Language.GOBLIN,
    Language.GIANT,
    strength=8,
    dexterity=14,
    constitution=13,
    intelligence=12,
    wisdom=10,
    charisma=15,
)
character.player_name = "Delta"
character.add_level(Warlock(skills=[Skill.DECEPTION, Skill.INTIMIDATION]))
character.warlock.add_invocation(PactOfTheBlade())

character.add_level(Warlock(hp=4))
character.warlock.add_invocation(AgonizingBlast(Spell.ELDRITCH_BLAST))
character.warlock.add_invocation(EldritchSpear(Spell.ELDRITCH_BLAST))

character.add_level(WarlockArchFey(hp=6))
character.add_level(WarlockArchFey(hp=3, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
character.add_level(WarlockArchFey(hp=6))
character.warlock.add_invocation(EldritchSmite())
character.warlock.add_invocation(ThirstingBlade())

character.add_level(WarlockArchFey(hp=4))
character.add_level(WarlockArchFey(hp=4))
character.add_level(WarlockArchFey(hp=3, feat=Slasher(Stat.DEXTERITY)))
character.add_level(WarlockArchFey(hp=4))
character.warlock.add_invocation(Lifedrinker())
character.add_level(WarlockArchFey(hp=4))
character.add_level(WarlockArchFey(hp=5, mystic=MysticArcanum(Spell.ARCANE_GATE)))
character.add_level(WarlockArchFey(hp=4, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))
character.add_level(WarlockArchFey(hp=5))

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
