from charsheets.constants import Skill, Origin
from charsheets.spells import Spells
from charsheets.classes.warlock import AgonizingBlast, ArmorOfShadows, GiftOfTheDepths
from charsheets.classes import OldOneWarlock
from charsheets.species.homebrew.kuatoa import Kuatoa

character = OldOneWarlock(
    "Thiir",
    Origin.ACOLYTE,
    Kuatoa(),
    Skill.DECEPTION,
    Skill.INTIMIDATION,
    strength=8,
    dexterity=15,
    constitution=13,
    intelligence=12,
    wisdom=10,
    charisma=18,
)
character.player_name = "Delta"
character.add_level(4)  # Level 2
character.add_level(6)  # Level 3
character.add_level(3)  # Level 4
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
