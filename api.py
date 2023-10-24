import grequests
import logging

logging.basicConfig(level=logging.INFO, format='- %(name)s - %(levelname)s - %(message)s')

def pokemon(pokemon_id):
    logger = logging.getLogger(f'Pokemon #{pokemon_id}')

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    url_legends = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}/"

    responses = grequests.map([grequests.get(url), grequests.get(url_legends)])

    poke = responses[0]
    legend = responses[1]

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

    if legend.status_code == 200:
        lege = legend.json()
        logger.info(f"Lendario: {lege['is_legendary']}\n========")

# Loop 
for i in range(1, 152):
    pokemon(i)
