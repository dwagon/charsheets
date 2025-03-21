from charsheets.classes import WarlockFiend, MysticArcanum
from charsheets.classes.warlock import AgonizingBlast, ArmorOfShadows, GiftOfTheDepths
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, MagicInitiateCleric, Sharpshooter
from charsheets.origins import Acolyte
from charsheets.species import Orc
from charsheets.spell import Spell

character = WarlockFiend(
    "Thiir",
    Acolyte(
        Stat.CHARISMA,
        Stat.CHARISMA,
        Stat.CHARISMA,
        MagicInitiateCleric(Stat.CHARISMA, Spell.SPARE_THE_DYING, Spell.THAUMATURGY, Spell.CURE_WOUNDS),
    ),
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
character.level2(hp=4)
character.level3(hp=6)
character.level4(hp=3, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA))
character.level5(hp=6)
character.level6(hp=4)
character.level7(hp=4)
character.level8(hp=3, feat=Sharpshooter())
character.level9(hp=4)
character.level10(hp=4)
character.level11(hp=5, mystic=MysticArcanum(Spell.ARCANE_GATE))
character.level12(hp=6, feat=AbilityScoreImprovement(Stat.CONSTITUTION, Stat.DEXTERITY))
character.level13(hp=5)


character.add_languages(Language.GOBLIN, Language.UNDERCOMMON)
character.extras = {"hair": "bald", "alignment": "CE", "image": "characters/images/nende.png"}
character.add_equipment("Stuff", "More Stuff", "Something Else")
character.add_invocation(AgonizingBlast(Spell.ELDRITCH_BLAST))
character.add_invocation(ArmorOfShadows())
character.add_invocation(GiftOfTheDepths())

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
