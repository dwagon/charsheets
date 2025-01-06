from charsheets.classes import WarlockOldOne
from charsheets.classes.warlock import AgonizingBlast, ArmorOfShadows, GiftOfTheDepths
from charsheets.constants import Skill, Stat
from charsheets.origins import Acolyte
from charsheets.species.homebrew.kuatoa import Kuatoa
from charsheets.spells import Spells
from charsheets.abilities import AbilityScoreImprovement


character = WarlockOldOne(
    "Thiir",
    Acolyte(Stat.CHARISMA, Stat.CHARISMA, Stat.CHARISMA),
    Kuatoa(),
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
character.level2(hp=4)
character.level3(hp=6)
character.level4(hp=3, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA))
character.extras = {"hair": "bald", "alignment": "CE", "image": "characters/images/nende.png"}
character.add_equipment("Stuff", "More Stuff", "Something Else")
character.add_invocation(AgonizingBlast(Spells.ELDRITCH_BLAST))
character.add_invocation(ArmorOfShadows())
character.add_invocation(GiftOfTheDepths())

character.learn_spell(
    Spells.ELDRITCH_BLAST,
    Spells.PRESTIGITATION,
    Spells.DETECT_THOUGHTS,
    Spells.DISSONANT_WHISPERS,
    Spells.PHANTASMAL_FORCE,
    Spells.ARMOR_OF_AGATHYS,
    Spells.HEX,
    Spells.INVISIBILITY,
    Spells.MISTY_STEP,
    Spells.SUGGESTION,
    Spells.TASHAS_HIDEOUS_LAUGHTER,
)
