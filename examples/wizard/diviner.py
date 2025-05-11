#
from charsheets.armour import Leather
from charsheets.character import Character
from charsheets.classes import WizardDiviner, Scholar, Wizard
from charsheets.constants import Skill
from charsheets.constants import Stat, Language
from charsheets.features import AbilityScoreImprovement, Telekinetic, BoonOfSpellRecall
from charsheets.origins import Criminal
from charsheets.species import Aasimar
from charsheets.spell import Spell
from charsheets.weapons import Quarterstaff

character = Character(
    "Waznerson",
    Criminal(Stat.DEXTERITY, Stat.INTELLIGENCE, Stat.INTELLIGENCE),
    Aasimar(),
    Language.GNOMISH,
    Language.ORC,
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


character.wear_armour(Leather())
character.add_weapon(Quarterstaff())
character.add_equipment("Snacks")

character.add_level(Wizard(skills=[Skill.ARCANA, Skill.MEDICINE]))
character.learn_spell(
    Spell.FIRE_BOLT, Spell.DANCING_LIGHTS, Spell.MAGE_HAND, Spell.MAGIC_MISSILE, Spell.SHIELD, Spell.BURNING_HANDS
)
character.prepare_spells(Spell.MAGIC_MISSILE, Spell.SHIELD)
character.add_level(Wizard(hp=6, scholar=Scholar(Skill.MEDICINE)))
character.learn_spell(Spell.MAGE_ARMOR)
character.prepare_spells(Spell.MAGE_ARMOR)

character.add_level(WizardDiviner(hp=3))
character.learn_spell(Spell.DRAGONS_BREATH, Spell.INVISIBILITY, Spell.MISTY_STEP)
character.prepare_spells(Spell.DRAGONS_BREATH)

character.add_level(WizardDiviner(hp=3, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.INTELLIGENCE)))
character.learn_spell(Spell.SCORCHING_RAY, Spell.MAGIC_MOUTH)
character.prepare_spells(Spell.SCORCHING_RAY)

character.add_level(WizardDiviner(hp=6))
character.learn_spell(Spell.FIREBALL, Spell.LIGHTNING_BOLT)
character.prepare_spells(Spell.FIREBALL)

character.add_level(WizardDiviner(hp=3))
character.learn_spell(Spell.COUNTERSPELL, Spell.LEOMUNDS_TINY_HUT)
character.prepare_spells(Spell.FIREBALL)

character.add_level(WizardDiviner(hp=5))
character.learn_spell(Spell.OTILUKES_RESILIENT_SPHERE, Spell.MORDENKAINENS_PRIVATE_SANCTUM)
character.prepare_spells(Spell.DIMENSION_DOOR)

character.add_level(WizardDiviner(hp=4, feat=Telekinetic(Stat.INTELLIGENCE)))

character.add_level(WizardDiviner(hp=4))
character.add_level(WizardDiviner(hp=4))
character.add_level(WizardDiviner(hp=6))
character.add_level(WizardDiviner(hp=3, feat=AbilityScoreImprovement(Stat.CONSTITUTION, Stat.CONSTITUTION)))
character.add_level(WizardDiviner(hp=5))

character.add_level(WizardDiviner(hp=5))
character.add_level(WizardDiviner(hp=5))
character.add_level(WizardDiviner(hp=3, feat=AbilityScoreImprovement(Stat.CONSTITUTION, Stat.DEXTERITY)))
character.add_level(WizardDiviner(hp=5))
character.add_level(WizardDiviner(hp=5))
character.add_level(WizardDiviner(hp=5, boon=BoonOfSpellRecall(Stat.INTELLIGENCE)))
character.add_level(WizardDiviner(hp=5))


# EOF
