# RAOEUS Plover Dictionaries (Plover Theory Based)

Clone the contents of the repo directly into the plover configuration folder with `git clone https://github.com/RAOEUS/plover-dictionaries.git` and init submodules with `git submodule update --init --recursive`

My main.json and commands.json dictionaries are just the standard ones that come with Plover, so I have excluded those dictionaries from this repository.

Credit to [@jenchanws](https://gist.github.com/jenchanws/5c8dedb826c775fc2a1521c9b9104ea9) for the raw steno python dictionaries

## Required Plover plugins:

- `plover-dict-commands` for raw mode
- `plover-python-dictionary` for Emily's Modifiers, Emily's Symbols, and raw.py
- `plover-retro-stringop` for retro string alterations in retro.json
- `plover-stitching` for raw mode

## Optional Plover plugins:

- plover-clippy (For the `clippy-monitor.ps1` PowerShell script)
- plover-tapey-tape (For the `tapey-tape-monitor.ps1` PowerShell script)

## modes.json
- Starter chord is SPH- for "**S**witch **M**ode"

| Mode Name   | Chord        | Notes                                                 |
|-------------|--------------|-------------------------------------------------------|
| Reset       | SPH-R        | Resets all modes                                      |
| kebap-case  | SPH-FP       |                                                       |
| camelCase   | SPH-PBLG     |                                                       |
| CAPS        | SPH-PBG      |                                                       |
| lower       | SPH-L        |                                                       |
| snake_case  | SPH-T        | You can still use KPA to capitalize                   |
| nospaces    | SPH-FP       | Very useful for URLs.                                 |
| Title Case  | SPH-T        | You can still use HRO*ER to lowercase                 |
| PascalCase  | SPH-FP/SPH-T | Combined nospaces and Title Case gives you PascalCase |




## retro.json
This dictionary is used with the `plover-retro-stringop` plugin.
- `KWR` is the arbitrary starter chord; it is always pressed.
- `STPH` represent binary numbers. For example, to retroactively change 6 words to camelCase, `TKPWR-B`. `KWR-B` is camelCase, adding `TP` for 6 words.
  - S = 8, T = 4, P = 2, H = 1
- `-R` is snake_case, `-B` is camelCase, `-G` is PascalCase, `-RB` is UPPER_SNAKE_CASE, `-BG` is kebap-case
- As an alternative to using STPH for binary numbers, you can also just repeat it once per word.
  - For example, to change three words to snake_case, `KWR-R/KWR-R/KWR-R` instead of `KPWHR-R`

## Ordering and Enabled/Disabled

The dictionaries should be in a particular order and some should be kept disabled. This is the current order of my dictionaries, and it will be unchecked if it should be left disabled.

This information should already be stored in the plover.cfg (you can simply move this over to your main Plover config directory and then modify it), but if you don't want to use that, this may help you out.

- [x] plover-dictionaries/raw_enter.py [For creating raw steno output]
- [x] plover-dictionaries/raoeus.json
- [x] plover-dictionaries/raoeus-commands.json
- [x] plover-dictionaries/raoeus-text-expansion.json
- [x] plover-dictionaries/emily-symbols/emily-symbols.py
- [x] plover-dictionaries/emily-modifiers/emily-modifiers.py
- [x] plover-dictionaries/retro.json
- [x] plover-dictionaries/text-emoji-western.json
- [x] commands.json
- [x] main.json
- [ ] plover-dictionaries/raw.py [Will be the only enabled dict when raw steno mode is turned on via raw-enter.py]
