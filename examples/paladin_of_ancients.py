from charsheets.armour import Plate, Shield
from charsheets.character import Character
from charsheets.classes import PaladinOathOfAncients, Paladin
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, HeavyArmorMaster
from charsheets.origins import Wayfairer
from charsheets.species import Tiefling, Legacy
from charsheets.weapons import Musket, Scimitar

character = Character(
    "Filoph",
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
character.add_level(Paladin(hp=6))
character.add_level(PaladinOathOfAncients(hp=7))
character.add_level(PaladinOathOfAncients(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CHARISMA)))
character.add_level(PaladinOathOfAncients(hp=8))
character.add_level(PaladinOathOfAncients(hp=6))
character.add_level(PaladinOathOfAncients(hp=6))
character.add_level(PaladinOathOfAncients(hp=8, feat=HeavyArmorMaster(Stat.CONSTITUTION)))
character.add_level(PaladinOathOfAncients(hp=4))
character.add_level(PaladinOathOfAncients(hp=10))
character.add_level(PaladinOathOfAncients(hp=10))
character.add_level(PaladinOathOfAncients(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CHARISMA)))
character.add_level(PaladinOathOfAncients(hp=5))

character.add_weapon(Musket())
character.add_weapon(Scimitar(dmg_bonus=1, atk_bonus=1, name="Scimitar +1"))
character.wear_armour(Plate(ac_bonus=1, name="Plate +1"))
character.wear_shield(Shield(name="Basher", ac_bonus=1))
