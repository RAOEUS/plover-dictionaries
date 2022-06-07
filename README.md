# RAOEUS Plover Dictionaries

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

This information should already be stored in the plover.cfg when it is pulled to your Plover configuration directory, but if you don't want to use that, this may help you out.

- [x] dicts/raw_enter.py [For creating raw steno output]
- [ ] dicts/caps-on.json [For when MODE:CAPS is enabled]
- [x] dicts/raoeus.json 
- [x] dicts/raoeus-commands.json
- [x] dicts/fancy-text.json
- [x] dicts/plover-retro-string-op.json
- [x] commands.json
- [x] main.json
- [ ] dict/sraw.py [Will be the only enabled dict when raw steno mode is turned on via raw-enter.py]
