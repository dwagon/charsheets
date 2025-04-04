from charsheets.armour import Studded
from charsheets.character import Character
from charsheets.classes import RogueArcaneTrickster, Rogue
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Expertise, Skilled, Charger, Chef
from charsheets.origins import Charlatan
from charsheets.species import Tiefling, Legacy
from charsheets.spell import Spell
from charsheets.weapons import Rapier, Shortbow

character = Character(
    "Aradim",
    Charlatan(
        Stat.DEXTERITY, Stat.DEXTERITY, Stat.CONSTITUTION, skilled=Skilled(Skill.INVESTIGATION, Skill.ATHLETICS, Skill.PERCEPTION)
    ),
    Tiefling(Legacy.ABYSSAL, Stat.INTELLIGENCE),
    Language.DWARVISH,
    Language.ORC,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=10,
    charisma=8,
)
character.extras = {"alignment": "CN", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Phi"
character.add_level(
    Rogue(
        language=Language.HALFLING,
        skills=[Skill.SLEIGHT_OF_HAND, Skill.STEALTH, Skill.INSIGHT, Skill.INVESTIGATION],
        expertise=Expertise(Skill.STEALTH, Skill.ARCANA),
    )
)
character.add_level(Rogue(hp=5))
character.add_level(RogueArcaneTrickster(hp=6))
character.learn_spell(Spell.MIND_SLIVER, Spell.MINOR_ILLUSION)
character.learn_spell(Spell.SHIELD, Spell.MAGIC_MISSILE)
character.add_level(RogueArcaneTrickster(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.INTELLIGENCE)))
character.learn_spell(Spell.SLEEP)
character.add_level(RogueArcaneTrickster(hp=6))
character.learn_spell(Spell.DETECT_MAGIC)
character.add_level(RogueArcaneTrickster(hp=4, expertise=Expertise(Skill.INVESTIGATION, Skill.PERCEPTION)))
character.learn_spell(Spell.COMPREHEND_LANGUAGES)
character.add_level(RogueArcaneTrickster(hp=4))
character.learn_spell(Spell.FEATHER_FALL)
character.add_level(RogueArcaneTrickster(hp=5, feat=Chef(Stat.CONSTITUTION)))
character.learn_spell(Spell.BLINDNESS_DEAFNESS)
character.prepare_spells(Spell.BLINDNESS_DEAFNESS, Spell.FEATHER_FALL, Spell.SLEEP)
character.add_level(RogueArcaneTrickster(hp=5))
character.add_level(RogueArcaneTrickster(hp=6, feat=Charger(Stat.DEXTERITY)))
character.add_level(RogueArcaneTrickster(hp=8))
character.add_level(RogueArcaneTrickster(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.INTELLIGENCE)))
character.add_level(RogueArcaneTrickster(hp=5))

character.add_weapon(Rapier(atk_bonus=1, dmg_bonus=1, name="Pointy End"))
character.add_weapon(Shortbow())
character.wear_armour(Studded(ac_bonus=1, name="Glamour"))
