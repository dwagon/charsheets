from charsheets.armour import Studded
from charsheets.classes import RogueArcaneTrickster
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Expertise, Skilled, Charger, Chef
from charsheets.origins import Charlatan
from charsheets.species import Tiefling, Legacy
from charsheets.spell import Spell
from charsheets.weapons import Rapier, Shortbow

character = RogueArcaneTrickster(
    "Aradim",
    Charlatan(
        Stat.DEXTERITY, Stat.DEXTERITY, Stat.CONSTITUTION, skilled=Skilled(Skill.INVESTIGATION, Skill.ATHLETICS, Skill.PERCEPTION)
    ),
    Tiefling(Legacy.ABYSSAL, Stat.INTELLIGENCE),
    Skill.SLEIGHT_OF_HAND,
    Skill.STEALTH,
    Skill.INSIGHT,
    Skill.INVESTIGATION,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=10,
    charisma=8,
)
character.extras = {"alignment": "CN", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Phi"
character.level1(language=Language.HALFLING, expertise=Expertise(Skill.STEALTH, Skill.ARCANA))
character.level2(hp=5)
character.level3(hp=6)
character.learn_spell(Spell.MIND_SLIVER, Spell.MINOR_ILLUSION)
character.learn_spell(Spell.SHIELD, Spell.MAGIC_MISSILE)
character.level4(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.INTELLIGENCE))
character.learn_spell(Spell.SLEEP)
character.level5(hp=6)
character.learn_spell(Spell.DETECT_MAGIC)
character.level6(hp=4, expertise=Expertise(Skill.INVESTIGATION, Skill.PERCEPTION))
character.learn_spell(Spell.COMPREHEND_LANGUAGES)
character.level7(hp=4)
character.learn_spell(Spell.FEATHER_FALL)
character.level8(hp=5, feat=Chef(Stat.CONSTITUTION))
character.learn_spell(Spell.BLINDNESS_DEAFNESS)
character.prepare_spells(Spell.BLINDNESS_DEAFNESS, Spell.FEATHER_FALL, Spell.SLEEP)
character.level9(hp=5)
character.level10(hp=6, feat=Charger(Stat.DEXTERITY))
character.level11(hp=8)
character.level12(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.INTELLIGENCE))
character.level13(hp=5)

character.add_languages(Language.DWARVISH, Language.ORC)
character.add_weapon(Rapier(atk_bonus=1, dmg_bonus=1, name="Pointy End"))
character.add_weapon(Shortbow())
character.wear_armour(Studded(ac_bonus=1, name="Glamour"))
