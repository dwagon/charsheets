#
from charsheets.armour import Breastplate, Shield
from charsheets.character import Character
from charsheets.classes import Cleric, ClericLightDomain
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, MagicInitiateCleric, GreatWeaponMaster
from charsheets.origins import Acolyte
from charsheets.species import Halfling
from charsheets.spell import Spell
from charsheets.weapons import Mace

character = Character(
    "Malaketh",
    Acolyte(
        Stat.INTELLIGENCE,
        Stat.WISDOM,
        Stat.WISDOM,
        MagicInitiateCleric(Stat.WISDOM, Spell.GUIDANCE, Spell.SACRED_FLAME, Spell.INFLICT_WOUNDS),
    ),
    Halfling(),
    Language.HALFLING,
    Language.ELVISH,
    strength=14,
    dexterity=8,
    constitution=13,
    intelligence=11,
    wisdom=17,
    charisma=12,
)
character.player_name = "Phi"
character.extras = {
    "eyes": "brown",
    "hair": "black",
    "height": "3'",
    "alignment": "LE",
    "image": "characters/images/nende.png",
    "age": "20",
    "skin": "waxy",
}

character.learn_spell(Spell.THAUMATURGY, Spell.MENDING, Spell.TOLL_THE_DEAD)  # Cantrips
character.prepare_spells(Spell.HEALING_WORD, Spell.CURE_WOUNDS, Spell.BLESS, Spell.SHIELD_OF_FAITH)

character.add_level(Cleric(skills=[Skill.MEDICINE, Skill.HISTORY]))
character.add_level(Cleric(hp=8))
character.prepare_spells(Spell.DETECT_MAGIC)
character.add_level(ClericLightDomain(hp=5))
character.prepare_spells(Spell.AID)
character.add_level(ClericLightDomain(hp=3, feat=AbilityScoreImprovement(Stat.CONSTITUTION, Stat.WISDOM)))
character.add_level(ClericLightDomain(hp=7))
character.add_level(ClericLightDomain(hp=6))
character.prepare_spells(Spell.SPIRIT_GUARDIANS, Spell.MASS_HEALING_WORD)
character.add_level(ClericLightDomain(hp=5))
character.prepare_spells(Spell.STONE_SHAPE, Spell.DIVINATION)
character.add_level(ClericLightDomain(hp=3, feat=GreatWeaponMaster()))
character.add_level(ClericLightDomain(hp=4))
character.add_level(ClericLightDomain(hp=4))
character.add_level(ClericLightDomain(hp=8))
character.add_level(ClericLightDomain(hp=3, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.WISDOM)))
character.add_level(ClericLightDomain(hp=5))

character.wear_armour(Breastplate(ac_bonus=1))
character.wear_shield(Shield())
character.add_weapon(Mace(dmg_bonus=2, atk_bonus=2, name="+2 Mace"))

character.add_equipment("Packed lunch")

# EOF
