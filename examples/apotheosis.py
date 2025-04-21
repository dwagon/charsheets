from charsheets.character import Character2014
from charsheets.classes import Wizard
from charsheets.constants import Skill
from charsheets.race import MountainDwarf
from charsheets.spell import Spell
from charsheets.weapons import Quarterstaff

character = Character2014(
    "Apotheosis", MountainDwarf(), strength=12, dexterity=13, constitution=14, intelligence=15, wisdom=8, charisma=10
)

character.add_level(Wizard(skills=[Skill.ARCANA, Skill.INVESTIGATION]))
character.learn_spell(Spell.MAGE_HAND, Spell.POISON_SPRAY, Spell.LIGHT)  # Cantrip
character.learn_spell(
    Spell.MAGIC_MISSILE, Spell.DETECT_MAGIC, Spell.MAGE_ARMOR, Spell.SHIELD, Spell.TASHAS_HIDEOUS_LAUGHTER, Spell.BURNING_HANDS
)  # Lvl 1 Spells
character.prepare_spells(Spell.MAGIC_MISSILE, Spell.SHIELD)

character.add_weapon(Quarterstaff())
