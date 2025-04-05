from charsheets.character import Character
from charsheets.classes import WarlockOldOne, Warlock
from charsheets.classes.warlock import AgonizingBlast, MaskOfManyFaces, PactOfTheTome
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement
from charsheets.origins import Hermit
from charsheets.species.homebrew.kuatoa import Kuatoa
from charsheets.spell import Spell

character = Character(
    "Thiir",
    Hermit(
        Stat.CHARISMA,
        Stat.CHARISMA,
        Stat.CONSTITUTION,
    ),
    Kuatoa(),
    Language.GOBLIN,
    Language.DEEP_SPEECH,
    strength=8,
    dexterity=12,
    constitution=14,
    intelligence=10,
    wisdom=13,
    charisma=15,
)
character.player_name = "Jesse"
character.add_level(Warlock(skills=[Skill.RELIGION, Skill.DECEPTION]))
character.add_level(Warlock(hp=5))
character.add_level(WarlockOldOne(hp=4))
character.add_level(WarlockOldOne(hp=8, feat=AbilityScoreImprovement(Stat.WISDOM, Stat.CHARISMA)))

character.extras = {"hair": "bald", "alignment": "CE", "image": "characters/images/thiir.png"}
character.warlock.add_invocation(AgonizingBlast(Spell.ELDRITCH_BLAST))
character.warlock.add_invocation(
    PactOfTheTome(Spell.TOLL_THE_DEAD, Spell.MIND_SLIVER, Spell.BLADE_WARD, Spell.IDENTIFY, Spell.FIND_FAMILIAR)  # Get real spells
)
character.warlock.add_invocation(MaskOfManyFaces())

character.learn_spell(Spell.ELDRITCH_BLAST, Spell.MAGE_HAND, Spell.MINOR_ILLUSION)
character.learn_spell(Spell.ARMOR_OF_AGATHYS, Spell.HEX, Spell.SUGGESTION, Spell.INVISIBILITY, Spell.MISTY_STEP)
