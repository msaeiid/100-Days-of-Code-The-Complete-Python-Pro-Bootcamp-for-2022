travel_log = [
    {
        "Country": "France",
        "visited": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "Country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    }
]


def add_new_country(country_visited: str, visits_visited: int, cities_visited: list):
    travel_log.append(
        {
            "Country": country_visited,
            "visits": visits_visited,
            "cities": cities_visited,
        })


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
