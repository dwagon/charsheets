from charsheets.armour import Scale
from charsheets.character import Character
from charsheets.classes import Bard, BardValorCollege
from charsheets.constants import Skill, Stat, Language
from charsheets.features import Expertise, AbilityScoreImprovement, Speedy, BoonOfSpellRecall
from charsheets.origins import Guard
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell
from charsheets.weapons import LightCrossbow, Rapier

character = Character(
    "Brave Sir Robin",
    Guard(Stat.STRENGTH, Stat.INTELLIGENCE, Stat.WISDOM),
    Elf(Lineages.WOOD_ELF, Skill.PERCEPTION),
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
character.add_weapon(LightCrossbow())
character.add_level(Bard(skills=[Skill.HISTORY, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
character.learn_spell(Spell.FRIENDS, Spell.VICIOUS_MOKERY)
character.prepare_spells(Spell.CHARM_PERSON, Spell.COLOR_SPRAY, Spell.DISSONANT_WHISPERS, Spell.HEALING_WORD)

character.add_level(Bard(hp=5, expertise=Expertise(Skill.PERSUASION, Skill.PERFORMANCE)))
character.learn_spell(Spell.INVISIBILITY, Spell.SILENCE)
character.add_level(BardValorCollege(hp=3))
character.add_level(BardValorCollege(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY)))
character.add_level(BardValorCollege(hp=5))
character.add_level(BardValorCollege(hp=6))
character.add_level(BardValorCollege(hp=3))
character.add_level(BardValorCollege(hp=5, feat=Speedy(Stat.DEXTERITY)))
character.add_level(BardValorCollege(hp=5, expertise=Expertise(Skill.MEDICINE, Skill.NATURE)))
character.add_level(BardValorCollege(hp=3))
character.add_level(BardValorCollege(hp=8))
character.add_level(BardValorCollege(hp=6, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY)))
character.add_level(BardValorCollege(hp=5))
character.add_level(BardValorCollege(hp=5))
character.add_level(BardValorCollege(hp=5))
character.add_level(BardValorCollege(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
character.add_level(BardValorCollege(hp=5))
character.add_level(BardValorCollege(hp=5))
character.add_level(BardValorCollege(hp=5, boon=BoonOfSpellRecall(Stat.CHARISMA)))
character.add_level(BardValorCollege(hp=5))

character.wear_armour(Scale())
character.add_weapon(Rapier())
