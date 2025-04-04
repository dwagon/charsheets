from charsheets.armour import Padded
from charsheets.character import Character
from charsheets.classes import BardLoreCollege, BonusProficiencies, MagicalDiscoveries, Bard
from charsheets.constants import Skill, Stat, Language
from charsheets.features import Expertise, AbilityScoreImprovement, Poisoner
from charsheets.origins import Guard
from charsheets.species import Human, Skillful, Versatile
from charsheets.spell import Spell
from charsheets.weapons import Shortbow, Quarterstaff

character = Character(
    "Ara Librarysmith",
    Guard(Stat.STRENGTH, Stat.INTELLIGENCE, Stat.WISDOM),
    Human(Skillful(Skill.ANIMAL_HANDLING), Versatile(Poisoner(Stat.DEXTERITY))),
    Language.ELVISH,
    Language.ORC,
    strength=8,
    dexterity=14,
    constitution=12,
    intelligence=13,
    wisdom=10,
    charisma=15,
)

character.player_name = "Iota"
character.extras = {"hair": "greasy", "alignment": "CE"}
character.add_weapon(Shortbow())
character.add_weapon(Quarterstaff())
character.add_level(Bard(skills=[Skill.HISTORY, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
character.learn_spell(Spell.FRIENDS, Spell.VICIOUS_MOKERY)
character.prepare_spells(Spell.CHARM_PERSON, Spell.COLOR_SPRAY, Spell.DISSONANT_WHISPERS, Spell.HEALING_WORD)

character.add_level(Bard(hp=5, expertise=Expertise(Skill.PERSUASION, Skill.PERFORMANCE)))
character.add_level(BardLoreCollege(hp=3, bonus=BonusProficiencies(Skill.MEDICINE, Skill.NATURE, Skill.SURVIVAL)))
character.learn_spell(Spell.INVISIBILITY, Spell.SILENCE)
character.add_level(BardLoreCollege(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY)))
character.add_level(BardLoreCollege(hp=5))
character.add_level(BardLoreCollege(hp=6, bonus=MagicalDiscoveries(Spell.MAGIC_MISSILE, Spell.LIGHT)))
character.add_level(BardLoreCollege(hp=3))
character.add_level(BardLoreCollege(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.INTELLIGENCE)))
character.add_level(BardLoreCollege(hp=5, expertise=Expertise(Skill.HISTORY, Skill.INVESTIGATION)))
character.add_level(BardLoreCollege(hp=3))
character.add_level(BardLoreCollege(hp=8))
character.add_level(BardLoreCollege(hp=7, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.INTELLIGENCE)))
character.learn_spell(Spell.TRUE_SEEING, Spell.SEEMING)
character.add_level(BardLoreCollege(hp=5))


character.wear_armour(Padded())
