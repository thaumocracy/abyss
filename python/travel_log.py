travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(log, country, visits, cities):
    log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })
    return log


add_new_country(travel_log, "Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
