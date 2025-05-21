from charsheets.armour import Unarmoured
from charsheets.character import Character
from charsheets.classes import Monk, MonkWarriorOfTheOpenHand
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, MagicInitiateWizard, WeaponMaster, BoonOfIrresistibleOffense
from charsheets.origins import Sage
from charsheets.species import Elf, Lineages
from charsheets.spell import Spell

character = Character(
    "Justine the Slapper",
    Sage(
        Stat.INTELLIGENCE,
        Stat.CONSTITUTION,
        Stat.WISDOM,
        MagicInitiateWizard(Stat.WISDOM, Spell.MESSAGE, Spell.MAGE_HAND, Spell.MAGIC_MISSILE),
    ),
    Elf(Lineages.HIGH_ELF, Skill.INSIGHT, Stat.WISDOM),
    Language.ELVISH,
    Language.GNOMISH,
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=10,
    wisdom=14,
    charisma=8,
)

character.player_name = "Phi"
character.extras = {"hair": "bald", "alignment": "LG"}
character.add_level(Monk(skills=[Skill.HISTORY, Skill.RELIGION]))
character.add_level(Monk(hp=5))
character.add_level(MonkWarriorOfTheOpenHand(hp=6))
character.add_level(MonkWarriorOfTheOpenHand(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
character.add_level(MonkWarriorOfTheOpenHand(hp=6))
character.add_level(MonkWarriorOfTheOpenHand(hp=5))
character.add_level(MonkWarriorOfTheOpenHand(hp=4))
character.add_level(MonkWarriorOfTheOpenHand(hp=7, feat=WeaponMaster(Stat.DEXTERITY)))
character.add_level(MonkWarriorOfTheOpenHand(hp=4))
character.add_level(MonkWarriorOfTheOpenHand(hp=4))
character.add_level(MonkWarriorOfTheOpenHand(hp=8))
character.add_level(MonkWarriorOfTheOpenHand(hp=7, feat=AbilityScoreImprovement(Stat.DEXTERITY, Stat.DEXTERITY)))
character.add_level(MonkWarriorOfTheOpenHand(hp=5))
character.add_level(MonkWarriorOfTheOpenHand(hp=5))
character.add_level(MonkWarriorOfTheOpenHand(hp=5))
character.add_level(MonkWarriorOfTheOpenHand(hp=7, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.INTELLIGENCE)))
character.add_level(MonkWarriorOfTheOpenHand(hp=5))
character.add_level(MonkWarriorOfTheOpenHand(hp=5))
character.add_level(MonkWarriorOfTheOpenHand(hp=5, boon=BoonOfIrresistibleOffense(Stat.DEXTERITY)))
character.add_level(MonkWarriorOfTheOpenHand(hp=5))

character.wear_armour(Unarmoured())
character.add_equipment("Packed Lunch", "Ointment")
