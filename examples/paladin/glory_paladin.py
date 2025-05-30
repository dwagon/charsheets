from charsheets.armour import Plate, Shield
from charsheets.character import Character
from charsheets.classes import Paladin, PaladinOathOfGlory, BlessedWarrior
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, Piercer, BoonOfTruesight
from charsheets.origins import Wayfairer
from charsheets.species import Tiefling, Legacy
from charsheets.spell import Spell
from charsheets.weapons import Musket, Scimitar
from charsheets.items import BeltOfStormGiantStrength

character = Character(
    "Sir Quench",
    Wayfairer(Stat.WISDOM, Stat.CHARISMA, Stat.CHARISMA),
    Tiefling(Legacy.CHTHONIC, Stat.CHARISMA),
    Language.INFERNAL,
    Language.GOBLIN,
    strength=15,
    dexterity=10,
    constitution=13,
    intelligence=8,
    wisdom=12,
    charisma=14,
)
character.extras = {"alignment": "N", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Epsilon"
character.add_level(Paladin(skills=[Skill.INSIGHT, Skill.RELIGION]))
character.add_level(Paladin(hp=6, style=BlessedWarrior(Spell.GUIDANCE, Spell.SPARE_THE_DYING)))
character.add_level(PaladinOathOfGlory(hp=7))
character.add_level(PaladinOathOfGlory(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CHARISMA)))
character.add_level(PaladinOathOfGlory(hp=8))
character.add_level(PaladinOathOfGlory(hp=6))
character.add_level(PaladinOathOfGlory(hp=6))
character.add_level(PaladinOathOfGlory(hp=8, feat=Piercer(Stat.STRENGTH)))
character.add_level(PaladinOathOfGlory(hp=4))
character.add_level(PaladinOathOfGlory(hp=10))
character.add_level(PaladinOathOfGlory(hp=10))
character.add_level(PaladinOathOfGlory(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CHARISMA)))
character.add_level(PaladinOathOfGlory(hp=5))
character.add_level(PaladinOathOfGlory(hp=5))
character.add_level(PaladinOathOfGlory(hp=5))
character.add_level(PaladinOathOfGlory(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CHARISMA)))
character.add_level(PaladinOathOfGlory(hp=5))
character.add_level(PaladinOathOfGlory(hp=5))
character.use_item(BeltOfStormGiantStrength())
character.add_level(PaladinOathOfGlory(hp=5, boon=BoonOfTruesight(Stat.STRENGTH)))
character.add_level(PaladinOathOfGlory(hp=5))

character.add_weapon(Musket())
character.add_weapon(Scimitar(dmg_bonus=1, atk_bonus=1, name="Scimitar +1"))
character.wear_armour(Plate(ac_bonus=1, name="Plate +1"))
character.wear_shield(Shield(name="Basher", ac_bonus=1))
