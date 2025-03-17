import requests
# import json

base_url = "https://pokeapi.co/api/v2/pokemon/"

# make a function 
def get_pokemon_info(name):  # here name is a parameter (parameterized constructor) parameter acts as place holder
    url = f'{base_url}{name}'
    response = requests.get(url)  
    # we used requests module, then used get method and pass in the url, this will return a response object
    # which we will assign in response
    # response is a response object
    # if we print response object - print(response) we get http status code in output - <Response [200]> , the response is okay 
    # we can check the HTTP response status code

    if response.status_code == 200 :  # status_code checks the status
       pokemon_data = response.json() 
       # here our response is a json format,
       # by this method we convert it to python dictionary, consists of key-value pairs,
       #and we will store it into variable called pokemonm_data
       #to check for retrieval, print("Data retrieved!") instead of pokemon_data = response.json()
       # print(pokemon_data)
       # here we get a lot of data but the format is not readable (but we got our dictionary)
       return pokemon_data 
       # once we have the dictionary we can return the dictionary 
       # back to the place where we called the function in get_pokemon_info
       # and the function we will change it to the variable pokemon_info = get_pokemon_info(pokemon_name)  
    else :
        print(f'Failed to retrive data, {response.status_code}')

# make a variable
pokemon_name = "pikachu"

# now call the function
# get_pokemon_info(pokemon_name)  # here pokemon_name is an argument, argument supplies real data to the function

pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info: # if pokemon_info exists/true
    print(f'Name : {pokemon_info["name"]}') # i will print the following
# to access the value of dictionary we will take the pokemon_info variable and access the key i.e ["name"]
# 
# we can also access other data (height, weight, id, etc) of the pokemon we want but here we have used pokemon_name as pikachu
    print(f'Height : {pokemon_info["height"]}')
    print(f'Weight : {pokemon_info["weight"]}')