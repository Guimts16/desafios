
import grequests
import logging
import threading


logging.basicConfig(level=logging.INFO, format='- %(name)s - %(levelname)s - %(message)s')

for i in range(1, 152):

    def pokemon_base():
        logger = logging.getLogger(f'Pokemon #{i}')
        url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
        url_legends = f"https://pokeapi.co/api/v2/pokemon-species/{i}/"
        responses = grequests.map([grequests.get(url), grequests.get(url_legends)])

        poke = responses[0]
        if poke.status_code == 200:
            data = poke.json()
            logger.info(f"ID: {data['id']}")
            logger.info(f"Nome: {data['name']}")
            logger.info(f"Altura: {data['height']}")
            logger.info(f"Peso: {data['weight']}")
            tipo_string = "Tipo: "
            for tipo in data["types"]:
                tipo_string += f"{tipo['type']['name']}/"
            logger.info(tipo_string)
        decrease_moves = data["moves"]

        if decrease_moves is not None:
            ataques_string = "Ataques: "
            max_moves = 3
            moves_printed = 0
            for movim in decrease_moves:
                if moves_printed >= max_moves:
                    break

                url_moves = movim["move"]["url"]
                moves = grequests.map([grequests.get(url_moves)])[0]
                poder = moves.json()
                poderes = poder["power"]
                if poderes is not None:
                    move_name = movim["move"]["name"]
                    ataques_string += f"{move_name} / "
                    moves_printed += 1
            logger.info(ataques_string)

        if decrease_moves is not None:
            poderes_string = "Poderes: "
            max_moves = 3
            moves_printed = 0
            for movim in decrease_moves:
                if moves_printed >= max_moves:
                    break

                url_moves = movim["move"]["url"]
                moves = grequests.map([grequests.get(url_moves)])[0]
                poder = moves.json()
                poderes = poder["power"]
                if poderes is not None:
                    poderes_string += f"{poderes}/"
                    moves_printed += 1
            logger.info(poderes_string)
def vidas():
    logger = logging.getLogger(f'Pokemon #{i}')
    url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
    url_legends = f"https://pokeapi.co/api/v2/pokemon-species/{i}/"
    responses = grequests.map([grequests.get(url), grequests.get(url_legends)])
    poke = responses[0]
    data = poke.json()
    vida = data["stats"]

    if vida is not None:
        for life in vida:
            live = life["stat"]["name"]
            amor = life["base_stat"]
            if live == "hp":
                logger.info(f"{live}: {amor}")

    if vida is not None:
        for life in vida:
            live = life["stat"]["name"]
            amor = life["base_stat"]
            if live == "attack":
                logger.info(f"{live}: {amor}")

    if vida is not None:
        for life in vida:
            live = life["stat"]["name"]
            amor = life["base_stat"]
            if live == "defense":
                logger.info(f"{live}: {amor}")
def leg():
    logger = logging.getLogger(f'Pokemon #{i}')
    url_legends = f"https://pokeapi.co/api/v2/pokemon-species/{i}/"
    responses = grequests.map([grequests.get(url_legends)])
    legend = responses[0]
    if legend.status_code == 200:
        lege = legend.json()
        logger.info(f"Lendario: {lege['is_legendary']}\n========")


    # Loop
for i in range(1, 152):
    ant = 0
    pokemons = threading.Thread(target=pokemon_base())
    pokemons.start()

    life = threading.Thread(target=vidas)
    life.start()

    lag = threading.Thread(target=leg)
    lag.start()
