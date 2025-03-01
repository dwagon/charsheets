from charsheets.armour import Padded
from charsheets.classes import BardLoreCollege, BonusProficiencies, MagicalDiscoveries
from charsheets.constants import Skill, Stat, Language
from charsheets.features import Expertise, AbilityScoreImprovement, Poisoner
from charsheets.origins import Guard
from charsheets.species import Human, Skillful, Versatile
from charsheets.spell import Spell
from charsheets.weapons import Shortbow, Quarterstaff

character = BardLoreCollege(
    "Brillig",
    Guard(Stat.STRENGTH, Stat.INTELLIGENCE, Stat.WISDOM),
    Human(Skillful(Skill.ANIMAL_HANDLING), Versatile(Poisoner(Stat.DEXTERITY))),
    Skill.HISTORY,
    Skill.RELIGION,
    Skill.ANIMAL_HANDLING,
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
character.level1()
character.learn_spell(Spell.FRIENDS, Spell.VICIOUS_MOKERY)
character.prepare_spells(Spell.CHARM_PERSON, Spell.COLOR_SPRAY, Spell.DISSONANT_WHISPERS, Spell.HEALING_WORD)

character.level2(hp=5, expertise=Expertise(Skill.PERSUASION, Skill.PERFORMANCE))
character.level3(hp=3, bonus=BonusProficiencies(Skill.MEDICINE, Skill.NATURE, Skill.SURVIVAL))
character.learn_spell(Spell.INVISIBILITY, Spell.SILENCE)
character.level4(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY))
character.level5(hp=5)
character.level6(hp=6, bonus=MagicalDiscoveries(Spell.MAGIC_MISSILE, Spell.LIGHT))
character.level7(hp=3)
character.level8(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.INTELLIGENCE))
character.level9(hp=5, expertise=Expertise(Skill.HISTORY, Skill.INVESTIGATION))
character.level10(hp=3)
character.level11(hp=8)

character.wear_armour(Padded())
character.add_languages(Language.ELVISH, Language.ORC)
