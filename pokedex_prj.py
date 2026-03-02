import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

def func1():
    pokemon_number = input("What number pokemon would you like to choose? ")
    pokemon = int(pokemon_number)
    language = input("What language would you like it translated to? ")

    names = [cheese['id'] for cheese in data]

    print(data[names.index(pokemon)]['name'][language])
#func1()

def pokesearch():
    poketype = input("What types of pokemon do you want to see? ")
    

