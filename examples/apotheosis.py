from charsheets.features import AbilityScoreImprovement
from charsheets.origins import Criminal
from charsheets.character import Character
from charsheets.classes import Wizard, Scholar, WizardAbjurer
from charsheets.constants import Skill, Language, Stat
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell
from charsheets.money import Coin
from charsheets.weapons import Quarterstaff, Shortbow

character = Character(
    "Apotheosis",
    Criminal(Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE),
    Elf(Lineages.HIGH_ELF, Skill.PERCEPTION, Stat.INTELLIGENCE),
    Language.ELVISH,
    Language.ORC,
    strength=12,
    dexterity=13,
    constitution=14,
    intelligence=15,
    wisdom=8,
    charisma=10,
)

character.add_level(Wizard(skills=[Skill.ARCANA, Skill.INVESTIGATION]))
character.learn_spell(Spell.FIRE_BOLT, Spell.MAGE_HAND, Spell.MESSAGE, Spell.BLADE_WARD)  # Cantrip
character.learn_spell(Spell.MAGIC_MISSILE, Spell.SHIELD, Spell.TASHAS_HIDEOUS_LAUGHTER, Spell.IDENTIFY)  # Lvl 1 Spells
character.prepare_spells(Spell.MAGIC_MISSILE, Spell.SHIELD)
character.add_equipment(
    "Dice Set",
    "Bedroll",
    "Rations x 7",
    "Burglar's Pack",
    "Spellbook",
    "Quiver",
    "Waterskin",
    "Arcane Focus (Crystal)",
    "Components Pouch",
    "Necklace of Fireballs (1 charges)",
    "Potion of Healing",
    "Wand of Mending",
    "Titan Heart Crystal (Meld into Stone 1/day)",
    "Glabrezu Statue (One off Confusion)",
    "Blink Dog heads (x3)",
    "Tome of Harvesting Monsters",
    "Burning Chicken Head Hat" "Aboleth Statue (Dominate Monster once) worth 200gp" "5 pieces of jewellery @ 50gp",
)
character.add_weapon(Quarterstaff())
character.add_weapon(Shortbow())

character.add_level(Wizard(hp=5, scholar=Scholar(Skill.ARCANA)))
character.learn_spell(Spell.BURNING_HANDS)
character.prepare_spells(Spell.BURNING_HANDS)

character.add_level(WizardAbjurer(hp=3))
character.learn_spell(Spell.KNOCK, Spell.ARCANE_LOCK, Spell.ARCANE_VIGOR)
character.prepare_spells(Spell.KNOCK, Spell.ARCANE_LOCK)
character.prepare_spells(Spell.LIGHT)  # Boon from the Temple Statue

BACKGROUND = """Offspring of a forbidden dalliance between a Male Drow sell-sword adventurer (Chaszonim Yauntorzza)
    and a Female High-Elf weapon maker (Lythienne Eilfina). He has a younger brother (Folmon), from a different father
    who became a Law Keeper.
    
    Apotheosis was never really accepted into the highly snobbish High Elf society, so hid away from them,
    eventually hooking up with a criminal gang, using his burgeoning magical abilities to assist in burglaries and such.
    
    When the heat got too much (and after an emotional showdown with Folmon), Apotheosis headed into the town of
    Fenloe to make his way in the World, throw off the reach of the Law, and maybe also find his long missing Father."""

character.extras = {
    "character_background": BACKGROUND,
    "eyes": "Pale red",
    "skin": "Ashen grey",
    "hair": "White gold",
    "player_name": "Dougal",
    "alignment": "CE",
    "ideals": "Fuck society and their moral structures.",
    "image": "characters/images/apotheosis.png",
}
character.add_coins(Coin.GOLD, 726)
character.remove_coins(Coin.GOLD, 50)  # Bought healing potions
character.remove_coins(Coin.GOLD, 10)  # Tome of body bits
character.add_coins(Coin.GOLD, 160)  # Looting
character.add_coins(Coin.SILVER, 100)
character.add_coins(Coin.COPPER, 34)

character.add_level(WizardAbjurer(hp=3, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.INTELLIGENCE)))
character.prepare_spells(Spell.RAY_OF_FROST)
character.prepare_spells(Spell.SPIDER_CLIMB)
