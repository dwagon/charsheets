#
from charsheets.constants import CharSpecies, Armour, Weapon, Origin, Skill
from charsheets.classes.fighter import Fighter

character = Fighter(
    "Freya",
    Origin.CRIMINAL,
    CharSpecies.GOLIATH,
    Skill.ACROBATICS,
    Skill.INSIGHT,
    strength=16,
    dexterity=14,
    constitution=15,
    intelligence=10,
    wisdom=10,
    charisma=12,
)
character.player_name = "Delta"
character.extras = {
    "eyes": "yellow",
    "hair": "purple",
    "height": "7'5",
    "alignment": "CN",
    "image": "characters/images/freya.png",
    "age": "20",
}
character.add_level(hp=9)
character.add_level(hp=7)
character.add_level(hp=9)
character.armour = Armour.RING
character.shield = False
character.add_weapon(Weapon.MAUL)
character.languages = {"Common", "Dwarvish"}
character.add_equipment("Stuff", "More Stuff")
character.add_equipment("Packed lunch")

# feats = {Feat.ALERT, Feat.UNARMED_FIGHTING}
