# Step 1- getting the data
# Step 2- Checks for non-existing words
# Step 3- Case sensitivity
# Step 4- Closet Match

#Import library
import json
import difflib
from difflib import SequenceMatcher

#Load the json data as python dictionary
data = json.load(open("dictionary.json"))

def retrive_definitation(word):
    # Remove the case-sensitivity form the program
    # Converting all letter to lower beacuse out dat is in the format
    word = word.lower()

    #adding check for non-existing words
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("The word doesn't exist in Dictonary")


#input from user
word_user  = input("Enter word: ")

print(retrive_definitation(word_user))