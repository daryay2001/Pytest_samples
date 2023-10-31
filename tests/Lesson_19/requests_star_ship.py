import json

import requests
from requests.exceptions import RequestException

# Уважно вивчіть документацію цього API (https://swapi.dev/documentation) і напишіть програму,
# яка зберігає в JSON-файл інформацію легендарного корабля Millennium Falcon та його пілотів.
#
# Інформація про корабель має містити такі пункти:
#
# назва,
# максимальна швидкість,
# клас,
# список пілотів.
# Усередині списку про кожного пілота має бути така інформація:
# ім'я,
# зріст,
# вага,
# рідна планета,
# посилання на інформацію про рідну планету.

FALCON_URL = "https://swapi.dev/api/starships/10/"

if __name__ == '__main__':
    try:
        response = requests.get(FALCON_URL)
        response.raise_for_status()
        assert response.status_code == 200
        ship_data = response.json()

        selected_ship_data = {}
        ship_keys_to_select = ['name', 'max_atmosphering_speed', 'starship_class', 'pilots']
        for key in ship_keys_to_select:
            selected_ship_data[key] = ship_data[key]

        pilots_url_list = selected_ship_data["pilots"]

        pilot_info_list = []
        pilot_keys_to_select = ['name', 'height', 'mass', 'homeworld']

        for pilot_url in pilots_url_list:
            pilot_resp = requests.get(pilot_url)
            assert pilot_resp.status_code == 200
            pilot_data = pilot_resp.json()

            selected_pilot_data = {}

            for key in pilot_keys_to_select:
                selected_pilot_data[key] = pilot_data[key]

            pilot_info_list.append(selected_pilot_data)

        for pilot in pilot_info_list:
            homeworld_url = pilot["homeworld"]
            homeworld_resp = requests.get(homeworld_url)
            assert homeworld_resp.status_code == 200

            homeworld_data = homeworld_resp.json()
            pilot["planet"] = homeworld_data["name"]

        selected_ship_data["pilots"] = pilot_info_list

        file_name = "falcon.json"

        with open(file_name, "w") as json_file:
            json.dump(selected_ship_data, json_file)

        print(f"Data was saved to the {file_name}")

    except RequestException as error:
        print(f"Request error: {error}")
    except Exception as error:
        print(error)
