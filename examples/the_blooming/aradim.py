from charsheets.armour import Studded
from charsheets.character import Character
from charsheets.classes import Rogue, RogueArcaneTrickster
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Expertise, MagicInitiateDruid
from charsheets.origins import Guide
from charsheets.species import Dwarf
from charsheets.spell import Spell
from charsheets.weapons import Rapier, HandCrossbow

character = Character(
    "Aradim",
    Guide(
        Stat.DEXTERITY,
        Stat.DEXTERITY,
        Stat.CONSTITUTION,
        initiate=MagicInitiateDruid(
            spellcasting_stat=Stat.INTELLIGENCE, cantrip1=Spell.GUIDANCE, cantrip2=Spell.STARRY_WISP, level1=Spell.CURE_WOUNDS
        ),
    ),
    Dwarf(),
    Language.DWARVISH,
    Language.ORC,
    strength=10,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=8,
    charisma=12,
)
character.extras = {"alignment": "CN", "image": "characters/images/aradim.png"}
character.player_name = "Phi"
character.add_level(
    Rogue(
        language=Language.UNDERCOMMON,
        skills=[Skill.SLEIGHT_OF_HAND, Skill.ACROBATICS, Skill.INVESTIGATION, Skill.PERCEPTION],
        expertise=Expertise(Skill.STEALTH, Skill.SLEIGHT_OF_HAND),
    )
)
character.add_equipment("Thieves' Tools")
character.add_level(Rogue(hp=5))
character.add_level(RogueArcaneTrickster(hp=6))
# 3 Cantrips, 3 Prepared
character.learn_spell(Spell.MAGE_HAND, Spell.RAY_OF_FROST, Spell.PRESTIGITATION)
character.learn_spell(Spell.SHIELD, Spell.MAGIC_MISSILE, Spell.COMPREHEND_LANGUAGES)
character.prepare_spells(Spell.SHIELD, Spell.MAGIC_MISSILE, Spell.PRESTIGITATION)
character.add_level(RogueArcaneTrickster(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.INTELLIGENCE)))
character.add_level(RogueArcaneTrickster(hp=5))

# 4 Prepared spells
character.learn_spell(Spell.FOG_CLOUD)
character.prepare_spells(Spell.FOG_CLOUD)

character.add_weapon(Rapier())
character.add_weapon(HandCrossbow())
character.wear_armour(Studded(ac_bonus=1, name="Glamoured Studded"))
