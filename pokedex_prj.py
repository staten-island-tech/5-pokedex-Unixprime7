import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

pokemon = input("What pokemon would you like to choose? ")
language = input("What language would you like it translated to? ")

names = [cheese['name'] for cheese in data]

print(data[names.index(pokemon)][language])




