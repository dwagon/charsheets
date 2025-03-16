#
from charsheets.armour import Leather
from charsheets.classes import WizardEvoker, Scholar
from charsheets.constants import Stat, Language
from charsheets.constants import Tool, Skill
from charsheets.features import AbilityScoreImprovement, Skilled, SpellSniper
from charsheets.origins import Charlatan
from charsheets.species import Aasimar
from charsheets.spell import Spell
from charsheets.weapons import Quarterstaff

character = WizardEvoker(
    "Waznerson",
    Charlatan(
        Stat.DEXTERITY, Stat.DEXTERITY, Stat.CONSTITUTION, skilled=Skilled(Tool.DISGUISE_KIT, Skill.ATHLETICS, Skill.INTIMIDATION)
    ),
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
    Spell.FIRE_BOLT, Spell.DANCING_LIGHTS, Spell.MAGE_HAND, Spell.MAGIC_MISSILE, Spell.SHIELD, Spell.BURNING_HANDS
)
character.prepare_spells(Spell.MAGIC_MISSILE, Spell.SHIELD)

character.level1()
character.level2(hp=6, scholar=Scholar(Skill.MEDICINE))
character.learn_spell(Spell.MAGE_ARMOR)
character.prepare_spells(Spell.MAGE_ARMOR)

character.level3(hp=3)
character.learn_spell(Spell.DRAGONS_BREATH, Spell.INVISIBILITY, Spell.MISTY_STEP)
character.prepare_spells(Spell.DRAGONS_BREATH)

character.level4(hp=3, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.INTELLIGENCE))
character.learn_spell(Spell.SCORCHING_RAY, Spell.MAGIC_MOUTH)
character.prepare_spells(Spell.SCORCHING_RAY)

character.level5(hp=6)
character.learn_spell(Spell.FIREBALL, Spell.LIGHTNING_BOLT)
character.prepare_spells(Spell.FIREBALL)

character.level6(hp=3)
character.learn_spell(Spell.COUNTERSPELL, Spell.LEOMUNDS_TINY_HUT)
character.prepare_spells(Spell.FIREBALL)

character.level7(hp=5)
character.learn_spell(Spell.OTILUKES_RESILIENT_SPHERE, Spell.MORDENKAINENS_PRIVATE_SANCTUM)
character.prepare_spells(Spell.DIMENSION_DOOR)
character.level8(hp=4, feat=SpellSniper(Stat.INTELLIGENCE))
character.level9(hp=4)
character.level10(hp=4)
character.level11(hp=6)
character.level12(hp=2, feat=AbilityScoreImprovement(Stat.INTELLIGENCE, Stat.INTELLIGENCE))


# EOF
