import re
import json

LONGEST_KEY = 5
starter = "SKWR"
dictionary_path = "dicts/aerick/lapwing-prefixed-proper-nouns.json"

def change_starter(dictionary_file, starter):
    modified_dictionary = {}
    with open("/home/zach/.config/plover/" + dictionary_file) as temp_dictionary:
        temp_dictionary = json.load(temp_dictionary)
        for stroke in temp_dictionary:
            outline = temp_dictionary[stroke]
            if len(stroke) > 1 and stroke.startswith('#/'):
                new_stroke = starter + '/' + stroke[2:]  # Replace #/ with starter/
                modified_dictionary[new_stroke] = outline
            else:
                modified_dictionary[stroke] = outline

    return modified_dictionary

modified_dictionary = change_starter(dictionary_path, starter)

def lookup(strokes):
    return modified_dictionary[strokes]

def reverse_lookup(outline):
    return [key for key, value in modified_dictionary.items() if value == outline]

# Testing the lookup and reverse_lookup functions
# print(lookup(starter + '/' + 'SABG'))
# print(reverse_lookup("Zach")) # okay huh

