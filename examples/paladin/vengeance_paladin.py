from charsheets.armour import Plate, Shield
from charsheets.character import Character
from charsheets.classes import PaladinOathOfVengeance, Paladin
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, MountedCombatant, Defense, BoonOfTruesight
from charsheets.origins import Wayfairer
from charsheets.species import Dragonborn, Ancestor
from charsheets.weapons import Musket, Scimitar

character = Character(
    "Inigo",
    Wayfairer(Stat.WISDOM, Stat.CHARISMA, Stat.CHARISMA),
    Dragonborn(Ancestor.BRONZE),
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
character.add_level(Paladin(skills=[Skill.INSIGHT, Skill.RELIGION]))
character.add_level(Paladin(hp=6, style=Defense()))
character.add_level(PaladinOathOfVengeance(hp=7))
character.add_level(PaladinOathOfVengeance(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CHARISMA)))
character.add_level(PaladinOathOfVengeance(hp=8))
character.add_level(PaladinOathOfVengeance(hp=6))
character.add_level(PaladinOathOfVengeance(hp=6))
character.add_level(PaladinOathOfVengeance(hp=8, feat=MountedCombatant(Stat.STRENGTH)))
character.add_level(PaladinOathOfVengeance(hp=4))
character.add_level(PaladinOathOfVengeance(hp=10))
character.add_level(PaladinOathOfVengeance(hp=10))
character.add_level(PaladinOathOfVengeance(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CHARISMA)))
character.add_level(PaladinOathOfVengeance(hp=5))
character.add_level(PaladinOathOfVengeance(hp=8))
character.add_level(PaladinOathOfVengeance(hp=8))
character.add_level(PaladinOathOfVengeance(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.STRENGTH)))
character.add_level(PaladinOathOfVengeance(hp=6))
character.add_level(PaladinOathOfVengeance(hp=6))
character.add_level(PaladinOathOfVengeance(hp=6, boon=BoonOfTruesight(Stat.STRENGTH)))
character.add_level(PaladinOathOfVengeance(hp=6))


character.add_weapon(Musket())
character.add_weapon(Scimitar(dmg_bonus=1, atk_bonus=1, name="Scimitar +1"))
character.wear_armour(Plate(ac_bonus=1, name="Plate +1"))
character.wear_shield(Shield(name="Basher", ac_bonus=1))
