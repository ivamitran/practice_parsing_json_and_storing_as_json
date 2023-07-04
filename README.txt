Practice Parsing Json and Storing Data as Json:
This is a simple python program that does 3 things:
1. It loads existing json data from a json file into a python program
2. It allows the user to add to the existing json data
3. It writes the new instance of the data back to the json file

Additonal Notes:
- The json file of this program is a list of dictionaries
- Because of this, the data is converted into a list of objects of the person class. This is done so that we could potentially use methods for the data
- The most up to date version of the data is reflected in the list of objects, so that is converted back into a list of dictionaries and then written to the json file