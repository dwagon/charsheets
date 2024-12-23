from charsheets.classes import PathOfTheBeserker
from charsheets.constants import Skill, Armour, Weapon, Stat
from charsheets.origins import Artisan
from charsheets.species.dwarf import Dwarf
from charsheets.abilities.feat import AbilityScoreImprovement


character = PathOfTheBeserker(
    "Rugor",
    Artisan(Stat.STRENGTH, Stat.STRENGTH, Stat.STRENGTH),
    Dwarf(),
    Skill.INTIMIDATION,
    Skill.ATHLETICS,
    strength=15,
    dexterity=13,
    constitution=14,
    intelligence=10,
    wisdom=12,
    charisma=8,
)


character.player_name = "Beta"
character.level2(hp=8)
character.level3(hp=5)
character.level4(hp=8, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.CONSTITUTION))
character.armour = Armour.SCALE
character.shield = True
character.add_weapon(Weapon.SHORTBOW)
character.add_weapon(Weapon.WARHAMMER)
character.extras = {"hair": "bushy"}
