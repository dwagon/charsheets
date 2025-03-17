from charsheets.armour import Plate, Shield
from charsheets.classes import PaladinOathOfAncients
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement, HeavyArmorMaster
from charsheets.origins import Wayfairer
from charsheets.species import Tiefling, Legacy
from charsheets.weapons import Musket, Scimitar

character = PaladinOathOfAncients(
    "Filoph",
    Wayfairer(Stat.WISDOM, Stat.CHARISMA, Stat.CHARISMA),
    Tiefling(Legacy.CHTHONIC, Stat.CHARISMA),
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
character.level1()
character.level2(hp=6)
character.level3(hp=7)
character.level4(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CHARISMA))
character.level5(hp=8)
character.level6(hp=6)
character.level7(hp=6)
character.level8(hp=8, feat=HeavyArmorMaster(Stat.CONSTITUTION))
character.level9(hp=4)
character.level10(hp=10)
character.level11(hp=10)
character.level12(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CHARISMA))
character.level13(hp=5)

character.add_languages(Language.INFERNAL, Language.GOBLIN)
character.add_weapon(Musket())
character.add_weapon(Scimitar(dmg_bonus=1, atk_bonus=1, name="Scimitar +1"))
character.wear_armour(Plate(ac_bonus=1, name="Plate +1"))
character.wear_shield(Shield(name="Basher", ac_bonus=1))
