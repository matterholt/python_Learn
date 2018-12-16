#import Library
import json 
# This is a python library for 'Test Procssing Serveices', as the offcial site suggest.

import difflib
from difflib import SequenceMatcher 

#loading the same data 
data = json.load(open("dictionary.json"))

# Run a Squence Matcher
#First parameter is 'Junk' which includes white spaces, blank lines and so onself.
# Second and third parameters are the words you want to find similarities in-between.
# Ratio is used to find how close those two words are in numberical terms

value = SequenceMatcher(None, "rainn", "rain").ratio()

print(value)
#Method one, that out put a percent of match