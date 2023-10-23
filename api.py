import requests

prg = input('Envie o ID ou Nome de um Pokemon: ')
# URL's
url = f"https://pokeapi.co/api/v2/pokemon/{prg}/"
url_legends = f"https://pokeapi.co/api/v2/pokemon-species/{prg}/"
# JSON's
poke = requests.get(url)
legend = requests.get(url_legends)
# Função
def Pokemon(start: int, end: int):
    if poke.status_code == 200:
        data = poke.json()
        print(f"ID: {data['id']}")
        print(f"Nome: {data['name']}")
        print(f"Altura: {data['height']}")
        print(f"Peso: {data['weight']}")
        print("Tipo: ", end='')
        for tipo in data["types"]:
            print(f"{tipo['type']['name']}/", end='')
        print()
# Ataques
    if poke.status_code == 200:
        dete = poke.json()
        decrease_moves = dete["moves"]

# Not Power None
    if decrease_moves is not None:
        print("Ataques: ", end='')

        max_moves = 3
        moves_printed = 0
        for movim in decrease_moves:
            if moves_printed >= max_moves:
                break

            url_moves = movim["move"]["url"]
            moves = requests.get(url_moves)
            poder = moves.json()
            poderes = poder["power"]
            if poderes is not None:
                move_name = movim["move"]["name"]
                print(f"{move_name} / ", end='')
                moves_printed += 1
        print()
# Poderes
    if decrease_moves is not None:
        print("Poderes: ", end='')

        max_moves = 3
        moves_printed = 0
        for movim in decrease_moves:
            if moves_printed >= max_moves:
                break

            url_moves = movim["move"]["url"]
            moves = requests.get(url_moves)
            poder = moves.json()
            poderes = poder["power"]
            if poderes is not None:

                print(f"{poderes}/", end='')
                moves_printed += 1
    print()
# Status
    vida = data["stats"]

    if vida is not None:
        for life in vida:
            live = life["stat"]["name"]
            amor = life["base_stat"] 
            if live == "hp":
                print(f"{live}: {amor}")

    if vida is not None:
        for life in vida:
            live = life["stat"]["name"]
            amor = life["base_stat"] 
            if live == "attack":
                print(f"{live}: {amor}")

    if vida is not None:
        for life in vida:
            live = life["stat"]["name"]
            amor = life["base_stat"] 
            if live == "defense":
                print(f"{live}: {amor}")
# Lendario?
    if legend.status_code == 200:
        lege = legend.json()
        print(f"Lendario: {lege['is_legendary']}")
# Incia a função
Pokemon(1, 151)
