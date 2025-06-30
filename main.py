import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '1d8c83ba2c004d5fd2c14f96b5f62d0e'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
    }

body_create = {
    "name": "generate",
    "photo_id": -1
}

response_create = requests.post(
    url=f'{URL}/pokemons',
    headers=HEADER,
    json=body_create
)

print(response_create.json())

pokemon_id = response_create.json()['id']


body_update = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": -1
}

response_update = requests.put(
    url=f'{URL}/pokemons',
    headers=HEADER,
    json=body_update
)

print(response_update.json())


body_pokeball = {
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post(
    url=f'{URL}/trainers/add_pokeball',
    headers=HEADER,
    json=body_pokeball
)

print(response_pokeball.json())
