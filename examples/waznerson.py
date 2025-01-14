#
from charsheets.armour import Leather
from charsheets.classes import WizardEvoker
from charsheets.constants import Stat, Feat, Language
from charsheets.constants import Tool, Skill
from charsheets.feats import AbilityScoreImprovement
from charsheets.origins import Charlatan
from charsheets.species import Aasimar
from charsheets.spells import Spells
from charsheets.weapons import Quarterstaff

character = WizardEvoker(
    "Waznerson",
    Charlatan(Stat.DEXTERITY, Stat.DEXTERITY, Stat.CONSTITUTION),
    Aasimar(),
    Skill.ARCANA,
    Skill.MEDICINE,
    strength=8,
    dexterity=12,
    constitution=13,
    intelligence=15,
    wisdom=14,
    charisma=10,
)
character.find_feat(Feat.SKILLED).set_skills(Tool.DISGUISE_KIT, Skill.ATHLETICS, Skill.INTIMIDATION)  # type: ignore
character.player_name = "Epsilon"
character.extras = {
    "eyes": "glowing red",
    "hair": "white",
    "height": "6'4",
    "alignment": "NE",
    "image": "characters/images/nende.png",
    "age": "80",
    "skin": "alabaster",
}


character.add_languages(Language.GNOMISH, Language.ORC)
character.wear_armour(Leather())
character.add_weapon(Quarterstaff())

character.add_equipment("Snacks")
character.learn_spell(
    Spells.FIRE_BOLT, Spells.DANCING_LIGHTS, Spells.MAGE_HAND, Spells.MAGIC_MISSILE, Spells.SHIELD, Spells.BURNING_HANDS
)
character.prepare_spells(Spells.MAGIC_MISSILE, Spells.SHIELD)

character.level2(hp=6)
character.learn_spell(Spells.MAGE_ARMOR)
character.prepare_spells(Spells.MAGE_ARMOR)

character.level3(hp=3)
character.learn_spell(Spells.DRAGONS_BREATH, Spells.INVISIBILITY, Spells.MISTY_STEP)
character.prepare_spells(Spells.DRAGONS_BREATH)

character.level4(hp=3, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.INTELLIGENCE, character))
character.learn_spell(Spells.SCORCHING_RAY, Spells.MAGIC_MOUTH)
character.prepare_spells(Spells.SCORCHING_RAY)

character.level5(hp=6)
character.learn_spell(Spells.FIREBALL, Spells.LIGHTNING_BOLT)
character.prepare_spells(Spells.FIREBALL)

character.level6(hp=3)
character.learn_spell(Spells.FIREBALL, Spells.LIGHTNING_BOLT)
character.prepare_spells(Spells.FIREBALL)


# EOF
