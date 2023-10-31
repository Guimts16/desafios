import requests
import logging

logger = logging.getLogger('Pokemon')
logging.basicConfig(level=logging.INFO, format='- %(name)s - %(levelname)s - %(message)s')

def pokemon(i):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}/"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        logger.info(f"Pokemon #{i}")
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
            ataques = []
            poderes = []
            max_moves = 3
            moves_printed = 0
            for movim in decrease_moves:
                if moves_printed >= max_moves:
                    break

                url_moves = movim["move"]["url"]
                move_response = requests.get(url_moves)
                if move_response.status_code == 200:
                    poder = move_response.json()
                    move_name = movim["move"]["name"]
                    power = poder["power"]
                    if power is not None:
                        ataques.append(move_name)
                        poderes.append(power)
                        moves_printed += 1

            logger.info("Ataques: " + " / ".join(ataques))
            logger.info("Poderes: " + " / ".join(map(str, poderes)))

def ststs(i):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        vida = data["stats"]
        info = []

        for life in vida:
            live = life["stat"]["name"]
            amor = life["base_stat"]
            if live == "hp":
                info.append(f"HP: {amor}")
            elif live == "attack":
                info.append(f"Ataque: {amor}")
            elif live == "defense":
                info.append(f"Defesa: {amor}")

        for item in info:
            logger.info(item)

def lendario(i):
    url_legends = f"https://pokeapi.co/api/v2/pokemon-species/{i}/"
    response = requests.get(url_legends)
    if response.status_code == 200:
        data = response.json()
        info = []
        info.append(f"Lendario: {data['is_legendary']}")
        info.append("========")

        for item in info:
            logger.info(item)

def main():
    for i in range(1, 152):
        pokemon(i)
        ststs(i)
        lendario(i)

if __name__ == "__main__":
    main()
