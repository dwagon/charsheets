from charsheets.character import Character2014
from charsheets.classes import Wizard
from charsheets.constants import Skill, Language
from charsheets.race import HighElf
from charsheets.spell import Spell
from charsheets.weapons import Quarterstaff, Shortbow
from charsheets.backgrounds import Hermit

character = Character2014(
    "Apotheosis",
    Hermit(Language.DWARVISH),
    HighElf(Spell.FIRE_BOLT, Language.HALFLING),
    strength=12,
    dexterity=13,
    constitution=14,
    intelligence=15,
    wisdom=8,
    charisma=10,
    eyes="pale red",
    skin="ashen grey",
    hair="white gold",
    player_name="Dougal",
)

character.add_level(Wizard(skills=[Skill.ARCANA, Skill.INVESTIGATION]))
character.learn_spell(Spell.MAGE_HAND, Spell.POISON_SPRAY, Spell.LIGHT)  # Cantrip
character.learn_spell(
    Spell.MAGIC_MISSILE, Spell.DETECT_MAGIC, Spell.MAGE_ARMOR, Spell.SHIELD, Spell.TASHAS_HIDEOUS_LAUGHTER, Spell.BURNING_HANDS
)  # Lvl 1 Spells
character.prepare_spells(Spell.MAGIC_MISSILE, Spell.SHIELD)

character.add_weapon(Quarterstaff())
character.add_weapon(Shortbow())


# Offspring of a forbidden dalliance between a Male Drow sell-sword adventurer (Chaszonim Yauntorzza) and a Female
# High-Elf weapon maker (Lythienne Eilfina). He was never really accepted into the highly snobbish High Elf society,
# so hid away in libraries and places of solitude. As soon as he had finished his schooling, Apotheosis headed into
# the town of Fenloe to make his way in the World, and maybe also find his long missing Father.
