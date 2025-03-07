from charsheets.armour import Studded
from charsheets.classes import RogueArcaneTrickster
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Expertise, MagicInitiateDruid
from charsheets.origins import Guide
from charsheets.species import Dwarf
from charsheets.spell import Spell
from charsheets.weapons import Rapier, HandCrossbow

character = RogueArcaneTrickster(
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
    Skill.SLEIGHT_OF_HAND,
    Skill.STEALTH,
    Skill.PERCEPTION,
    Skill.INVESTIGATION,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=10,
    charisma=8,
)
character.extras = {"alignment": "CN", "image": "characters/images/aradim.jpg"}
character.player_name = "Phi"
character.level1(language=Language.HALFLING, expertise=Expertise(Skill.STEALTH, Skill.SLEIGHT_OF_HAND))
character.level2(hp=5)
character.level3(hp=6)
# 3 Cantrips, 3 Prepared
character.learn_spell(Spell.MAGE_HAND, Spell.RAY_OF_FROST, Spell.PRESTIGITATION)
character.learn_spell(Spell.SHIELD, Spell.MAGIC_MISSILE, Spell.COMPREHEND_LANGUAGES)
character.prepare_spells(Spell.SHIELD, Spell.MAGIC_MISSILE, Spell.PRESTIGITATION)
character.level4(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.INTELLIGENCE))
# 4 Prepared spells
character.learn_spell(Spell.FOG_CLOUD)
character.prepare_spells(Spell.FOG_CLOUD)

character.add_languages(Language.DWARVISH, Language.ORC)
character.add_weapon(Rapier())
character.add_weapon(HandCrossbow())
character.wear_armour(Studded(ac_bonus=1, name="Glamour"))
