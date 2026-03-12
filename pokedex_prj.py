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

def get_pokemon_types(pokemon_val):
    for pokemon in pokedex:
        e_pokename = pokemon['name']['english']
        if pokemon_val == e_pokename:
            poke_type = pokemon['type']
            return poke_type

# def get_type_moves(type_vals):
#     move_list = []

#     for move in moves:
#         move_type = move['type']
#         if move_type == type_vals[0]:
#             move_list.append(move['ename'])
        
#     for move in moves:
#         move_type = move['type']
#         if move_type == type_vals[1]:
#             move_list.append(move['ename'])
#         if int(move['id']) == 619:
#             return move_list
        
def get_type_moves(type_val):
    move_list = []
    
    for move in moves:
        move_type = move['type']
        if move_type == type_val:
            move_list.append(move['ename'])
    
    return move_list

def func4():
    user_poke = input("Which pokemon's moves would you like to see? ")
    poke_types = get_pokemon_types(user_poke)

    moves_list = []
    for poke_type in poke_types:
        # print(f"poke type {poke_type}")
        type_moves = get_type_moves(poke_type)

        for type_move in type_moves:
            moves_list.append(type_move)

    for move in moves_list:
        print(move)
func4()






