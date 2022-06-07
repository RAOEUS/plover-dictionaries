# RAOEUS Plover Dictionaries

Pull this repo directly into your Plover configuration directory in AppData

My main.json and commands.json dictionaries are just the standard ones that come with Plover.

Credit to [@jenchanws](https://gist.github.com/jenchanws/5c8dedb826c775fc2a1521c9b9104ea9) for the raw steno python dictionaries

## Required Plover plugins:

- plover-dict-commands
- plover-fancy-text
- plover-python-dictionary
- plover-retro-stringop
- plover-stitching

## Ordering and Enabled/Disabled

The dictionaries should be in a particular order and some should be kept disabled. This is the current order of my dictionaries, and it will be unchecked if it should be left disabled. 

- [x] raw_enter.py [For creating raw steno output]
- [ ] caps-on.json [For when MODE:CAPS is enabled]
- [x] user.json 
- [x] user-commands.json
- [x] fancy-text.json
- [x] plover-retro-string-op.json
- [x] commands.json
- [x] main.json
- [ ] raw.py [Will be the only enabled dict when raw steno mode is turned on via raw-enter.py]
