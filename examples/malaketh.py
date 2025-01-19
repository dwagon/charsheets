#
from charsheets.armour import Breastplate
from charsheets.classes import ClericLifeDomain
from charsheets.constants import Skill, Stat, Language
from charsheets.origins import Acolyte
from charsheets.species import Halfling
from charsheets.spell import Spell
from charsheets.weapons import Mace
from charsheets.abilities import AbilityScoreImprovement, MagicInitiateCleric

character = ClericLifeDomain(
    "Malaketh",
    Acolyte(
        Stat.INTELLIGENCE,
        Stat.WISDOM,
        Stat.WISDOM,
        MagicInitiateCleric(Stat.WISDOM, Spell.GUIDANCE, Spell.SACRED_FLAME, Spell.INFLICT_WOUNDS),
    ),
    Halfling(),
    Skill.MEDICINE,
    Skill.HISTORY,
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

character.level2(hp=8)
character.prepare_spells(Spell.DETECT_MAGIC)
character.level3(hp=5)
character.prepare_spells(Spell.AID)
character.level4(hp=3, feat=AbilityScoreImprovement(Stat.WISDOM, Stat.WISDOM))
character.level5(hp=7)
character.level6(hp=6)

character.add_languages(Language.HALFLING, Language.ELVISH)
character.wear_armour(Breastplate(ac_bonus=1))
character.shield = True
character.add_weapon(Mace())

character.add_equipment("Packed lunch")

# EOF
