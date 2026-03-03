import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
types = open("./types.json", encoding="utf8")
type = json.load(types)

def func1():
    pokemon_number = input("What number pokemon would you like to choose? ")
    pokemon = int(pokemon_number)
    language = input("What language would you like it translated to? ")

    names = [cheese['id'] for cheese in data]

    print(data[names.index(pokemon)]['name'][language])
#func1()

def pokesearch(data2, type2):
    poketype = input("What types of pokemon do you want to see? ")
    types_found = 0
    for cheese in data2:
        if poketype in cheese['type']:
            print(cheese['name']['english'])
            types_found = 1
        else:
            if poketype not in type2['english']:
                types_found == 0
                return
    if types_found == 0:
            print('This type does not exist')
        
pokesearch(data, type)

