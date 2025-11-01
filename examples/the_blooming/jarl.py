#
from charsheets.armour import Studded
from charsheets.character import Character
from charsheets.classes import Fighter, FighterChampion
from charsheets.constants import Skill, Stat, Language
from charsheets.features import FeyTouched, AbilityScoreImprovement, MagicInitiateDruid, Alert, Defense
from charsheets.origins import Guide
from charsheets.species import Human, Skillful, Versatile
from charsheets.spell import Spell
from charsheets.weapons import Longsword, Shortbow

character = Character(
    "Jarl",
    Guide(
        Stat.DEXTERITY,
        Stat.CONSTITUTION,
        Stat.CONSTITUTION,
        initiate=MagicInitiateDruid(Stat.WISDOM, Spell.DRUIDCRAFT, Spell.POISON_SPRAY, Spell.CURE_WOUNDS),
    ),
    Human(skillful=Skillful(Skill.SURVIVAL), versatile=Versatile(Alert())),
    Language.ELVISH,
    Language.ORC,
    strength=16,
    dexterity=14,
    constitution=13,
    intelligence=10,
    wisdom=12,
    charisma=8,
)
character.extras = {
    "eyes": "brown",
    "hair": "black",
    "height": "6'1",
    "alignment": "LG",
    "age": "120",
    "skin": "yes",
    "image": "characters/images/jarl.jpg",
}
character.add_level(Fighter(skills=[Skill.STEALTH, Skill.SURVIVAL], style=Defense()))
character.add_level(Fighter(hp=7))
character.add_level(FighterChampion(hp=6))
character.add_level(FighterChampion(hp=4, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION)))
character.add_level(FighterChampion(hp=9))
character.add_level(FighterChampion(hp=10, feat=FeyTouched(Spell.DETECT_POISON_AND_DISEASE, Stat.WISDOM)))


character.wear_armour(Studded())
character.add_weapon(Longsword())
character.add_weapon(Shortbow())

# EOF
