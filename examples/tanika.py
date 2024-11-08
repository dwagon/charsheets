from charsheets.constants import CharClassName, CharSpecies, Origin, WeaponType, Armour, Skill

char_class = CharClassName.DRUID
name = "Tanika"
player = "Alpha"
level = 4
hp = 30
origin = Origin.NOBLE
species = CharSpecies.ELF
strength = 8
dexterity = 12
constitution = 14
intelligence = 14
wisdom = 16
charisma = 12
alignment = "Neutral"
image = "characters/images/aaliyah.jpg"
weapons = {WeaponType.SICKLE, WeaponType.SHORTBOW}
skill_proficiencies = {Skill.INSIGHT, Skill.PERCEPTION, Skill.SURVIVAL}
other_proficiencies = ["Dragonchess", "Herbalism"]
languages = ["Common"]
armour = Armour.LEATHER
shield = True
