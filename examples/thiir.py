from typing import cast

from charsheets.armour import Leather
from charsheets.character import Character
from charsheets.classes import WarlockOldOne, Warlock
from charsheets.classes.warlock import AgonizingBlast, MaskOfManyFaces, PactOfTheTome, MasterOfMyriadForms, OneWithShadows
from charsheets.constants import Skill, Stat, Language, DamageType
from charsheets.features import AbilityScoreImprovement
from charsheets.origins import Hermit
from charsheets.species.homebrew.kuatoa import Kuatoa
from charsheets.spell import Spell
from charsheets.spells import EldritchBlast

character = Character(
    "Thiir",
    Hermit(
        Stat.CHARISMA,
        Stat.CHARISMA,
        Stat.CONSTITUTION,
    ),
    Kuatoa(),
    Language.AQUAN,
    cast(Language, Language.DEEP_SPEECH),
    strength=8,
    dexterity=12,
    constitution=14,
    intelligence=10,
    wisdom=13,
    charisma=15,
    bonds="Everything I do is for the common people",
    flaws="Unquestioning loyalty to my patron and God",
    ideals="We must help bring about the changes that the Gods are constantly working on in the world",
    traits="I am intolerant of other faiths and condemn the worship of other Gods",
    age=40,
    height="5'2",
    weight="100lb",
    skin="Bone White",
    hair="None",
    alignment="CE",
    image="characters/images/thiir.png",
    player_name="Jesse",
)

character.add_level(Warlock(skills=[Skill.RELIGION, Skill.DECEPTION], add_invocation=AgonizingBlast(Spell.ELDRITCH_BLAST)))
# character.add_spell_attack(Spell.ELDRITCH_BLAST, 7, "1d10", 4, DamageType.FORCE)
character.add_spell_details(EldritchBlast())
character.learn_spell(Spell.ELDRITCH_BLAST, Spell.MAGE_HAND)
character.wear_armour(Leather())
character.add_level(
    Warlock(
        hp=5,
        add_invocation=[
            PactOfTheTome(Spell.TOLL_THE_DEAD, Spell.MIND_SLIVER, Spell.BLADE_WARD, Spell.ALARM, Spell.FIND_FAMILIAR),
            MaskOfManyFaces(),
        ],
    )
)
character.add_level(WarlockOldOne(hp=4))
character.add_level(WarlockOldOne(hp=8, feat=AbilityScoreImprovement(Stat.WISDOM, Stat.CHARISMA)))
character.learn_spell(Spell.MINOR_ILLUSION)

character.add_level(WarlockOldOne(hp=5, add_invocation=[MasterOfMyriadForms(), OneWithShadows()]))
character.learn_spell(Spell.ARMOR_OF_AGATHYS, Spell.HEX, Spell.SUGGESTION, Spell.INVISIBILITY, Spell.MISTY_STEP)

character.add_equipment(
    "Leather Armor",
    "Scroll Case (Notes and Prayers)",
    "Common Clothes",
    "Arcane Focus (Sacred Water Flask)",
    "Herbalism Kit x8",
    "Healing Potion",
    "Crowbar",
    "Hammer",
    "Pitons x10",
    "Torches x10",
    "Tinder Box",
    "Rations x3",
    "Waterskin",
    "50ft Hempen Rope",
    "Eel Eggs x11",
    "Small Purple Mushrooms x10",
)
character.add_treasure(
    "Tetrahedron ('The Chime' from the Drowned Temple)",
    "Jewellery Box",
    "Small Gem (50g)",
    "Sketch of path to Temple of Ungulas",
    "Davach Mask",
)
character.extras = {"gp": "307"}
