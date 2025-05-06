[![Coverage Status](https://coveralls.io/repos/github/dwagon/charsheets/badge.svg)](https://coveralls.io/github/dwagon/charsheets)

Generate DND 5E character sheets based on traceable decisions.

Uses https://github.com/matsavage/DND-5e-LaTeX-Character-Sheet-Template to do the actual rendering

Lots of examples in the '`examples`' directory.

## Process
I highly recommend using a language aware editor like PyCharm to understand all the arguments to the functions,
lists of features, etc.

### Define the person
Start by defining the person (must be assigned to `character` variable).

By default, this will generate a 2024 style character.
``` python
from charsheets.character import Character
from charsheets.origins import Entertainer
from charsheets.species import Dwarf

 character = Character(
      name="Desmond",
      origin=Entertainer(Stat.DEXTERITY, Stat.DEXTERITY, Stat.CHARISMA),
      species=Dwarf(),
      language1=Language.DWARVISH,
      language2=Language.ORC,
      strength=12,
      dexterity=15,
      constitution=13,
      intelligence=14,
      wisdom=10,
      charisma=8,
  )
```

A character must have:
* a name,
* an origin (which defines a number of stats to boost, amongst other things),
* a couple of languages to learn,
* standard stats

### Add the classes
``` python
character.add_level(Cleric(skills=[Skill.MEDICINE, Skill.HISTORY]))
```

The first level you add you need to define a couple of skills.

### Add some equipment
``` python
character.wear_armour(Breastplate())
character.wear_shield(Shield())
character.add_equipment("Packed lunch")
```

### Keep adding classes as you level up
``` python
character.add_level(Cleric(hp=8))
```

### Define choices made
``` python
character.add_level(ClericWarDomain(hp=3, feat=AbilityScoreImprovement(Stat.STRENGTH, Stat.DEXTERITY)))
character.prepare_spell(Spell.AID)
```

### Generate TeX
```bash
./charsheets/main.py desmond.py > ../DND-5e-LaTeX-Character-Sheet-Template/characters/desmond.tex
```
The TeX file will also have the reasons behind various values. For example:
```  tex
\DexterityScore{16}  % Origin charlatan (2) + Base (12) + AbilityScoreImprovement (2)
```


### Generate PDF
```bash
latexmk -pdf -lualatex characters/desmond.tex
```

## 2014 Character Sheets
A similar process is used for 2014 characters, just with `race` instead of `species` and `background` instead of 
`origin`.

``` python
character = Character2014(
    name="Fingers",
    background=Entertainer(),
    race=HalfElf(language=Language.ORC, stat1=Stat.DEXTERITY, stat2=Stat.INTELLIGENCE, skill1=Skill.ACROBATICS, skill2=Skill.ATHLETICS),
    strength=12,
    dexterity=15,
    constitution=13,
    intelligence=14,
    wisdom=10,
    charisma=8,
)
```

### 2014 Classes
You have to use different classes
``` python
from charsheets.classes2014 import Rogue
```
instead of
```python
from charsheets.classes import Rogue
```