from charsheets.character import Character2014
from charsheets.classes2014 import Wizard
from charsheets.constants import Skill, Language
from charsheets.race2014 import HighElf
from charsheets.spell import Spell
from charsheets.weapons import Quarterstaff, Shortbow
from charsheets.backgrounds2014 import Criminal

character = Character2014(
    "Apotheosis",
    Criminal(),
    HighElf(Spell.FIRE_BOLT, Language.ORC),
    strength=12,
    dexterity=13,
    constitution=14,
    intelligence=15,
    wisdom=8,
    charisma=10,
)

character.add_level(Wizard(skills=[Skill.ARCANA, Skill.INVESTIGATION]))
character.learn_spell(Spell.MAGE_HAND, Spell.POISON_SPRAY, Spell.LIGHT)  # Cantrip
character.learn_spell(
    Spell.MAGIC_MISSILE, Spell.DETECT_MAGIC, Spell.MAGE_ARMOR, Spell.SHIELD, Spell.TASHAS_HIDEOUS_LAUGHTER, Spell.BURNING_HANDS
)  # Lvl 1 Spells
character.prepare_spells(Spell.MAGIC_MISSILE, Spell.SHIELD)
character.add_equipment(
    "Quarterstaff",
    "Shortbow",
    "Dice Set",
    "Bedroll",
    "Rations x 7",
    "Burglar's Pack",
    "Spellbook",
    "Quiver",
    "Waterskin",
    "Arcane Focus (Crystal)",
    "Components Pouch",
)
character.add_weapon(Quarterstaff())
character.add_weapon(Shortbow())

background = """Offspring of a forbidden dalliance between a Male Drow sell-sword adventurer (Chaszonim Yauntorzza) 
    and a Female High-Elf weapon maker (Lythienne Eilfina). He has a younger brother (Folmon), from a different father 
    who became a Law Keeper.
    
    Apotheosis was never really accepted into the highly snobbish High Elf society, so hid away from them, 
    eventually hooking up with a criminal gang, using his burgeoning magical abilities to assist in burglaries and such.
    
    When the heat got too much (and after an emotional showdown with Folmon), Apotheosis headed into the town of
    Fenloe to make his way in the World, throw off the reach of the Law, and maybe also find his long missing Father."""
character.extras = {
    "character_background": background,
    "eyes": "Pale red",
    "skin": "Ashen grey",
    "hair": "White gold",
    "player_name": "Dougal",
    "alignment": "CE",
    "ideals": "Fuck society and their moral structures.",
}
