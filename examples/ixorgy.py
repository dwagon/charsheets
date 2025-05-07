from charsheets.armour import Leather
from charsheets.backgrounds2014 import Outlander
from charsheets.character import Character2014
from charsheets.classes2014 import GreatOldOneWarlock
from charsheets.constants import Skill, Stat, Language
from charsheets.race2014 import HalfElf
from charsheets.spell import Spell
from charsheets.weapons import ShortSword

character = Character2014(
    "Ixorgy the Bound",
    Outlander(language=Language.DWARVISH),
    HalfElf(language=Language.ORC, stat1=Stat.DEXTERITY, stat2=Stat.INTELLIGENCE, skill1=Skill.ACROBATICS, skill2=Skill.ATHLETICS),
    strength=8,
    dexterity=14,
    constitution=13,
    intelligence=12,
    wisdom=10,
    charisma=15,
    player_name="Phi",
)
character.extras = {"alignment": "LE", "image": "characters/images/aradim.png"}
character.add_level(GreatOldOneWarlock(skills=[Skill.ARCANA, Skill.DECEPTION]))
character.learn_spell(Spell.ELDRITCH_BLAST, Spell.CHILL_TOUCH)  # Cantrips
character.prepare_spells(Spell.CHARM_PERSON, Spell.WITCH_BOLT)
character.add_weapon(ShortSword())
character.wear_armour(Leather())
