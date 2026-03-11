import json
## Open the JSON file of pokemon data
pokedex_file = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
pokedex = json.load(pokedex_file)
types_file = open("./types.json", encoding="utf8")
types = json.load(types_file)
moves_file = open("./moves.json", encoding="utf8")
moves = json.load(moves_file)

def func1():
    pokemon_number = input("What number pokemon would you like to choose? ")
    pokemon = int(pokemon_number)
    language = input("What language would you like it translated to? ")

    names = [cheese['id'] for cheese in pokedex]

    print(pokedex[names.index(pokemon)]['name'][language])
#func1()



def is_valid_type(search_type):

    for type_object in types:
        english_type = type_object["english"]
        if search_type == english_type:
            return True
            
    return False

def search_pokedex(search_type):
    
    for pokemon in pokedex:
        if search_type in pokemon['type']:
            print(pokemon['name']['english'])
        else:
            pass

#user_type = input("What types of pokemon do you want to see? ")

def func2():
    valid = is_valid_type(user_type)
    if valid == True:
        search_pokedex(user_type)
    else:
        print("This type does not exist")
#func2()

def search_pokemon(search_pokemon):
    found = False
    for pokemons in pokedex:
        english_names = pokemons['name']['english']
        if search_pokemon in english_names:
            print(english_names)
            found = True
    if not found:
        print("Sorry, there aren't any pokemon like this")
        
            
    

#user_poke_part = input("What do you want the pokemon that you want to see to start with? ")

#search_pokemon(user_poke_part)
def func4():
    user_poke = input("Which pokemon's moves would you like to see? ")
    user_type = pokedex.index(user_poke)['type']


    for move in moves:
        check_types = move['type']
        if user_type == check_types:
            print(move['ename'])
func4()
        





