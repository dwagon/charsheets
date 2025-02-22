from charsheets.classes import WarlockArchFey
from charsheets.classes.warlock import AgonizingBlast, PactOfTheBlade, EldritchSpear, EldritchSmite, ThirstingBlade, Lifedrinker
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Slasher
from charsheets.origins import Hermit
from charsheets.species import Orc
from charsheets.spell import Spell

character = WarlockArchFey(
    "Thiir",
    Hermit(Stat.CONSTITUTION, Stat.CHARISMA, Stat.CHARISMA),
    Orc(),
    Skill.DECEPTION,
    Skill.INTIMIDATION,
    strength=8,
    dexterity=14,
    constitution=13,
    intelligence=12,
    wisdom=10,
    charisma=15,
)
character.player_name = "Delta"
character.level1()
character.add_invocation(PactOfTheBlade())

character.level2(hp=4)
character.add_invocation(AgonizingBlast(Spell.ELDRITCH_BLAST))
character.add_invocation(EldritchSpear(Spell.ELDRITCH_BLAST))

character.level3(hp=6)
character.level4(hp=3, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA))
character.level5(hp=6)
character.add_invocation(EldritchSmite())
character.add_invocation(ThirstingBlade())


character.level6(hp=4)
character.level7(hp=4)
character.level8(hp=3, feat=Slasher(Stat.DEXTERITY))
character.level9(hp=4)
character.add_invocation(Lifedrinker())


character.add_languages(Language.GOBLIN, Language.GIANT)
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
