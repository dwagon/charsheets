from charsheets.armour import Padded
from charsheets.classes import BardLoreCollege, BonusProficiencies
from charsheets.constants import Skill, Stat, Language, Weapon
from charsheets.features import Expertise
from charsheets.origins import Guard
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell
from charsheets.weapons import Shortbow, Quarterstaff

character = BardLoreCollege(
    "Brillig",
    Guard(Stat.STRENGTH, Stat.INTELLIGENCE, Stat.WISDOM),
    Elf(Lineages.DROW, Skill.PERCEPTION),
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


character.wear_armour(Padded())
character.add_languages(Language.ELVISH, Language.ORC)
