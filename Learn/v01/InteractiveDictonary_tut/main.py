# Step 1- getting the data
# Step 2- Checks for non-existing words
# Step 3- Case sensitivity
# Step 4- Closet Match

#Import library
import json
import difflib 
from difflib import get_close_matches


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
    #3rd elif: To find a similar word
    #-- len > 0 because we can print only when the word has 1 or more close matches
    #-- In the return statement, the last [0] represents the first element from the list of close matches
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word does not exist, yet.")
        else:
            print("Does not compute")

#input from user
word_user  = input("Enter word: ")

# Retrive tge definition using function an print the results
output = retrive_definitation(word_user)
#If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print("-",item)
#For words haveing single definition
else:
    print("-",output)