from charsheets.armour import Padded
from charsheets.character import Character
from charsheets.classes import BardGlamourCollege, Bard
from charsheets.constants import Skill, Stat, Language
from charsheets.features import Expertise, Telepathic, AbilityScoreImprovement, BoonOfSpellRecall
from charsheets.origins import Guard
from charsheets.species import Orc
from charsheets.spell import Spell
from charsheets.weapons import Sling, Dagger

character = Character(
    "Bascina the Fascinator",
    Guard(Stat.STRENGTH, Stat.INTELLIGENCE, Stat.WISDOM),
    Orc(),
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
character.add_weapon(Sling())
character.add_weapon(Dagger())
character.add_level(Bard(skills=[Skill.HISTORY, Skill.RELIGION, Skill.ANIMAL_HANDLING]))
character.learn_spell(Spell.FRIENDS, Spell.VICIOUS_MOKERY)
character.prepare_spells(Spell.CHARM_PERSON, Spell.COLOR_SPRAY, Spell.DISSONANT_WHISPERS, Spell.HEALING_WORD)

character.add_level(Bard(hp=5, expertise=Expertise(Skill.PERSUASION, Skill.PERFORMANCE)))

character.add_level(BardGlamourCollege(hp=3))
character.learn_spell(Spell.INVISIBILITY, Spell.SILENCE)
character.add_level(BardGlamourCollege(hp=5, feat=Telepathic(Stat.CHARISMA)))
character.add_level(BardGlamourCollege(hp=5))
character.add_level(BardGlamourCollege(hp=6))
character.add_level(BardGlamourCollege(hp=3))
character.add_level(BardGlamourCollege(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.DEXTERITY)))
character.add_level(BardGlamourCollege(hp=5, expertise=Expertise(Skill.INVESTIGATION, Skill.INTIMIDATION)))
character.add_level(BardGlamourCollege(hp=3))
character.add_level(BardGlamourCollege(hp=8))
character.add_level(BardGlamourCollege(hp=5, feat=AbilityScoreImprovement(Stat.CHARISMA, Stat.CHARISMA)))
character.add_level(BardGlamourCollege(hp=5))
character.add_level(BardGlamourCollege(hp=5))
character.add_level(BardGlamourCollege(hp=5))
character.add_level(BardGlamourCollege(hp=5, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.STRENGTH)))
character.add_level(BardGlamourCollege(hp=5))
character.add_level(BardGlamourCollege(hp=5))
character.add_level(BardGlamourCollege(hp=5, boon=BoonOfSpellRecall(Stat.CHARISMA)))
character.add_level(BardGlamourCollege(hp=5))

character.wear_armour(Padded())
