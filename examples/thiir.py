from charsheets.constants import (
    EldritchInvocation,
    Skill,
    CharSpecies,
    Origin,
    CharSubclassName,
)
from charsheets.spells import Spells
from charsheets.classes.warlock import Warlock

character = Warlock(
    "Thiir",
    Origin.ACOLYTE,
    CharSpecies.HUMAN,
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
character.set_sub_class(CharSubclassName.GREAT_OLD_ONE_PATRON)
character.add_level(3)  # Level 4
character.extras = {"hair": "bald", "alignment": "CE", "image": "characters/images/nende.png"}
character.add_equipment("Stuff", "More Stuff", "Something Else")
eldritch_invocations = {EldritchInvocation.AGONIZING_BLAST, EldritchInvocation.GIFT_OF_THE_DEPTHS}
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
