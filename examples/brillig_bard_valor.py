from charsheets.armour import Scale
from charsheets.classes import BardValorCollege
from charsheets.constants import Skill, Stat, Language
from charsheets.features import Expertise, AbilityScoreImprovement, Speedy
from charsheets.origins import Guard
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell
from charsheets.weapons import LightCrossbow, Rapier

character = BardValorCollege(
    "Brillig",
    Guard(Stat.STRENGTH, Stat.INTELLIGENCE, Stat.WISDOM),
    Elf(Lineages.WOOD_ELF, Skill.PERCEPTION),
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
character.add_weapon(LightCrossbow())
character.level1()
character.learn_spell(Spell.FRIENDS, Spell.VICIOUS_MOKERY)
character.prepare_spells(Spell.CHARM_PERSON, Spell.COLOR_SPRAY, Spell.DISSONANT_WHISPERS, Spell.HEALING_WORD)

character.level2(hp=5, expertise=Expertise(Skill.PERSUASION, Skill.PERFORMANCE))
character.learn_spell(Spell.INVISIBILITY, Spell.SILENCE)
character.level3(hp=3)
character.level4(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY))
character.level5(hp=5)
character.level6(hp=6)
character.level7(hp=3)
character.level8(hp=5, feat=Speedy(Stat.DEXTERITY))
character.level9(hp=5, expertise=Expertise(Skill.MEDICINE, Skill.NATURE))
character.level10(hp=3)

character.wear_armour(Scale())
character.add_weapon(Rapier())
character.add_languages(Language.ELVISH, Language.ORC)
