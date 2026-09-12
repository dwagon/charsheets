from charsheets.armour import Studded
from charsheets.character import Character
from charsheets.constants import Skill, Stat, Language
from charsheets.features import Expertise, AbilityScoreImprovement, MagicInitiateWizard
from charsheets.origins import Sage
from charsheets.species import Elf, Lineages
from charsheets.classes import Rogue, RogueSoulknife
from charsheets.spell import Spell
from charsheets.weapons import Rapier, Shortbow

character = Character(
    "Nahdria",
    Sage(
        Stat.CONSTITUTION,
        Stat.INTELLIGENCE,
        Stat.WISDOM,
        initiate=MagicInitiateWizard(
            spellcasting_stat=Stat.INTELLIGENCE, cantrip1=Spell.WISH, cantrip2=Spell.WISH, level1=Spell.WISH
        ),
    ),
    Elf(Lineages.DROW, keen_sense=Skill.PERCEPTION, casting_stat=Stat.INTELLIGENCE),
    language1=Language.COMMON_SIGN,
    language2=Language.HALFLING,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=10,
    charisma=8,
)
character.extras = {}
character.player_name = "Shae"
character.add_level(
    Rogue(
        skills=[Skill.DECEPTION, Skill.INVESTIGATION, Skill.PERCEPTION, Skill.STEALTH],
        expertise=Expertise(Skill.DECEPTION, Skill.STEALTH),
        language=Language.GOBLIN,
    )
)

character.add_level(Rogue(hp=2))  # Level 2
character.add_level(RogueSoulknife(hp=8))  # Level 3
character.add_level(RogueSoulknife(hp=3, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.CHARISMA)))  # Level 4
character.add_level(RogueSoulknife(hp=7))  # Level 5
character.add_level(RogueSoulknife(hp=2, expertise=Expertise(Skill.SLEIGHT_OF_HAND, Skill.PERCEPTION)))  # Level 6
character.add_level(RogueSoulknife(hp=4))  # Level 7

character.add_weapon(Rapier())
character.add_weapon(Shortbow())
character.wear_armour(Studded())
