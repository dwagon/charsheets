#
from charsheets.armour import Breastplate
from charsheets.classes import ClericLifeDomain
from charsheets.constants import Skill, Stat
from charsheets.origins import Acolyte
from charsheets.species import Halfling
from charsheets.spells import Spells
from charsheets.weapons import Mace
from charsheets.feats import AbilityScoreImprovement

character = ClericLifeDomain(
    "Malaketh",
    Acolyte(Stat.INTELLIGENCE, Stat.WISDOM, Stat.WISDOM),
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
character.learn_spell(Spells.GUIDANCE, Spells.SACRED_FLAME, Spells.THAUMATURGY)
character.learn_spell(Spells.LIGHT, Spells.RESISTANCE)  # Magic Initiate Cleric

character.level2(hp=8)
character.level3(hp=5)
character.level4(hp=3, feat=AbilityScoreImprovement(Stat.WISDOM, Stat.WISDOM, character))
character.level5(hp=7)
character.level6(hp=6)


character.wear_armour(Breastplate(ac_bonus=1))
character.shield = True
character.add_weapon(Mace())

character.add_equipment("Packed lunch")

# EOF
