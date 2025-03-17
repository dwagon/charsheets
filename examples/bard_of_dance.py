from charsheets.armour import Padded
from charsheets.classes import BardDanceCollege
from charsheets.constants import Skill, Stat, Language
from charsheets.features import Expertise, ShadowTouched, AbilityScoreImprovement
from charsheets.origins import Guard
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell
from charsheets.weapons import LightCrossbow, Sickle

character = BardDanceCollege(
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
character.add_weapon(LightCrossbow())
character.add_weapon(Sickle())
character.level1()
character.learn_spell(Spell.FRIENDS, Spell.VICIOUS_MOKERY)
character.prepare_spells(Spell.CHARM_PERSON, Spell.COLOR_SPRAY, Spell.DISSONANT_WHISPERS, Spell.HEALING_WORD)

character.level2(hp=5, expertise=Expertise(Skill.PERSUASION, Skill.PERFORMANCE))
character.learn_spell(Spell.INVISIBILITY, Spell.SILENCE)
character.level3(hp=3)
character.level4(hp=6, feat=ShadowTouched(Spell.WRATHFUL_SMITE, Stat.CHARISMA))
character.level5(hp=5)
character.level6(hp=6)
character.level7(hp=3)
character.level8(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY))
character.level9(hp=5, expertise=Expertise(Skill.ACROBATICS, Skill.ATHLETICS))
character.level10(hp=3)
character.level11(hp=8)
character.level12(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY))
character.level13(hp=5)


character.wear_armour(Padded())
character.add_languages(Language.ELVISH, Language.ORC)
