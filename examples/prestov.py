from charsheets.armour import Plate
from charsheets.classes import PaladinOathOfVengeance
from charsheets.constants import Skill, Stat
from charsheets.origins import Wayfairer
from charsheets.species import Tiefling, Legacy
from charsheets.weapons import Musket, Scimitar
from charsheets.feats import AbilityScoreImprovement


character = PaladinOathOfVengeance(
    "Prestov",
    Wayfairer(Stat.WISDOM, Stat.CHARISMA, Stat.CHARISMA),
    Tiefling(Legacy.CHTHONIC),
    Skill.INSIGHT,
    Skill.RELIGION,
    strength=15,
    dexterity=10,
    constitution=13,
    intelligence=8,
    wisdom=12,
    charisma=14,
)
character.extras = {"alignment": "N", "image": "characters/images/aaliyah.jpg"}
character.player_name = "Epsilon"
character.level2(hp=6)
character.level3(hp=7)
character.level4(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CHARISMA, character))
character.level5(hp=8)


character.add_weapon(Musket())
character.add_weapon(Scimitar(dmg_bonus=1, atk_bonus=1, name="Scimitar +1"))
character.wear_armour(Plate(ac_bonus=1, name="Plate +1"))
character.shield = True
