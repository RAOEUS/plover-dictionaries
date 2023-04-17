# RAOEUS Plover Dictionaries

Copy the contents of the repo directly into the plover configuration folder

My main.json and commands.json dictionaries are just the standard ones that come with Plover, so I have excluded those dictionaries from this repository.

Credit to [@jenchanws](https://gist.github.com/jenchanws/5c8dedb826c775fc2a1521c9b9104ea9) for the raw steno python dictionaries

Credit to [@EPLHREU](https://github.com/EPLHREU) for the symbols dictionary

Credit to [@jthlim](https://github.com/jthlim) for the numbers & modifiers dictionary

## Required Plover plugins:

- plover-dict-commands
- plover-fancy-text
- plover-python-dictionary
- plover-retro-stringop
- plover-stitching

## Optional Plover plugins:

- plover-clippy (For the `clippy-monitor.ps1` PowerShell script)
- plover-tapey-tape (For the `tapey-tape-monitor.ps1` PowerShell script)

## Ordering and Enabled/Disabled

The dictionaries should be in a particular order and some should be kept disabled. This is the current order of my dictionaries, and it will be unchecked if it should be left disabled.

This information should already be stored in the plover.cfg (you can simply move this over to your main Plover config directory and then modify it), but if you don't want to use that, this may help you out.

- [x] plover-dictionaries/raw_enter.py [For creating raw steno output]
- [ ] plover-dictionaries/caps-on.json [For when MODE:CAPS is enabled]
- [x] plover-dictionaries/raoeus.json
- [x] plover-dictionaries/raoeus-commands.json
- [x] plover-dictionaries/jeff-numbers.py
- [x] plover-dictionaries/jeff-modifiers.py
- [x] plover-dictionaries/emily-symbols.py
- [x] plover-dictionaries/fancy-text.json
- [x] plover-dictionaries/plover-retro-string-op.json
- [x] commands.json
- [x] main.json
- [ ] plover-dictionaries/raw.py [Will be the only enabled dict when raw steno mode is turned on via raw-enter.py]
