from charsheets.constants import CharClassName, CharSpecies, Origin, Weapon, Armour, Skill

char_class = CharClassName.DRUID
name = "Tanika"
player_name = "Alpha"
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
weapons = {Weapon.DAGGER, Weapon.SHORTBOW}
skill_proficiencies = {Skill.INSIGHT, Skill.PERCEPTION, Skill.SURVIVAL}
other_proficiencies = ["Dragonchess", "Herbalism"]
languages = ["Common"]
armour = Armour.LEATHER
shield = True
