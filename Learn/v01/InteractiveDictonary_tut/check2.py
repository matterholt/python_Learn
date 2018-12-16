# IMPORT library
import json
# this is a python library for 'Text Processing Serveices'
import difflib 
from difflib import get_close_matches

#Let's load the data
data = json.load(open("dictionary.json"))

# Defor you dive in, the basic template of this function is as follows
# get_close_matches(word, posibilities, n=3, butoff=0.66)
# First parameter is of course the word for which you want to find close matches
# Second is a list of sequences against which to match the word
# [optional] Third is a maximum number of close matches
# [optional] Where to stop considering a word as a moatch (0.99 being the closest to  word while 0.0 beign otherwise)

output = get_close_matches("rain", ["help", "mate", "rainy"], n=1, cutoff = 0.75)

print(output)